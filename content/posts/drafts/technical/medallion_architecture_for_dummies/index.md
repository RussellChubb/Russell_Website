---
title: "Medallion Architecture for Dummies"
description: "A practical introduction to Bronze, Silver, and Gold data layers — and the marketing behind them."
summary: "What Medallion Architecture actually is, why you'd use it, and when data should move from Bronze to Silver to Gold."
showReadingProgress: true
draft: true
showAuthor: true
featureimage: "featured.png"
date: 2026-10-04
tags: ["Technical", "Data Engineering"]
---

<!-- Space for a Quote -->
{{< typeit
  tag=h4
  speed=80
  lifeLike=true
  breakLines=true
  loop=false
>}}
u/jeffvanlaethem:  

Bronze: Raw data

Silver: Cleaned

Gold: Shaped and Casted appropriately

Platinum: Cross-joined to every table in your warehouse

Uranium: Irrelevant PII added to every record

Diamond: Everything exported in MS Word files

Unobtanium: All the MS Word files committed to a branch in a public github repo

Ether: Entire department laid off
{{< /typeit >}}

---

<!-- TODO -->
<!-- Redo intro with either my question, or with something about cutting through marketing hype and renaming old patterns -->
<!-- Add Bronze Silver Gold Images to the Thumbnail -->

You've probably seen this before:

