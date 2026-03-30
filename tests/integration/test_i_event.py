import pytest


@pytest.mark.integration
def test_register_new_member(event, ms):

    name = "Sally"

    event.register_new_member(name, ms)

    assert ms.is_registered(name)
