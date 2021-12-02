from ex2 import getUglyNumber

expected = [
    (1,1),
    (2,2),
    (3,3),
    (7,8),
    (100, 1536),
    (101, 1600),
    (102, 1620),
    (103, 1728),
    (200, 16200),
    (333, 131220)
]

def test_numbers():
    for (nth, n) in expected:
        result = getUglyNumber(nth)
        assert result == n