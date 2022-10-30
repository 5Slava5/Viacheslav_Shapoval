s = "Python World"
b = "I like "

def mane_function():
    print(s.upper())
    print(len(s))
    print(s * 3)
    print(s.swapcase())


def test_function():
    c = b + s
    print(c.upper())


mane_function()
test_function()

