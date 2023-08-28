import pytest


@pytest.mark.parametrize('program_output', ['1', '50', '55.55', '100'], indirect=True)
def test_first_segment(program_output):
    """
    Проверка диапазона 1-100
    """
    assert program_output == '1'


@pytest.mark.parametrize('program_output', ['101', '150', '155.55', '200'], indirect=True)
def test_second_segment(program_output):
    """
    Проверка диапазона 101-200
    """
    assert program_output == '2'


@pytest.mark.parametrize('program_output', ['201', '250', '255.55', '300'], indirect=True)
def test_third_segment(program_output):
    """
    Проверка диапазона 201-300
    """
    assert program_output == '3'


@pytest.mark.parametrize('program_output', ['301', '350', '355.55', '400'], indirect=True)
def test_fourth_segment(program_output):
    """
    Проверка диапазона 301-400
    """
    assert program_output == '4'


@pytest.mark.parametrize('program_output', ['0', '401', 'abc'], indirect=True)
def test_invalid_values(program_output):
    """
    Проверка значений за пределами диапазонов, указанных в документации
    """
    assert program_output == '0'
