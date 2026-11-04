# Module 9: Working with Files and Folders

These notes explain how Python can save information in files, read it later, and create or remove folders. A **file** keeps information on a computer after a program finishes. A **folder** (also called a directory) organizes files and other folders.

## 1. File paths

A **path** tells the computer where a file or folder is. A relative path such as `"notes.txt"` is interpreted from the program's **current working directory**. That directory may not be the same folder as the Python script, depending on how the script was started.

```python
file = open("notes.txt", "r")
```

If you need a file in a particular place, use a clear path. Python's `pathlib` module offers a convenient way to work with paths across operating systems:

```python
from pathlib import Path

path = Path("data") / "notes.txt"
```

## 2. Opening a file

The built-in `open()` function opens a file and returns a **file object**. You use that object to read or write the file.

```python
file = open("notes.txt", "r")
```

The second argument is the **mode**: it says what you intend to do with the file.

| Mode | Meaning |
|---|---|
| `"r"` | Read an existing file. It raises an error if the file does not exist. |
| `"w"` | Write from the beginning. Creates the file, or replaces its old contents. |
| `"a"` | Append at the end. Creates the file if it does not exist. |
| `"x"` | Create a new file; raises an error if it already exists. |

Be careful with `"w"`: opening a file in this mode can erase its previous contents immediately.

## 3. Writing text to a file

The file object's `write()` method writes text. It does **not** automatically add a new line, so include `\n` where you want lines to end.

```python
file = open("student.txt", "w")
file.write("Name: Asha\nCity: Pune\n")
file.close()
```

`close()` tells Python you are finished and flushes pending data. Closing files matters because it releases system resources and helps ensure written data is saved.

## 4. Prefer `with open(...)`

If an error happens before `close()`, the file may be left open. The `with` statement closes it automatically when the indented block ends, including when an error occurs. This is the recommended pattern:

```python
with open("student.txt", "w", encoding="utf-8") as file:
    file.write("Name: Asha\n")
```

`encoding="utf-8"` supports a wide range of characters. Use it explicitly when reading or writing text files so the character encoding is clear.

## 5. Appending instead of replacing

Use append mode `"a"` when new information should be added after the existing contents:

```python
with open("visitors.txt", "a", encoding="utf-8") as file:
    file.write("Asha visited\n")
```

If you run this several times, the line is added several times. Append mode keeps the old contents; write mode replaces them.

## 6. Reading a file

Open a file in read mode. Several methods are available:

```python
with open("student.txt", "r", encoding="utf-8") as file:
    text = file.read()
    print(text)
```

- `read()` returns the remaining contents as one string.
- `readline()` reads the next line as a string.
- `readlines()` reads the remaining lines into a list of strings.
- `for line in file:` reads one line at a time and is often a good choice for a file of any size.

After reading, a line may still contain its ending newline. Use `line.strip()` if you want to remove whitespace from both ends for display or comparison:

```python
with open("student.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

## 7. Creating a file

Opening a file with `"w"` or `"a"` creates it if it does not exist. Use `"x"` when you specifically want to create a brand-new file and avoid replacing an existing one.

```python
with open("new_file.txt", "x", encoding="utf-8") as file:
    file.write("Created once.\n")
```

The `file_create.py` example uses `"x"`; if you run it again after the file was created, Python raises `FileExistsError`. That is the mode working as designed.

## 8. Deleting a file

Python's `os` module can remove a file:

```python
import os

os.remove("old.txt")
```

The file must exist, and the program needs permission to remove it. If it does not exist, Python raises `FileNotFoundError`. Deleting a file removes it from the filesystem; check the path carefully before doing so.

With `pathlib`, a file can be removed using `Path.unlink()`. Either approach should handle the case where the file is missing if that is expected.

## 9. Creating folders

Use `os.mkdir()` to create one folder:

```python
import os

os.mkdir("reports")
```

It raises an error if the folder already exists. `os.chdir()` changes the program's current working directory:

```python
os.chdir("reports")
```

Changing the working directory affects how later relative paths are interpreted. This can make programs confusing, so prefer building an explicit path when possible.

`pathlib` can create folders too:

```python
from pathlib import Path

Path("reports/monthly").mkdir(parents=True, exist_ok=True)
```

`parents=True` creates missing parent folders. `exist_ok=True` avoids an error if the folder already exists.

## 10. Errors to expect

File and folder operations can raise exceptions. Common examples include:

- `FileNotFoundError`: the file or folder path does not exist.
- `FileExistsError`: a file or folder already exists where a new one was requested.
- `PermissionError`: the program is not allowed to perform the operation.
- `IsADirectoryError`: a file operation was attempted on a folder.

Handle an error when your program has a useful response. For example, tell the user a file could not be found instead of letting the program stop without explanation.

```python
try:
    with open("missing.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("The file does not exist yet.")
```

## 11. Understanding this module's examples

- `file_create.py` uses `"x"` to create a file and writes text. Running it repeatedly can fail once the file already exists.
- `file_write.py` uses `"w"`, which creates or replaces a file's contents.
- `file_write_input.py` collects values from the keyboard, opens a file in append mode, and writes those values as labelled lines. It then demonstrates write and append modes on other files.
- `file_append.py` writes a name in append mode. Each run adds another copy at the end.
- `file_read.py` shows `read()`, `readline()`, and `readlines()` as alternatives, then loops through the file line by line. The commented examples are turned off; uncomment one at a time to explore it.
- `file_delete.py` calls `os.remove("test.txt")`. It will fail if that file is not present in the current working directory.
- `folder_create.py` creates a folder in the current working directory.
- `subfolder_create.py` changes into `Newfolder` and creates a folder inside it. `Newfolder` must already exist, and the relative path depends on the program's current working directory.

For clearer and safer beginner programs, use `with open(...)` and explicit paths. Use a small practice folder so it is easy to see which files your examples create or change.

## 12. A simple save-and-read example

```python
student_name = input("Student name: ")
city = input("City: ")

with open("students.txt", "a", encoding="utf-8") as file:
    file.write(f"{student_name},{city}\n")

with open("students.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

This stores one comma-separated line, then reads and prints every line. For more complex data, a CSV file or database is usually a better fit than inventing your own text format.

## 13. A good file workflow

1. Decide whether you need to read, replace, append, or create only if absent.
2. Choose the correct mode (`r`, `w`, `a`, or `x`).
3. Open the file with `with` and an explicit text encoding.
4. Read or write using the file object.
5. Use a clear path and handle expected errors.

## Practice ideas

1. Write your name and favourite subject to a new file.
2. Read the file and print its contents.
3. Add a second line without removing the first.
4. Read the file line by line and number each line in the output.
5. Create a folder called `practice_files` and create a file inside it.
6. Try to open a missing file and handle `FileNotFoundError` with a helpful message.

