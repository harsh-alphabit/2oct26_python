# Module 8: Databases with Python

These notes start with the basic idea of a database and gradually build up to using related tables from Python. The examples use Python's built-in `sqlite3` module, so no separate database server is needed.

## Learning path

1. Understand why programs use databases.
2. Learn tables, rows, columns, and SQL.
3. Connect Python to SQLite and perform basic operations.
4. Learn keys, rules, and relationships between tables.
5. Use a join table and `JOIN` queries.
6. Recognize DDL, DML, DQL, and TCL commands.

## 1. What is a database?

A **database** is an organized place to store information so it remains available after a program ends. A school may store students and courses; a shop may store products and orders.

For example, a Python list can hold student names while a program runs:

```python
students = ["Asha", "Ravi"]
```

When the program stops, this list normally disappears. A database saves information on disk and provides ways to find, add, change, and remove it. A database also lets us connect related information and enforce rules about what may be stored.

## 2. Tables, rows, and columns

A **relational database** organizes information in tables. A table is a little like a spreadsheet:

- A **table** holds information about one kind of thing.
- A **column** describes one fact about that thing, such as a name or city.
- A **row** (also called a record) stores the facts for one item or person.
- A **cell** is one value at the intersection of a row and column.

Example `students` table:

| id | name | city |
|---:|---|---|
| 1 | Asha | Pune |
| 2 | Ravi | Surat |

Here `students` is the table; `id`, `name`, and `city` are columns; each student is a row.

## 3. SQL: the database language

**SQL** means Structured Query Language. SQL is the language we use to describe database work. Python runs the program and sends SQL instructions to the database. The database performs the instruction and sends results back to Python.

Think of the roles this way:

```text
Python program  -- sends SQL -->  Database
Python program  <-- returns rows -- Database
```

The SQL examples below appear inside Python strings because Python is sending them to SQLite. SQL keywords such as `SELECT` and `CREATE TABLE` are conventionally written in uppercase for readability, but SQL generally accepts lowercase too.

## 4. SQLite and Python connection basics

SQLite is a database system that stores its data in a local file. Python includes the `sqlite3` module, so it is a convenient first database to learn.

```python
import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()
```

- A **connection** represents Python's open link to a database.
- A **cursor** sends SQL commands and helps retrieve query results.
- `school.db` is the database file. If it does not exist, SQLite creates it. A relative file path is based on the program's current working directory.

The existing module examples use names such as `db` for a connection and `cr` for a cursor. These are just variable names; their jobs are the same.

## 5. Create a table and understand data types

Before adding rows, create a table and decide what columns it needs. A simple SQLite table might be:

```python
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        city TEXT
    )
""")
```

`CREATE TABLE` defines the structure. `IF NOT EXISTS` means “create it if it is not already there.” Common SQLite type names include:

- `INTEGER`: whole numbers, such as an ID or count.
- `REAL`: numbers that may have a decimal part.
- `TEXT`: words or other text.
- `BLOB`: binary data such as raw file contents.
- `NULL`: a missing or unknown value (not the same as zero or empty text).

SQLite is flexible about types, but choose a type that makes sense for each column. A database's schema is its structure: its tables, columns, and rules.

## 6. Add, read, update, and delete rows

These four operations are often shortened to **CRUD**: Create (rows), Read, Update, Delete. “Create” in CRUD means adding a data row with `INSERT`; this is different from the DDL command `CREATE TABLE`, which creates the table structure.

### Add a row: `INSERT`

```python
cursor.execute(
    "INSERT INTO students (name, city) VALUES (?, ?)",
    ("Asha", "Pune")
)
connection.commit()
```

The column list says where each value goes. The `?` symbols are placeholders for values supplied separately. The final values are a Python tuple. When a tuple has one item, write a trailing comma, as in `("Asha",)`.

### Read rows: `SELECT`

```python
cursor.execute("SELECT id, name, city FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)
```

`SELECT` reads data. `*` means all columns, though listing the columns you need is often clearer:

```python
cursor.execute("SELECT name, city FROM students")
```

To filter rows, use `WHERE`:

```python
cursor.execute("SELECT id, name FROM students WHERE city = ?", ("Pune",))
print(cursor.fetchall())
```

`fetchone()` reads one result row, `fetchmany(n)` reads up to `n` rows, and `fetchall()` reads all remaining result rows. SQLite rows commonly arrive as tuples. Python's `None` represents SQL `NULL`.

### Change a row: `UPDATE`

```python
cursor.execute(
    "UPDATE students SET city = ? WHERE id = ?",
    ("Surat", 1)
)
connection.commit()
```

`SET` names the value to change, and `WHERE` selects which row. Without `WHERE`, every row in the table may be updated.

### Remove a row: `DELETE`

