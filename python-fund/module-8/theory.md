# Module 8: Databases with Python

These notes explain the database ideas used in this module from the beginning. A **database** is an organized place to store information so a program can add it, find it, change it, or remove it later.

## 1. Why use a database?

A program can keep information in variables while it runs, but that information usually disappears when the program closes. A database stores information on disk so it is still available later. Databases are useful for student records, products, orders, appointments, and many other kinds of information.

## 2. Database vocabulary

- A **database** contains related information.
- A **table** stores one kind of information, much like a spreadsheet sheet.
- A **row** (also called a record) contains information about one item or person.
- A **column** (also called a field) describes one kind of information, such as `name` or `city`.
- A **primary key** is a value that uniquely identifies each row. An `id` column is often used for this.
- A **query** is an instruction sent to the database, usually written in SQL.

Imagine a `students` table with columns `id`, `name`, and `city`:

| id | name | city |
|---:|---|---|
| 1 | Harsh | Pune |
| 2 | Ashok | Baroda |

Each row is one student's record. The `id` distinguishes students even if two people have the same name.

## 3. SQL basics

**SQL** stands for Structured Query Language. It is the common language used to tell relational databases what data to store and retrieve. The module examples use SQL commands such as `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, and `DELETE`.

### Create a table

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    city TEXT
)
```

This creates a `students` table. `INTEGER` stores whole numbers; `TEXT` stores text. In SQLite, `AUTOINCREMENT` asks the database to assign increasing IDs for new rows.

### Add rows

```sql
INSERT INTO students (name, city)
VALUES ('Harsh', 'Pune')
```

The column names say where each value goes. Text values are enclosed in single quotes in SQL.

### Read rows

```sql
SELECT * FROM students
```

`SELECT` reads data. `*` means all columns. You can ask for selected columns, too:

```sql
SELECT name, city FROM students
```

### Filter rows

```sql
SELECT * FROM students WHERE city = 'Pune'
```

`WHERE` keeps rows that meet a condition. Without a `WHERE` condition, an update or delete can affect every row, so take care.

### Change rows

```sql
UPDATE students SET city = 'Surat' WHERE id = 1
```

This changes the city only for the row whose ID is 1.

### Delete rows

```sql
DELETE FROM students WHERE id = 1
```

This removes that row. A database deletion is not the same as deleting a Python variable; the stored row is removed from the database.

## 4. SQLite: a database in a file

SQLite is included with Python as the `sqlite3` module. It stores the database in a local file and does not require a separate database server. It is convenient for learning and small local applications.

```python
import sqlite3

connection = sqlite3.connect("school.db")
```

If `school.db` does not exist, SQLite creates it. If it already exists, SQLite opens it. The path is relative to the program's current working folder unless you give a full path.

## 5. Connections and cursors

A **connection** represents your program's connection to a database. A **cursor** is an object used to send SQL commands and read results. SQLite lets you run commands using either the connection directly or a cursor; using a cursor makes the database steps clear.

```python
connection = sqlite3.connect("school.db")
cursor = connection.cursor()
```

The examples use `db` for the connection and `cr` for a cursor. Variable names can differ; their roles are what matter.

## 6. Creating a table and inserting data in Python

```python
import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        city TEXT
    )
""")

cursor.execute(
    "INSERT INTO students (name, city) VALUES (?, ?)",
    ("Harsh", "Pune")
)
connection.commit()
connection.close()
```

`IF NOT EXISTS` avoids an error if the table is already present. `NOT NULL` means a value must be supplied for that column. `execute()` sends one SQL command. `commit()` saves changes such as table creation, inserts, updates, and deletes. `close()` releases the connection when finished.

## 7. Use placeholders for values

When a value comes from a user or a variable, do **not** build SQL by joining text together. Use placeholders. In SQLite, the placeholder is `?`:

```python
name = input("Student name: ")
city = input("City: ")

cursor.execute(
    "INSERT INTO students (name, city) VALUES (?, ?)",
    (name, city)
)
connection.commit()
```

The database safely treats the supplied values as data. Building SQL directly from user input can cause errors and can create a security problem called **SQL injection**. Database libraries use different placeholder styles; for example, PyMySQL commonly uses `%s`. Follow the library's documentation and use its parameter feature.

## 8. Read query results

Run a `SELECT` command, then fetch the result rows:

```python
cursor.execute("SELECT id, name, city FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)
```

Each row is usually returned as a tuple, for example `(1, 'Harsh', 'Pune')`.

- `fetchone()` gets the next single row, or `None` if there are no more rows.
- `fetchmany(2)` gets up to two rows.
- `fetchall()` gets all remaining rows as a list.

The module's `dbapp.py` demonstrates selecting records and looping over `fetchall()` results.

## 9. Save changes with `commit()`

Many database changes are part of a **transaction**. A transaction groups changes so they can be saved together. Call `commit()` when you want the changes to persist. If you close a connection without committing, pending changes may not be saved.

```python
cursor.execute("UPDATE students SET city = ? WHERE id = ?", ("Surat", 1))
connection.commit()
```

For more advanced programs, a failed group of changes can be undone with `rollback()` before closing or continuing.

## 10. Handling database errors and cleaning up

Database operations can fail: a table may already exist, the database file may not be writable, or a query may have a typo. Use `try`/`except` when you can respond usefully to an error, and make sure the connection is closed.

```python
import sqlite3

connection = sqlite3.connect("school.db")
try:
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM students")
    for row in cursor.fetchall():
        print(row[0])
finally:
    connection.close()
```

Python's `with` statement can also manage SQLite connections. In production code, handle expected exceptions thoughtfully rather than hiding all errors with an empty or overly broad `except` block.

## 11. SQLite and MySQL

The module includes both `sqlite3` and PyMySQL examples. SQLite uses a local database file. MySQL is a database server, usually running separately, and requires connection settings such as host, username, password, and database name. PyMySQL is an extra Python package, so it must be installed before the import works.

The SQL ideas are similar, but details such as data types, automatic IDs, connection setup, and parameter placeholders can differ between database systems. In `dbapp_mysqlapp.py`, the code connects to a MySQL server at `localhost`; that example only runs if the server, database, credentials, and PyMySQL package are set up correctly.

## 12. Understanding this module's examples

- `dbapp.py` and `dbapp_sqlite.py` connect to SQLite, create a table, insert rows, and read rows. The commented sections show update and delete queries.
- `dbapp_sqlite.py` opens `my_database.db`, which is a database file in this module folder.
- `dbapp_mysqlapp.py` shows a MySQL connection using PyMySQL. It assumes a local MySQL server and a database named `python` already exist.

Repeated runs may encounter “table already exists” or add duplicate rows because the sample statements create and insert data each time. For learning, inspect the database state and understand each statement before rerunning it. `CREATE TABLE IF NOT EXISTS` helps with the table-creation case; unique keys or deliberate cleanup help avoid duplicate sample data.

## 13. A good database workflow

1. Connect to the database.
2. Create a cursor if needed.
3. Execute SQL using placeholders for values.
4. Fetch results for `SELECT` queries.
5. Commit changes that should be saved.
6. Close the connection.

## Practice ideas

1. Create a `books` table with `id`, `title`, and `author` columns.
2. Insert two books using placeholders.
3. Select and print all books.
4. Select only books by one author using `WHERE`.
5. Update one book by its ID, then commit.
6. Delete one book by its ID, then confirm the remaining rows.

