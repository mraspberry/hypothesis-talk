from hypothesis import given
from hypothesis.strategies import integers

from hypothesis_talk.adder import add_nums


def test_add_nums_gives_right_answer():
    assert add_nums(2, 2) == 4


@given(integers(), integers())
def test_add_nums_is_commutative(a, b):
    assert add_nums(a, b) == add_nums(b, a)


@given(integers())
def test_add_nums_is_additive(a):
    assert add_nums(a) == a


@given(integers(), integers(), integers())
def test_add_nums_is_associative(a, b, c):
    assert add_nums(a, (b + c)) == add_nums((a + b), c)


@given(integers(), integers(), integers())
def test_add_nums_is_distributive(a, b, c):
    assert a * add_nums(b, c) == add_nums((a * b), (a * c))
