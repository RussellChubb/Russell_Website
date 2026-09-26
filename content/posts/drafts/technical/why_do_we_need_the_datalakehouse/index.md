---
title: "Why do we need the Data-Lakehouse?"
draft: true
description: "Databases, Data-Lakes and Data-Warehouses all solve half the problem. Here's why the Data-Lakehouse exists to solve the other half."
summary: "Databases, Data-Lakes and Data-Warehouses all solve half the problem. Here's why the Data-Lakehouse exists to solve the other half."
date: 2026-09-22
featureimage: "featured.jpg"
tags: ["Technical"]
---

<!-- Space for a Quote -->
{{< typeit
  tag=h4
  speed=80
  lifeLike=true
  breakLines=true
  loop=false
>}}
u/Data-Sleek: How do you decide between a database, data lake, data warehouse, or lakehouse?
u/[DELTETED]: That's the neat thing, they all become data swamps
{{< /typeit >}}

---

## Introduction 🎯

Data, Data, Data, business's and users have data coming out their ears, and with so much of it, teams keep reaching for a new system to store it in.

First it was the database. Then the warehouse. Then the lake. And now everyone's talking about the **lakehouse**.

<!-- Main Lead -->
{{< lead >}}
> **So why do we keep needing a new one?**
{{< /lead >}}

That's the real question this post is trying to answer. Not "*what's the difference between these systems*", but "*what problem did each one fail to solve, badly enough that someone had to invent the next thing*?"

Because that's exactly how we ended up at the Data-Lakehouse. It isn't a trend, it's a patch job for two systems that were each brilliant at one job and genuinely bad at the other.

