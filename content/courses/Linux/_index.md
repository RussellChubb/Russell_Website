---
title: "Linux"
description: "Russell's Linux Course"
summary: "Russell's Linux Course"
showAuthor: true
date: 2026-05-09
featureimage: "featured.jpg"
tags: ["Linux"]
---

<!-- Shout out to all my Tik Tok Hustlers who think they're going to escape a permanent underclass by selling courses lol -->
{{< typeit
  tag=h4
  speed=80
  lifeLike=true
  breakLines=true
  loop=false
>}}
“Don't ever make the mistake [of thinking] that you can design something better than what you get from ruthless massively parallel trial-and-error with a feedback cycle. That's giving your intelligence much too much credit.” ― Linus Torvalds
{{< /typeit >}}

---

## Introduction to Linux - Video

<!-- Link to Video -->
{{< youtubeLite id="1b3PYXsHw9U" label="Video - Introduction to Linux" >}}

### Introduction to Linux - Content

Linux is an operating system, like macOS or Windows.

It is also the most popular Open Source and free, (*as in freedom*), operating system.

It powers the vast majority of the servers that compose the Internet. It's the base upon which everything is built upon.

But not just that. Android is based on (*a modified version of*) Linux.

The Linux "core" (*called kernel*) was born in 1991 in Finland, and it went a really long way from its humble beginnings. It went on to be the kernel of the GNU Operating System, creating the duo GNU/Linux.

There's one thing about Linux that corporations like Microsoft and Apple, or Google, will never be able to offer:

* The freedom to do whatever you want with your computer.

They're actually going in the opposite direction, building walled gardens, especially on the mobile side.

Linux is the ultimate freedom.

It is developed by volunteers, some paid by companies that rely on it, some independently, but there's no single commercial company that can dictate what goes into Linux, or the project priorities.

Linux can also be used as your day to day computer. I use macOS because I really enjoy the applications, the design and I also used to be an iOS and Mac apps developer, but before using it I used Linux as my main computer Operating System.

No one can dictate which apps you can run, or "*call home*" with apps that track you, and more.

Linux is also special because there's not just "*one Linux*", like it happens on Windows or macOS. Instead, we have distributions.

A "*distro*" is made by a company or organization and packages the Linux core with additional programs and tooling. For example you have:

* Debian
* Red Hat
* Ubuntu (*probably the most popular.*)

<!-- Estimated Market Share Graph -->
{{< chart >}}
type: 'doughnut',
data: {
  labels: ['Ubuntu', 'Debian', 'Fedora', 'Arch', 'Mint', 'RHEL/CentOS', 'openSUSE', 'Other'],
  datasets: [{
    data: [22, 15, 13, 12, 10, 8, 6, 14],
    backgroundColor: [
      'rgba(255, 99, 132, 0.8)',
      'rgba(255, 159, 64, 0.8)',
      'rgba(255, 205, 86, 0.8)',
      'rgba(75, 192, 192, 0.8)',
      'rgba(54, 162, 235, 0.8)',
      'rgba(153, 102, 255, 0.8)',
      'rgba(201, 203, 207, 0.8)',
      'rgba(255, 99, 255, 0.8)'
    ],
    borderColor: '#14191f',
    borderWidth: 3
  }]
},
options: {
  plugins: {
    title: {
      display: true,
      text: 'Linux Distro Market Share (Rough Estimate)',
      color: '#ffffff',
      font: {
        size: 16,
        weight: 'bold'
      },
      padding: {
        bottom: 20
      }
    },
    legend: {
      position: 'bottom',
      labels: {
        color: '#ffffff',
        padding: 20,
        font: {
          size: 13,
          weight: 'bold'
        }
      }
    },
    tooltip: {
      callbacks: {
        label: function(context) {
          return ' ' + context.label + ': ~' + context.parsed + '% of estimated market share';
        }
      }
    }
  }
}
{{< /chart >}}

Many, many more exist. You can create your own distribution, too. But most likely you'll use a popular one, one that has lots of users and a community of people around it, so you can do what you need to do without losing too much time reinventing the wheel and figuring out answers to common problems.

Some desktop computers and laptops ship with Linux preinstalled. Or you can install it on your Windows-based computer, or on a Mac. But you don't need to disrupt your existing computer just to get an idea of how Linux works.

I personally don't (*currently*) have a Linux computer.

If you use a Mac you need to know that under the hood macOS is a UNIX Operating System, and it shares a lot of the same ideas and software that a GNU/Linux system uses, (*because GNU/Linux is a free alternative to UNIX.*)

<!-- Dropdown for the definition here -->
{{< accordion mode="collapse" >}}
  {{< accordionItem title="UNIX Definition" icon="lightbulb" >}}
  UNIX is an umbrella term that groups many operating systems used in big corporations and institutions, starting from the 70's.
  
  The macOS terminal gives you access to the same exact commands I'll describe in the rest of this handbook.
  {{< /accordionItem >}}
{{< /accordion >}}

Microsoft has an official Windows Subsystem for Linux which you can (*and should!*) install on Windows. This will give you the ability to run Linux in a very easy way on your PC.

But the vast majority of the time you will run a Linux computer in the cloud via a VPS (*Virtual Private Server*) like DigitalOcean.

A shell is a command interpreter that exposes to the user an interface to work with the underlying operating system.

It allows you to execute operations using text and commands, and it provides users advanced features like being able to create scripts.

**This is important**: shells let you perform things in a more optimized way than a GUI (*Graphical User Interface*) could ever possibly let you do.

Command line tools can offer many different configuration options without being too complex to use.

There are many different kind of shells. This post focuses on Unix shells, the ones that you will find commonly on Linux and macOS computers.

Many different kind of shells were created for those systems over time, and a few of them dominate the space:

* Bash
* Csh
* Zsh (*I use this*)
* Fish

And many more!

All shells originate from the Bourne Shell, called sh . "Bourne" because its creator was Steve Bourne.

Bash means Bourne-again shell. sh was proprietary and not open source, and Bash was created in 1989 to create a free alternative for the GNU project and the Free Software Foundation.

Since projects had to pay to use the Bourne shell, Bash became very popular.

If you use a Mac, try opening your Mac terminal. Which, by default is running ZSH. (*or, pre-Catalina, Bash*)

You can set up your system to run any kind of shell, for example I used to use the Fish shell on my Windows PC.

Each single shell has its own unique features and advanced usage, but they all share a common functionality: they can let you execute programs, and they can be programmed.

In the course content below, we'll learn in detail the most common (*and useful*) commands.
