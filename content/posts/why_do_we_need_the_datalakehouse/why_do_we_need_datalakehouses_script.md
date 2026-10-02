# Video Script: Why Do We Need the Data-Lakehouse?

So there's this Reddit exchange that I think about a lot. Someone asks: "*How do you decide between a database, a data lake, a data warehouse, or a lakehouse?*". The top reply is just: "That's the neat thing — they all become data swamps.". Funny, anyway, businesses have data coming out of their ears.

Over the years, we've invented four completely different places to put it: databases, data lakes, data warehouses, and now lakehouses.

Now, today I want to examine why we kept needing the *next* one? Fundamentally, each one showed up because the last one was failing at something. And once you see it that way, the Data-Lakehouse stops looking like a buzzword and starts looking like... the inevitable result of two systems that were each really good at one job, and genuinely bad at the other.

Let's build up to it properly.

Before any of this makes sense, we need two acronyms: OLTP and OLAP. They sound intimidating. They're not.

OLTP is Online Transaction Processing. It's about *running an application*.

Say I've got an online shop — "Russell's Widgets." Someone buys a widget. The system now has to, in order: create the order, update the customer's account, subtract one from inventory, and record the payment.

And it has to do that correctly, and fast, every single time. That's what relational databases — Postgres, MySQL, SQL Server — are built for: transactions, constraints, consistency, handling lots of writes at once.

OLAP is Online Analytical Processing, and it's a completely different question. Instead of "which widget did this one customer just buy," it's: "what were our total widget sales by product, region, and month, over the last five years?"

That could mean scanning millions or billions of rows. Joining datasets. Aggregating. That's not a quick transaction — that's a big, slow, heavy read.

So here's the tension, right at the start: one kind of system is built for lots of tiny, protected writes. Another is needed for huge, sprawling reads. That mismatch is the root of everything we're about to talk about.

The database is our system of record. It's what the application actually needs to run. It's great at OLTP.

But then the CEO walks over and asks: "can you tell me how revenue's changed by customer segment over the last ten years?"

Technically, you *could* run that against production. You really shouldn't. Your poor Postgres instance has enough on its plate without a ten-year analytical query running at the same time ten thousand customers are trying to check out.

So the database, on its own, isn't the full answer. We need somewhere else to send the big questions.

That's the Data Warehouse. Its whole reason for existing is: handle analytical workloads *without* wrecking the application.

Instead of being the thing that powers the app, it's the place we bring data together specifically to analyse it. Production keeps running the app, the warehouse handles the questions, and the data usually gets reshaped along the way — fact tables, dimension tables, star schemas, the works.

And to be fair — this is a genuinely good solution, for structured, well-understood business data.

But that's the catch. It assumes the data already looks like tidy rows and columns. What happens when it doesn't?

Now imagine your company's also pulling in APIs, CSV exports, JSON, logs, IoT data, images, video, event streams. Forcing all of that into a relational schema before you've even stored it? That's a losing game.

So the Data Lake solves a *different* problem than the warehouse. Not "how do I analyse structured data" — but "where do I even put everything else, cheaply, before I know what I'll do with it."

It's great when you don't yet know how the data will be used, when you're dealing with huge volumes, when you need to keep the raw version, or when it's just not structured at all.

Great — flexibility problem solved. Except now remember that Reddit quote.

"They all become data swamps." Dump everything into object storage with no governance, no metadata, no ownership, and you get exactly this: final.csv, final_final.csv, final_v2.csv, definitely_final.csv, a raw folder, a raw_new folder, a raw_old folder, and a folder literally called PLEASE_DO_NOT_DELETE.

The lake's biggest strength — "put anything here, we'll sort it out later" — is the exact same thing that turns it into a swamp.

So here's where we've landed. The warehouse is trustworthy but rigid. The lake is flexible but messy. And a lot of teams respond to that by just... running both. A lake for the raw stuff, a warehouse for trusted BI, and a small army of pipelines constantly copying data between them to keep everyone happy.

That's two systems to pay for. Two systems to secure. And data duplicated — and slowly drifting out of sync — between them.

*That's* the real reason the Data-Lakehouse needed to exist. Not because lakes or warehouses are bad — but because permanently running both, just to cover for each other's weaknesses, is expensive and fragile.

The lakehouse keeps the lake's cheap, flexible storage as the foundation, but bolts on the things that made warehouses trustworthy in the first place: ACID transactions, schema enforcement and evolution, versioning and time travel, table metadata, governance, SQL analytics, performance optimisation.

One copy of the data. One system. Flexible enough for a data scientist, reliable enough for the CFO. That's what Delta Lake, Apache Iceberg, and Apache Hudi are actually doing under the hood — giving object storage the table-like guarantees it never had on its own.

If you take one thing away from this video, let it be this:

- Database — "I need to run an application, correctly, right now."
- Data Warehouse — "I need to analyse structured business data, without breaking the application."
- Data Lake — "I need somewhere cheap and flexible to store everything else."
- Data Lakehouse — "I need the lake's flexibility and the warehouse's trust — without running two systems to get both."

So no — you don't always need a lakehouse. Loads of teams are perfectly well served by just a database, or just a warehouse, or just a lake. But the moment you've felt the pain of running two systems just to patch each other's gaps, the lakehouse stops being a buzzword and starts making a lot of sense.

That's it for this one — if this helped, subscribe for more of these, and I'll catch you in the next video.
