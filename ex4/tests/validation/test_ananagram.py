from ex4 import find_ananagrams

def test_multiline():
    res = find_ananagrams('input_files/test_1')
    expected = ['ladder', 'soon', 'eye', 'NotE', 'derail', 'drIed', 'Disk']
    assert res == expected

def test_long_line():
    res = find_ananagrams('input_files/test_2')
    assert res == None

def test_long_word():
    res = find_ananagrams('input_files/test_3')
    assert res == None

def test_nothing():
    res = find_ananagrams('input_files/test_4')
    assert res == []

def test_5():
    res = find_ananagrams('input_files/test_5')
    expected = ["frown", "Kjlek"]
    assert res == expected

def test_empty():
    res = find_ananagrams('input_files/test_6')
    assert res == None

def test_6():
    res = find_ananagrams('input_files/test_7')
    expected = ['TaR']
    assert res == expected

def test_7():
    res = find_ananagrams('input_files/test_8')
    expected = ['CCCa']
    assert res == expected

def test_8():
    res = find_ananagrams('input_files/test_9')
    expected = ['sitar', 'ris']
    assert res == expected

def test_9():
    res = find_ananagrams('input_files/test_10')
    expected = ['3312']
    assert res == expected
