from ex3 import find_anagrams

def test_1():
    result = find_anagrams('input_files/test_1')
    expected = {
        'WILLIAM SHAKESPEARE': [
            ['AWHILE', 'REALISM', 'SPEAK'], 
            ['AWHILE', 'SPEAK', 'REALISM'],
            ['REALISM', 'AWHILE', 'SPEAK'], 
            ['REALISM', 'SPEAK', 'AWHILE'], 
            ['SPEAK', 'AWHILE', 'REALISM'], 
            ['SPEAK', 'REALISM', 'AWHILE']]}
    assert result == expected

def test_2():
    result = find_anagrams('input_files/test_2')
    expected = {
        'XK XYZZ Y': [
            ['KX', 'Y', 'ZZXY'], 
            ['KX', 'ZZXY', 'Y'], 
            ['Y', 'KX', 'ZZXY'], 
            ['Y', 'ZZXY', 'KX'], 
            ['ZZXY', 'KX', 'Y'], 
            ['ZZXY', 'Y', 'KX']]}
    assert result == expected

def test_3():
    result = find_anagrams('input_files/test_3')
    expected = {
        '321': [
            ['1', '2', '3'], 
            ['1', '3', '2'], 
            ['2', '1', '3'], 
            ['2', '3', '1'], 
            ['3', '1', '2'], 
            ['3', '2', '1']]}
    assert result == expected

def test_4():
    result = find_anagrams('input_files/test_4')
    expected = {
        'ABBCCC': [
            ['A', 'BB', 'CCC'], 
            ['A', 'CCC', 'BB'],
            ['BB', 'A', 'CCC'], 
            ['BB', 'CCC', 'A'], 
            ['CCC', 'A', 'BB'], 
            ['CCC', 'BB', 'A']]}
    assert result == expected

def test_5():
    result = find_anagrams('input_files/test_5')
    expected = {}
    assert result == expected

def test_6():
    result = find_anagrams('input_files/test_6')
    expected = {
        'ATRAPS': [['SPARTA']],
        'ATRAPS SI': [['IS', 'SPARTA'], ['SPARTA', 'IS']],
        'THIS IS SPARTA': [
            ['IS', 'SPARTA', 'THIS'], 
            ['IS', 'THIS', 'SPARTA'], 
            ['SPARTA', 'IS', 'THIS'], 
            ['SPARTA', 'THIS', 'IS'], 
            ['THIS', 'IS', 'SPARTA'], 
            ['THIS', 'SPARTA', 'IS']]}
    assert result == expected

def test_7():
    result = find_anagrams('input_files/test_7')
    expected = {'AB': [['A', 'B'], ['B', 'A']]}
    assert result == expected

def test_8():
    result = find_anagrams('input_files/test_8')
    expected = {}
    assert result == expected

def test_9():
    result = find_anagrams('input_files/test_9')
    expected = {
        '10': [['0', '1'], ['1', '0']], '01': [['0', '1'], ['1', '0']]}
    assert result == expected

def test_10():
    result = find_anagrams('input_files/test_10')
    expected = {'YY': [['YY']], 'XXZZ': [['XX', 'ZZ'], ['ZZ', 'XX']]}
    assert result == expected