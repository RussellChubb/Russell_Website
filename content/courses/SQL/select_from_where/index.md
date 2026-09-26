---
title: "Select, From, Where"
description: "Introduction to the SELECT, FROM, and WHERE statements in SQL"
summary: "Introduction to the SELECT, FROM, and WHERE statements in SQL"
showAuthor: true
date: 2026-05-12
featureimage: "featured.png"
tags: ["SQL"]
series: ["Learn SQL"]
series_order: 1
---

## Video 📹

<!-- YouTube Video Link -->
{{< youtubeLite id="H0yHQS5jWpU" label="SQL - Select From Where" >}}

## SELECT and FROM

The `SELECT` statement is used to fetch data from a database and is one of the most fundamental building blocks of SQL queries. The `FROM` statement specifies the exact table and database target from which to retrieve that data.

> [!NOTE]
> SQL statement execution order is strict. A query must define what to fetch (`SELECT`) and where to fetch it from (`FROM`) before applying filters.

### SELECT and FROM Syntax

To return all columns from a table, use the asterisk (`*`) wildcard:

```SQL
SELECT * 
FROM table_name;
```

To specify individual columns rather than fetching the entire dataset:

```SQL
SELECT column1, column2, ...
FROM table_name;
```

### Demo Database

Below is a selection from a made-up **People table** (*from Russell's Surf Store Database*):

| PersonID | Name           | Age | City      |
|---------:|----------------|----:|-----------|
| 1        | Oscar Macdonald| 25  | Brighton  |
| 2        | Kian Knight    | 25  | Munich    |
| 3        | Jock Adams     | 25  | Sydney    |
| 4        | Liam Barnes    | 25  | Vancouver |
| 5        | Jake Faville   | 24  | Cork      |

## WHERE

The `WHERE` clause is used to filter records so that only rows meeting specific criteria are returned.

### WHERE Syntax

```SQL
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

### SQL WHERE Example

The following SQL returns only the names and ages of people older than 30:

```SQL
-- Example
SELECT Name, Age
FROM my_dataset.my_table
WHERE Age > 30;
```

## Query Rules & Best Practices

### 1. Clause Order

Statements must follow a strict order (`SELECT` → `FROM` → `WHERE`). Placing clauses out of sequence will result in a syntax error:

```SQL
-- Incorrect Query (Will not execute):
WHERE Age > 30;
SELECT Name, Age
FROM my_dataset.my_table
```

### 2. Case Sensitivity

SQL keywords are generally case-insensitive, meaning the following queries produce identical results:

```SQL
-- Uppercase (Recommended)
SELECT Name, Age
FROM my_dataset.my_table
WHERE Age > 30;

-- Lowercase
select Name, Age
from my_dataset.my_table
where Age > 30;
```

> [!NOTE]
> While keywords are case-insensitive, string literals (e.g., `'John'`) or database object names may be case-sensitive depending on the database engine.

### 3. Readability & Performance

* **Keywords vs. Identifiers:** Write keywords in `UPPERCASE` and column/table names in `lowercase` or `PascalCase`.
* **Line Breaks:** Avoid running long queries on a single line. Break statements onto new lines for legibility.
* **Avoid `SELECT *` in Production:** Explicitly state column names instead of using `*` to optimize performance and reduce unnecessary query bandwidth.
