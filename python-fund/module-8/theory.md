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

This creates a `students` table. `INTEGER` stores whole numbers; `TEXT` stores text. In SQLite, `INTEGER PRIMARY KEY` automatically assigns an ID when one is not supplied. `AUTOINCREMENT` adds the stronger rule that previously used IDs are not reused; it is optional for most beginner tables.

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

---

# Database Fundamentals for Complete Beginners

The rest of these notes builds the ideas behind databases in more detail. Every database command below is sent from Python using `sqlite3`, so students can see how Python and SQL work together.

## 14. What problem does a database solve?

Imagine a school program that stores student names in a Python list:

```python
students = ["Asha", "Ravi"]
```

This works while the program is running, but the list is normally lost when Python stops. We could write information to a text file, but then we would need to invent how to search, update, avoid duplicates, and connect related records. A database provides a reliable structure and a language for those jobs.

Think of a database as a well-organized digital filing cabinet. It contains **tables**. A table is similar to a spreadsheet: columns describe what facts are stored, and rows hold facts about individual things. Unlike a simple spreadsheet, a relational database can enforce rules and connect tables using keys.

## 15. Plan a small database before writing code

Suppose a school needs to record students and the courses they take. Start by identifying the kinds of things to store:

- Student information belongs in a `students` table.
- Course information belongs in a `courses` table.
- The fact that a particular student takes a particular course belongs in an enrollment table.

This separation prevents us from repeatedly typing a student's details every time we record a course. It also makes updates safer: a student's name is stored in one place.

## 16. Keys: how tables identify and connect rows

### Primary key

A **primary key** is the chosen column (or set of columns) that uniquely identifies each row in a table. A primary key cannot be missing and cannot repeat. It is like a unique library card number: two people may share a name, but they should not share the same student ID.

```sql
id INTEGER PRIMARY KEY
```

In SQLite, an `INTEGER PRIMARY KEY` is assigned an integer ID when the inserted row does not supply one. `AUTOINCREMENT` can request that SQLite never reuse previously used row IDs, but most simple SQLite tables only need `INTEGER PRIMARY KEY`.

### Foreign key

A **foreign key** is a column in one table whose value refers to a primary key in another table. It creates a valid link between rows. For example, `enrollments.student_id` refers to `students.id`. A foreign key helps prevent an enrollment for a student who does not exist.

```sql
student_id INTEGER NOT NULL,
FOREIGN KEY (student_id) REFERENCES students(id)
```

The foreign key is stored in the table that needs to refer to the other table. The student's primary key is not copied as a new identity; its value is referenced.

### Other useful constraints

Constraints are rules the database enforces when data is stored:

- `NOT NULL`: a value is required.
- `UNIQUE`: no two rows may have the same value in this column (for example, an email address).
- `CHECK`: a value must pass a condition (for example, age must be at least zero).
- `DEFAULT`: use a value when none is provided.
- `PRIMARY KEY`: uniquely identifies a row.
- `FOREIGN KEY`: requires a reference to a valid row in another table.

The Python program can validate input too, but database constraints are an important second layer of protection. They still apply if another program writes to the same database.

## 17. Relationships between tables

Tables can be related in three common ways:

1. **One-to-one:** one row in table A relates to at most one row in table B. Example: one person and one passport record.
2. **One-to-many:** one row in table A can relate to many rows in table B, but each B row belongs to one A row. Example: one customer can have many orders. Put the customer's foreign key in the `orders` table.
3. **Many-to-many:** many rows in table A can relate to many rows in table B. Example: each student can take many courses, and each course can have many students.

A relational database does not normally store a list of course IDs in one student cell. To represent a many-to-many relationship, create a third table called a **junction table**, **link table**, or **join table**.

## 18. What is a join table?

In the school example, the `enrollments` table connects students and courses:

```text
students                 courses                 enrollments
+----+------+             +----+---------+         +------------+-----------+
| id | name |             | id | title   |         | student_id | course_id|
+----+------+             +----+---------+         +------------+-----------+
| 1  | Asha |             | 10 | Python  |         | 1          | 10       |
| 2  | Ravi |             | 11 | Databases|        | 1          | 11       |
+----+------+             +----+---------+         | 2          | 10       |
                                                   +------------+-----------+
```

Each enrollment row means “this student takes this course.” The pair `(student_id, course_id)` should usually be unique, because the same student should not be enrolled in the same course twice. The pair can itself be the table's **composite primary key** (a key made from more than one column).

The join table can also store facts about the relationship, such as `enrolled_on`, `grade`, or `status`. Those facts belong to the enrollment, not solely to the student or course.

## 19. Create and fill related tables using Python

This complete example uses an in-memory SQLite database. `:memory:` means the database exists only while this program runs, so it will not change the module's existing database file. SQLite foreign-key enforcement is switched on explicitly for this connection.