```python
cursor.execute("DELETE FROM students WHERE id = ?", (1,))
connection.commit()
```

This removes the row with ID 1. Without `WHERE`, all rows may be deleted. The table itself remains.

## 7. Placeholders: pass values safely

Always use placeholders when values come from a variable, user input, or another source. For SQLite, the placeholder is `?`:

```python
name = input("Student name: ")
city = input("City: ")

cursor.execute(
    "INSERT INTO students (name, city) VALUES (?, ?)",
    (name, city)
)
connection.commit()
```

Do not build the SQL by inserting user input into an f-string. That can break when text contains quotes and may allow **SQL injection**, where input is treated as part of a command. Placeholders tell the database that the supplied values are data. PyMySQL commonly uses `%s` placeholders instead; use the placeholder style required by the database library.

## 8. Save and undo changes: transactions

A **transaction** is a group of database changes treated as one unit. `commit()` saves pending changes. `rollback()` cancels pending changes that have not been committed.

```python
try:
    cursor.execute("INSERT INTO students (name, city) VALUES (?, ?)", ("Mina", "Rajkot"))
    connection.commit()
except sqlite3.Error:
    connection.rollback()
    raise
```

For example, transferring money between two accounts involves taking money from one and adding it to another. Both changes should succeed together, or neither should be kept. Transactions help maintain this kind of consistency.

## 9. Keys: identify rows and connect tables

### Primary key

A **primary key** uniquely identifies each row in a table. It must not be missing or duplicated. A person's name is a poor key because two people may share a name or a person may change their name. An ID is a better key.

```sql
id INTEGER PRIMARY KEY
```

In SQLite, an `INTEGER PRIMARY KEY` is assigned an ID when one is not supplied. `AUTOINCREMENT` adds a stronger rule that an old ID will not be reused, but it is usually unnecessary in beginner examples.

### Foreign key

A **foreign key** stores a reference to a row in another table. If an order belongs to a customer, the `orders` table can have a `customer_id` column that refers to `customers.id`.

```sql
customer_id INTEGER NOT NULL,
FOREIGN KEY (customer_id) REFERENCES customers(id)
```

This gives the database a way to check that the referenced customer exists. SQLite foreign key checking should be enabled for each connection with:

```python
connection.execute("PRAGMA foreign_keys = ON")
```

### Other database rules (constraints)

Constraints are rules the database checks when data is inserted or changed:

- `NOT NULL`: this column must have a value.
- `UNIQUE`: values in this column must not repeat, such as an email address.
- `CHECK`: a value must pass a condition, such as `grade BETWEEN 0 AND 100`.
- `DEFAULT`: use a value when no value is supplied.
- `PRIMARY KEY`: this row's unique identity.
- `FOREIGN KEY`: this reference must point to a valid row.

Python can also validate input, but database constraints protect the data even if it is changed by a different program.

## 10. Relationships: one-to-one, one-to-many, many-to-many

- **One-to-one:** one row in the first table is associated with at most one row in the second. Example: a person and a passport record.
- **One-to-many:** one row in the first table may be associated with many rows in the second. Example: one customer can have many orders. Put the customer's foreign key in `orders`.
- **Many-to-many:** many rows in the first table can relate to many rows in the second. Example: one student takes many courses, and one course has many students.

The many-to-many relationship needs a third table to record each pairing.

## 11. What is a join table?

A **join table** (also called a junction table or link table) stores links between rows in two other tables. It is a real table that holds data. This is different from a `JOIN` query, which is an instruction for combining related rows in a result.

For students and courses, we can use:

```text
students                courses                  enrollments
+----+------+            +----+----------+         +------------+-----------+
| id | name |            | id | title    |         | student_id | course_id |
+----+------+            +----+----------+         +------------+-----------+
| 1  | Asha |            | 10 | Python   |         | 1          | 10        |
| 2  | Ravi |            | 11 | Databases|         | 1          | 11        |
+----+------+            +----+----------+         | 2          | 10        |
                                                   +------------+-----------+
```

Each row in `enrollments` means “this student takes this course.” The pair `(student_id, course_id)` should usually be unique, so the same student cannot be enrolled in the same course twice. This pair can be a **composite primary key**: a primary key made from more than one column. Details such as grade or enrollment date belong in this join table because they describe the student's enrollment in that course.

## 12. Build the example database in Python

This complete example creates three related tables, adds sample data, and saves it in `school.db`. Run it as one program. The `IF NOT EXISTS` clauses make table creation safe to repeat; the sample inserts will still add duplicate names if the program is run repeatedly.

