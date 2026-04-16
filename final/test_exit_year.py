from test_final import *

def test_digits():
    assert cleanexityear('82') == '1982'
    assert cleanexityear('2') == '1902'

def test_letters():
    assert cleanexityear('88S') == '1988'
    assert cleanexityear('1988 AD') == '1988'
