"""
This module contains tests for the main application code.
"""

from app import hello_world

def test_hello_world():
    """
    Test the hello_world function.
    """
    assert hello_world() == "Hello, world!"

