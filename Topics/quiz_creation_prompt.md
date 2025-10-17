"""
    Quiz Creation Prompt
    
    Prompt to create multiple-choice quizzes and mini projects on a given topic for unit revision
"""

Prompt = """Act as a expert Learning Tutor of Python Programming

Your task to create multiple choice questions with answers on Python List theory and code snippets, to assist me in preparing for my weekly quiz.

The quiz will be a total of 100 multiple choice questions. I am to review the question and supply my answer.
The quiz will have 20 sections of five questions per section.
Each section covers a python method.
When starting a new section, a description of the method will be displayed
Each question will get progressively harder - Easy ->Medium->Hard->Hardest->Expert.
You will ask one question at a time, and wait for my answer. If I get the question correct, move to the next questions, if I get the question wrong, tell me the correct answer and explain why.
The list of sections are:
index() method
count() method
sort() method
sorted() method
reverse() method
reversed() method
copy() method
min() method
max() method
sum() method
split() method
join() method
enumerate() method
zip() method
remove() method
pop() method
clear() method
append() method
insert() method
extend() method


// ...existing code...
### Section 2: values() method (Medium)

Question:
```python
d = {'a': 1, 'b': 2}
print(d.values()[0])
```

Choices:
A) 1  
B) 2  
C) Raises TypeError ('dict_values' object is not subscriptable)  
D) None

Answer: C) Raises TypeError

Explanation: dict_values returns a view object which is not subscriptable. To get the first value, convert to a list (list(d.values())[0]) or use an iterator (next(iter(d.values()))).
// ...existing code...

### Section 2: values() method (Medium)

Question:
```python
d = {'a': 1, 'b': 2}
print(d.values()[0])
```

Choices:
A) 1  
B) 2  
C) Raises TypeError ('dict_values' object is not subscriptable)  
D) None

Answer: C) Raises TypeError

Explanation: dict_values returns a dynamic view object which is not subscriptable. To get the first value use list(d.values())[0] or next(iter(d.values())).


### Section 2: values() method (Hard)

Question:
```python
d = {'a': 1, 'b': 2}
print(list(d.values()) == [1, 2])
```

Choices:
A) True  
B) False  
C) Raises TypeError  
D) dict_values([1, 2])

Answer: A) True

Explanation: Dictionaries preserve insertion order, so list(d.values()) yields [1, 2], which equals the list on the right.


### Section 3: items() method (Easy)

Question:
```python
d = {'a': 1, 'b': 2}
print(d.items())
```

Choices:
A) `[('a', 1), ('b', 2)]`  
B) `dict_items([('a', 1), ('b', 2)])` (a view object)  
C) `['a', 'b']`  
D) `None`

Answer: B) `dict_items([('a', 1), ('b', 2)])`

Explanation: `dict.items()` returns a dynamic view of (key, value) pairs as tuples. Converting to list gives a snapshot: `list(d.items())`.

### Section 3: items() method (Hard)

Question:
```python
d1 = {'x': [1, 2], 'y': [3, 4]}
d2 = {'x': [1, 2], 'y': [3, 4]}
print(d1.items() == d2.items())
```

Choices:
A) True  
B) False  
C) Raises TypeError  
D) Depends on insertion order

Answer: A) True

Explanation: `dict.items()` compares the contents of the view (the (key, value) pairs). The two dictionaries contain equal key/value pairs, and equality checks for the values (here lists) are based on list contents, so the items views compare equal and the expression evaluates to `True`.

### Section 3: items() method (Hardest)

Question:
```python
d = {'a': 1, 'b': 2}
it = iter(d.items())
d['a'] = 100
print(next(it))
```

Choices:
A) ('a', 1)  
B) ('a', 100)  
C) Raises RuntimeError  
D) ('b', 2)

Answer: B) ('a', 100)

Explanation: The iterator over `d.items()` yields (key, value) pairs reflecting the current mapping when each item is produced. Changing the value of an existing key before consuming the iterator updates what will be yielded, so the first item shows the new value `100`. Removing/adding keys during iteration can raise runtime issues, but updating a value is permitted and is reflected in the iterator.

### Section 3: items() method (Medium)

Question:
```python
d = {'a': 1, 'b': 2}
items_view = d.items()
d.pop('a')
print(('a', 1) in items_view)
```

Choices:
A) True  
B) False  
C) Raises KeyError  
D) ('a', 1)

Answer: B) False

Explanation: `dict.items()` returns a dynamic view of (key, value) pairs. When the key `'a'` is removed with `pop()`, the items view reflects that change, so the tuple `('a', 1)` is no longer present and membership returns `False`.

