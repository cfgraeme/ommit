def hello(name):
    print(_hello(name))


def _hello(name):
    return f"Hello, {name}!"


def hello_world():
    hello("World")


if __name__ == "__main__":
    hello_world()
