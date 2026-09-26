# Select From Where Script

This video covers an introduction to the SELECT, FROM and WHERE statements in SQL.
The SELECT statement is used to fetch data from a database, and is one of the most commonly used SQL statements.
You can use the SELECT statement to return all columns from a table by using the asterisk wildcard by typing

```SQL
SELECT *
```

When writing queries, you may want to specify the columns you want returned. In this case, you can specify the column names in the query, for example:

```SQL
SELECT column1, column2, ...
```

NOTE: The previous two example queries, won’t actually return anything, as we need to specify where we’d like SQL to pull the data from, by using the next statement “FROM”.

The FROM statement, allows us to specify the table, and database that we’d like our query to target. For example, let’s build on our original example by typing FROM, then “table_name”, and then finish the query with a semicolon, which tells SQL that we’ve ended the statement.

```SQL
SELECT * 
FROM table_name;
```

Not all SQL dialects require the use of the semicolon to end a query, however, it’s good practice to use semicolons, especially when writing multiple queries in a script.

When writing queries, you may also want to filter records based on specific conditions, in these situations, we can use the WHERE clause.

For example, if we wanted a query to select only the rows where age is greater than 30, we’d type:

```SQL
SELECT name, age
FROM my_dataset.my_table
WHERE age > 30;
```

This query then returns the names and ages of people older than 30.

One thing to keep in mind when writing SQL queries, is that the order of statements and clauses must be strictly followed to ensure the query executes correctly.

To demonstrate this principle, this query won’t run in SQL, as the order of statements isn’t being correctly followed.

```SQL
WHERE age > 30;
SELECT name, age
FROM my_dataset.my_table
```

SQL is generally case-insensitive, meaning that keywords like `SELECT`, `FROM`, and `WHERE` can be written in uppercase, lowercase, or a mix of both.

For example, the following queries are equivalent:

```SQL
SELECT name, age
FROM my_dataset.my_table
WHERE age > 30;

select name, age
from my_dataset.my_table
where age > 30;
```

However, case sensitivity can matter when dealing with string comparisons or database object names, depending on the database system.

```SQL
SELECT name
FROM my_dataset.my_table
WHERE name = 'John';  -- Case-sensitive comparison in some databases
```

To ensure consistency and readability, it's a good practice to write SQL keywords in uppercase and identifiers (like table and column names) in lowercase.
Other good practice SQL habits include proper indentation, as it’s crucial for making SQL queries more readable and maintainable.

For instance, this code would still run in SQL:

```SQL
SELECT name, age FROM my_dataset.my_table WHERE age > 30;
```

However, this code (*in my humble opinion*) is much more legible, as you’re able to see the query statements, line by line.

```SQL
SELECT name, age
FROM my_dataset.my_table
WHERE age > 30;
```

Where possible, also use the specific column names you’re looking to return, instead of always using the asterisk wildcard, to optimize performance, and query times.

Cool, let’s finish the video off with a quiz:

Question # 1 - Easy. What does the asterisk wildcard allow you to do when combined with the Select Statement?

```SQL
SELECT * 
```

Question # 2 - Medium. Why do we use the semicolon at the end of our queries?

```SQL
SELECT name, age
FROM my_dataset.my_table
WHERE age > 30;
```

Question # 3 - Hard. Why does this Query not run

```SQL
WHERE age > 30;
SELECT name, age
FROM my_dataset.my_table
```

This concludes my introduction to `SELECT`, `FROM` and `WHERE` in SQL. If you like the video, like the video, if you’d like to see more of me, press subscribe.

Thanks for watching.
