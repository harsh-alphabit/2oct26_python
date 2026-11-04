# Module 7: Regular Expressions (Regex) in Python

These notes assume you are new to programming and to regular expressions. Read each pattern from left to right: every symbol adds a small rule about the text Python should look for.

## 1. What is a regular expression?

A **regular expression**, usually shortened to **regex**, is a pattern for finding or checking text. You can use it to find numbers in a sentence, check whether a username follows rules, or locate a particular word.

For example, the pattern `cat` looks for the exact letters `cat`. The pattern `\\d` looks for a digit. A regex is a description of text, not the text itself.

Python provides regex tools in its built-in `re` module. Import it before using those tools:

```python
import re

message = "My order number is 4821"
result = re.findall(r"\\d", message)
print(result)  # ['4', '8', '2', '1']
```

The `r` before the string makes it a **raw string**. It helps Python pass backslashes to the regex engine as written. For regex patterns, `r"..."` is a good habit.

## 2. Literal characters and special characters

Most ordinary characters match themselves. The pattern `Python` matches the letters `Python` in that order. Regex treats uppercase and lowercase as different unless you request case-insensitive matching.

Some characters have a special meaning. For example, `.` means “any one character.” If you want to find an actual period, write `\\.` because the backslash removes the special meaning of the dot.

```python
re.findall(r"Py..on", "Python Pylon")  # ['Python', 'Pylon']
re.findall(r"\\.", "File: notes.txt")   # ['.']
```

## 3. Character shortcuts

These shortcuts describe a type of character:

| Pattern | Meaning | Example |
|---|---|---|
| `\\d` | One digit, usually 0 through 9 | `7` |
| `\\D` | One character that is not a digit | `a`, `!` |
| `\\w` | One word character: a letter, digit, or underscore | `A`, `4`, `_` |
| `\\W` | One character that is not a word character | space, `!` |
| `\\s` | One whitespace character, such as a space or newline | ` ` |
| `\\S` | One character that is not whitespace | `x`, `8` |
| `.` | Almost any one character except a newline by default | `x`, `5` |

Capitalizing one of these shortcuts often gives the opposite category: `\\d` means digit, while `\\D` means non-digit.

## 4. Character sets and ranges

Square brackets mean “match one character from this set.” For example, `[aeiou]` matches one lowercase vowel. `[0-9]` matches one digit. `[A-Z]` matches one uppercase English letter, and `[A-Za-z]` matches one English letter in either case.

```python
re.findall(r"[A-Z]", "Hello PYTHON")    # ['H', 'P', 'Y', 'T', 'H', 'O', 'N']
re.findall(r"[A-Za-z]", "Hi 42!")       # ['H', 'i']
re.findall(r"[A-Z]|[a-z]", "Hi!")       # ['H', 'i']
```

Inside brackets, a hyphen can describe a range, as in `[0-9]`. Outside brackets, `|` means “or.” Thus `[A-Z]|[a-z]` means an uppercase letter or a lowercase letter, one match at a time.

To match anything *except* a set, put `^` first inside the brackets: `[^0-9]` matches one character that is not a digit.

## 5. Repetition: how many characters?

Quantifiers tell regex how many times the preceding character or group may appear:

| Pattern | Meaning |
|---|---|
| `*` | Zero or more times |
| `+` | One or more times |
| `?` | Zero or one time (optional) |
| `{3}` | Exactly 3 times |
| `{2,5}` | From 2 through 5 times |
| `{2,}` | At least 2 times |

The quantifier applies to the thing immediately before it. So `\\d+` means one or more digits, while `[A-Z]{2}` means exactly two uppercase letters.

```python
re.findall(r"\\d+", "Room 12, floor 3")  # ['12', '3']
re.findall(r"[A-Z]{2}", "AB cd XY")     # ['AB', 'XY']
```

## 6. Start and end of text

`^` means the start of the text, and `$` means the end of the text. Together they let you check whether the **whole input** follows a pattern.

```python
re.findall(r"^\\d{4}$", "2026")  # ['2026']
re.findall(r"^\\d{4}$", "Year 2026")  # []
```

Without the anchors, `\\d{4}` can find four digits inside a longer string. With both anchors, the text must contain exactly four digits.

Python also provides `\\A` for the beginning of the string and `\\Z` for its end. The example in `ascii.py` uses `\\Z`. For beginner checks of a whole string, `^...$` is commonly used; be aware that multiline mode changes how `^` and `$` behave.

