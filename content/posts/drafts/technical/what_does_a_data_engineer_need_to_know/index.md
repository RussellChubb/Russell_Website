---
title: "2026 Data Engineering Roadmap"
draft: true
description: "In the year, 2026, what are the fundamentals that Data Engineers need to know?"
summary: "In the year, 2026, what are the fundamentals that Data Engineers need to know?"
date: 2026-08-24
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

## Introduction 🎯

One of the first things I did when I started studying to become a Data Analyst was try to answer a deceptively simple question:

<!-- What does a Data Analyst need to Know Lead -->
{{< lead >}}
> **What does a Data Analyst actually need to know?**
{{< /lead >}}

After researching this question, I was left trying to make sense of a fairly broad field that was entirely new to me.

There were terms like:

- SQL
- Python
- Statistics
- BI / Data Visualisation
- Data modelling
- Databases, and an ever-growing list of tools and technologies.

Now, a few years later (*and slightly more informed*), I'm finding myself asking a similar question again:

<!-- What does a Data Engineer need to Know Lead -->
{{< lead >}}
> **What does a Data Engineer actually need to know?**
{{< /lead >}}

<!-- Moeeee -->
![Wooooody](https://media2.giphy.com/media/v1.Y2lkPTZjMDliOTUyOHJ3bmNxcGljM3RkbnE4M3kzdmtiZ3ptdTRzaWhsODh4N3F4empsciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OWqbks1ewpnbWH6RtQ/giphy.gif)

## Why do I care? ❓

I'm increasingly interested in moving into more technical work (*not that cutting my teeth as a Data Analyst isn't fun*) using different technologies and new skills to solve harder problems.

As such, the path I've chosen is that of the "*Data Engineer*"! Therefore, I need to develop some kind of roadmap to understand what I need to learn to solve Data Engineering Problems.

<!-- Matrix Meme -->
![Plumber hehe](https://karimjedda.com/content/images/2023/07/Screenshot-2023-07-15-at-16.01.04-2.png)

## TLDR 📋

If you really don't want to read the article, and instead just want to see the resources I've recomended, here's the condensed version:

Task Status Key:

- Not Started (❌)
- In Progress (🚧)
- Completed (✅)

### Books 📚

| Title | Author | Status |
| --- | --- | --- |
| Grokking Algorithms | Aditya Bhargava | ❌ |
| Algorithms - Theory and Practice | Thomas Cormen | ❌ |
| OSTEP: Operating Systems - Three Easy Pieces | Remzi & Andrea Arpaci-Dusseau | ❌ |
| Computer Networking: A Top-Down Approach | Kurose & Ross | ❌ |
| Use The Index, Luke (SQL Performance Explained) | Markus Winand | ❌ |
| Database Internals | Alex Petrov | ❌ |
| Designing Data-Intensive Applications | Martin Kleppmann | ❌ |
| Fundamentals of Data Engineering | Reis & Housley | ❌ |
| Site Reliability Engineering | Google | ❌ |

### Courses / Certifications / Misc 🎓

| Task | Provider | Status |
| --- | --- | --- |
| CS50: Introduction to Computer Science | Harvard | ❌ |
| Data Engineering Zoomcamp | DataTalksClub | 🚧 |
| AWS Well-Architected Framework | AWS | ❌ |
| Blind 75 | NeetCode | ❌ |
| Data Engineer Associate | Databricks | ❌ |
| Data Engineer Professional | Databricks | ❌ |

## Preface 💬

Before I start, I'll state two things:

1) This roadmap assumes competency in certain technologies, i.e. SQL, Python, Git, Linux etc - If you're just starting out in the "*tech-world*", I'd recommend developing foundational knowledge in some of these technologies before jumping straight into this Roadmap!

2) If you disagree with anything I've posted in this article, feel free to email me to discuss, given I'm not a Data Engineer, and only just learning about these topics, I'm in a position where mistakes could be made. As such, I'm happy to make amendments to this article as necessary.

### How I'm going to learn 💡

Where possible, I recommend a blended approach when it comes to learning.

