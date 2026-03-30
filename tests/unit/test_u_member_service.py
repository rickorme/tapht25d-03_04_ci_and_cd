import pytest


@pytest.mark.unit
def test_register_new_member(ms):

    name = "Helen"

    ms.register_new_member(name)

    assert ms.is_registered(name)


@pytest.mark.unit
def test_is_registered__not_registered(ms):

    name = "Dave"

    assert ms.is_registered(name) is False


@pytest.mark.unit
def test_register_new_member__with_spying(ms, mocker):

    spy = mocker.spy(ms, 'register_new_member')
    name = "Terry"

    ms.register_new_member(name)

    assert ms.is_registered(name)
    spy.assert_called_once()
