def f(a, b):
    if b == 0:
        return None
    return a / b

def test_f():
    assert f(5, 2) == 2.5
    assert f(10 ** 30 - 1, 2) == 5 * 10 ** 29 + 500.5
    assert f(5, 0) is None

"""
a = int(input())
b = int(input())
print(f(a, b))
"""

