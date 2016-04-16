import perfectmath.perfectmath

def test_is_six():
    """ test 6 """
    assert perfectmath.is_perfect_number(6) == True

def test_is_twentyeight():
    """ test 28 """
    assert perfectmath.is_perfect_number(28) == True

def test_is_fourhundredninetysix():
    """ test 496 """
    assert perfectmath.is_perfect_number(496) == True

def test_is_eightthousand():
    """ test 8128 """
    assert perfectmath.is_perfect_number(8128) == True

def test_is_eight():
    """ test 8 """
    assert perfectmath.is_perfect_number(8) == False

def test_is_thirtyfour():
    """ test 34 """
    assert perfectmath.is_perfect_number(34) == False

def test_is_fiverhundredeightyfour():
    """ test 584 """
    assert perfectmath.is_perfect_number(584) == False

def test_is_tenthousand():
    """ test 10460 """
    assert perfectmath.is_perfect_number(10460) == False