The most fatal mistake when learning something new is to never get your hands dirty (*so to speak*), and to just consume content adjacent to what you're trying to learn.

So what do I mean when I say a "*blended*" approach? Well, instead of just watching the lectures or completing the readings, you also:

1) Create content sharing what you learned.
2) Talk to interested folk about what you learned and how you aim to apply it.
3) Actually apply what you learned, create a small (*or big*) project etc.

### How this road-map might differ to other courses? 🆚

From my research, I see quite a few Data Engineering courses that approach learning Data Engineering as a list of technologies to learn, (*which might look like something like the below*):

<!-- Turn this into a Mermaid Chart -->
<!-- ```text
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
``` -->

<!-- Mermaid Chart for Technology Stack -->
{{< mermaid >}}
graph TD
    A[Python]
    B[SQL]

    C[AWS]
    D[Docker]
    E[Kubernetes]
    F[Terraform]

    G[Spark]
    H[Kafka]
    I[Airflow]

    J[Snowflake]
    K[dbt]

    A --> G
    A --> I
    B --> J
    B --> K

    D --> E
    F --> C
    C --> D

    G --> C
    H --> G
    I --> C
    J --> C
    K --> J
{{< /mermaid >}}

This approach might make for a good CV keyword list, but it doesn't necessarily produce a deep understanding of Data Engineering.

