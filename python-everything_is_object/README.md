# Python - Everything is object

Questions about how Python handles objects: `id()` and `type()`, mutable and immutable types, aliases, `==` vs `is`, and how arguments are passed to functions. Each answer file holds a single line.

| File | Question | Answer |
|------|----------|--------|
| 0-answer.txt | Function to print the type of an object | type |
| 1-answer.txt | Function to get the variable identifier | id |
| 2-answer.txt | a = 89, b = 100: same object? | No |
| 3-answer.txt | a = 89, b = 89: same object? | Yes |
| 4-answer.txt | a = 89, b = a: same object? | Yes |
| 5-answer.txt | a = 89, b = a + 1: same object? | No |
| 6-answer.txt | s2 = s1, s1 == s2 | True |
| 7-answer.txt | s2 = s1, s1 is s2 | True |
| 8-answer.txt | two equal strings, == | True |
| 9-answer.txt | two equal strings, is | True |
| 10-answer.txt | two equal lists, == | True |
| 11-answer.txt | two equal lists, is | False |
| 12-answer.txt | l2 = l1, == | True |
| 13-answer.txt | l2 = l1, is | True |
| 14-answer.txt | l1.append(4), print(l2) | [1, 2, 3, 4] |
| 15-answer.txt | l1 = l1 + [4], print(l2) | [1, 2, 3] |
| 16-answer.txt | n += 1 inside a function on an int | 1 |
| 17-answer.txt | n.append(4) inside a function on a list | [1, 2, 3, 4] |
| 18-answer.txt | n = v inside a function | [1, 2, 3] |
| 19-copy_list.py | Function that returns a copy of a list | |
| 20-answer.txt | a = () is a tuple? | Yes |
| 21-answer.txt | a = (1, 2) is a tuple? | Yes |
| 22-answer.txt | a = (1) is a tuple? | No |
| 23-answer.txt | a = (1, ) is a tuple? | Yes |
| 24-answer.txt | (1) is (1) | True |
| 25-answer.txt | (1, 2) is (1, 2) | False |
| 26-answer.txt | () is () | True |
| 27-answer.txt | a = a + [5] keeps the same id? | No |
| 28-answer.txt | a += [4] keeps the same id? | Yes |
