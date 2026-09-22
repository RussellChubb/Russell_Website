---
title: "SQL"
description: "Russell's SQL Course"
draft: true
---

<!-- Shout out to all my Tik Tok Hustlers who think they're going to escape a permanent underclass by selling courses lol -->
{{< typeit
  tag=h4
  speed=80
  lifeLike=true
  breakLines=true
  loop=false
>}}

Wrong Database Selected...


(8309560 Rows Affected)


( ͡ʘ ͜ʖ ͡ʘ)

{{< /typeit >}}

---

SQL, or Structured Query Language, is a powerful tool used for managing and manipulating databases. Whether you're pulling data for reports, analyzing trends, or just curious about your dataset, SQL is the go-to language.

SQL was developed in the early 1970s at IBM by Donald D. Chamberlin and Raymond F. Boyce. Originally called SEQUEL, or Structured English Query Language, it was designed to manipulate and retrieve data stored in IBM's original quasi-relational database management system, System R. In 1979, Oracle released the first commercial implementation of SQL.

Today, SQL is essential across various relational database management systems like MySQL, PostgreSQL, Microsoft SQL Server, and Google BigQuery. However, with the advent of big data, NoSQL databases like MongoDB and Cassandra have gained traction, offering scalability and flexibility. Despite this, SQL remains crucial for data professionals due to its standardized querying and manipulation capabilities across relational and non-relational databases.

SQL operates on relational databases, which store data in tables composed of rows and columns. Columns represent the different attributes or fields of the data, while rows represent individual records.

A relational database is a type of database that stores data in tables that can be related to each other. This relationship is established through keys, both primary and foreign.

A primary key is a unique identifier for each record in a table. For example, in an 'employees' table, the 'employee_id' could be the primary key, ensuring each employee is uniquely identifiable.

A foreign key is a field in one table that uniquely identifies a row of another table. It creates a link between the two tables. For example, an 'orders' table might have a 'customer_id' that serves as a foreign key linking to the 'customers' table's primary key.

This relational structure allows us to efficiently organize, retrieve, and manage large amounts of data across different tables. Now that we have a basic understanding of tables, rows, columns, and what relational databases are, let’s write a simple SQL query.

NOTE: The SQL variant that I’ll be using is Google’s Big Query, however, the syntactic differences between BigQuery, and other SQL dialects is fairly minimal. With this in mind, let's navigate to bigquery and see how we can start writing our own SQL queries.

First, log in to your Google Cloud Console. Navigate to BigQuery from the main menu. Here, you'll see the BigQuery editor where you can write and execute your SQL queries.

Let's write our first SQL query, the database that I’m going to be querying is the Russ_Mix table, from the Russ.All Database.

```SQL
SELECT *
FROM `mix-data-421423.Russ_All.Russ_Mix` 
LIMIT 10
```

This query selects all rows and columns from the Russ_Mix table, but limits the amount of rows returned to 10.

If you don’t fully understand what’s going on in this query, don’t worry, as I’ll be covering how to build out your own queries using SQL syntax in a future video.

That's it for our introduction to SQL in BigQuery. Thanks for watching, and feel free to leave any questions or feedback in the comments below.
