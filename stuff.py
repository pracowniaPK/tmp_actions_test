import os


def do_stuff(x):
    return 2*x

def show_me_X():
    return 'X'

def hello():
    return 'hello'


if __name__ == "__main__":
    hello()
    print('tajny secret:', os.environ['STUFF'])
