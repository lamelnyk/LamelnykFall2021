import pytest 
from temp_calc import detect_fever

@pytest.mark.parameterize("input, expected", [
    ([96, 96.5, 103.1, 98.7], True) ,
    ([96, 96.5, 103.1, 98.7], False)])
def test_detect_fever():
    answer = detect_fever(input)
    assert answer == expected

