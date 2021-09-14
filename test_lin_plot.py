import pytest

@pytest.mark.parametrize("list1, list2, expected", [
    ((1,1), (2,2), 1.0)])
def test_calculate_slope(list1, list2, expected): 
    from lin_plot import calculate_slope
    answer = calculate_slope(list1, list2)
    assert answer == expected

@pytest.mark.parametrize("tuple1, value3, slope, expected", [
    ((1,1), 3 , 1.0, 3 )])
def test_calculate_y3(slope, tuple1, value3, expected): 
    from lin_plot import calculate_y3
    answer = calculate_y3(slope, tuple1, value3)
    assert answer == expected
    