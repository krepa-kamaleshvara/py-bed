import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.app import hello_world

def test_hello_world():
    assert hello_world() == "Hello, world!"