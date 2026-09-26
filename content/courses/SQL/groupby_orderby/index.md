---
title: "Group By, Order By"
description: "Introduction to the Group By, Order By parameters in SQL"
summary: "Introduction to the Group By, Order By parameters in SQL"
showAuthor: true
date: 2026-05-11
featureimage: "featured.png"
tags: ["SQL"]
series: ["Learn SQL"]
series_order: 2
---

## Video 📹

<!-- YouTube Video Link -->
{{< youtubeLite id="3fP22J2FRT8" label="SQL - Group By Order By" >}}

## GROUP BY

The `GROUP BY` statement is used to group rows that have the same values into summary rows, like "*Find the number of customers in each country*".

> [!NOTE]
> The `GROUP BY` statement is almost always used in conjunction with aggregate functions, like `COUNT()`, `MAX()`, `MIN()`, `SUM()`, `AVG()`, to perform calculations on each group.

### GROUP BY Syntax

```SQL
SELECT column1, aggregate_function(column2), column3, ...
FROM table_name
WHERE condition
GROUP BY column1, column3
ORDER BY column_name;
```

### Demo Database

Below is a selection from a made-up **Customers table** (*from Russell's Surf Store Database*).

| CustomerID | CustomerName           | ContactName      | Address           | City      | PostalCode | Country   |
|-----------:|------------------------|------------------|-------------------|-----------|------------|-----------|
| 1          | Coastal Surf Co.       | Oscar Macdonald  | 14 Harbour Road   | Brighton  | BN1 4QF    | UK        |
| 2          | Alpine Outdoor Gear    | Kian Knight      | 27 Bergstrasse    | Munich    | 80331      | Germany   |
| 3          | Pacific Wave Supplies  | Jock Adams       | 82 Ocean Avenue   | Sydney    | NSW 2000   | Australia |
| 4          | North Shore Adventures | Liam Barnes      | 51 Beach Road     | Vancouver | V6K 2G2    | Canada    |
| 5          | Atlantic Surfwear      | Jake Faville     | 9 Seaview Terrace | Cork      | T12 X2F5   | Ireland   |

### SQL GROUP BY Examples

The following SQL returns the number of customers in each country:

```SQL
-- Example
SELECT Country, COUNT(CustomerID) AS [Number of Customers]
FROM Customers
GROUP BY Country;
```

The following SQL returns the number of customers in each country, sorted from high to low:

```SQL
-- Example
SELECT Country, COUNT(CustomerID) AS [Number of Customers]
FROM Customers
GROUP BY Country
ORDER BY COUNT(CustomerID) DESC;
```

## ORDER BY

The `ORDER BY` keyword is used to sort the result set in ascending or descending order. By default, it sorts in ascending order (`ASC`).

```SQL
-- Example:
-- Sort the products from lowest to highest price:
SELECT *
FROM Products
ORDER BY Price;
```

### Order By Syntax

```SQL
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC;
```

### Example Database

Below is a made-up selection from a **Products table** (*from Russell's Surf Store Database*) used in the examples below:

| ProductID | ProductName       | SupplierID | CategoryID | Unit      |  Price |
| --------: | ----------------- | ---------: | ---------: | --------- | -----: |
|         1 | 6' Fish Surfboard |          1 |          1 | 1 board   | 449.99 |
|         2 | 7' Funboard       |          1 |          1 | 1 board   | 599.99 |
|         3 | 3/2mm Wetsuit     |          2 |          2 | 1 wetsuit | 129.99 |
|         4 | Reef Surf Wax     |          2 |          3 | 12 bars   |  24.99 |
|         5 | Leash 7ft         |          3 |          4 | 1 leash   |  34.99 |

### Order Descending

To sort the records in descending order, use the `DESC` keyword.

```SQL
-- Example:
-- Sort the products from highest to lowest price:
SELECT * 
FROM Products
ORDER BY Price DESC;
```

### Order Alphabetically

For string values, the `ORDER BY` keyword sorts the values in the column alphabetically:

```SQL
-- Example
-- Sort the ProductName column alphabetically:
SELECT *
FROM Products
ORDER BY ProductName;
```

### Alphabetically DESC

To sort text values in descending order, use the `DESC` keyword:

```SQL
-- Example
-- Sort the ProductName column in reverse alphabetical order:
SELECT *
FROM Products
ORDER BY ProductName DESC;
```

The following SQL statement selects all customers from the `Customers` table and sorts them by `Country`, then by `CustomerName`.

This means it sorts by `Country` first, and if two records share the same country, it sorts them by `CustomerName`:

```SQL
-- Example
SELECT * 
FROM Customers
ORDER BY Country, CustomerName;
```

### Combine ASC and DESC

The following SQL statement selects all customers from the `Customers` table and sorts them in ascending order by `Country` and descending order by `CustomerName`:

```SQL
-- Example
SELECT * 
FROM Customers
ORDER BY Country ASC, CustomerName DESC;
```
