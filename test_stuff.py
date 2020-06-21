import os

from stuff import do_stuff, show_me_X, hello

def test_do_stuff():
    assert do_stuff(0) == 0
    assert do_stuff(1) == 2

def test_show_me():
    assert show_me_X() == "X"

def test_hello():
    assert hello() == 'hello'

def test_secret():
    assert 'nie dla psa' == os.environ['STUFF']