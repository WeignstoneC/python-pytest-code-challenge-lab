import pytest

from palindrome import longest_palindromic_substring


@pytest.mark.parametrize(
    "value, expected",
    [
        ("babad", "bab"),
        ("cbbd", "bb"),
        ("a", "a"),
        ("ac", "a"),
        ("racecar", "racecar"),
        ("banana", "anana"),
        ("abacdfgdcaba", "aba"),
        ("abcda", "a"),
    ],
)
def test_longest_palindromic_substring_basic_cases(value, expected):
    assert longest_palindromic_substring(value) == expected


def test_empty_string_returns_empty_string():
    assert longest_palindromic_substring("") == ""


def test_all_same_characters_returns_full_string():
    assert longest_palindromic_substring("aaaaa") == "aaaaa"


def test_no_palindrome_returns_single_character():
    assert longest_palindromic_substring("abc") == "a"


def test_mixed_alphanumeric_string():
    assert longest_palindromic_substring("a1b22b1a") == "a1b22b1a"
