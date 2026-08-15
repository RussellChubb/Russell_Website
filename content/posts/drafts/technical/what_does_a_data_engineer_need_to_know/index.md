---
title: "2026 Data-Engineering Roadmap"
draft: true
description: "In the year, 2026, what are the fundamentals that Data-Engineers need to know?"
summary: "In the year, 2026, what are the fundamentals that Data-Engineers need to know?"
date: 2026-08-14
featureimage: "featured.jpg"
tags: ["Data Engineering", "Technical"]
---

{{< typeit
  tag=h4
  speed=80
  lifeLike=true
  breakLines=true
  loop=false
>}}
"It ain't what you don't know that gets you into trouble. It's what you know for sure that just ain't so." - Mark Twain
{{< /typeit >}}

---

## Introduction 🎯

One of the first things I did when I started studying to become a Data Analyst was try to answer a deceptively simple question:

<!-- What does a Data Analyst need to Know Lead -->
{{< lead >}}
> **What does a Data Analyst actually need to know?**
{{< /lead >}}

At the time, I was trying to make sense of a fairly broad field that was entirely new to me. There were terms like:

* SQL
* Python
* Statistics
* BI / Data Visualisation
* Data modelling
* Databases, and an ever-growing list of tools and technologies.

Now, a few years later (*and slightly more informed*), I'm finding myself asking a similar question again:

<!-- What does a Data Engineer need to Know Lead -->
{{< lead >}}
> **What does a Data Engineer actually need to know?**
{{< /lead >}}

<!-- Moeeee -->
![Wooooody](https://media2.giphy.com/media/v1.Y2lkPTZjMDliOTUyOHJ3bmNxcGljM3RkbnE4M3kzdmtiZ3ptdTRzaWhsODh4N3F4empsciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OWqbks1ewpnbWH6RtQ/giphy.gif)

I'm increasingly interested in moving into more technical work (*not that cutting my teeth as a Data-Analsyt isn't fun*) using different technologies and new skills to solve harder problems.

As such, the path I've chosen is that of the Data-Engineer, and therefore, I need to start thinking like a Data-Engineer, and understanding what I need to know to solve problems like one!

<!-- Matrix Meme -->
![Plumber hehe](https://karimjedda.com/content/images/2023/07/Screenshot-2023-07-15-at-16.01.04-2.png)

## 2026 Data Engineering Roadmap 🗺️

### Preface

Before I start, state three things:

1) This Roadmap assumes a certain level of confidence in some technologies, i.e. SQL, Python, Git, Liux etc - If you're just starting out in the "*tech-world*", I'd reccomend developing foundational knowledge in some of these technologies before jumping straight into this Roadmap!

2) If you disagree with anything I've posted in this article, feel free to email me to discuss, given I'm not a Data-Engineer, and only just learning about these topics, I'm in a posistion where mistakes could be made. As such, I'm happy to make amendments to this article as necessary.

3) Where possible, I try to reccomend a blended approach when it comes to learning, I think that a fatal mistake that you can make when trying to learn something is to never get your hand's dirty (*so to speak*), and to just consume content adjacent to what you're trying to learn.

With this being said, I reccomended a blended approach when it comes to some of the resources that I reccomened. I.e. You watch the CS-50 Bootcamp and instead of stopping there, you:

a) Create content sharing what you learned
b) Talk to interested folk about what you learned and how you can apply it
c) actually apply what you learned, create a small (*or big*) project etc

I've been trying to avoid approaching this as a list of technologies (*I know this is in contradiction with this article's thumbnail, but it was created in irony*). It's very easy to make a roadmap that looks like this:

<!-- Turn this into a Mermaid Chart -->
```text
Python
SQL
AWS
Docker
Kubernetes
Spark
Kafka
Airflow
Snowflake
dbt
Terraform
```

Which might make for a good CV keyword list, but it doesn't necessarily produce a deep understanding of Data Engineering.

