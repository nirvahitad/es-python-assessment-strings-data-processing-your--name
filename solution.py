
"""
Python Programming Assessment
Strings & Data Processing
"""


def reverse_string(text: str) -> str:
    """
    Reverse the given string and return the result.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    return text[::-1]


def count_vowels(text: str) -> int:
    """
    Count the vowels (a, e, i, o, u) in a string.
    Both uppercase and lowercase vowels are counted.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    vowels = "aeiouAEIOU"
    count = 0

    for character in text:
        if character in vowels:
            count += 1

    return count


if __name__ == "__main__":
    # Task 1: Reverse a string
    text = "hello"
    print("Original string:", text)
    print("Reversed string:", reverse_string(text))

    print()

    # Task 2: Count vowels
    text = "Hello World"
    print("Input string:", text)
    print("Vowel count:", count_vowels(text))