<!-- Move this somewhere else -->
<!-- I am an expert meme -->
<!-- ![I am an expert mee](https://i.programmerhumor.io/2026/04 4c18f52c254c7f95f144fcb32f3852a5dd7602070c676b66daf397ee0d78eb2d.jpeg) -->

Instead, I'm approaching Data Engineering as a series of concepts, with the idea being that each layer builds on the one before it.

Starting out with... (*drum-roll*)

<!-- I removed this as it was getting too busy -->
<!-- wtf is this image lol
![crazy-eyes](https://4.bp.blogspot.com/-xPAO7FWpV4g/UwdYtr-Y8eI/AAAAAAAAAg4/fG58MVJBUtU/s1600/bigstock-Angry-African-Girl-Playing-Dru-22379981.jpg) -->

## Computer Science Foundations

I'm starting here because I don't actually have a Computer Science degree.

Although I've spent time "*programming*", I've mostly learned by building things and messing around, rather than through formal computer science education.

This has worked reasonably well so far, but I increasingly want to understand *why* the things I'm building work. As such, I need to fill in some of those foundational gaps.

Now, while I'm not trying to become a Comp Sci Graduate, I'll be utilizing a few *classic* University resources to learn about Computer Science Foundations, while utilizing programming as a thread to apply these learnings.

<!-- Removed this as I had too many images already -->
<!-- Tower of Pisa -->
<!-- ![Tower of Pisa](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgURtCNwnnaLH_jyL0yfftfGT4r9aOOKTYNurxjEcqh-TT8Lwj8rdRdlSuEhlNkJWSoYtfDNw564eVG4YIR76WoDMd3N29Wnzk-km77D-n62hRaWfHsEK5Z046Amy9uiFP5C6mf/s1600/9B3A668F-C79A-485B-B9EE-9513738A7547.jpeg) -->

The resources that I've linked below will allow us to learn about concepts like:

- Algorithms
- Data structures
- Complexity
- Memory
- Processes
- Threads
- Concurrency
- Networking
- Operating systems

<!-- Computer Science Learning Map -->
{{< mermaid >}}
graph TD
    CS[Computer Science Foundations]

    CS --> A[Algorithms]
    CS --> DS[Data Structures]
    CS --> C[Complexity]
    CS --> M[Memory]
    CS --> P[Processes]
    CS --> T[Threads]
    CS --> CO[Concurrency]
    CS --> N[Networking]
    CS --> OS[Operating Systems]

    A --> C
    DS --> A
    M --> P
    P --> T
    T --> CO
    P --> OS
    T --> OS
    CO --> OS
    N --> OS
{{< /mermaid >}}

<!-- Uni Comp Sci Course -->
![Course Overview](https://www.millersville.edu/computerscience/prereq/2020.05-csci.png)

### Harvard CS50

<!-- CS50 -->
![CS50](https://i.ytimg.com/vi/LfaMVlDaQ24/maxresdefault.jpg)

I'm going to be completing the [CS-50 Introduction to Computer Science](https://pll.harvard.edu/course/cs50-introduction-computer-science), which is a series of free lectures released by Harvard on an introduction to the intellectual enterprises of computer science and the art of programming.

(*Which I actually made a start on a long time ago, but never finished...*)

### Grokking Algorithms

<!-- Grokking Algo's Image -->
![Grokking Algorithms](https://m.media-amazon.com/images/I/81BdMC18EUL._AC_UF1000,1000_QL80_.jpg)

I've consistently seen Aditya Bhargava's book, [Grokking Algorithms](https://www.google.com/url?sa=t&source=web&rct=j&url=https%3A%2F%2Fwww.amazon.com.be%2F-%2Fen%2FGrokking-Algorithms-illustrated-programmers-curious%2Fdp%2F1617292230&opi=89978449) recommended for Data Structures and Algorithm Theory.

> [!NOTE]
> [Discussion online](https://www.reddit.com/r/leetcode/comments/1f5ofaf/thoughts_on_grokking_algorithms/) does seem to suggest that Grokking Algorithms is very much intended for beginners. However, if you want to get your feet wet, then this is appropriate!

<!-- Algorithms Theory and Practice Thomas -->
![Algorithms - Theory and Practice](https://i.ebayimg.com/00/s/MTYwMFgxNjAw/z/fRQAAeSwnxZpvBXS/$_57.PNG?set_id=880000500F)

If you've already read Grokking Algorithms and/or are slightly more competent with DSA (*Data Structures and Algorithms*) i.e., not me! - Thomas Cormen's book, [Algorithms - Theory and Practice](https://www.google.com/url?sa=t&source=web&rct=j&url=https%3A%2F%2Fwww.amazon.com%2FIntroduction-Algorithms-Thomas-H-Cormen%2Fdp%2F0070131430&opi=89978449) may be a much better use of your time.

### LeetCode / NeetCode

<!-- LeetCode Image -->
![LeetCode](https://trypear.ai/images/leetcode.png)

Welcome to the most controversial section of this article, where I recommend using LeetCode as a way to test whether you're actually understanding and retaining the concepts you're learning around Data Structures and Algorithms.

Now, if you've never heard of LeetCode (*or NeetCode*) it's a platform for practising programming problems, particularly algorithms and data structures, commonly used in **software engineering interviews**.

These problems range from simple exercises to extremely difficult problems and is primarily useful for developing problem-solving skills and **interview readiness**.

> [!NOTE]
> I really don't think that LeetCode should be the way you learn DSA — it's much more useful as a place to apply and test what you've learned.

<!-- Which Language for LeetCode Disclaimer -->
{{< accordion mode="false" separated=true >}}
  {{< accordionItem title="Which Programming Language should I solve problems in?" icon="code" open=false >}}
You could solve these coding problems in pretty much any language. I'll probably use Python, as it's the language I'm most comfortable with and lets me focus on the algorithm rather than the syntax.

However... It could be interesting to implement some of these structures and algorithms in a lower-level language such as C or C++.

The reason for this is that submitting solutions in C or C++ exposes concepts that higher-level languages like Python tend to abstract away (*via a bunch of boilerplate*), particularly around memory and data representation.
  {{< /accordionItem >}}
{{< /accordion >}}

<!-- NeetCode Blind 75 Image -->
![NeetCodeBlind75](https://miro.medium.com/v2/resize:fit:1400/1*MFPFgvCBftU2heYerQL9eQ.png)

I'd also like to be specific about what I'm going to be attempting, specifically, Navdeep Singh's [NeetCode Blind 75](https://neetcode.io/practice/practice/coreSkills).

The NeetCode Blind 75 centers on a curated list of 75 LeetCode-style problems that target common coding interview patterns and data structures encountered in technical interviews.

The benefit of this approach is that rather than grinding through thousands of LeetCode problems without direction, you're able to work through this carefully selected subset, organized by difficulty.

Also, I like this list because I think that Navdeep passes the ["Beer Test"](https://en.wikipedia.org/wiki/Beer_question).

<!-- Move this around somewhere else -->
<!-- Leet Code Meme -->
<!-- ![Leet Code Meme](https://i.programmerhumor.io/2025/05/7f44339c9eb11eff85568ec27867eb7e77ba206db6510cc9af1687589d441276.jpeg) -->

### OSTEP

<!-- OSTEP Image -->
![OSTEP](https://rezised-images.knhbt.cz/1920x1920/34147928.jpg)

[OSTEP Operating Systems: Three Easy Pieces - For learning about Operating Systems](https://pages.cs.wisc.edu/~remzi/OSTEP/) (*or the Comet Book*) is centered around three conceptual pieces that are fundamental to operating systems:

- virtualization
- concurrency
- persistence

So, why OSTEP for learning about computer operating systems? Well to be blunt, OSTEP is [widely considered one of the best computer science textbooks ever written](https://www.reddit.com/r/compsci/comments/1bjwv4l/how_do_i_break_down_operating_systems_three_easy/). I haven't even mentioned that it's free (*accessible via the link above!*)

Off-topic, but I also enjoyed Remzi Arpaci-Dusseau's article on [why textbooks should be free](https://from-a-to-remzi.blogspot.com/2014/01/the-case-for-free-online-books-fobs.html) - Well worth a read if you have the time!

### Computer Networking: A Top-Down Approach

<!-- Sloppy Toppy Approach -->
![Top Down](https://m.media-amazon.com/images/I/71sqPf9w2hL._UF1000,1000_QL80_.jpg)

[Networking: Computer Networking A Top-Down Approach](https://www.amazon.com/Computer-Networking-Top-Down-Approach-7th/dp/0133594149) by Jim Kurose and Keith W. Ross is another seminal text in the field of Computer Science, and is a [widely recommended](https://www.reddit.com/r/computerscience/comments/1iijm8a/computer_netwroks_a_top_down_approach/) read for Computer Science students.

Also, if you don't feel like reading the book, Jim has actually [published videos onto YouTube](https://www.youtube.com/watch?v=74sEFYBBRAY&list=PL1ya5dD_M8uX-BLUF1FEvUNsYWQL5_l0O), where he explains these concepts, through a series of free lectures!

> [!NOTE]
> One person in the comments of this video that Jim actually responded to him by email, replying to one of his questions.
> Which I personally think is really cool.

<!-- Jim Kurose Video -->
{{< youtubeLite id="74sEFYBBRAY" label="Jim the GOAT" >}}

## Databases

Why do we need to know about Databases? Well, even though this is my msot common SQL Query:

```sql
SELECT *
FROM table
WHERE ...
```

Knowing SQL and understanding databases are two very different things. What I mean by this is that I want to move beyond the basics and begin to understand what happens under the hood, after I press enter.

<!-- - How is the query parsed?
- How does the database decide how to execute it?
- What is an execution plan?
- How do indexes work?
- Why are some queries fast and others slow?
- What are transactions?
- What does ACID actually mean?
- How does concurrency work?
- What is MVCC?
- How does a database store data on disk?
- What happens when the database crashes? -->

<!-- Database Action Flow Mermaid -->
{{< mermaid >}}

flowchart TD

A["SQL Query"] --> B["Query Parsing"]

B --> C["Query Optimisation"]

C --> D["Execution Plan"]

D --> E["Query Execution"]

E --> F["Indexes & Access Paths"]

F --> G["Storage Engine"]

G --> H["Pages / Disk"]

E --> I["Transactions & ACID"]

I --> J["Concurrency"]

J --> K["MVCC"]

H --> L["Write-Ahead Log"]

L --> M{"Database Crash?"}

M -->|No| N["Commit"]

M -->|Yes| O["Recovery"]

O --> N

{{< /mermaid >}}

Now, as far as the "*how am I going to learn about Databases*", I'm going to recommend the following resources below:

### Use the Index Luke

<!-- Use the Index Luke -->
![Use the Index Luke](https://use-the-index-luke.com/static/shop-sticker.HtqZbaZO.jpg)

Use The Index, Luke is the free web-edition of Markus Winand's book [SQL Performance Explained](https://sql-performance-explained.com/).

The websites biggest strength is that it teaches you to think about SQL as something executed by a database engine, rather than just a language you use to retrieve data.

> [!NOTE]
> From the discourse I see online about the book, I gather that Winand has a **very** strong developer-centric perspective, and the book occasionally presents concepts in a deliberately simplified or provocative way.
> Given I haven't actually read the book, I can't weigh in on this further, and while this criticism may prove true, the content of the book is still too valuable to not include.

### Database Internals

<!-- Database Internals -->
![Database Internals](https://images.openai.com/static-rsc-4/KoBMLjZyflHz7eP_YWCwHuyzA_YAbmYqQChDiTU0PrYSY5Npaa9s_ydlHimqvSptP4fA-F2Qwbwn3MOqWMK4zSiSm9PWG1vh8ZFy1WqVoIx2K3WemAseulljS2-JuBAO3WzH2_sctrMeJFVcscWw-HMOMhthoG9ZHV21NRr7NiGKOCl9h9kQcvz_dckNG8zZ?purpose=fullsize)

[Database Internals](https://www.databass.dev/) by Alex Petrov, is widely recommended in Data Engineering circles, however, the book is fairly dense, a couple of dudes on Reddit recommended taking like 6 months to read it, first giving it a skim, then coming back to it with a fine-tooth comb.

While researching, I also found a great series of lectures on Database Internals on YouTube from a bloke named Professor [Andy Pavlo](https://www.youtube.com/watch?v=LWS8LEQAUVc&list=PLSE8ODhjZXjYzlLMbX3cR0sxWnRM7CLFn&index=1).

<!-- Andy Pavlo Video -->
{{< youtubeLite id="LWS8LEQAUVc" label="Anduxxx" >}}

### Designing Data Intensive Applications

<!-- Managed to find one with both! -->
![DDIA](https://pbs.twimg.com/media/HG8iMwha8AA7Pzl.jpg)

[Designing Data Intensive Applications](https://0-lucas.github.io/digital-garden/99.-Books/Martin-Kleppmann---Designing-Data-Intensive-Applications_-O%E2%80%99Reilly-Media-(2017).pdf) by Martin Kleppmann is another one of these "*dense*" books, that is almost a rite of passage in the Data Engineering community. Once again, a couple blokes on Reddit just recommended taking your time with the book and being methodical.

<!-- Build things Admonition -->
> [!TIP]
> **Build things and / or mess around with concepts!**
> Now is a good time to remind everyone that we aren't just reading these books! - We need to apply what we've actually learned!

## Data Modelling

Once I understand the systems storing the data, I want to understand how the data itself should be structured.

This is where data modelling comes into play. The goal isn't just to know what a fact table or dimension table is, but to be able to look at a messy collection of source tables and reason about what the resulting model should look like.

Some of the concepts I'll cover include:

- Fact tables
- Dimension tables
- Star schemas
- Snowflake schemas
- Normalisation & Denormalisation
- Slowly Changing Dimensions
- Aggregate tables

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

### Business Analysis for Data Engineers

Before deciding whether something should be a fact table, dimension, aggregate, or something else, we first need to understand what the data is supposed to represent.

This is where Data Engineering overlaps with Business Analysis. You don't need to become a Business Analyst, but you do need to be able to translate business requirements into data requirements.

<!-- Business Analysis Meme -->
![Business Analysis Meme](https://www.modernanalyst.com/Portals/0/Public%20Uploads/Fin608-Abducted-Business-Analyst.jpg)

When presented with a messy collection of source tables, we should be able to ask:

- Who will consume this data?
- What decisions are they trying to make?
- What questions does the data need to answer?
- What are the important business processes and events?
- What do important business terms actually mean?
- What does a "customer", "order", "sale", or "active user" actually represent?
- What level of freshness is required?
- How much historical data needs to be retained?
- What does "correct" data look like?
- What edge cases or business rules need to be accounted for?

These questions come before designing the model.

For example, being told "*we need a sales dataset*" isn't enough to design a model. The consumer might want to analyse individual transactions, daily store performance, customer behaviour, sales targets, or some combination of these.

Those requirements ultimately determine things like the grain, entities, relationships, metrics, history, and transformations in the resulting data model.

So, how are we going to learn all of this?

### Fundamentals of Data Engineering

<!-- Fundamentals of Data Engineering Image -->
![Fundamentals of Data Engineering](https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1654271050i/61218623.jpg)

[Fundamentals of Data Engineering](https://www.amazon.com/Fundamentals-Data-Engineering-Robust-Systems/dp/1098108302/)

The general consensus on FDE is that the book is exceptionally useful at providing a high level generalized overview of the current state of Data Engineering.

One bloke notes that it's:

"*Not going to make you better at your job but will be extremely helpful for interviews and being able to speak about the data engineering landscape and key concepts at a high/medium level*."

With this being said, a few people (*in the reddit threads I read*) mention that the book is a bit of a slog, so we've got that to look forward to.

### LLM-Based Modelling Practice

As I mention throughout this article, I don't want this roadmap to be all theory. As such, I'd like to get to working with a few LLM based prompts along the lines of:

<!-- ChatGPT Prompt -->
```text
Heya, ChatGPT/Claude/Gemini etc,

Question:
I'm looking to practice my data-modelling skills, could you please throw me a messy set of data and then I'll return a possible data-model?

I'd like to work specifically on the following tasks:
* Grain Determination
* Entity Identification
* Relationship Identification i.e.:
  * One customer can have many ______.
  * One order can contain many ______.
  * One product can appear in many ______.
* Determine the Keys
* Identify problems with the raw data.

Output:
* Please output a "made-up" table and a list of questions designed to improve my data-modelling skills

Context:
* I'm looking to become a Data Engineer and wish to improve my skills
* Take the tone of a teacher / lecturer for this specific task.
```

This task will be beneficial as we're actually beginning to get experience solving (*potentially*) real Data-Modelling business problems!

## Distributed Systems

<!-- NOTE: Consider adding a small practical exercise here. You do not necessarily need a full distributed-systems implementation; a small experiment involving partitioning, replication, failure, or message ordering could make the theory much more tangible. -->

A lot of the problems in modern Data Engineering exist because **one computer isn't enough**.

If I have a few thousand rows, almost anything will work, however, what happens when the data grows, think 1 Million, 1 Billion, 10 Trillion - **What happens then?**

<!-- Big Data Meme -->
![Big Data](https://i.redd.it/9uviprh35b4b1.jpg)

At some point, I need multiple machines. And as soon as I have multiple machines, I inherit a whole new category of problems.

- Machines fail.
- Networks fail.
- Messages arrive late.
- Machines disagree.
- Data needs to be replicated.
- Work needs to be partitioned.
- Different machines need to coordinate.

<!-- Map Reduce Meme -->
![Map Reduce](https://i.programmerhumor.io/2025/06/4ed716d98534cccc7a187cd9cbfb3d9bf98aeb6829f5b90e6a209531cae8e48f.webp)

These problems inevitably lead into concepts like:

- Partitioning
- Replication
- Fault tolerance
- Consistency
- Availability
- CAP theorem
- Consensus
- Distributed transactions
- Eventual consistency

These are concepts that sit underneath a huge amount of modern Data Engineering infrastructure. Understanding them should make technologies like Spark, Kafka and distributed databases feel much less magical.

So, how are we learning about Distributed Systems? - Well, to be honest, we've got a couple of options here, as [Designing Data-Intensive Applications](https://0-lucas.github.io/digital-garden/99.-Books/Martin-Kleppmann---Designing-Data-Intensive-Applications_-O%E2%80%99Reilly-Media-(2017).pdf) already does a fairly good job with Distributed systems, however, if you really wanted to punish yourself...

### MIT 6.5840 — Distributed Systems

<!-- Distributed Systems Image -->
![Distributed Systems](https://miro.medium.com/v2/resize:fit:1358/format:webp/1*nwww3E-TWR_ldNwOp-i_qg.png)

[MIT's 6.5840](https://pdos.csail.mit.edu/6.5840/) is a graduate distributed-systems course covering fault tolerance, replication and consistency, with lectures, papers and programming labs.

This is considerably more academic than we may necessarily need for Data Engineering, but it's still a great resource nonetheless.

With this being said, I don't think that I'll be completing it in the near future...

## Data Systems

We've spent the first part of this roadmap building the foundations.

We've learned how computers work, how databases store and retrieve data, how data should be modelled, and what happens when our systems grow beyond a single machine.

<!-- Data Organisation Meme -->
![Data Organisation](https://i.programmerhumor.io/2025/06/18631647a46eb5586f4fdb9ab0f483528f554fdb8e5f3a4a53514c75766e4946.jpeg)

At this point, I don't think reading another ten books is going to make us better Data Engineers.

So, I proclaim to the world:

{{< lead >}}
> **Lay them books down!**
{{< /lead >}}

It's time to start building.

The goal of this section is to take everything we've learned so far and start putting the pieces together into actual data systems.

A modern data platform might look something like this:

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

On a whiteboard, this looks relatively straightforward.

In reality, this is where things get interesting.

- What happens when the API goes down?
- What happens when we receive the same record twice?
- What happens when yesterday's data arrives tomorrow?
- What happens when the source changes its schema?
- What happens when a transformation fails halfway through?
- Can we safely rerun the pipeline?
- How do we backfill three years of historical data?
- How do we know whether the pipeline is actually working?

And perhaps most importantly:

> How do we know whether the data we're producing is actually correct?

These are the kinds of problems that start separating writing data pipelines from engineering data systems.

This is where concepts (*such as the following*) start becoming much more than just theoretical concepts:

- Idempotency
- Retries
- Backfills
- Data quality
- Data contracts
- Schema evolution
- Data lineage
- Observability
- SLAs

So, how are we going to learn this? At this point, I don't think another purely theoretical course is the answer.

We've already covered the theory through resources such as Designing Data-Intensive Applications and Fundamentals of Data Engineering. Now we need something that forces us to build.

This is where DataTalksClub's Data Engineering Zoomcamp comes in.

### Data Engineering Zoomcamp

{{< github repo="ziritrion/dataeng-zoomcamp" showThumbnail=true >}}

The Data Engineering Zoomcamp is a practical, project-oriented course covering many of the technologies and workflows that show up in modern Data Engineering.

More importantly, it gives us something we've been missing so far:

> A reason to actually put the theory into practice.

Rather than studying each technology in isolation, we'll start building pipelines that have to deal with ingestion, storage, transformation, orchestration, infrastructure and deployment.

And that's exactly what I want at this stage of the roadmap. The objective isn't to simply complete the Zoomcamp, instead, it's to use it as a sandbox for applying everything we've learned so far. i.e. :

- If we learn about Docker, we'll containerise something.
- If we learn about orchestration, we'll orchestrate a pipeline.
- If we learn about data modelling, we'll model the data properly rather than dumping everything into one table.
- If we learn about cloud infrastructure, we'll deploy something.

And when something inevitably breaks, we'll investigate why it broke rather than immediately reaching for a tutorial.

## Cloud and Infrastructure

<!-- NOTE: This is currently the least concrete section. Consider explaining how you will actually encounter Docker, Airflow, Terraform, CI/CD, networking, secrets, permissions, and orchestration through progressively more complex projects rather than learning each technology in isolation. -->

Modern data systems rarely live on a laptop, so eventually I need to understand the infrastructure they run on. This is where the following things come into the picture like:

- Cloud storage
- Compute
- Containers
- Docker
- Networking
- Infrastructure as Code
- CI/CD
- Secrets
- Permissions
- Orchestration

<!-- This meme has a fucking grammar issue... -->
![Cloud Computing Meme](https://i.programmerhumor.io/2026/08/5a5aecac6562044e5b09681c5452ceaadc1de97a864437a7402d6a2f1cb80243.png)

Say it with me people "*So how are we going to be learning about Cloud...*"

### AWS: Well Architected Framework

<!-- Well Architected Framework Image -->
![Well Architected Framework](https://media.geeksforgeeks.org/wp-content/uploads/20240428202058/logoo.jpg)

The [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) is useful here, even though I'm primarily interested in Azure.

The reason I don't mind, is because I want us to view the resource through an architectural lens rather than a resource for learning AWS itself. This is because it can help us evaluate:

- reliability
- security
- cost
- performance
- operational excellence
- sustainability

after we understand the underlying cloud building blocks.

## Production Engineering

Building something that works is one thing. Building something that **continues working** is another.

<!-- Production Meme -->
![Production Meme](https://preview.redd.it/morning-motivation-v0-7m2m2up0mz991.jpg?width=640&crop=smart&auto=webp&s=944984c8f1d4af77503947378de3d3a7bb05862b)

Production Engineering is where I want to learn about:

- Monitoring
- Logging
- Alerting
- Reliability
- Incident response
- Testing
- Deployment
- Rollbacks
- Capacity planning
- Performance
- Security
- Cost

### Google SRE Books

<!-- Google SRE -->
![Google SRE](https://getfreeebooks.b-cdn.net/wp-content/uploads/2020/04/50-googleebooks-100.jpg)

I've heard the following books from Google recommended as resources for learning about Site Reliability Engineering and the underlying principles and learnings that guide this field of study:

- [Site Reliability Engineering (2016)](https://sre.google/books/)
- [The Site Reliability Workbook (2018)](https://sre.google/books/)
- [Building Secure & Reliable Systems (2020)](https://sre.google/books/)

<!-- Why these books? -->

<!-- Removed the section where I talk about the fact that there is no set paths -->
<!-- No paths Image -->
<!-- ![No Paths...](https://pbs.twimg.com/media/EcZrpA6XsAIFTcG.jpg) -->

## Other useful Data Engineering Resources

### Data Engineer Wiki

[Data Engineering Wiki](https://dataengineering.wiki/Guides/Getting+Started+With+Data+Engineering)

### Data Engineering Cookbook

<!-- Data Engineering Cookbook -->
{{< github repo="andkret/Cookbook" showThumbnail=true >}}

### Data Engineer Handbook

<!-- Data Engineering Handbook -->
{{< github repo="DataExpert-io/data-engineer-handbook" showThumbnail=true >}}

### Data Engineering for Beginners

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

The only Data Engineering Certificates I'm going to go after are:

- Databricks - Data Engineer Associate
- Databricks - Data Engineer Professional

The reason for this is that I've already worked with Databricks and had exposure to some Data Engineering on the Azure Databricks platform.

> [!NOTE]
> At $200 NZD a pop for each of these two certifications, Databricks (*Microsoft*) sure knows how to pull money from wallets.

With this being said, there are also the following *other* options for certification, and feel free to choose one that works best for you:

- Databricks - Certified Associate Developer for Apache Spark
- Google Cloud Certified - Professional Data Engineer
- Microsoft DP-600: Fabric Analytics Engineer Associate
- Microsoft DP-700: Fabric Data Engineer Associate
- AWS Certified Data Engineer - Associate

## Useful Media Personalities in the Data Engineering Space

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

[Start Data Engineering](https://www.startdataengineering.com/?utm_source=chatgpt.com)

<!-- Joseph is a veteran of the industry with 15+ YOE (*Years of Experience*) and frequently writes, posts, and comments on different facets of the Data Engineering eco-system!

This, and the fact that I like his website, and writing style, meant that he was always getting a mention in this article. Also, from his Reddit AMA, he seems like a really chill guy! 

[Start Data Engineering](https://www.startdataengineering.com/?utm_source=chatgpt.com) is a great resource for any aspiring, or current data-engineers. -->

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

Cheers!

<!-- Subscribe Button -->
{{< subscribe >}}