```python
import sqlite3

connection = sqlite3.connect("school.db")
connection.execute("PRAGMA foreign_keys = ON")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL UNIQUE
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS enrollments (
        student_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        grade INTEGER CHECK (grade BETWEEN 0 AND 100),
        PRIMARY KEY (student_id, course_id),
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(id)
    )
""")

cursor.execute(
    "INSERT OR IGNORE INTO students (name, email) VALUES (?, ?)",
    ("Asha", "asha@example.com")
)
cursor.execute(
    "INSERT OR IGNORE INTO students (name, email) VALUES (?, ?)",
    ("Ravi", "ravi@example.com")
)
cursor.execute("INSERT OR IGNORE INTO courses (title) VALUES (?)", ("Python",))
cursor.execute("INSERT OR IGNORE INTO courses (title) VALUES (?)", ("Databases",))

asha_id = cursor.execute(
    "SELECT id FROM students WHERE email = ?", ("asha@example.com",)
).fetchone()[0]
python_id = cursor.execute(
    "SELECT id FROM courses WHERE title = ?", ("Python",)
).fetchone()[0]

cursor.execute(
    "INSERT OR IGNORE INTO enrollments (student_id, course_id, grade) VALUES (?, ?, ?)",
    (asha_id, python_id, 95)
)
connection.commit()
connection.close()
```

Important details:

- Tables that are referenced by foreign keys (`students`, `courses`) are created before `enrollments`.
- The database gives IDs to students and courses. The program looks them up instead of assuming what numbers SQLite assigned.
- `INSERT OR IGNORE` skips a row if it violates a uniqueness rule. It is a simple way to make this sample rerunnable; in real programs, handle duplicates deliberately.
- `connection.close()` closes the database connection.

## 13. What does a JOIN query do?

A `JOIN` query combines related rows from tables for a result. It does not permanently merge or change the tables. The `ON` part tells the database which key values must match.

```python
import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("""
    SELECT students.name, courses.title, enrollments.grade
    FROM enrollments
    JOIN students ON enrollments.student_id = students.id
    JOIN courses ON enrollments.course_id = courses.id
""")

for name, course, grade in cursor.fetchall():
    print(name, course, grade)

connection.close()
```

In plain language: start with each enrollment, find the matching student using `student_id`, find the matching course using `course_id`, then show the student's name, course title, and grade.

### Common join types

- `INNER JOIN` (or simply `JOIN`): return rows where a match exists in both tables.
- `LEFT JOIN`: keep every row from the table on the left, even when there is no matching row on the right. Missing right-side values appear as SQL `NULL` and Python `None`.

To list all students, including those with no course enrollment, use left joins:

```python
cursor.execute("""
    SELECT students.name, courses.title
    FROM students
    LEFT JOIN enrollments ON enrollments.student_id = students.id
    LEFT JOIN courses ON enrollments.course_id = courses.id
""")
for row in cursor.fetchall():
    print(row)
```

## 14. SQL command families: DDL, DML, DQL, and TCL

These names group SQL commands by their purpose. Python sends the SQL text using `cursor.execute()`. In Python's SQLite API, transaction actions are often performed with `connection.commit()` and `connection.rollback()`.

### DDL — Data Definition Language

DDL defines or changes the database **structure**, such as tables and columns.

- `CREATE`: make a table.
- `ALTER`: change a table's structure.
- `DROP`: remove a table or other object.

```python
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clubs (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
""")
```

### DML — Data Manipulation Language

DML adds, changes, or removes **rows** in a table.

- `INSERT`: add rows.
- `UPDATE`: change rows.
- `DELETE`: remove rows.

```python
cursor.execute("INSERT INTO clubs (name) VALUES (?)", ("Chess",))
cursor.execute("UPDATE clubs SET name = ? WHERE id = ?", ("Chess Club", 1))
cursor.execute("DELETE FROM clubs WHERE id = ?", (1,))
connection.commit()
```

Always check the `WHERE` condition on `UPDATE` and `DELETE`. Without it, all rows can be changed or removed.

### DQL — Data Query Language

DQL asks for/read data. `SELECT` is the main DQL command.

```python
cursor.execute("SELECT id, name FROM students WHERE name = ?", ("Asha",))
rows = cursor.fetchall()
```

`SELECT` returns results; it does not ordinarily change table data.

### TCL — Transaction Control Language

TCL controls whether a group of changes is saved or undone.

- `COMMIT`: save the transaction.
- `ROLLBACK`: undo uncommitted changes.
- `SAVEPOINT`: mark a point to which part of a transaction can be undone.

In Python with SQLite:

```python
connection.commit()    # save pending changes
connection.rollback()  # undo pending changes
```

Some database textbooks also include **DCL** (Data Control Language), such as `GRANT` and `REVOKE`, for database permissions. Permission features vary by database system; SQLite does not manage users and permissions like a server database such as MySQL.

| Family | What it is for | Example |
|---|---|---|
| DDL | Define database structure | `CREATE TABLE` |
| DML | Change table rows | `INSERT`, `UPDATE`, `DELETE` |
| DQL | Read/query table rows | `SELECT` |
| TCL | Save or undo a group of changes | `commit()`, `rollback()` |