## 7. Groups and alternatives

Parentheses group parts of a pattern. A quantifier after a group applies to the whole group. A vertical bar `|` means “or.”

```python
re.findall(r"(ha)+", "haha ha")        # ['ha', 'ha']
re.findall(r"cat|dog", "cat and dog")  # ['cat', 'dog']
```

Groups are useful for patterns such as `(ab){2}`, which means `abab`. A group can also capture part of a match; `findall` may return the captured groups instead of the entire match, so keep that behavior in mind.

## 8. The main `re` functions

### `re.search(pattern, text)`

Looks anywhere in the text for the **first** match. It returns a match object if found, otherwise `None`.

```python
match = re.search(r"\\d+", "Order 4821")
if match:
    print(match.group())  # 4821
```

### `re.match(pattern, text)`

Checks for a match only at the **beginning** of the text. It does not automatically check the entire string. Use anchors if you need the entire string to follow a rule.

### `re.findall(pattern, text)`

Returns a list of all matches. It returns an empty list when there are no matches. This is the function used in several examples in this module.

```python
numbers = re.findall(r"\\d+", "A12 B7")
print(numbers)  # ['12', '7']
```

### `re.finditer(pattern, text)`

Returns match objects one by one. This is useful when you need each match's position in the text.

### `re.sub(pattern, replacement, text)`

Replaces each matching part with other text.

```python
cleaned = re.sub(r"\\s+", " ", "too   many   spaces")
print(cleaned)  # too many spaces
```

## 9. Case-insensitive matching

Pass `re.IGNORECASE` (also called `re.I`) to ignore uppercase/lowercase differences:

```python
found = re.search(r"python", "I am learning Python", re.IGNORECASE)
print(bool(found))  # True
```

The `ignorecase.py` example calls `findall` without this option, so searching for lowercase `python` will not match `Python` with a capital `P`.

## 10. Newlines and multiline text

By default, `.` does not match a newline. `re.DOTALL` (or `re.S`) makes a dot match newlines too. `re.MULTILINE` (or `re.M`) changes `^` and `$` so they can match the start and end of each line, not only the whole string.

```python
text = "first line\nsecond line"
print(re.findall(r"first.*second", text))  # []: dot stops at newline
print(re.findall(r"first.*second", text, re.DOTALL))  # matches across newline
```

## 11. Understanding the module examples

- `search_fun.py` searches for `is` anywhere in the text. Its `if x:` checks whether a match was found.
- `match_fun.py` looks for `Python` at the beginning. Since the example text begins with `This`, it does not match.
- `findall.py` demonstrates character ranges and returns every matching character in a list.
- `ascii.py` demonstrates shortcuts such as `\\w`, `\\d`, `\\s`, and the `\\Z` end anchor. The active pattern `96\\Z` asks whether the text ends with `96`; the example text does not.
- `multiline.py` demonstrates the dot wildcard and the `|` alternative.
- `ignorecase.py` shows a case-sensitive search by default; pass `re.IGNORECASE` to make it case-insensitive.
- `dotall.py` and `username_pattern.py` provide places to explore matching across lines and checking user input.

## 12. Improving the username example

The existing pattern `[A-Z]+[a-z]+[0-9]` finds a matching portion; it does not guarantee the whole username is valid. For example, extra characters before or after that portion may be ignored. Anchors make the rule apply to the full input:

```python
username_pattern = r"^[A-Z]+[a-z]+[0-9]$"
username = input("Enter a username: ")

if re.fullmatch(username_pattern, username):
    print("Username is valid!")
else:
    print("Invalid username")
```

This particular rule means: one or more uppercase letters, followed by one or more lowercase letters, followed by exactly one digit. It is only an example rule; a real application should explain its username requirements clearly.

## 13. A safe way to build a regex

Start with a sentence describing the rule. For example, “The entire input must be exactly five digits.” Translate each piece: start `^`, five digits `\\d{5}`, end `$`. Then test ordinary valid examples and invalid examples. Regex patterns can become difficult to read, so build them in small steps and add comments or a plain-language explanation.

## Practice ideas

1. Find all digits in `"Apt 8, building 24"`.
2. Check that a string is exactly two uppercase letters.
3. Find every occurrence of `cat` or `dog` in a sentence.
4. Replace repeated spaces with a single space.
5. Update the username example so it accepts exactly 3 lowercase letters followed by 2 digits.

