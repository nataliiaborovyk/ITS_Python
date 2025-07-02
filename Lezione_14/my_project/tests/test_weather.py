from my_project.weather import check_weather
import pytest

'''
#passed
def test_check_weather1():
    assert check_weather(21.00) == "hot", 'temperature greater than 20 degree  must be considered as hot'

def test_check_weather2():
    assert check_weather(5.00) == "average", 'temperature beatween 10 e 20 degree  must be considered as  average'

def test_check_weather3():
    assert check_weather(5.00) == "cold", 'temperature lower then 10 gradi must be considered as cold'

def test_check_weather4():
    assert check_weather(13.00) == "average", 'temperature beatween 10 e 20 degree  must be considered as  average'

def test_check_weather5():
    assert check_weather(30.00) == "hot", 'temperature greater than 20 degree  must be considered as hot'
    assert check_weather(11.00) == "cold", 'temperature lower then 10 gradi must be considered as cold'
'''
@pytest.mark.parametrize("temperature, expected", [
    (21.00, "hot"),
    (13.00, "average"),
    (0.00, "cold"),
    (15.00, "cold")
])


# def test_check_weather(temperature, expected):
#     assert check_weather(temperature) == expected


def test_check_weather(temperature, expected):
    ae:str = "" 
    if temperature > 20:
        ae = 'temperature greater than 20 degree  must be considered as hot'
    elif 10 < temperature <= 20:
        ae = 'temperature beatween 10 e 20 degree  must be considered as  average'
    else:
        ae = 'temperature lower then 10 gradi must be considered as cold'
    assert check_weather(temperature) == expected, ae
    