<!-- Medallion Architecture Image -->
![Medallion_Databricks](https://www.databricks.com/sites/default/files/inline-images/building-data-pipelines-with-delta-lake-120823.png)

It looks simple. And, to be fair, it is.

But somewhere along the way, three fairly sensible ideas about organising data turned into "*The Medallion Architecture™*", complete with:

* diagrams
* conference talks
* consulting decks

<!-- Trying out a Gallery -->
{{< gallery >}}
  <img src="https://i.programmerhumor.io/2025/08/f470e30d6c89733466baa6a4265675f388d2d93b99b739e855e301cc4fd8f218.png" alt="Gallery image 1" caption="First caption" class="grid-w50 md:grid-w33 xl:grid-w25"/>

  <img src="https://preview.redd.it/my-linkedin-profile-v0-bka1gb843z7z.jpg?auto=webp&s=6cfb96d8655d60640be922271e2ce66569730a34" alt="Gallery image 2" caption="Second caption" class="grid-w50 md:grid-w33 xl:grid-w25"/>

  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlZHEsR7xWXsnAyYJ3aepny_tNh6bdhP88cgYLhLbSvkrupaNZtYiTmCk&s=10" alt="Gallery image 2" caption="Third caption" class="grid-w50 md:grid-w33 xl:grid-w25" />
{{< /gallery >}}

So what actually is it? But more importantly:

<!-- Main Lead -->
{{< lead >}}
> **Why should you care?**
{{< /lead >}}

## What is Medallion Architecture?

Medallion Architecture is a way of organising data into progressively more useful layers. The three commonly used layers are:

* 🥉 Bronze — raw data
* 🥈 Silver — cleaned and structured data
* 🥇 Gold — business-ready data

The basic idea is:

```text
Raw
 ↓
Clean
 ↓
Useful

Or, if you prefer the corporate version:

Bronze
   ↓
Silver
   ↓
Gold
```

The important thing is that each layer has a different job, and that despite the naming convention, there is value in each of the layers.

<!-- Meme I'm probably going to remove later -->
![Hmmm](https://i.programmerhumor.io/2025/11/48f56cec67143e89d98a639c0c83cc52743b5e8eee008155f753e44591d088eb.jpeg)

### 🥉 Bronze — Keep the Raw Stuff

You can think of "Bronze" as the landing zone for raw data. The primary objective in this space isn't to make the data beautiful, it's to instead preserve what you have received.

Imagine an energy company called "*Russell's Energy Company*" where-in IoT devices send generation data every five minutes:

<!-- TODO -->
<!-- Convert to MD Table -->
timestamp           site        generation_mw
2026-10-01 10:00    Site A      42.7
2026-10-01 10:05    Site A      43.1
2026-10-01 10:10    Site A      41.9

This data might get moved into a bronze table, as is, or there might be some ingestion meta-data added at this stage (*it's really down to the specific business requirement*).

I've added some examples of ingestion meta-data below.

```text
_ingested_at
_source
_file_name
_batch_id
```

However, generally Bronze isn't where you want to be doing loads of business logic (*ergo you might choose to omit the ingestion columns*).

#### Why keep raw data?

For the following reasons:

* Data pipelines break.
* Sources change.
* People make mistakes.

Think about an imaginery situation (*not one that I've never personally been in during my time working at an electricity company*) where someone asks:

> "*Why does this number look different from what we reported three months ago?*"

If we've already transformed everything immediately and thrown away the original data, we've got a problem...

However... if you've kept the raw data, you can go back and investigate.

So to summarize bronze, it's essentially your "*source-of-truth-ish*" copy of what arrived.

> [!NOTE]
> **Not necessarily the ultimate source of truth!**
> That's an important distinction — but a record of what your pipeline received.

### 🥈 Silver — Make It Usable

Silver is where we start making the data actually pleasant to work with. This where the following things start happening:

* cleaning
* deduplication
* type conversion
* standardisation
* joins
* validation
* handling missing values
* basic transformations

For example, Bronze might contain:

<!-- TODO -->
<!-- Convert to .md table -->
timestamp             site       generation
01/10/2026 10:00      Site A    "42.7"
01/10/2026 10:05      Site A    "43.1"
01/10/2026 10:10      Site A    "N/A"
01/10/2026 10:10      Site A    "41.9"

Silver might turn that into:

<!-- TODO -->
<!-- Convert to .md table -->
timestamp            site       generation_mw
2026-10-01 10:00     Site A     42.7
2026-10-01 10:05     Site A     43.1
2026-10-01 10:10     Site A     NULL

We've:

* parsed the timestamp
* converted generation to a numeric type
* standardised the column name
* dealt with the invalid value
* removed the duplicate

Which now makes the data much easier for downstream systems to consume.

### 🥇 Gold — Make It Useful to Humans

Gold is where we start thinking less about what the source system looks like and more about what the business wants to know.

For example, Silver might contain:

```text
timestamp
site
generation_mw
```

But a business user might want:

```text
site
date
total_generation_mwh
average_generation_mw
capacity_factor
```

#### Charcteristics of Gold

Gold datasets are often:

* aggregated
* business-oriented
* modelled for specific use cases
* optimised for reporting
* consumed by BI tools, applications, analysts or ML models

You might have a Gold table called `daily_site_generation` rather than `raw_generation_readings`

## Why Bother? 🤷‍♂️

At this point you might be thinking:

> "*Couldn't I just put everything in one table?*"

Fuck yeah, technically you could (*And for a small project, you probably should*).

Medallion Architecture becomes useful when your data platform starts becoming more complicated...

Imagine this:

```text

             ┌─────────────┐
             │  Source A   │
             └──────┬──────┘
                    │
             ┌──────▼──────┐
             │   Bronze    │
             └──────┬──────┘
                    │
             ┌──────▼──────┐
             │   Silver    │
             └──────┬──────┘
                    │
             ┌──────┴──────┐
             ↓             ↓
        ┌──────────┐  ┌──────────┐
        │   Gold   │  │   Gold   │
        │   BI     │  │    ML    │
        └──────────┘  └──────────┘
```

Now you have:

* multiple consumers.
* Your BI dashboard wants one version of the data & Your ML model wants another.
* An analyst wants something slightly different.
* A new source system arrives.

Suddenly, having some structure starts looking like a pretty good idea.

## When Does Data Move Between Layers? ➡️

This is a question that I personally had before starting this article, and my mother used to tell me that if I had a question, it's more than likely that someone else has the same question.

From my research, I've found that there isn't some magical moment when a Bronze table becomes Silver.

There is no:

```python
if data.is_ready():
    move_to_silver()
```

Instead, you **internally define the rules for each layer.**

A useful way to think about it is:

> Data moves to the next layer when it meets the quality and transformation requirements of that layer.

For example:

### Bronze → Silver

You might move data into Silver when:

* the schema has been interpreted
* data types are correct
* duplicates have been handled
* obvious invalid records have been dealt with
* identifiers have been standardised
* data quality checks pass

### Silver → Gold

You might move data into Gold when:

* the data is trustworthy enough for consumption
* business definitions have been applied
* required joins have been performed
* aggregations have been created
* the dataset serves a specific business use case

The important point is:

**Bronze, Silver and Gold aren't really stages of time. They're stages of responsibility.**

## Does Everything Have to Go Through All Three?

**Nope!** - This is where the marketing starts to creep in. You might hear something like:

> "*All data should flow through the Bronze → Silver → Gold architecture*".

That sounds nice... It also isn't necessarily true.

Imagine you ingest a reference table containing:

```text
country_code
country_name
continent
```

You might barely need a Bronze/Silver/Gold pipeline for that. Or perhaps you've got a small application where the raw data is already clean and structured.

Creating three layers because "*that's the architecture*" could make the system worse, not better. Architecture exists to solve problems.

Not to make diagrams look impressive.

## The Marketing Hype

"*Medallion Architecture*" sounds like a grand architectural philosophy, but if you strip away the branding, the underlying idea is pretty straightforward:

**Keep your raw data, clean it, then create data products from it.**

The terms Bronze, Silver and Gold are useful because they give teams a shared vocabulary. Instead of saying:

> "*The cleaned-but-not-yet-business-modelled version of the customer data...*"

you can say:

> "*It's in Silver.*"

The problem comes when the terminology starts being treated as a set of commandments.

### Bronze Doesn't Mean Bad

I touched on this at the start, but one of the stranger implications of the terminology is that Bronze sounds like the "bad" data.

**FYI: It's not.**

Bronze data can be extremely valuable. In fact, its rawness is the point. A Bronze dataset might be the only copy you have of exactly what a source system sent you.

That's useful for:

* auditing
* debugging
* replaying pipelines
* investigating historical changes
* recovering from transformation bugs

So don't think:

```python
Bronze == Bad
Silver == Good
Gold == Great
```

Think:

```python
Bronze == Raw
Silver == Refined
Gold == Purpose-built
```

**Silver Doesn't Mean Perfect!** - Similarly, Silver isn't necessarily "*clean data*".

It's data that has been cleaned **according to the requirements of your system**.

There can still be:

* missing values
* anomalies
* late-arriving records
* questionable source data
* business-specific edge cases

Data quality is not binary. A dataset doesn't suddenly become trustworthy because somebody moved it to an environment / folder called "*silver*".

This is another important distinction. Gold isn't necessarily more correct than Silver. It's usually more useful for a particular purpose.

For example:

```text
Silver
│
├── customer_id
├── transaction_id
├── timestamp
├── product_id
└── amount
```

might be a great general-purpose dataset.

Gold might contain:

```text
customer_id
month
total_spend
number_of_orders
average_order_value
```

That's much more useful for a sales dashboard. But it's terrible if you suddenly need individual transactions.

Gold is therefore often purpose-built rather than universally better.

## The Real Architecture

If you strip away the terminology, the architecture is really about controlling the flow of data:

```text
              Preserve
                 ↓
               Refine
                 ↓
              Consume
```

Or:

```text
     What did we receive?
              ↓
     What does it actually mean?
              ↓
     What does the business need?
```

That's the useful mental model. The Bronze/Silver/Gold labels are just names we put on those concepts.

## When Should You Use Medallion Architecture?

I'd consider it when:

* you have multiple data sources
* you need reproducible transformations
* data quality is becoming a problem
* multiple teams consume the same data
* you need to reprocess historical data
* you're building a lakehouse
* you're starting to create multiple downstream data products

I'd probably not reach for it just because you have a CSV file.

If your entire data platform is just this:

```text
sales.csv
   ↓
pandas
   ↓
chart
```

You probably don't need a three-layer architecture (*You've got bigger things to worry about.*)

## The Big Idea

Medallion Architecture isn't really about Bronze, Silver and Gold. It's about separating responsibilities.

Bronze answers:

> "*What did we receive?*"

Silver answers:

> "*What does this data actually look like and mean?*"

Gold answers:

> "*How can we make this useful for a particular consumer?*"

> [!Important]
> Don't build Bronze, Silver and Gold because someone put it in a PowerPoint.

Build layers when the separation solves a problem! Otherwise you're just putting medals on your CSV files.