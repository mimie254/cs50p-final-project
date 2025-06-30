from project import check_correct_args, select_colour, select_mileage_from_price
import pytest

def test_check_correct_args():
    with pytest.raises(SystemExit):
        check_correct_args()



def test_select_colour():
    assert select_colour(2016) == "White"
    assert select_colour(2017) == "White"
    assert select_colour(2018) == 'Pearl_white'
    assert select_colour(2019) == 'Pearl_white'


def test_select_mileage_from_price():
    assert select_mileage_from_price("1.2M") == 'Above 50,000 km'
    assert select_mileage_from_price("2.01M") == 'Below 50,000 km'
    assert select_mileage_from_price("2.0M") == 'Above 50,000 km'
    assert select_mileage_from_price("4.2M") == 'Below 50,000 km'

