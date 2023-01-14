# test_app.py

import app

def test_say_hello():
    assert app.say_hello() == "Hello, World!"
