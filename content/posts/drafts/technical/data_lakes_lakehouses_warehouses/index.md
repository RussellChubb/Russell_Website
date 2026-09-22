---
title: "Data Lakes, Data Lakehouses & Data Warehouses"
draft: true
description: "Ever wanted to know the difference between Data-Lakes, Data-Warehouses, and Data Lake-Houses?"
date: 2026-09-14
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

Data, Data Data, business's and users have data coming out their ears, and with so much of it, the question naturally becomes:

<!-- Main Lead -->
{{< lead >}}
> **Where do we put it?**
{{< /lead >}}

Well, fear not dear reader, there's a load of different places you can put "data", you've got:

* Databases
* Data Lakes
* Data Warehouses
* Data Lakehouses

Which then of course leads into the obvious question of "*What's the difference between those systems?*"

<!-- Pam what's the difference meme -->
![What's the difference?](https://i.postimg.cc/6QHbq89h/OLAP-vs-OLTP.png)

Well, before we decide which to use, we need to first understand "*what are we actually trying to do with our data?*?

## OLTP vs OLAP ⚖️

<!-- OLAP vs OLTP Image -->
![OLAP VS OLTP](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2VANwXN4EoFsdC8uEdoiQbN9iwK1f5dtF34o4VcwoJqbSqNG8UZGsq2s&s=10)

However, before we get into any fun and games, I want to first take a small detour into the history of data storage to understand the difference between **OLTP** and **OLAP**.

*BTW: These acronyms sound much more complicated than they are.*

### OLTP (Online Transaction Processing)

<!-- Removed because it's too heavy -->
<!-- OLTP Image -->
![OLTP](https://media.geeksforgeeks.org/wp-content/uploads/20200428171539/OLTP1.png)

OLTP systems are generally concerned with **running an application**.

Imagine an online shop called "*Russells Widgets*", someone places an order (*for a widget*), therefore, the system then needs to:

1. Create the order
2. Update the customer's account
3. Reduce the inventory (*subtract a widget*)
4. Record the payment

And it needs to do all of that **correctly and quickly**. A typical OLTP database might therefore look something like:

<!-- Typical OLTP Database Mermaid Chart  -->
{{< mermaid >}}
graph TD;
    A["Application"] --> B[("PostgreSQL")];
    B --> C["customers"];
    B --> D["orders"];
    B --> E["products"];
    B --> F["payments"];
{{< /mermaid >}}

This is where traditional relational databases shine, as they're designed around things like:

* Transactions
* Constraints
* Consistency
* Concurrent writes
* Fast lookups

### OLAP (Online Analytical Processing)

<!-- OLAP Image -->
![OLAP Image](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSb8a22wtlj9HRHYLmZgBmqp2KM8VLrU0Jw7OT6OL3v8aCKFdVggfsX1Ys&s=10)

OLAP has a rather different problem, instead of asking "*Which widget did a user just buy?*", we might ask:

> "*What were our total widget sales by product, region and month over the last five years?*"

That's crazy different, as we could be scanning **millions or billions of records**, aggregating them, joining datasets together and calculating statistics.

<!-- Unrelated Meme 0 -->
![Unrelated Meme](https://imgs.xkcd.com/comics/heatmap_2x.png)

So, instead of lots of tiny transactions, we're interested in **large analytical queries**. So **OLAP is about analysing the business.**

## The Database 🗄️

Now, that we've learnt the differences between OLAP and OLTP, let's get into our core content, starting out with databases, which are fundamentally a system for storing and retrieving data.

When people say "*database*" in the context of Data Engineering, they're often talking about a traditional relational database such as PostgreSQL, MySQL, SQL Server or Oracle.

<!-- Not Excel Admonition -->
> [!CAUTION]
> Excel isn't, and always won't be a RDBMS.

<!-- Unrelated Meme I liked -->
![Unrelated Meme](https://i.programmerhumor.io/2024/05/programmerhumor-io-databases-memes-backend-memes-ec728de3b8df49b.jpg)

These systems are particularly good at OLTP workloads.

For example:

{{< mermaid >}}
graph TD;
    A["Application"] --> B[("Database")];
    B --> C["Orders"];
    B --> D["Users"];
    B --> E["Products"];
{{< /mermaid >}}

The database is usually the **system of record**, it contains the data that the application actually needs to function. But this creates a problem. What happens when the CEO asks:

> "Can you tell me how revenue has changed by customer segment over the last ten years?"

We *could* run that query against our production database.... But perhaps we shouldn't.

Our poor PostgreSQL instance has enough problems without someone asking it to perform a ten-year analytical query while 10,000 customers are trying to place orders.

<!-- Real men test in production meme -->
![Xbox Controller](https://preview.redd.it/productiontesting-v0-ynp50nf1339b1.png?auto=webp&s=5247856ff1a1f986415bf2be8c09c2e63aa774a6)

This is where the **Data Warehouse** starts to make sense.

## The Data Warehouse 🏢

A Data Warehouse is essentially a system designed specifically for **analytical workloads**.

Instead of being the database that powers our application, it becomes the place where we bring together data from different sources so that we can analyse it.

<!-- Another unrelated meme -->
![Unrelated meme 2](https://preview.redd.it/who-can-explain-this-xkcd-comic-for-me-v0-t3i8v65wtkxe1.jpeg?auto=webp&s=3a9a0d7d49d1ce544dd8b8f6d4a4f6c64ff308cc)

Our architecture might now look something like:

<!-- Application Architecture Mermaid -->
{{< mermaid >}}
graph TD;
    A["Application (Widget Store)"] --> B[("Database")];
    B --> C["Ingestion"];
    C --> D[("Data Warehouse")];
    D --> E["BI / Analytics"];
{{< /mermaid >}}

Now our production database can concentrate on running the application and the warehouse can concentrate on answering questions.

Now, because analytical workloads have different requirements from transactional workloads, warehouses tend to make different design choices.

For example, we might have:

{{< mermaid >}}
graph TD;
    A["Sales"] --> B["Customer"];
    A --> C["Product"];
    A --> D["Date"];
{{< /mermaid >}}

Rather than simply mirroring the application's database, we might transform the data into a model designed for analysis.

This is where the following terms start to appear:

* Fact tables
* Dimension tables
* Star schemas
* Aggregations

So why not just use a Database? Well, you *can*... And this is an important point. There isn't some magical rule saying:

Database ❌ & Warehouse ✅

The appropriate architecture depends on the problem. A small company with a relatively small dataset might happily run analytical queries against PostgreSQL. As the volume and complexity of analytical workloads grow, however, separating transactional and analytical workloads becomes increasingly useful.

This gives us our first mental model:

{{< mermaid >}}
graph TD;
    subgraph OLTP
        A["Run the application"] --> B[("Database")];
    end
    subgraph OLAP
        C["Analyse the business"] --> D[("Warehouse")];
    end
{{< /mermaid >}}

But then another problem appears. What if we don't just have nice, clean, structured tables?

What if we have **everything else**?

## The Data Lake 🌊

Imagine that our company starts collecting data from:

* APIs
* Application databases
* CSV files
* JSON
* Logs
* IoT devices
* Images
* Videos
* Event streams

Suddenly, forcing everything into a traditional relational schema before storing it becomes rather inconvenient. The basic idea behind a Data Lake is relatively simple:

**Store large amounts of data in relatively cheap object storage, often in its original or near-original form.**

Something like:

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

Instead of requiring everything to fit neatly into a relational database, we can throw a much wider variety of data into the lake.

This is particularly useful when:

* We don't know exactly how the data will be used yet
* We have very large datasets
* We need to retain raw data
* We work with semi-structured or unstructured data
* We want cheap, scalable storage

The lake therefore gives cheap storage, for almost anything we want to chuck at it. However, there's a catch... Remember our Reddit user from the beginning?

> "That's the neat thing, they all become data swamps."

They're joking about a very real problem.

A Data Lake can become a **Data Swamp**.

If you dump everything into object storage without good organisation, metadata, governance, schemas, ownership and documentation, you eventually end up with:

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

The flexibility of the Data Lake is both its greatest strength and its greatest weakness.

## The Data Lakehouse 🏠

At this point, we have two systems solving somewhat different problems.

|                 | Data Warehouse                | Data Lake                      |
| --------------- | ----------------------------- | ------------------------------ |
| Primary purpose | Analytics                     | Storage + processing           |
| Data            | Structured                    | Structured + semi/unstructured |
| Schema          | Often before/around ingestion | Often applied later            |
| Storage         | Traditionally specialised     | Usually object storage         |
| Cost            | Generally higher              | Generally cheaper              |
| Typical users   | Analysts / BI                 | Engineers / ML / analysts      |
| Data state      | Curated                       | Often raw → curated            |

But this separation created another interesting problem. Why do we necessarily need **two systems?**, could we somehow get the flexibility of a Data Lake **and** the analytical capabilities and reliability of a Data Warehouse?

Well, this is where the Data Lakehouse enters the chat... The Data Lakehouse is, at a high level, an attempt to combine the strengths of the two architectures.

The basic idea is:

{{< mermaid >}}
graph TD;
    A["Data Sources"] --> B[("Object Store")];
    B --> C["Lakehouse"];
    C --> D["BI / SQL"];
    C --> E["ML / AI"];
{{< /mermaid >}}

We still use relatively cheap object storage as the underlying storage layer. But we add a layer of technology that gives us many of the capabilities traditionally associated with warehouses and databases.

Depending on the implementation, this can include things like:

* ACID transactions
* Schema enforcement
* Schema evolution
* Versioning / time travel
* Table metadata
* Data governance
* SQL analytics
* Performance optimisation

The result is something that *looks* more like a warehouse to the person querying it, while retaining some of the flexibility and storage economics of a Data Lake.

This is one of the ideas behind technologies such as **Delta Lake**, **Apache Iceberg** and **Apache Hudi**.

## So... which one should I use? 🤔

That's the best part, **you don't!**.

Intead, the decision is made at a golf course that you’re not invited to (*I wish I was invited*).

## The Mental Model 🧠

If I had to reduce this entire article to a handful of ideas, I'd probably remember it like this:

* Database = "*I need to run an application.*"
* Data Warehouse = "*I need to analyse structured business data.*"
* Data Lake = "*I need somewhere cheap and flexible to store lots of data.*"
* Data Lakehouse = "*I want the flexibility of a lake with many of the analytical and management capabilities of a warehouse.*"

Cheers!

{{< subscribe >}}
