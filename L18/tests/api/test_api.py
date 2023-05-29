import pytest

browser = "firefox"

#@pytest.mark.skip(reason="Not implemeted")
@pytest.mark.skipif(condition=(browser == 'firefox'), reason="Another platform")
@pytest.mark.login
def test_api_1():
    assert 4 == 4


@pytest.mark.login
@pytest.mark.smoke
def test_api_2():
    assert 3 == 4

@pytest.mark.xfail(reason="JIRA-1234")
def test_api_3():
    assert 4 == 4
