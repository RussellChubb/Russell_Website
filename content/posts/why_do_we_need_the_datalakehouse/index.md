---
title: "Why do we need the Data-Lakehouse?"
draft: false
showReadingProgress: true
description: "Databases, Data-Lakes and Data-Warehouses all solve half the problem. Here's why the Data-Lakehouse exists to solve the other half."
summary: "Databases, Data-Lakes and Data-Warehouses all solve half the problem. Here's why the Data-Lakehouse exists to solve the other half."
date: 2026-09-22
featureimage: "featured.png"
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

Data, Data, Data... Everyone has data coming out their ears, and with so much of it, users keep reaching for a new system to store it in.

First it was the database. Then the warehouse. Then the lake. And now we're up to the **lakehouse**.

<!-- Main Lead -->
{{< lead >}}
> **So why do we keep needing a new system?**
{{< /lead >}}

<!-- Pam what's the difference meme -->
![What's the difference?](https://i.postimg.cc/6QHbq89h/OLAP-vs-OLTP.png)

Well my dear user, before I answer this question, we first need to understand the two jobs data systems are actually asked to do on a day-to-day basis...

## OLTP vs OLAP ⚖️

<!-- OLAP vs OLTP Image -->
<!-- ![OLAP VS OLTP](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2VANwXN4EoFsdC8uEdoiQbN9iwK1f5dtF34o4VcwoJqbSqNG8UZGsq2s&s=10) -->

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

That's a [different animal, (*and the same beast*)](https://www.youtube.com/watch?v=2YgXOlH8Q2I).

<!-- Different Animal and the Same Beast -->
{{< youtubeLite id="2YgXOlH8Q2I" label="Two Very Problematic Dudes" >}}

<!-- Removed this as I didn't think it fit. -->
<!-- Unrelated Meme 0 -->
<!-- ![Unrelated Meme](https://imgs.xkcd.com/comics/heatmap_2x.png) -->

So, instead of lots of tiny, protected transactions, we're interested in **large analytical queries**.

OLTP runs the business, (*kind of like the workers of a business*), and **OLAP is about analysing it**, (*kind of like the C - Suite of the same business*)

<!-- OLAP VS OLTP Video -->
Now, if you didn't find my explanation fulfilling, I've linked off to a video by [techTFQ](https://www.youtube.com/@techTFQ) to further explain the differences between the two systems.

(*btw @TechTFQ, your videos rock, but I don't like your new AI thumbnails*)

{{< youtubeLite id="6-VVu68hbgw" label="TechTFQ" >}}

## Database's 🗄️

Databases are fundamentally a system for storing and retrieving data, and when people say "*database*" (*in a Data Engineering context*), they usually mean a relational one.

Generally, people are referring to one of the big four (*listed below*):

* PostgreSQL
* MySQL
* Microsoft SQL Server
* Oracle (*yuck*)

<!-- Not Excel Admonition -->
> [!CAUTION]
> Excel isn't, and will never be a RDBMS. (Even if some people treat it like one...)

<!-- Unrelated Meme I liked -->
![Unrelated Meme](https://i.programmerhumor.io/2024/05/programmerhumor-io-databases-memes-backend-memes-ec728de3b8df49b.jpg)

These systems are great at OLTP workloads (*such as the example flow, I've featured below*):

{{< mermaid >}}
graph TD;
    A["Application"] --> B[("Database")];
    B --> C["Orders"];
    B --> D["Users"];
    B --> E["Products"];
{{< /mermaid >}}

The database is the **system of record**, it holds the data the application needs to actually function. And that's exactly why it starts to "*break*" when the CEO wanders over and asks:

> "Can you tell me how revenue has changed by customer segment over the last ten years?"

We *could* run that query against production.

But we probably shouldn't, as our poor PostgreSQL instance has enough problems without a ten-year analytical scan running while 10,000 customers are mid-checkout (*or some other production-esque situation*).

<!-- Abuse Goblin PostGres SQL -->
![I hate the abuse goblin memes, it makes me sad](Abuse_Goblin_Data.png)

<!-- Real men test in production meme -->
<!-- ![Xbox Controller](https://preview.redd.it/productiontesting-v0-ynp50nf1339b1.png?auto=webp&s=5247856ff1a1f986415bf2be8c09c2e63aa774a6) -->

So the database alone can't be the whole answer, we instead need somewhere else to send those questions...

## Data Warehouses 🏢

The Data Warehouse exists to run **analytical workloads, without wrecking the application.**

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

Now the production database can concentrate on running the application, and the warehouse can concentrate on answering questions.

Because analytical workloads have different needs from transactional ones, the warehouse reshapes the data for that job:

{{< mermaid >}}
graph TD;
    A["Sales"] --> B["Customer"];
    A --> C["Product"];
    A --> D["Date"];
{{< /mermaid >}}

This is where fact tables, dimension tables, star schemas and aggregations show up. And to be clear, **this is a genuinely good solution — for structured, well-understood business data**.

But it only solves *half* of the original problem. It assumes the data already looks like rows and columns. What happens when it doesn't?

> [!NOTE]
> I make a statement here that **the warehouse assumes that data is already modeled in rows and columns**.
>
> This statement holds true historically, however, modern data warehouses can ingest JSON, nested data, semi-structured data, external tables, files, etc.

## Data Lakes 🌊

Imagine Russell's Widgets company starts collecting data from:

* APIs
* CSV files
* JSON
* Logs
* IoT devices
* Images
* Videos

Forcing all of that into a tidy relational schema before we've even stored it is a **losing game**.

<!-- Cramming Gif -->
![Cramming](https://media1.tenor.com/m/EYfxDVbJtTwAAAAd/nos-fat-lois.gif)

So the Data Lake solves a different problem than the warehouse does: not "*how do we analyse structured data*", but "*where do we even put everything else, cheaply, before we know what we'll do with it*?".

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

So, why would we use this particular paradigm? Well, it's super useful when:

* We don't know exactly how the data will be used yet
* We have very large datasets
* We need to retain raw data
* We work with semi-structured or unstructured data
* We want cheap, scalable storage

So now we've solved the flexibility problem the warehouse couldn't.

**Great.**

Except the lake trades that flexibility for something else...

Remember our Reddit user from the beginning? Mr "*That's the neat thing, they all become data swamps.*"

They weren't [capping](https://www.urbandictionary.com/define.php?term=cap), [fr](https://www.urbandictionary.com/define.php?term=fr).

<!-- Data-Swamp Meme -->
![Data Swamp](https://i.redd.it/lr1ohtueoje71.png)

If you dump everything into object storage without:

* organisation structure
* metadata
* governance systems
* ownership or documentation

you [lowkey](https://www.reddit.com/r/NoStupidQuestions/comments/1nocad4/does_the_modern_slang_use_of_lowkey_have_a/) end up with this:

<!-- (*side-note, urban dictionary doesn't have the NZ slang meaning of lowkey correct.*): -->

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

**Scary stuff huh? ^ 🫣**

So, the lake's greatest strength, the whole "*put anything here, we'll figure it out later*" is also exactly what turns it into a swamp.

> [!NOTE]
> **A data lake isn't inherently a "*bad*" or untrustworthy place.**
>
> I use colorful language in this article, but fundamentally, the quality of a data-lake, (*much like any other system*) is a reflection of the effort and expertise put into the system.

<!-- Data Swamp Meme -->
<!-- ![Data Swamp 2](https://i.redd.it/n86id1wgssg91.png) -->

And that's the second unsolved half of the problem: we now have a place that's flexible enough to hold everything, but not reliable enough to actually trust for analytics.

## So Why Do We Need the Lakehouse? 🏠

Take a look at where that leaves us:

|                 | Data Warehouse                 | Data Lake                      |
| --------------- | ------------------------------ | ------------------------------ |
| Primary purpose | Analytics                      | Storage + processing           |
| Data            | Structured                     | Structured + semi/unstructured |
| Schema          | Often before/around ingestion  | Often applied later            |
| Storage         | Traditionally specialised      | Usually object storage         |
| Cost            | Generally higher               | Generally cheaper              |
| Typical users   | Analysts / BI                  | Engineers / ML / analysts      |
| Data state      | Curated                        | Often raw → curated            |

Neither of these two systems is inherently wrong (*neither is completely right either*)...

Plenty of organisations and teams end up running **both**:

* a lake (*for raw everything*)
* a warehouse (*for trusted BI*)

And a bunch of pipelines copying data between them just to keep both sides happy.

However, that means there's two systems to pay for, two systems to secure, and data duplicated (*and drifting out of sync between them*).

<!-- Oh No Gif -->
![Kermit](https://storage.ghost.io/c/5d/65/5d65c639-c03a-49a0-968c-4c50eeefc4ba/content/images/2024/11/https-3a-2f-2fsubstack-post-media-s3-amazonaws-com-2fpublic-2fimages-2f12d0a7f0-f65b-4a74-a63f-ae4fb73a8de3_498x280.gif)

<!-- Data-Lakehouse Memes -->
<!-- ![Data Lakehouse Meme](https://storage.ghost.io/c/18/db/18db57b5-6733-4aa7-891a-c0b44ef81075/content/images/2025/02/image--28-.png) -->

**That duplication is the actual reason the Data-Lakehouse exists.**

The Lakehouse keeps the lake's cheap, flexible object storage as the foundation, but adds a layer on top that brings in the things that made warehouses trustworthy in the first place:

* [ACID transactions](https://www.youtube.com/watch?v=oGmxzUBCYtY)
* [Schema enforcement](https://docs.databricks.com/aws/en/tables/schema-enforcement)
* [Schema evolution](https://www.mongodb.com/docs/manual/core/schema-validation/)
* [Versioning / time travel](https://medium.com/@prachikushwah/data-versioning-using-time-travel-feature-5a5bde2c5e3)
* [Table metadata](http://docs.sqlalchemy.org/en/latest/core/metadata.html)
* [Data governance](https://www.youtube.com/watch?v=6kFByuEK1lc&t=34s)
* [Performance optimisation](https://www.geeksforgeeks.org/sql/sql-performance-tuning/)

> [!NOTE]
> **A lake-house is an architectural pattern, rather than a specific technology.**
>
> This pattern is enabled by tools like:
> Databricks + Delta Lake, Snowflake's modern architecture / Iceberg support, AWS + S3 + Iceberg, BigQuery + BigLake & Microsoft Fabric (*ew*)

### Compute vs Storage ⚙️

There's another important idea hiding underneath the whole Data Lakehouse architecture: **storage and compute can be decoupled.**

Traditionally, a database is responsible for both:

* Storage
* Compute

However, Cloud data platforms changed this relationship.

Instead, we can keep our data in relatively cheap object storage and bring compute to it when we actually need to do something with it:

<!--  -->
{{< mermaid >}}
graph TD;
    subgraph Compute
        A["Spark"]
        B["SQL"]
        C["BI / ML"]
    end

    A --> D[("Object Storage")];
    B --> D;
    C --> D;

    D["S3 / ADLS / GCS"];
{{< /mermaid >}}

This is one of the reasons data lakes became so attractive. We can store enormous amounts of data without needing a database engine sitting there processing it 24/7.

### ETL vs ELT 🔄

We've talked a lot about moving data around, but there's another question... **When should we transform it?**

There are two common approaches: **ETL** and **ELT**.

<!-- ETL vs ELT Image -->
![ETL vs ELT](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKLcr1nz4H_QFBJ-FQxzogdMVxBYj1SHu6Y7e0bTyT0uEjhGuecEbcidAP&s=10)

#### ETL — Extract, Transform, Load

The traditional approach is:

```text
Source
  ↓
Extract
  ↓
Transform
  ↓
Load
  ↓
Warehouse
```

We take the data out of the source system, clean and reshape it, and then load the transformed result into the warehouse.

This made a lot of sense when storage and compute were relatively expensive and the warehouse was expected to contain mostly clean, structured data.

#### ELT — Extract, Load, Transform

Modern cloud platforms often flip that around:

```text
Source
  ↓
Extract
  ↓
Load
  ↓
Data Lake / Lakehouse
  ↓
Transform
  ↓
Analytics
```

Instead of transforming everything before storing it, we can **store the raw data first** and transform it later.

This works particularly well with cheap, scalable object storage.

It also means we don't necessarily have to decide exactly what the data will look like before we've even stored it.

And this is another reason the lakehouse architecture is interesting: the same underlying data can support raw ingestion, transformation, analytics and machine learning without necessarily requiring a separate copy of the data for every stage.

So, very roughly:

> **ETL:** "Clean it, then store it."

> **ELT:** "Store it, then figure out what to do with it."

<!-- Side note [JordanHasNoLife](https://www.youtube.com/@jordanhasnolife5163) is "*funny as aye*":

![This Guy](https://i.ytimg.com/vi/vkLAU23raOI/maxresdefault.jpg) -->

## The Mental Model 🧠

Wrapping up, if I had to boil this whole post down to why each system exists, not just what it does, I'd put it like this:

* Database = "*I need to run an application, correctly, right now.*"
* Data Warehouse = "*I need to analyse structured business data, without breaking the application.*"
* Data Lake = "*I need somewhere cheap and flexible to store everything else.*"
* Data Lakehouse = "*I need the lake's flexibility and the warehouse's trust, without running two systems to get both.*"

So no, **you don't always need a lakehouse**.

Plenty of business's and teams exist right now who are served perfectly well by just a database, or a warehouse, or a lake on its own.

But once you've felt the pain of maintaining two systems just to cover each other's gaps, it becomes obvious why the lakehouse showed up.

Cheers!

{{< subscribe >}}
