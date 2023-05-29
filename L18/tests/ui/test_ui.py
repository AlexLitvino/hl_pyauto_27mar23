import pytest

def test_ui_1():
    assert 4 == 5

@pytest.mark.smoke
def test_ui_2():
    assert 4 == 4

@pytest.mark.login
def test_ui_3():
    assert 4 == 4


@pytest.mark.smoke
def test_ui_login_screen_first():
    assert 4 == 4


def test_ui_login_screen_second():
    assert 4 == 4
