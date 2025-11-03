# Unit tests for the comfort_level() function

# Fill in the blank spaces in the calls to comfort_level() below, using
# the values you've chosen for testing the function

# Then write a test_ok() function that tests the other equivalence class

from weather import comfort_level

def test_cold():
    assert comfort_level(15) == "COLD"
    assert comfort_level(-100) == "COLD"

def test_hot():
    assert comfort_level(26) == "HOT"
    assert comfort_level(100) == "HOT"

def test_OK():
    assert comfort_level(25) == "OK"
    assert comfort_level(16) == "OK"

test_cold()
test_hot()
test_OK()