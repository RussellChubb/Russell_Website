---
title: "About"
description: "The Story of Russell Chubb"
showAuthor: true
showViews: true
showLikes: true
showDate: false
---

<!-- Adding this in to let people know that this page is WIP -->
> [!NOTE]
> As with other pages on the russellchubb.com , this page is a work in progress.

<!-- Saw this from an image on Pinterest, thought it went hard, kinda references a few things I'm into lol -->
{{< typeit
  tag=h4
  speed=80
  lifeLike=true
  breakLines=true
  loop=false
>}}
Student: Master, what is the most complex game that man has invented?
Master: Chess!
Student: What about Go?
Master: Go has always existed.
{{< /typeit >}}

---

## TL;DR 👋

I'm a Data-Analyst living (*as of 12/04/26*) in New Zealand (*although moving to Scotland in 2026!*).

I've been doing ***Data Stuff*** (*including but not limited to Software Engineering, UX/UI Design and Development, Video and Graphics Editing, Project Implementation*) for ~ 3 years at this point, with a key area that I enjoy being the dissemination of complex and or technical information to a large audience, emphasising design and purpose that fits the need of an end user.

<!-- Adding this in to let the people know wsup -->
> [!IMPORTANT]
> i.e. I like making shit that people use and enjoy.

<!-- TODO: Add in BASH & Terminal / Git -->
### Skills 🎯

I always think it's a little silly to have to create a skill matrix for yourself and boil an entire person down to just some skills or characteristics. However, just taking a look at this chart gives you a good idea of what kind of skills I have out of the box.

I've expressed my level of "*skill*" in a given area, by providing a value between 1-10 (*1 being a complete novice, 10 being a master*). The catch with a skills matrix is that different people will interpret your skills in different ways, combined with the fact that mastery is easy to point out, but hard to define.

> [!NOTE]
> I do think though, if you do want to get a really good vibe on who I am, and what I can do for you, it's much better that you evaluate my skills based on the outputs of my work, as opposed to a skill matrix that I could in theory, be bullshitting on.
>
> **NOTE:** I've noticed this chart has some text cut-off on mobile, best to view the site on desktop anyway.

<!-- TODO: Why is there so much room at the top and bottom of this chart? -->
#### Skill Matrix Spider Chart 🕷️

{{< chart >}}
type: 'radar',
data: {
  labels: ['SQL', 'Python', 'Data Visualisation', 'UX / UI Design', 'Web Development', 'Data Modelling', 'Databricks / Cloud', 'Project Management', 'Graphic Design', 'Communications / Marketing'],
  datasets: [{
    label: 'Russell Chubb',
    data: [6, 6, 8, 8, 3, 5, 3, 3, 7, 8],
    fill: true,
    backgroundColor: 'rgba(255, 99, 132, 0.2)',
    borderColor: 'rgba(255, 99, 132, 1)',
    pointBackgroundColor: [
      'rgba(255, 99, 132, 1)',
      'rgba(255, 159, 64, 1)',
      'rgba(255, 205, 86, 1)',
      'rgba(75, 192, 192, 1)',
      'rgba(54, 162, 235, 1)',
      'rgb(250, 102, 255)',
      'rgba(153, 102, 255, 1)',
      'rgba(201, 203, 207, 1)',
      'rgba(255, 99, 132, 1)',
      'rgba(255, 159, 64, 1)'
    ],
    pointBorderColor: '#fff',
    pointHoverBackgroundColor: '#fff',
    pointHoverBorderColor: 'rgba(255, 99, 132, 1)',
    borderWidth: 2,
    pointRadius: 5,
    pointHoverRadius: 7
  }]
},
options: {
  scales: {
    r: {
      min: 0,
      max: 10,
      ticks: {
        stepSize: 2,
        display: false
      },
      grid: {
        color: 'rgba(255, 255, 255, 0.2)'
      },
      angleLines: {
        color: 'rgba(255, 255, 255, 0.2)'
      },
      pointLabels: {
        font: {
          size: 13,
          weight: 'bold'
        },
        color: '#ffffff'
      }
    }
  },
  plugins: {
    title: {
      display: false
    },
    legend: {
      display: false
    },
    tooltip: {
      callbacks: {
        label: function(context) {
          const value = context.raw;
          const percent = value * 10;
          return ' ' + value + '/10 — ' + percent + '% progress towards "mastery"';
        }
      }
    }
  }
}
{{< /chart >}}

## Long Version 📜

Heyo! - My name is **Russell David Chubb**.

At the time of writing this, I'm 25 years old. I was born in Brisbane Australia, and moved over to New Zealand when I was around ~ 1 year old. I grew up in Palmerston North, and studied in Wellington, then, moved to Masterton to be closer to my girlfriend and her family!

Somewhere in late 2026, I'll be settling down in Edinburgh, Scotland, wherein I'll be exploring a brand new country!

### Free Time Donut Chart 🍩

When I'm not doing "*Data Stuff*", I'm normally engaged in one of the following activities (*shown in this donut-graph*):

