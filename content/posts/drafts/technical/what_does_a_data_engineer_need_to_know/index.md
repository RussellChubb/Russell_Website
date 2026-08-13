---
title: "What does a Data-Engineer need to Know in 2026?"
draft: true
description: "In the year, 2026, what are the fundamentals that our Data-Engineers need to know?"
summary: "In the year, 2026, what are the fundamentals that our Data-Engineers need to know?"
date: 2026-08-13
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

## Overview 🎯

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

## My Data Engineering Roadmap 🗺️

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

The purpose of completing the CS-50 is that you're able to come out the other side with a introductory...

#### Grokking Algorithims

<!-- Notes -->
<!-- Do I need a reference to algorithmic complexity here? -->

<!-- Grokking Algo's Image -->
![Grokking Algorithims](https://m.media-amazon.com/images/I/81BdMC18EUL._AC_UF1000,1000_QL80_.jpg)

I've consistenly seen aditya bhargava's book, [Grokking Algorithims](https://www.google.com/url?sa=t&source=web&rct=j&url=https%3A%2F%2Fwww.amazon.com.be%2F-%2Fen%2FGrokking-Algorithms-illustrated-programmers-curious%2Fdp%2F1617292230&opi=89978449) reccomended for Data Structures and Algorithim Theory.

<!-- WHY? -->

<!-- Algorithms Theory and Practice Thomas -->
![Algorithims - Theory and Practice](https://i.ebayimg.com/00/s/MTYwMFgxNjAw/z/fRQAAeSwnxZpvBXS/$_57.PNG?set_id=880000500F)

However, I've also found that if you're slightly better than a complete beginner regarding Data Structures and Algorithims (*not me*), Thomas Cormen's book, [Algorithms - Theory and Practice](https://www.google.com/url?sa=t&source=web&rct=j&url=https%3A%2F%2Fwww.amazon.com%2FIntroduction-Algorithms-Thomas-H-Cormen%2Fdp%2F0070131430&opi=89978449) may be a much better use of your time.

#### LeetCode

<!-- LeetCode Image -->
![LeetCode](https://trypear.ai/images/leetcode.png)

<!-- Note -->
<!-- This needs to be re-written, the sentiment is correct, but the language needs tweaking -->

Welcome to the most controversial section of this article, where I recommend using LeetCode as a way to test whether you're actually understanding and retaining the concepts you're learning around Data Structures and Algorithms.

I'll note that I really don't think that LeetCode should be the way you learn DSA — it's much more useful as a place to apply and test what you've learned.

You can solve these problems in pretty much any language. I'll probably use Python, as it's the language I'm most comfortable with and lets me focus on the algorithm rather than the syntax.

It could be interesting to implement some of these structures and algorithms in a lower-level language such as C or C++. The reason for this is that submitting solutions in C or C++ exposes concepts that higher-level languages like Python tend to abstract away (*via a bunch of boilerplate*), particularly around memory and data representation.

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

Also, if you don't feel like reading the book, the author Jim Kurose, has actually [published videos onto YouTube](https://www.youtube.com/watch?v=74sEFYBBRAY), where he explains these concepts!

**NOTE:** I saw that one person in the comments of this video that Jim actually responded to him by email, replying to one of his questions. Which I personally think is really cool.

<!-- Jim Kurose Video -->
{{< youtubeLite id="74sEFYBBRAY" label="Jim the GOAT" >}}

<!-- WHY THE TOPDOWN -->

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

### Data Modelling

Once I understand the systems storing the data, I want to understand how we should structure the data itself. This is where the following concepts come into play:

* Fact tables
* Dimension tables
* Star schemas
* Snowflake schemas
* Normalisation
* Denormalisation
* Slowly Changing Dimensions
* Aggregate tables

I've encountered many of these concepts already, but there's a difference between recognising the terminology and being able to confidently design a model from scratch.

I'd like to get to the point where I can look at a messy collection of source tables and reason about:

* What should the model look like?
* Who is going to consume it?
* What should the grain be?
* What should be calculated upstream?
* What should be calculated downstream?
* How will this behave as the data grows?

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

## How do I plan to study all of these concepts?

It's all good and well for me to tell you what I'm going to study, but if you're in a similar situation to me, then you'll want to know where to go to study this kind of stuff, as well as what kind of stuff to study.

To answer the above simply, there is no one path that you need to follow to begin to learn. With this being said, I'll link to a few resources that I'll be using to up-skill.

<!-- No paths -->
![No Paths...](https://pbs.twimg.com/media/EcZrpA6XsAIFTcG.jpg)

### Data Engineer Zoomcamp

<!-- Notes -->
* Working my way through (*is his name Alexi?*)'s course right now.

### Creating and Sharing Content about my learning

<!-- Notes  -->
* Creating Videos, Articles
* Sharing content on Reddit, YouTube etc
* How the socratic method is particularly useful
* Being able to simplify concepts

### Certifications?

## Conclusion 🏁

<!-- Notes -->
* Taking my time, enjoying myself and not feeling rushed
* Learning in public
* Creating content to show-case my learning
* This article neglects the benefits of Soft-Skills, Presentation, Business Acumen / Context, but they are still as relevant as ever.

<!-- Subscribe Button -->
{{< subscribe >}}
