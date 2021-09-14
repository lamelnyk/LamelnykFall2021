import pytest

@pytest.mark.parametrize("tuple1, tuple2, expected", [
    ((1,1), (2,2), 1.0)])
def test_lin_plot(tuple1, tuple2, expected): 
    from lin_plot import calculate_slope
    answer = calculate_slope(tuple1, tuple2)
    assert answer == expected 