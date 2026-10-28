
# Python Programming Assessment
## Strings & Data Processing

**Candidate:** Nirvahita Devkate

### Overview

This project implements two Python functions:

1. `reverse_string(text)` - Reverses a string.
2. `count_vowels(text)` - Counts vowels in a string,
   including uppercase and lowercase vowels.

### Requirements

- Python 3.8 or later
- No external libraries required

### Project Files

- `solution.py` - Python function implementations
- `test_solution.py` - Automated unit tests
- `README.md` - Project documentation

### How to Run

Run the main program:

```bash
python solution.py
```

Expected output:

```text
Original string: hello
Reversed string: olleh

Input string: Hello World
Vowel count: 3
```

### How to Run Tests

```bash
python -m unittest -v
```

### Approach

- String reversal uses Python slicing.
- Vowels are counted using a loop and character comparisons.
- Both functions validate input types.
- Unit tests cover normal inputs and edge cases.

### Time Complexity

- `reverse_string`: O(n)
- `count_vowels`: O(n)

Here, n is the length of the input string.