{{< chart >}}
type: 'doughnut',
data: {
  labels: ['Golfing', 'Running', 'Gyming', 'Surfing', 'Mixing Music'],
  datasets: [{
    data: [35, 25, 25, 10, 5],
    backgroundColor: [
      'rgba(255, 99, 132, 0.8)',
      'rgba(255, 159, 64, 0.8)',
      'rgba(255, 205, 86, 0.8)',
      'rgba(75, 192, 192, 0.8)',
      'rgba(54, 162, 235, 0.8)'
    ],
    borderColor: '#14191f',
    borderWidth: 3
  }]
},
options: {
  plugins: {
    title: {
      display: true,
      text: 'How I Spend My Free Time',
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
          return ' ' + context.label + ': ' + context.parsed + '% of estimated free time';
        }
      }
    }
  }
}
{{< /chart >}}

### Computer Origins 🌱
<!-- First time on PC / Origins -->
I still remember the exact moment I first used a computer, I would have been about 7 or 8, and the computer would have looked something like the below image:

![My Childhood Computer](https://i.redd.it/can-anyone-please-tell-me-the-name-of-this-desktop-i-v0-8cpnf9fymosa1.jpg?width=612&format=pjpg&auto=webp&s=eda6ecca368cb69ff05fc2e487f6d546f6c9366d)

Since that pivotal moment, I've been completely enthralled in them. It's hard to say the amount of hours I've spent behind a computer screen, but I'd have to guess that it would be up there at maybe **> 30,000** Hours over the course of my entire life (*Jeez touch grass much*)

![Bro said how many hours!?](https://images.steamusercontent.com/ugc/2204010189983913838/E0E0AE30F1C491ABD8D962B74BD56BC9D4933524/)

<!-- Hacked CSGO Clients -->
I guess you could say that I first started "*programming*" circa 2016, when I was playing around with CS:GO Hacked Clients and Scripts, I remember following a YouTube video for how I can download Visual Studio, pasting some code C++ (*which would have essentially been straight jibberish to me*), and then injecting code into the CSGO run-time, just to bunny-hop around servers. (*good fun would reccomend it*).

<!-- Adding this in to let people know that crime doesn't pay -->
> [!WARNING]
> Cheating is against Steam Services ToC and can result in punishment (*I got banned lol*)

<!-- This is an image of an Indigo paste that I remember using back in the day. -->
![This is the image of the pasted cheat I was using](https://i.imgur.com/DkhoABu.jpg)

Even though I was coding (*coding is a loose term to describe what I would have been doing back in 2016*) in my free-time, I never picked up any computer sciences subjects in school, or even really understood how I could utilize computing as a skill that other people would be interested in. As such, in high-school I was actually studying to become an accountant, an idea, which, once I actually started studying accounting at University, went down the drain very quickly. Long story short, I pivoted across to Marketing and Management, and graduated from Victoria University, Wellington in 2023.

<!-- Graduation Photo -->
![Me on my Graduation day with my parents!](https://i.imgur.com/rRCndl9.jpeg)

Now, I know this doesn't really explain where those "*data skills*" I listed above came from. As it turns out, all a Marketing and Management Degree gives you is about **$50,000** worth of student loan debt, a bunch of life-long friends, and the ability to sink *brews* at an alarming rate.

### Working at the Ministry of Education 💼

I managed to get a job prior to finishing my degree as a "*Implementation Advisor*" at the [Ministry of Education](https://www.education.govt.nz/) (*MoE*) working on a project to remove the [Decile System](https://en.wikipedia.org/wiki/Socioeconomic_decile) from the New Zealand Education System.

<!-- What is decile Accordion -->
{{< accordion >}}
  {{< accordionItem title="What is a Decile?" icon="information-circle" >}}
  In the context of the New Zealand Education System, a decile is a measurement of socioeconomic disadvantage that the composition of students in a school face. Decile 1 schools were composed of students facing the highest proportion of socio-economic disadvantage.
  {{< /accordionItem >}}
{{< /accordion >}}

During this role, I engaged with a variety of Education Subject Matter Experts (SME's) to understand how decile was baked into a variety of initiatives, and work out how we can use the new "*Equity Index*" system instead.

<!-- MoE image. -->
![Image of the MoE Decile Removal Project Team!](https://i.imgur.com/2Pz7VRl.jpeg)

During this role, I was moved towards the ICT Business-Unit within MoE wherein I got to engage and work first-hand with ICT Professionals for the first time in my career, and I actually attribute this, (*combined with inspiration from a Data-Analyst within my team at MoE - shout out to you Scott*), for first opening my eyes to the world of data, and the outcomes that can be gleaned from it.

Anyway, once the project had wrapped up, I moved horizontally within MoE across to the Web-Services team, working as a "Web Advisor". It was during this role that I got my first kind of exposure to Web Development, Including:

* Business Analysis (*requirement gathering, project planning etc*).
* Design (*Designers and Front-End Developers working hand in hand, Wire-Frame Development, Figma etc*),  
* Web-Accessibility Standards,
* Backend-Development (*Development, Cloud Hosting etc*)
* And much more!

With this being said, my actual responsibilities in this role were limited to tending to the Web-Service Help Queue, making edits to the portfolio of *.education.govt.nz* using their CMS systems, as well as assisting with testing to websites following feature releases or bug fixes.

During this role was the first time that I actually began "*working*" directly with data. I was assigned responsibility for managing the Ministry of Educations [Google Analytics Platform](https://developers.google.com/analytics), ensuring that traffic volume data, usage patterns and user journey information was recorded, and continually flowing. It was also during this time that I created my first dashboard using [Looker Studio](https://lookerstudio.google.com/navigation/reporting) (*which I believe was a further breakdown of a user-journey map for a specific .education.govt.nz site which I can no longer remember the name of*).

<!-- Ministry of Education Dashboards -->
{{< carousel images="{<https://i.imgur.com/0NPMDXA.png,https://i.imgur.com/5oBLzcC.png,https://i.imgur.com/Oxbmacj.png,https://i.imgur.com/JGQhcZd.png,https://i.imgur.com/eqiPb8l.png}>" captions="{<https://i.imgur.com/0NPMDXA.png:He> Pikorua Website Dashboard,<https://i.imgur.com/5oBLzcC.png:Kauwhata> Reo Website Dashboard,<https://i.imgur.com/Oxbmacj.png:MoE> Intranet Dashboard,<https://i.imgur.com/JGQhcZd.png:NCEA> Education Website Dashboard,<https://i.imgur.com/eqiPb8l.png:Kauwhata> Reo Website Dashboard}" >}}

After developing my first dashboard, I got bit with the "**data bug**", as there was just something so satisfying about the creation of something that could be both:

1) Technical.
2) Good to look at.

### Self Driven Data Studies 🔬

At a certain point, I hit some kind of constraint with what I could do with Looker Studio as a data-visualisation engine that I began looking into what else is possible in this space, wherein my world opened to a variety of new avenues.

* SQL
* Python
* Databases
* Data Modelling
* Business Intelligence / Data Visualisation (*PowerBI, Tableau etc*)
* Databricks
* Statistics
* UX / UI

It was from this point on that I decided to dedicate a decent portion of my free-time towards studying data, with my specific goal to become a Data Analyst. I'm always so proud when I look back on where I came from, to where I am, and what I can do today. I don't remember exactly how I got started in all of this, but I'm pretty sure I would have googled something along the lines of "*how to become a data analyst*".

<!-- TODO: Maybe an image here? -->

From there, I belive I would have got onto the [Roadmap.sh](https://roadmap.sh/dashboard) website, wherein I would have taken a look at some of the Data-Analysis roadmaps they have.

<!-- BI Analyst Roadmap -->
{{< accordion >}}
  {{< accordionItem title="BI Analyst Roadmap" icon="information-circle" >}}
  ![BI Analyst Roadmap](https://i.imgur.com/5CJr0v3.jpeg)
  {{< /accordionItem >}}
{{< /accordion >}}

<!-- TODO: Rewrite this -->
I would actually recommend that more people go-down a path of semi-self driven study, as I attribute this work with expanding my:

* Creativity
* Presentation
* Problem Solving
* Communications
* And Much more!

<!-- TODO: Early Career Skill-Maps -->
<!-- {{< carousel images="{<https://i.imgur.com/0NPMDXA.png,https://i.imgur.com/5oBLzcC.png,https://i.imgur.com/Oxbmacj.png,https://i.imgur.com/JGQhcZd.png,https://i.imgur.com/eqiPb8l.png}>" captions="{<https://i.imgur.com/0NPMDXA.png:He> Pikorua Website Dashboard,<https://i.imgur.com/5oBLzcC.png:Kauwhata> Reo Website Dashboard,<https://i.imgur.com/Oxbmacj.png:MoE> Intranet Dashboard,<https://i.imgur.com/JGQhcZd.png:NCEA> Education Website Dashboard,<https://i.imgur.com/eqiPb8l.png:Kauwhata> Reo Website Dashboard}" >}} -->

<!-- ### YouTube Channel 📹

* TODO

### Working at Meridian Energy 💼

* TODO

### The Future! 🔮

* TODO

## TODO

* **Need some kind of disclaimer about the data that I'm showing on this page**

* Self Driven Study
  * Roadmaps
  * Personal Skill Maps
  * Being made redudnant
* YouTube Channel
  * Graphic Design
  * Video Editing
  * Making Minecraft Videos
* Working at Meridian
  * Engineering
* The Future!
  * Travel
  * Scotland -->

<!-- TODO: Possibly add a custom colour and Icon to this (*to make it a bit more fancy*) -->
<!-- Anti AI Slop Sentiment -->
> [!IMPORTANT]
> Every line on this page is written by me. I do use AI assistance for the following:
>
> * Ideation
> * Code Generation
> * Spelling / Grammar
>
> But the words, opinions, and bad jokes are mine.
