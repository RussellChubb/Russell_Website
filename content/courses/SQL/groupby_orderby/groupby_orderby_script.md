# Group By Order By Script

Today we're looking at two pretty simple SQL statements:

`GROUP BY` and `ORDER BY`. They're both useful for organising your query results, but they do two different things.

* `GROUP BY` groups rows together.
* `ORDER BY` sorts your results.

Let's start with `GROUP BY`.

---

## GROUP BY

Here's our Customers table, we've got customers from a few different countries. If I wanted to see how many customers we have from each country, I can use:

```sql
SELECT Country, COUNT(CustomerID) AS [Number of Customers]

FROM Customers

GROUP BY Country;
```

Here, `GROUP BY Country` groups all of the customers based on their country. Then `COUNT()` counts the customers within each group.

So, instead of getting every individual customer back, we might get something like the following back:

```text
UK          428
Germany     312
Australia   197
Canada      154
Ireland      83
```

This is where `GROUP BY` is usually used alongside aggregate functions.

Some common aggregate functions are:

```text
* COUNT()
* SUM()
* AVG()
* MIN()
* MAX()
```

For example, if we had a sales table, we could calculate the total sales for each customer:

```sql
SELECT CustomerID, SUM(Total) AS [Total Sales]

FROM Sales

GROUP BY CustomerID;
```

So the basic idea is:

**`GROUP BY` tells SQL what to group by, and the aggregate function tells SQL what to calculate.**

---

## ORDER BY

Next up is `ORDER BY`, which is used to sort your results. For example, if I want to sort my products by price:

```sql
SELECT *

FROM Products

ORDER BY Price;
```

By default, SQL sorts in ascending order, so we'd get the cheapest products first:

```text
24.99
34.99
129.99
449.99
599.99
```

If we want the most expensive products first, we can use `DESC`:

```sql
SELECT *

FROM Products

ORDER BY Price DESC;
```

Now the order is:

```text
599.99
449.99
129.99
34.99
24.99
```

So:

```text
ASC  = lowest to highest
DESC = highest to lowest
```

---

## Sorting Text

`ORDER BY` also works with text.

For example:

```sql
SELECT *

FROM Products

ORDER BY ProductName;
```

This sorts the products alphabetically.

And we can use `DESC` for reverse alphabetical order:

```sql
SELECT *

FROM Products

ORDER BY ProductName DESC;
```

---

## Multiple Columns

We can also sort by multiple columns.

For example:

```sql
SELECT *

FROM Customers

ORDER BY Country, CustomerName;
```

SQL will first sort by `Country`.

If two customers are from the same country, it then sorts those customers by `CustomerName`.

We can also specify the direction for each column:

```sql
SELECT *

FROM Customers

ORDER BY Country ASC, CustomerName DESC;
```

So countries are sorted A to Z, while customer names within each country are sorted Z to A.

---

## GROUP BY + ORDER BY

Finally, we can use these two together.

Going back to our customer example:

```sql
SELECT Country, COUNT(CustomerID) AS [Number of Customers]

FROM Customers

GROUP BY Country

ORDER BY COUNT(CustomerID) DESC;
```

First, `GROUP BY` groups the customers by country.

Then `COUNT()` counts the customers in each group.

Finally, `ORDER BY` sorts those groups from the largest number of customers to the smallest.

So we're combining the two:

**`GROUP BY` → creates the groups**

**`ORDER BY` → sorts the results**

And that's basically it.

`GROUP BY` is mainly used when you want to summarise your data into groups.

`ORDER BY` is used when you want to control the order of your results.

We'll use both of these quite a lot as we get into more complicated SQL queries.
