from stuff import do_stuff, show_me_X

def test_do_stuff():
    assert do_stuff(0) == 0
    assert do_stuff(1) == 2

def test_show_me():
    assert show_me_X() == "X"