## 15. Important database rules

1. Use one table for one kind of thing: students, courses, orders, and products are different kinds of things.
2. Give each table a primary key so every row has a dependable identity.
3. Use foreign keys to connect rows; do not connect records by names that can repeat or change.
4. Store one value per cell. For example, do not store `"Python, Math, Art"` in one course column if the courses must be searched and related individually.
5. Choose suitable data types and add constraints for essential rules.
6. Use placeholders (`?` in SQLite) for values, especially user input.
7. Include a carefully chosen `WHERE` clause when changing or deleting particular rows.
8. Commit changes that should be saved. Roll back a transaction when failed changes should be undone.
9. Fetch query results after `SELECT`; `execute()` runs the query but does not print the rows.
10. Close the connection when finished. `with` statements or `try/finally` can help manage cleanup.
11. Use a join table for a many-to-many relationship.
12. Avoid storing the same fact in many places. If a student's name changes, it is easier to update it once in `students` than in every enrollment.

## 16. NULL, zero, empty text, and Python None

SQL `NULL` means a value is missing or unknown. It is not the number `0` and not the empty string `""`. Python's `sqlite3` converts SQL `NULL` to Python `None` when returning data.

Check for missing database values with `IS NULL`, not `= NULL`:

```python
cursor.execute("SELECT name FROM students WHERE email IS NULL")
print(cursor.fetchall())
```

## 17. SQLite compared with MySQL

SQLite stores a database in a local file and is included with Python. MySQL is a database server that must be installed and running; a program connects using a host, username, password, and database name. The module's `dbapp_mysqlapp.py` uses the extra PyMySQL package and assumes a local MySQL server plus a database named `python` already exist.

The core SQL ideas are similar, but connection setup, data types, automatic ID syntax, and placeholder styles can differ. SQLite uses `?` placeholders; PyMySQL commonly uses `%s`. Use the syntax and parameter style for the database library in use.

## 18. Understanding the existing Module 8 files

- `dbapp.py` and `dbapp_sqlite.py` connect to SQLite, create a table, insert rows, and read rows. Commented sections demonstrate update and delete queries.
- `dbapp_sqlite.py` connects to `my_database.db` in the module folder.
- `dbapp_mysqlapp.py` shows a MySQL connection through PyMySQL. It needs the MySQL server, credentials, database, and package to be configured.

Running the original examples repeatedly can add duplicate rows or produce a “table already exists” message because they repeat table creation and inserts. `CREATE TABLE IF NOT EXISTS` prevents the table-creation error; a `UNIQUE` rule or deliberate duplicate handling can prevent repeated sample records.

## 19. Common beginner mistakes

- Forgetting `commit()` after inserts, updates, or deletes.
- Expecting `execute()` to display query results instead of calling `fetchone()` or `fetchall()`.
- Forgetting `WHERE` and accidentally changing or deleting every row.
- Putting values into SQL with f-strings instead of placeholders.
- Joining tables using names instead of primary and foreign keys.
- Confusing a **join table** (a stored table linking rows) with a **JOIN query** (a command that combines related rows in a result).
- Expecting SQLite foreign keys to be enforced without enabling `PRAGMA foreign_keys = ON` for the connection.
- Assuming sample insert statements will not add duplicates when run a second time.

## 20. A good workflow

1. Connect to the database.
2. Enable SQLite foreign keys if the schema uses them.
3. Create the tables in an order that respects their references.
4. Execute SQL with placeholders for values.
5. Fetch rows when using `SELECT`.
6. Commit successful changes or roll back failed transactions.
7. Close the connection.

## Practice

1. Create a `books` table with an ID, title, and author.
2. Insert two books with placeholders and print them using `SELECT`.
3. Add a `readers` table and a `loans` join table. What are their primary and foreign keys?
4. Write a `JOIN` query that displays each reader and the title of each borrowed book.
5. Classify `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`, and `commit()` as DDL, DML, DQL, or TCL.
6. Add a `CHECK` constraint so a book's rating must be from 1 through 5.

## Quick glossary

- **Database:** organized, persistent storage for information.
- **SQL:** language used to define, change, and query relational databases.
- **Schema:** the database's tables, columns, and rules.
- **Primary key:** unique identity of a table row.
- **Foreign key:** a reference to a key in another table.
- **Constraint:** a rule the database enforces on stored values.
- **Join table:** a table that records links in a many-to-many relationship.
- **JOIN query:** an instruction to combine related rows in query results.
- **Transaction:** a group of changes that can be saved or undone together.
- **Cursor:** Python object used to send SQL and fetch query results.
- **Placeholder:** marker (`?` in SQLite) for a value supplied separately.
