from code import example1
from hypothesis import given, example
from hypothesis.strategies import text

@given(s=text())
# this ensures this examples always runs
@example(s="")
def test_decode_inverts_encode(s):
	assert example1.decode(example1.encode(s)) == s