```python
import sqlite3

connection = sqlite3.connect(":memory:")
connection.execute("PRAGMA foreign_keys = ON")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE
    )
""")

cursor.execute("""
    CREATE TABLE courses (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL UNIQUE
    )
""")

cursor.execute("""
    CREATE TABLE enrollments (
        student_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        grade INTEGER CHECK (grade BETWEEN 0 AND 100),
        PRIMARY KEY (student_id, course_id),
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(id)
    )
""")

cursor.execute(
    "INSERT INTO students (name, email) VALUES (?, ?)",
    ("Asha", "asha@example.com")
)
cursor.execute(
    "INSERT INTO students (name, email) VALUES (?, ?)",
    ("Ravi", "ravi@example.com")
)
cursor.execute("INSERT INTO courses (title) VALUES (?)", ("Python",))
cursor.execute("INSERT INTO courses (title) VALUES (?)", ("Databases",))

# Look up IDs by their meaningful values so this example does not assume ID numbers.
asha_id = cursor.execute(
    "SELECT id FROM students WHERE name = ?", ("Asha",)
).fetchone()[0]
python_id = cursor.execute(
    "SELECT id FROM courses WHERE title = ?", ("Python",)
).fetchone()[0]

cursor.execute(
    "INSERT INTO enrollments (student_id, course_id, grade) VALUES (?, ?, ?)",
    (asha_id, python_id, 95)
)
connection.commit()
```

Notice `( "Python", )` is a one-value tuple: a one-value tuple needs a comma in Python. Without the comma, parentheses only group the value and do not make a tuple.

## 20. What does JOIN mean?

The `JOIN` keyword asks the database to combine rows from related tables. The connection is usually stated with `ON`, which explains which key columns must match. Here Python runs a query that returns each student's name, course title, and grade:

```python
cursor.execute("""
    SELECT students.name, courses.title, enrollments.grade
    FROM enrollments
    JOIN students ON enrollments.student_id = students.id
    JOIN courses ON enrollments.course_id = courses.id
""")

for name, course_title, grade in cursor.fetchall():
    print(name, course_title, grade)
```

Read this query in plain language: start with enrollment records, find the student whose ID matches each enrollment's `student_id`, then find the course whose ID matches its `course_id`, and show the requested columns.

### Common join types

- `INNER JOIN` (written `JOIN` in SQLite): return rows with matching records on both sides. An enrollment appears only if its student and course match.
- `LEFT JOIN`: keep every row from the left table, even if there is no match on the right. The right-side columns are `None`/`NULL` when there is no match.
- `RIGHT JOIN` and `FULL OUTER JOIN`: available in some database systems and SQLite versions; beginner examples can start with `JOIN` and `LEFT JOIN`.

Example: list all students, including students who have not enrolled in a course:

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

`None` in a returned Python row corresponds to SQL `NULL`, meaning no value/matching course was found. A join combines information for a result; it does not permanently merge or change the tables.

## 21. SQL command families: DDL, DML, DQL, and TCL

SQL commands are often taught in groups based on their job. These names describe the kind of SQL instruction. Python still sends each command as a string using `execute()`.

### DDL — Data Definition Language

DDL defines or changes the **structure** of a database: tables, columns, and other objects.

Common commands:

- `CREATE`: make a table or other database object.
- `ALTER`: change the structure of an existing object.
- `DROP`: remove a database object, such as a table.

Python example:

```python
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clubs (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
""")
```

### DML — Data Manipulation Language

DML changes the **rows/data inside tables**.

- `INSERT`: add rows.
- `UPDATE`: change existing rows.
- `DELETE`: remove rows.

```python
cursor.execute("INSERT INTO clubs (name) VALUES (?)", ("Chess",))
cursor.execute("UPDATE clubs SET name = ? WHERE id = ?", ("Chess Club", 1))
cursor.execute("DELETE FROM clubs WHERE id = ?", (1,))
connection.commit()
```

Always think about the `WHERE` clause before `UPDATE` and `DELETE`. Without `WHERE`, every row may be changed or removed.

### DQL — Data Query Language

DQL retrieves/asks questions about data. The main command is `SELECT`.

```python
cursor.execute("SELECT id, name FROM students WHERE name = ?", ("Asha",))
rows = cursor.fetchall()
```

`SELECT` does not ordinarily change table data. It returns results for Python to inspect.

### TCL — Transaction Control Language

TCL controls a **transaction**, which is a group of database changes treated as one unit.

- `COMMIT`: make the transaction's changes permanent.
- `ROLLBACK`: undo the transaction's uncommitted changes.
- `SAVEPOINT`: mark a point inside a transaction to which you may roll back.

In Python's `sqlite3`, you will commonly call methods instead of writing these words as query strings:

```python
try:
    cursor.execute("INSERT INTO clubs (name) VALUES (?)", ("Music",))
    connection.commit()  # save the transaction
except sqlite3.Error:
    connection.rollback()  # undo uncommitted changes if there was an error
    raise
```

Some textbooks also teach **DCL** (Data Control Language), such as `GRANT` and `REVOKE`, for permissions. Permission commands vary by database; SQLite does not use the same database-user permission system as a server such as MySQL.

### Simple difference to remember

| Family | Main question | Example command |
|---|---|---|
| DDL | What should the database structure look like? | `CREATE TABLE` |
| DML | How should stored rows change? | `INSERT`, `UPDATE`, `DELETE` |
| DQL | What stored information do I want to see? | `SELECT` |
| TCL | Should this group of changes be saved or undone? | `commit()`, `rollback()` |

## 22. SQL rules students should remember

1. **A table should represent one kind of thing.** Keep student details in `students`, course details in `courses`, and enrollment facts in `enrollments`.
2. **Give each table a primary key.** Use it to identify a row reliably; names may repeat or change.
3. **Use foreign keys for references.** Do not rely on matching names to connect records; names can be misspelled or duplicated.
4. **Use the correct data type.** Store counts as numbers and names as text. SQLite is flexible with types, but choosing sensible types still helps.
5. **Add constraints for important rules.** For example, a required name can use `NOT NULL`, and a unique email can use `UNIQUE`.
6. **Use placeholders for values.** In SQLite use `?`; never paste user input into the SQL string.
7. **Use `WHERE` to target changes.** Check the condition carefully before updating or deleting.
8. **Commit changes you want to keep.** Use rollback when a transaction fails and its changes should be undone.
9. **Fetch results after `SELECT`.** `execute()` runs the query; `fetchone()`/`fetchall()` obtains its rows.
10. **Close the connection when finished.** This releases resources. Python's `with` and `try/finally` help manage cleanup.
11. **Do not store a comma-separated list in one cell when each item needs its own relationship.** Use another table and a join table when appropriate.
12. **Avoid duplicate facts.** If the same fact is copied to many rows, changing it everywhere becomes difficult. Separate tables and keys help reduce that problem.

## 23. Database NULL is not the same as zero or empty text

SQL `NULL` means a value is missing or unknown. It is different from `0`, `""` (an empty string), and Python `None`. To check for missing values in SQL, use `IS NULL`, not `= NULL`:

```python
cursor.execute("SELECT name FROM students WHERE email IS NULL")
print(cursor.fetchall())
```

When SQLite returns a `NULL` value to Python, it becomes `None`.

## 24. A compact Python database pattern

This shows the overall shape of a small SQLite program. It assumes the `students` table already exists:

```python
import sqlite3

with sqlite3.connect("school.db") as connection:
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO students (name, city) VALUES (?, ?)",
        ("Mina", "Surat")
    )

    cursor.execute("SELECT id, name, city FROM students WHERE city = ?", ("Surat",))
    for student_id, name, city in cursor.fetchall():
        print(student_id, name, city)
```

For SQLite, leaving the `with` block commits on success and rolls back an active transaction if an exception occurs. The connection is then closed. `with` does not suppress the error; an exception still propagates unless you catch it.

## 25. Common beginner mistakes

- **Using `execute()` but forgetting `commit()`:** changes may not be saved.
- **Using `"w"`-style thinking for a database:** inserting the same sample rows again adds more rows unless a rule prevents duplicates.
- **Using a table name or column name that does not exist:** the database reports an SQL error; check spelling and table creation order.
- **Putting values directly into SQL with f-strings:** this can break on quotes and is unsafe. Use placeholders.
- **Forgetting `WHERE`:** an update/delete can affect all rows.
- **Expecting `execute(SELECT...)` to print results:** fetch the rows and print them in Python.
- **Trying to join tables on a person's name:** use primary/foreign keys instead.
- **Expecting foreign keys to be enforced automatically in every SQLite connection:** enable them with `PRAGMA foreign_keys = ON` for each connection.
- **Confusing a join table with the `JOIN` query:** the join table is a stored table connecting many-to-many rows; `JOIN` is a query operation that combines related rows in the result.

## 26. Mini glossary

- **Database:** organized persistent storage for information.
- **Relational database:** a database that stores related data in tables.
- **SQL:** language used to define, change, and query database data.
- **Primary key:** unique identity of a row.
- **Foreign key:** reference from a row to a key in another table.
- **Constraint:** a rule that data must obey.
- **Join table:** table that records links between two tables, especially for a many-to-many relationship.
- **JOIN query:** SQL operation that combines matching rows from tables.
- **Transaction:** a group of database changes saved or undone together.
- **Commit:** save pending transaction changes.
- **Rollback:** undo pending transaction changes.
- **Cursor:** Python object used to execute SQL and fetch query results.
- **Placeholder:** marker (`?` in SQLite) where a value is safely supplied separately.