<!-- Pam what's the difference meme -->
![What's the difference?](https://i.postimg.cc/6QHbq89h/OLAP-vs-OLTP.png)

To see why, we need to start with the two jobs data systems are actually asked to do.

## OLTP vs OLAP ⚖️

<!-- OLAP vs OLTP Image -->
<!-- ![OLAP VS OLTP](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2VANwXN4EoFsdC8uEdoiQbN9iwK1f5dtF34o4VcwoJqbSqNG8UZGsq2s&s=10) -->

<!-- *BTW: These acronyms sound much more complicated than they are.* -->

### OLTP (Online Transaction Processing)

<!-- OLTP Image -->
![OLTP](https://media.geeksforgeeks.org/wp-content/uploads/20200428171539/OLTP1.png)

OLTP systems are generally concerned with **running an application**.

Imagine an online shop called "*Russells Widgets*". Someone places an order (*for a widget*), and the system needs to:

1. Create the order
2. Update the customer's account
3. Reduce the inventory (*subtract a widget*)
4. Record the payment

And it needs to do all of that **correctly and quickly**, every single time. A typical OLTP database might look something like:

<!-- Typical OLTP Database Mermaid Chart -->
{{< mermaid >}}
graph TD;
    A["Application"] --> B[("PostgreSQL")];
    B --> C["customers"];
    B --> D["orders"];
    B --> E["products"];
    B --> F["payments"];
{{< /mermaid >}}

This is where traditional relational databases shine: transactions, constraints, consistency, concurrent writes, fast lookups. They're built to protect one order at a time.

### OLAP (Online Analytical Processing)

<!-- OLAP Image -->
![OLAP Image](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSb8a22wtlj9HRHYLmZgBmqp2KM8VLrU0Jw7OT6OL3v8aCKFdVggfsX1Ys&s=10)

OLAP has a completely different problem. Instead of asking "*Which widget did a user just buy?*", we might ask:

> "*What were our total widget sales by product, region and month over the last five years?*"

That's a different animal. We could be scanning **millions or billions of records**, aggregating them, joining datasets together, calculating statistics.

<!-- Unrelated Meme 0 -->
![Unrelated Meme](https://imgs.xkcd.com/comics/heatmap_2x.png)

So instead of lots of tiny, protected transactions, we're interested in **large analytical queries**. OLTP runs the business. **OLAP is about analysing it.**

And this mismatch — one system built for tiny fast writes, another needed for huge slow reads — is the root cause of everything that follows.

## Database's 🗄️

Databases are fundamentally a system for storing and retrieving data, and when people say "*database*" in a Data Engineering context, they usually mean a relational one: PostgreSQL, MySQL, SQL Server, Oracle.

<!-- Not Excel Admonition -->
> [!CAUTION]
> Excel isn't, and always won't be, a RDBMS.

<!-- Unrelated Meme I liked -->
![Unrelated Meme](https://i.programmerhumor.io/2024/05/programmerhumor-io-databases-memes-backend-memes-ec728de3b8df49b.jpg)

These systems are great at OLTP workloads:

{{< mermaid >}}
graph TD;
    A["Application"] --> B[("Database")];
    B --> C["Orders"];
    B --> D["Users"];
    B --> E["Products"];
{{< /mermaid >}}

The database is the **system of record**, it holds the data the application needs to actually function. And that's exactly why it starts to break when the CEO wanders over and asks:

> "Can you tell me how revenue has changed by customer segment over the last ten years?"

We *could* run that query against production. But we shouldn't. Our poor PostgreSQL instance has enough problems without a ten-year analytical scan running while 10,000 customers are mid-checkout.

<!-- Real men test in production meme -->
![Xbox Controller](https://preview.redd.it/productiontesting-v0-ynp50nf1339b1.png?auto=webp&s=5247856ff1a1f986415bf2be8c09c2e63aa774a6)

So the database alone can't be the whole answer. We need somewhere else to send those questions.

## Data Warehouses 🏢

The Data Warehouse exists to answer one need the database can't: **analytical workloads, without wrecking the application.**

<!-- Another unrelated meme -->
![Unrelated meme 2](https://preview.redd.it/who-can-explain-this-xkcd-comic-for-me-v0-t3i8v65wtkxe1.jpeg?auto=webp&s=3a9a0d7d49d1ce544dd8b8f6d4a4f6c64ff308cc)

Instead of being the database that powers our application, it becomes the place we bring data together specifically to be analysed:

<!-- Application Architecture Mermaid -->
{{< mermaid >}}
graph TD;
    A["Application (Widget Store)"] --> B[("Database")];
    B --> C["Ingestion"];
    C --> D[("Data Warehouse")];
    D --> E["BI / Analytics"];
{{< /mermaid >}}

Now the production database can concentrate on running the application, and the warehouse can concentrate on answering questions. Because analytical workloads have different needs from transactional ones, the warehouse reshapes the data for that job:

{{< mermaid >}}
graph TD;
    A["Sales"] --> B["Customer"];
    A --> C["Product"];
    A --> D["Date"];
{{< /mermaid >}}

This is where fact tables, dimension tables, star schemas and aggregations show up. And to be clear, this is a genuinely good solution — for structured, well-understood business data.

But it only solves *half* of the original problem. It assumes the data already looks like rows and columns. What happens when it doesn't?

## Data Lakes 🌊

Now imagine our company starts collecting data from:

* APIs
* Application databases
* CSV files
* JSON
* Logs
* IoT devices
* Images
* Videos
* Event streams

Forcing all of that into a tidy relational schema before we've even stored it is a losing game.

<!-- Cramming Gif -->
![Cramming](https://media1.tenor.com/m/EYfxDVbJtTwAAAAd/nos-fat-lois.gif)

So the Data Lake solves a different problem than the warehouse does: not "*how do we analyse structured data*", but "*where do we even put everything else, cheaply, before we know what we'll do with it*?"

<!-- Data-sources Mermaid Chart -->
{{< mermaid >}}
graph TD;
    subgraph Sources["Data Sources"]
        A["API"]
        B["CSV"]
        C["Logs"]
        D["IoT"]
    end
    A --> E[("Data Lake")];
    B --> E;
    C --> E;
    D --> E;
    E --> F["Processing"];
    F --> G["Analytics / ML"];
{{< /mermaid >}}

This is particularly useful when:

* We don't know exactly how the data will be used yet
* We have very large datasets
* We need to retain raw data
* We work with semi-structured or unstructured data
* We want cheap, scalable storage

So now we've solved the flexibility problem the warehouse couldn't. Great. Except the lake trades that flexibility for something else, and remember our Reddit user from the beginning?

> "That's the neat thing, they all become data swamps."

<!-- Data-Swamp Meme -->
![Data Swamp](https://i.redd.it/lr1ohtueoje71.png)

They weren't joking. Dump everything into object storage without organisation, metadata, governance, schemas, ownership or documentation, and you end up with:

```text
data/
├── final.csv
├── final_final.csv
├── final_v2.csv
├── definitely_final.csv
├── raw/
├── raw_new/
├── raw_old/
├── stuff/
└── PLEASE_DO_NOT_DELETE/
```

The lake's greatest strength — "*put anything here, we'll figure it out later*" — is also exactly what turns it into a swamp.

<!-- Data Swamp Meme -->
![Data Swamp 2](https://i.redd.it/n86id1wgssg91.png)

And that's the second unsolved half of the problem: we now have a place that's flexible enough to hold everything, but not reliable enough to actually trust for analytics.

## So Why Do We Need the Lakehouse? 🏠

Look at where that leaves us:

|                 | Data Warehouse                 | Data Lake                      |
| --------------- | ------------------------------ | ------------------------------ |
| Primary purpose | Analytics                      | Storage + processing           |
| Data            | Structured                     | Structured + semi/unstructured |
| Schema          | Often before/around ingestion  | Often applied later            |
| Storage         | Traditionally specialised      | Usually object storage         |
| Cost            | Generally higher               | Generally cheaper              |
| Typical users   | Analysts / BI                  | Engineers / ML / analysts      |
| Data state      | Curated                        | Often raw → curated            |

Neither column is wrong. Neither is complete either. Plenty of teams end up running **both**: a lake for raw everything, a warehouse for trusted BI, and a pile of pipelines constantly copying data between them just to keep both sides happy. That's two systems to pay for, two systems to secure, and data duplicated (and drifting out of sync) between them.

<!-- Data-Lakehouse Memes -->
![Data Lakehouse Meme](https://storage.ghost.io/c/18/db/18db57b5-6733-4aa7-891a-c0b44ef81075/content/images/2025/02/image--28-.png)

That duplication is the actual reason the Data-Lakehouse needed to exist. Not because lakes or warehouses are bad, but because running both, forever, to cover for each other's weaknesses, is expensive and fragile.

{{< mermaid >}}
graph TD;
    A["Data Sources"] --> B[("Object Store")];
    B --> C["Lakehouse"];
    C --> D["BI / SQL"];
    C --> E["ML / AI"];
{{< /mermaid >}}

The Lakehouse keeps the lake's cheap, flexible object storage as the foundation, but adds a layer on top that brings in the things that made warehouses trustworthy in the first place:

* ACID transactions
* Schema enforcement
* Schema evolution
* Versioning / time travel
* Table metadata
* Data governance
* SQL analytics
* Performance optimisation

That's the whole pitch: one copy of the data, one system, that's flexible enough for a data scientist and reliable enough for the CFO. Technologies like **Delta Lake**, **Apache Iceberg** and **Apache Hudi** are what actually make that possible, by giving object storage the table-like guarantees it never had on its own.

## The Mental Model 🧠

If I had to boil this whole post down to why each system exists, not just what it does, I'd put it like this:

* Database = "*I need to run an application, correctly, right now.*"
* Data Warehouse = "*I need to analyse structured business data, without breaking the application.*"
* Data Lake = "*I need somewhere cheap and flexible to store everything else.*"
* Data Lakehouse = "*I need the lake's flexibility and the warehouse's trust, without running two systems to get both.*"

So no, **you don't always need a lakehouse**.

Plenty of teams are perfectly well served by a database, or a warehouse, or a lake on its own. But once you've felt the pain of maintaining two systems just to cover each other's gaps, it becomes pretty obvious why the lakehouse showed up.

Cheers!

{{< subscribe >}}
