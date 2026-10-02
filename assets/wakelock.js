(() => {
  const wakeLockElement = document.querySelector("[data-wake-lock]");

  if (!wakeLockElement || !("wakeLock" in navigator)) {
    return;
  }

  const button = wakeLockElement.querySelector(".wake-lock__button");
  const text = wakeLockElement.querySelector(".wake-lock__text");
  const icon = wakeLockElement.querySelector(".wake-lock__icon");

  let wakeLockSentinel = null;
  let enabled = false;

  function updateButton(isEnabled) {
    icon.textContent = isEnabled ? "☀️" : "🌙";
    text.textContent = isEnabled ? "Screen will stay awake" : "Keep screen awake";
    button.setAttribute("aria-pressed", String(isEnabled));
  }

  async function requestWakeLock() {
    try {
      wakeLockSentinel = await navigator.wakeLock.request("screen");

      wakeLockSentinel.addEventListener("release", () => {
        wakeLockSentinel = null;

        if (enabled) {
          updateButton(false);
        }
      });

      enabled = true;
      updateButton(true);
    } catch (error) {
      console.error("Unable to keep screen awake:", error);
    }
  }

  async function releaseWakeLock() {
    if (wakeLockSentinel) {
      await wakeLockSentinel.release();
      wakeLockSentinel = null;
    }

    enabled = false;
    updateButton(false);
  }

  button.addEventListener("click", async () => {
    if (enabled) {
      await requestWakeLock();
    } else {
      await releaseWakeLock();
    }
  });

  document.addEventListener("visibilitychange", async () => {
    if (
      document.visibilityState === "visible" &&
      enabled &&
      !wakeLockSentinel
    ) {
      await requestWakeLock();
    }
  });
})();