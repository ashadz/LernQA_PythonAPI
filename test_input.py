import pytest
import requests

def test_assert_task():
    phrase = input("Set a phrase: ")
    assert len(phrase) < 15, f"Your phrase < 15 symbols, you phrase has {len(phrase)} symbols"