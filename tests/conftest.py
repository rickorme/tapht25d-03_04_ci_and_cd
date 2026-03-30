import pytest

from src.dive.event import Event
from src.dive.member_service import MemberService


@pytest.fixture
def event():
    return Event()


@pytest.fixture
def ms():
    return MemberService()
