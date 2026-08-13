---
title: "Courses"
description: "Turning normal people into weird tech folks, one step at a time..."
summary: "Turning normal people into weird tech folks, one step at a time..."
showTableOfContents: true # I love that this works
---

<!-- Shout out to all my Tik Tok Hustlers who think theyr'e going to escape a permanent underclass by selling courses lol -->
{{< typeit
  tag=h4
  speed=80
  lifeLike=true
  breakLines=true
  loop=false
>}}
"Intellectual growth should commence at birth and cease only at death." - Albert Einstein
{{< /typeit >}}

---

## Overview 📌

In this section of my Website, I'm publishing full courses (**for free**), on how you can go from knowing nothing about any of the given skills I'm teaching, to be being *somewhat* competent at them.

*or at the very least, get you going about which strings to start pulling on if you want to learn more.*

<!-- Dawg Image -->
![What tha dawg doing](https://web.archive.org/web/20170216002239if_/https://i.reddituploads.com/4bb3b26f3b27422aa3c1c26f1ffe7dfc?fit=max&h=1536&w=1536&s=cba7006996e1df2c262baf20e8ea0d6a)

*^ Took me so long to find a HD image of this meme.*

### Which courses are you working on right now? 🛠️

I've made a graph below which shows progress towards completion on the x-axis, and the specific courses I'm working on the y-axis.

I'll update this graph with each push to my Websites's [GitHub Repo](https://github.com/RussellChubb/Russell_Website).

<!-- Course Progress Chart -->
{{< chart >}}
type: 'bar',
options: {
  indexAxis: 'y',
  scales: {
    x: {
      min: 0,
      max: 100,
      ticks: {
        callback: (value) => value + '%'
      }
    }
  },
  plugins: {
    legend: {
      display: false
    }
  }
},
data: {
  labels: ['Python', 'Git', 'SQL', 'Bash', 'Power BI'],
  datasets: [{
    label: 'Course Completion',
    data: [5, 0, 2, 5, 0],
    backgroundColor: [
      '#EAB308',
      '#EF4444',
      '#3B82F6',
      '#7C3AED',
      '#CA8A04'
    ],
    borderWidth: 0,
    borderRadius: 4
  }]
}
{{< /chart >}}

### Why? ❓

When I graduated university with a Marketing and Management degree, I expected the world to open up for me.

Little did I know, but it's not enough (*any more*) to **just** have that degree anymore.

While I imagine that not everyone goes out into the real world and has this issue, it made me realise the necessity of adding a extra couple of "*arrows*" to my quiver.

<!-- Just Optimize Bro -->
![What tha dawg doing](https://i.redd.it/6us6d33g7ate1.png)

In my desperation, I tried to look forward to the future to understand what might be a future-proof industry to get into, as such, [Data came up as a solid option to look into.](https://ec.europa.eu/commission/presscorner/api/files/document/print/en/speech_11_872/SPEECH_11_872_EN.pdf)

<!-- Pondering my orb Image -->
![How I felt tbh](https://images.steamusercontent.com/ugc/1832425236567210581/E42B98E54BE45DAF2688938E3AC1BDFC0AF33E8E/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false)

Now, I know that data-work isn't for everyone. (*I know this for a fact as whenever I tell anyone what I do for work, I never get asked any follow-up questions*).

With this being said, if you've got an interest at all in the following areas:

* Technical Skills
* Problem Solving
* Design
* Communication
* Paying your rent

You might find working in Data is actually more interesting than you think.

> [!IMPORTANT]
> You don't have to use these courses to work in Data.
>
> In fact, you can think of the skills I'm teaching to be more like "tools" in your tool-box.
>
> Very often when solving a problem, you need to think less about which tool you'd like to use, and which one would get the job done in the most efficient, and productive manner.
>
> i.e. You wouldn't use a screwdriver to hammer a nail, much like you wouldn't use SQL to design GUI's.

<!-- DOOM in SQL -->
{{< youtubeLite id="1Q_62NigzN8" label="DOOM in SQL" >}}

*^ unless....*

Anyway, when I learned to code in 2023, you couldn't really just ask an AI to do your coding for you, and as such, I had to learn the fundamentals.

The only problem with this, is that I didn't have any computer science / technical background at all, and as such, I was in a position where I didn't even know, what I didn't know.

<!-- Don't know what you don't know -->
![Tough Position](https://bryanmmathers.com/wp-content/uploads/2021/07/020-You-dont-know-you-dont-know.png)

As well as this, one thing I found about a lot of technical courses is that there is an expectation that you:

1) Already know certain things... i.e. assumptions are made about your technical ability.

2) You already know how to solve your own issues. This is actually a bigger problem that some people struggle with, but I'll show you how to debug issues (*which is a skill that helps in more than just "technical" work.*)

### What do I want people to get out of these courses? 🌅

As such, I want to provide people with two things:

1) Courses that don't make any assumptions about your level of technical expertise, we're going to start right at the beginning.

2) Provide a holistic view of "*computer nerd*" work (*that's what my girlfriend, and Eva from Holland call it*).

Because here's the thing, you're not going to find much success just learning Python.

You'll probably want to learn about the Shell / Bash, or how to use Git to push your code somewhere, as well as how to do some basic CI / CD.

Or, if you want a job to do with Data (*Analytics, Science, Engineering*), you might want to learn how to use SQL to query Data-Warehouses (*Supppppppper useful skill that will never go away btw*).

Regardless, these skills work in synergy together, which is why I'd recommend that you learn (*atleast a little*) about each of these skills, and how they work together.

<!-- Fusion Dance Image -->
![Coudln't be bothered opening Affinity for this](https://preview.redd.it/a-question-about-the-fusion-dance-v0-zfnj6xst5p9d1.png?auto=webp&s=b78c8397a56cee1961508897cdb4fa66523afff4)

### What's in it for me? 👀

Well, believe it or not, but I actually started making [coding tutorials](https://www.youtube.com/@Russell_Chubb) to help myself learn.

As such, making these courses has a two-fold benefit for me:

1) It provides me with scripts to later use as videos

2) It helps me learn more!

*Consult the Pyramid below for further explanation...*

<!-- Link to Learning Pyramid -->
![Passive vs Active huh](https://j-os.com/uploads//2022/02/AdobeStock_318466660.jpg)

### The Elephant in the Room 🤖

<!-- Why do I need to learn to program? -->
{{< lead >}}
"Why should I learn to code when I can just have AI do it for me?"
{{< /lead >}}

<!-- AI Image -->
![broooooo](https://i.redd.it/uujc59abpslc1.jpeg)

My general response to that is that **there is so much more to code than just writing code**.

It's about thinking about how the decisions you make will impact existing architecture, other systems, how to design things in a way that will scale, and how to communicate and market your product to an audience.

However, if you think I'm wrong, I'll layout the challenge to you...

Go on, make something "*successful*" using just AI and no prior understanding... prove me wrong. (*I'd actually be super impressed if you're able to do this!*)

Finally, and this seems obvious, but without knowing fundamental concepts and principles, how do you expect to go anywhere?

> [!NOTE]
> Not all of the courses that I produce will be "coding", but quite a few of them are "touched", by developments in Large Language Models (LLM's), in the past couple of years, thus, it's crucial for me to address this comment.

### Couldn't you write these courses a whole lot faster using AI? 🏃

The other thing about these courses, I'm hand-writing everything.

I know I could make use of AI tooling to speed up this entire process, but in the back of my mind, I know for a fact that I wouldn't just be cheating anyone that learns from me, but I'd also be cheating myself.

#### With this being said ⏪

When I teach you how to "*Solve your own technical problems*", I'll show how I integrate AI into my workflow in a way that still gives me control over my code, but expedites my workflow in a positive way.

## Courses 🔗

Without further ado, here are the courses... (**NOTE: Might be empty if / when you first see this...**)