<!-- Move this somewhere else -->
<!-- I am an expert meme -->
<!-- ![I am an expert mee](https://i.programmerhumor.io/2026/04 4c18f52c254c7f95f144fcb32f3852a5dd7602070c676b66daf397ee0d78eb2d.jpeg) -->

Instead, I'm approaching Data Engineering as a series of concepts, with the idea being that each layer builds on the one before it.

Starting out with... (*drum-roll*)

<!-- I removed this as it was getting too busy -->
<!-- wtf is this image lol
![crazy-eyes](https://4.bp.blogspot.com/-xPAO7FWpV4g/UwdYtr-Y8eI/AAAAAAAAAg4/fG58MVJBUtU/s1600/bigstock-Angry-African-Girl-Playing-Dru-22379981.jpg) -->

### Computer Science Foundations

I'm starting here because I don't actually have a Computer Science degree.

Although I've spent time "*programming*", I've mostly learned by building things and messing around, rather than through formal computer science education.

This has worked reasonably well so far, but I increasingly want to understand *why* the things I'm building work. As such, I want to fill in some of those foundational gaps.

Wile I'm not trying to become a Comp-Sci Graduate, I'll still be going after a few different methods (*some of which I'll link below*) to learn this content, while using programming as the thread to tie these concepts together.

<!-- Tower of Pisa -->
![Tower of Pisa](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgURtCNwnnaLH_jyL0yfftfGT4r9aOOKTYNurxjEcqh-TT8Lwj8rdRdlSuEhlNkJWSoYtfDNw564eVG4YIR76WoDMd3N29Wnzk-km77D-n62hRaWfHsEK5Z046Amy9uiFP5C6mf/s1600/9B3A668F-C79A-485B-B9EE-9513738A7547.jpeg)

Things like:

* Algorithms
* Data structures
* Complexity
* Memory
* Processes
* Threads
* Concurrency
* Networking
* Operating systems

<!-- Uni Comp Sci Course -->
![Course Overview](https://www.millersville.edu/computerscience/prereq/2020.05-csci.png)

#### Harvard CS50

<!-- CS50 -->
![CS50](https://i.ytimg.com/vi/LfaMVlDaQ24/maxresdefault.jpg)

Firstly, I'm going to be completing the [CS-50 Introduction to Computer Science](https://pll.harvard.edu/course/cs50-introduction-computer-science), which is a series of free lectures released by Harvard on an introduction to the intellectual enterprises of computer science and the art of programming.

(*Which I actually made a start on a long time ago, but never finished...*).

#### Grokking Algorithims

<!-- Notes -->
<!-- Do I need a reference to algorithmic complexity here? -->

<!-- Grokking Algo's Image -->
![Grokking Algorithims](https://m.media-amazon.com/images/I/81BdMC18EUL._AC_UF1000,1000_QL80_.jpg)

I've consistenly seen aditya bhargava's book, [Grokking Algorithims](https://www.google.com/url?sa=t&source=web&rct=j&url=https%3A%2F%2Fwww.amazon.com.be%2F-%2Fen%2FGrokking-Algorithms-illustrated-programmers-curious%2Fdp%2F1617292230&opi=89978449) reccomended for Data Structures and Algorithim Theory. With this being said, discussion online does seem to reflect that this is very much intended for beginners.

<!-- Algorithms Theory and Practice Thomas -->
![Algorithims - Theory and Practice](https://i.ebayimg.com/00/s/MTYwMFgxNjAw/z/fRQAAeSwnxZpvBXS/$_57.PNG?set_id=880000500F)

Thus, if you're slightly better than a complete beginner (*regarding Data Structures and Algorithims*) i.e., not me! - Thomas Cormen's book, [Algorithms - Theory and Practice](https://www.google.com/url?sa=t&source=web&rct=j&url=https%3A%2F%2Fwww.amazon.com%2FIntroduction-Algorithms-Thomas-H-Cormen%2Fdp%2F0070131430&opi=89978449) may be a much better use of your time.

#### LeetCode

<!-- LeetCode Image -->
![LeetCode](https://trypear.ai/images/leetcode.png)

Welcome to the most controversial section of this article, where I recommend using LeetCode as a way to test whether you're actually understanding and retaining the concepts you're learning around Data Structures and Algorithms.

> [!NOTE]
> I really don't think that LeetCode should be the way you learn DSA — it's much more useful as a place to apply and test what you've learned.

<!-- Which Language for LeetCode Disclaimer -->
{{< accordion mode="false" separated=true >}}
  {{< accordionItem title="Interesting Programming Language Sidenote" icon="code" open=false >}}
You could solve these coding problems in pretty much any language. I'll probably use Python, as it's the language I'm most comfortable with and lets me focus on the algorithm rather than the syntax.

However... It could be interesting to implement some of these structures and algorithms in a lower-level language such as C or C++.

The reason for this is that submitting solutions in C or C++ exposes concepts that higher-level languages like Python tend to abstract away (*via a bunch of boilerplate*), particularly around memory and data representation.
  {{< /accordionItem >}}
{{< /accordion >}}

I'd also like to be specific about what I'm going to be attempting, specifically, Navdeep Singh's [NeetCode 150](https://neetcode.io/practice/practice/coreSkills).

<!-- NeetCode 150 Image -->
![NeetCode150](https://miro.medium.com/v2/resize:fit:1400/1*MFPFgvCBftU2heYerQL9eQ.png)

The NeetCode 150 centers on a curated list of 150 LeetCode-style problems that target common coding interview patterns and data structures encountered in technical interviews.

The benefit to this approach is that rather than grinding through thousands of LeetCode problems without direction, you're able to work through this carefully selected subset, organized by difficulty.

Also, I like this list because I think that Navdeep passes the ["Would I have a beer with you" test](https://en.wikipedia.org/wiki/Beer_question).

<!-- Move this around somewhere else -->
<!-- Leet Code Meme -->
<!-- ![Leet Code Meme](https://i.programmerhumor.io/2025/05/7f44339c9eb11eff85568ec27867eb7e77ba206db6510cc9af1687589d441276.jpeg) -->

#### OSTEP

<!-- OSTEP Image -->
![OSTEP](https://rezised-images.knhbt.cz/1920x1920/34147928.jpg)

[OSTEP Operating Systems: Three Easy Pieces - For learning about Operating Systems](https://pages.cs.wisc.edu/~remzi/OSTEP/) (*or the Comet Book*) is centered around three conceptual pieces that are fundamental to operating systems:

* virtualization
* concurrency
* persistence

So, why OSTEP for learning about computer operating systems? Well to be blunt, OSTEP is [widely considered one of the best computer science textbooks ever written](https://www.reddit.com/r/compsci/comments/1bjwv4l/how_do_i_break_down_operating_systems_three_easy/), I haven't even mentioned that it's free either (*accessible via the link above!*)

Off-topic, but I also enjoyed Remzi Arpaci-Dusseau's article on [why text-books should be free](https://from-a-to-remzi.blogspot.com/2014/01/the-case-for-free-online-books-fobs.html) - Well worth a read if you have the time!

#### Computer Networking: A Top-Down Approach

<!-- Sloppy Toppy Approach -->
![Top Down](https://m.media-amazon.com/images/I/71sqPf9w2hL._UF1000,1000_QL80_.jpg)

[Networking: Computer Networking A Top-Down Approach](https://www.amazon.com/Computer-Networking-Top-Down-Approach-7th/dp/0133594149) by Jim Kurose and Keith W. Ross is another seminal text in the field of Computer Science, and is [widely reccomended](https://www.reddit.com/r/computerscience/comments/1iijm8a/computer_netwroks_a_top_down_approach/) read for Computer Science students.

Also, if you don't feel like reading the book, the author Jim Kurose, has actually [published videos onto YouTube](https://www.youtube.com/watch?v=74sEFYBBRAY&list=PL1ya5dD_M8uX-BLUF1FEvUNsYWQL5_l0O), where he explains these concepts!

> [!NOTE]
> I saw that one person in the comments of this video that Jim actually responded to him by email, replying to one of his questions.
> Which I personally think is really cool.

<!-- Jim Kurose Video -->
{{< youtubeLite id="74sEFYBBRAY" label="Jim the GOAT" >}}

### Databases

I've used SQL for years, but knowing SQL and understanding databases are two very different things. I want to move beyond the basics (*i.e.*):

```sql
SELECT *
FROM table
WHERE ...
```

and begin to understand what happens after I press enter, for example:

* How is the query parsed?
* How does the database decide how to execute it?
* What is an execution plan?
* How do indexes work?
* Why are some queries fast and others slow?
* What are transactions?
* What does ACID actually mean?
* How does concurrency work?
* What is MVCC?
* How does a database store data on disk?
* What happens when the database crashes?

Now, as far as the "*how am I going to learn about Databases*", I'm going to reccomend the following resources below:

#### Use the Index Luke

<!-- Use the Index Luke -->
![Use the Index Luke](https://use-the-index-luke.com/static/shop-sticker.HtqZbaZO.jpg)

Use The Index, Luke is the free web-edition of Markus Winand's book [SQL Performance Explained](https://sql-performance-explained.com/), with the biggest strength of the website being that it teaches you to think about SQL as something executed by a database engine, rather than just a language you use to retrieve data.

> [!TIP]
> From the discourse I see online about the book, I gather that Winand has a **very** strong developer-centric perspective, and the book occasionally presents concepts in a deliberately simplified or provocative way.
> Given I haven't actually read the book, I can't weigh in on this further, and while this critiscm may prove true, the content of the book is still too valuable to not include.

#### Database Internals

<!-- Database Internals -->
![Database Internals](https://images.openai.com/static-rsc-4/KoBMLjZyflHz7eP_YWCwHuyzA_YAbmYqQChDiTU0PrYSY5Npaa9s_ydlHimqvSptP4fA-F2Qwbwn3MOqWMK4zSiSm9PWG1vh8ZFy1WqVoIx2K3WemAseulljS2-JuBAO3WzH2_sctrMeJFVcscWw-HMOMhthoG9ZHV21NRr7NiGKOCl9h9kQcvz_dckNG8zZ?purpose=fullsize) by Alex Petrov, is widely reccomended in Data-Engineering circles, however, the book is fairly dense, a couple of dudes on Reddit reccomended taking like 6 months to read it, first give it a skim, then come back at it with a fine tooth comb.

While researching, I also found a great series of lectures on Database Internals on YouTube from a bloke named Professor [Andy Pavlo](https://www.youtube.com/watch?v=LWS8LEQAUVc&list=PLSE8ODhjZXjYzlLMbX3cR0sxWnRM7CLFn&index=1).

<!-- Andy Pavlo Video -->
{{< youtubeLite id="LWS8LEQAUVc" label="Anduxxx" >}}

#### Designing Data Intesive Applications

<!-- Managed to find one with both! -->
![DDIA](https://pbs.twimg.com/media/HG8iMwha8AA7Pzl.jpg)

[Designing Data Intensive Applications](https://0-lucas.github.io/digital-garden/99.-Books/Martin-Kleppmann---Designing-Data-Intensive-Applications_-O%E2%80%99Reilly-Media-(2017).pdf) by Martin Kleppmann is another one of these "*dense*" books, that is almost a right-of-passage in the Data-Engineering community. Once again, a couple blokes on Reddit just reccomended taking your time with the book and being methodical.

<!-- Build things Admonition -->
> [!TIP]
> **Build things and / or mess around with concepts!**
> Now is a good time to remind everyone that we aren't just reading these books! - We need to apply what we've actually learned!

### Data Modelling

Once I understand the systems storing the data, I want to understand how the data itself should be structured.

This is where data modelling comes into play. The goal isn't just to know what a fact table or dimension table is, but to be able to look at a messy collection of source tables and reason about what the resulting model should look like.

Some of the concepts I'll cover include:

* Fact tables
* Dimension tables
* Star schemas
* Snowflake schemas
* Normalisation & Denormalisation
* Slowly Changing Dimensions
* Aggregate tables

If you've worked as a Data Analyst, or in some kind of BI-adjacent role, you've probably encountered some of these concepts already.

Ultimately, I'd like to be able to look at a collection of source tables and answer questions like:

What should the model look like?
Who is going to consume it?
What should the grain be?
What should be calculated upstream?
What should be calculated downstream?
How will the model behave as the data grows?
How should changes to the underlying data be handled over time?
Start With the Business

#### Business Analysis for Data-Engineers

Before deciding whether something should be a fact table, dimension, aggregate, or something else, we first need to understand what the data is supposed to represent.

This is where Data Engineering overlaps with Business Analysis. You don't need to become a Business Analyst, but you do need to be able to translate business requirements into data requirements.

When presented with a messy collection of source tables, we should be able to ask:

* Who will consume this data?
* What decisions are they trying to make?
* What questions does the data need to answer?
* What are the important business processes and events?
* What do important business terms actually mean?
* What does a "customer", "order", "sale", or "active user" actually represent?
* What level of freshness is required?
* How much historical data needs to be retained?
* What does "correct" data look like?
* What edge cases or business rules need to be accounted for?

These questions come before designing the model.

For example, being told "*we need a sales dataset*" isn't enough to design a model. The consumer might want to analyse individual transactions, daily store performance, customer behaviour, sales targets, or some combination of these.

Those requirements ultimately determine things like the grain, entities, relationships, metrics, history, and transformations in the resulting data model.

So, how are we going to learn all of this?

#### Fundamentals of Data Engineering

<!-- Fundamentals of Data Engineering Image -->
![Fundamentals of Data Engineering](https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1654271050i/61218623.jpg)

[Fundamentals of Data Engineering](https://www.amazon.com/Fundamentals-Data-Engineering-Robust-Systems/dp/1098108302/)

### Distributed Systems

A lot of the problems in modern Data Engineering exist because **one computer isn't enough**. If I have a few thousand rows, almost anything will work, however, what happens when the data grows, think 1 Million, 1 Billion, 10 Trillion - **What happens then?**

At some point, I need multiple machines. And as soon as I have multiple machines, I inherit a whole new category of problems.

* Machines fail.
* Networks fail.
* Messages arrive late.
* Machines disagree.
* Data needs to be replicated.
* Work needs to be partitioned.
* Different machines need to coordinate.

These problems inevitabily lead into concepts like:

* Partitioning
* Replication
* Fault tolerance
* Consistency
* Availability
* CAP theorem
* Consensus
* Distributed transactions
* Eventual consistency

These are concepts that sit underneath a huge amount of modern Data Engineering infrastructure. Understanding them should make technologies like Spark, Kafka and distributed databases feel much less magical.

### Data Systems

Once the foundations are in place, I want to understand how the pieces come together to form actual data systems. This is where the abstract concepts become something resembling a Data Engineer's day-to-day work.

For example:

```text
API
 ↓
Ingestion
 ↓
Object Storage
 ↓
Transformation
 ↓
Warehouse
 ↓
Data Model
 ↓
Analytics / ML
 ↓
Application
```

And then all the unpleasant questions appear:

* What happens if the API goes down?
* What if we receive the same record twice?
* What if yesterday's data arrives tomorrow?
* What if the schema changes?
* What if a transformation fails halfway through?
* Can I safely rerun it?
* How do I backfill three years of historical data?
* How do I know whether the pipeline is working?
* How do I know whether the data is correct?

This is where the following ideas become important:

* Idempotency
* Retries
* Backfills
* Data quality
* Data contracts
* Schema evolution
* Lineage
* Observability
* SLAs

### Cloud and Infrastructure

Modern data systems rarely live on a laptop, so eventually I need to understand the infrastructure they run on. This is where the following things come into the picture like:

* Cloud storage
* Compute
* Containers
* Docker
* Networking
* Infrastructure as Code
* CI/CD
* Secrets
* Permissions
* Orchestration

### Production Engineering

Building something that works is one thing. Building something that **continues working** is another. Production Engineering is where I want to learn about:

* Monitoring
* Logging
* Alerting
* Reliability
* Incident response
* Testing
* Deployment
* Rollbacks
* Capacity planning
* Performance
* Security
* Cost

<!-- Removed the section where I talk about the fact that there is no set paths -->
<!-- No paths Image -->
<!-- ![No Paths...](https://pbs.twimg.com/media/EcZrpA6XsAIFTcG.jpg) -->

## Other useful Data-Engineering Resources

### Data Engineer Zoomcamp

<!-- Alexi's Zoomcamp Repo -->
{{< github repo="ziritrion/dataeng-zoomcamp" showThumbnail=true >}}

### Data Engineer Wiki

[Data Engineering Wiki](https://dataengineering.wiki/Guides/Getting+Started+With+Data+Engineering)

### Data Engineering Cookbook

<!-- Data Engineering Cookbook -->
{{< github repo="andkret/Cookbook" showThumbnail=true >}}

### Data Engineer Handbook

<!-- Data Engineering Handbook -->
{{< github repo="DataExpert-io/data-engineer-handbook" showThumbnail=true >}}

### Data Engineering for Begineers

[Data Engineering for Beginners](https://de101.startdataengineering.com/)

### Missing Semester

[Missing Semester](https://missing.csail.mit.edu/) - I love this website, it doesn't really fit in anywhere super well, but I thought it needed a reference as Anish, Jon, and Jose have put in a lot of effort into the website, and learning content.

<!-- Removing this section, might add it back -->
<!-- ### Creating and Sharing Content about my learning -->

<!-- Notes  -->
<!-- * Creating Videos, Articles
* Sharing content on Reddit, YouTube etc
* How the socratic method is particularly useful (*What I mean by this, is that you need to be able to talk about something in order to prove understanding*)
* Being able to simplify concepts (*The ability to simplify a complex concept demonstrates deep understanding of topics*) -->

## Data Engineering Certifications

![Databricks Data Engineering](https://www.flexera.com/blog/wp-content/uploads/chaosgenius/images/2024/04/Databricks-Certification-11.png)

The only Data-Engineering Certificate's I'm going to go after are as follows:

* Databricks - Data Engineer Associate
* Databricks - Data Engineer Professional

The reason for this is that I've already worked with Databricks and had exposure to some Data-Engineering on the Azure Databricks platform.

> [!NOTE]
> At $200 NZD a pop for each of these two certifications, Databricks (*Microslop*) sure know's how to pull money from wallets.

With this being said, there are also the following *other* options for certification, and feel free to choose one that works best for you:

* Databricks - Certified Associate Developer for Apache Spark
* Google Cloud Certified - Professional Data Engineer
* Microsoft DP-600: Fabric Analytics Engineer Associate
* Microsoft DP-700: Fabric Data Engineer Associate
* AWS Certified Data Engineer - Associate

## Useful Media Personalities in the Data-Engineering Space

### Benjamin Rogojan (Seattle Data Guy)

<!-- Ben R Image -->
![Ben R](https://image-cdn-fa.spotifycdn.com/image/ab6772ab000016927c11db3b538733ea19221131)

[Benjamin Rogojan (*Seattle Data Guy*)](https://www.youtube.com/c/SeattleDataGuy)

### Alexey Grigorev (DataTalksClub)

<!-- Alexey Image -->
![Alexey](https://zdpdvwhvukelzzbzbjvh.supabase.co/storage/v1/object/public/imported-images/1769001998128-2ef08000-fe57-41e8-b401-7123e45bddf3-klj3bt.webp)

[Alexey Grigorev](https://www.youtube.com/@DataTalksClub)

### Ben Dickens

<!-- Benny D Image -->
![Benny D](https://benjdd.com/assets/ben-pfp-2025.jpg.jpg)

[Ben Dickens](https://benjdd.com/)

#### Joseph Machado (Start Data Engineering)

<!-- Start Data Engineering Image -->
![Joseph](https://pbs.twimg.com/profile_images/1552078944941342720/ni4XppfU_400x400.jpg)

Joseph is a veteran of the industry with 15 + YOE (*Years of Experience*) and frequently writes, posts, and comments on different facets of the Data-Engineering eco-system!

This, and the fact that I like his website, and writing style, meant that this he was always getting a mention in this article. Also, from his Reddit AMA, he seems like a really chill guy!

[Start Data Engineering](https://www.startdataengineering.com/?utm_source=chatgpt.com) is a super dope resource for any apsiring, or current data-engineers.

### Data with Zach

<!-- Big man Zach -->
![Zach](https://yt3.googleusercontent.com/DYDO-RWcu7qVkpokWkBe6-yTuY-F2sz7-ParNy5iH1SJRTLNFY36eZOiKjtOp1qoYUPXMIrWFg=s900-c-k-c0x00ffffff-no-rj)

[Data with Zach](https://www.youtube.com/c/datawithzach)

<!-- Data with Zach Disclaimer -->
{{< accordion mode="false" separated=true >}}
  {{< accordionItem title="Data with Zach Disclaimer" icon="code" open=false >}}
  You can't fault Zach on his technical knowledge, but I wouldn't necessarily take his broader opinions as gospel.

  Zach is an incredibly frequent poster, and his content can sometimes veer into what I'd consider classic LinkedIn cringe culture. He also frequently talks about his earnings and makes some fairly strong non-technical claims that I don't necessarily agree with.

  That said, his technical material is often genuinely excellent, and that's the reason I've included some of it here.
  {{< /accordionItem >}}
{{< /accordion >}}

## Conclusion 🏁

If you've made it this far, you'll probably have noticed that this isn't really a roadmap for learning a bunch of technologies. I'm much more interested in developing a **mental model for how data systems work**, and then using that understanding to decide which tools are appropriate for a particular problem.

I'm also not in any rush. I'll be learning, building things, writing about what I learn, and inevitably discovering things I've got wrong along the way.

And while this roadmap focuses heavily on the technical side of Data Engineering, being a good Data Engineer isn't just about technical knowledge. **Communication, presentation, business context, and domain knowledge are just as important.**

For now, I'm going to take my time, enjoy the process, and see where it takes me. I suspect I'll be updating this roadmap for quite some time.

<!-- Subscribe Button -->
{{< subscribe >}}
