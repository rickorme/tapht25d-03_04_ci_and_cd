import pytest
from src.dive.member_service import MemberService


@pytest.mark.unit
def test_get_attendees_empty(event):
    # event = Event()
    attendees = event.get_attendees()

    # Assertions
    assert len(attendees) == 0, "Expected no attendees for a new event"


# Test register_attendee functionality of Event class
@pytest.mark.unit
def test_register_attendee(event):

    attendee = "Rick"
    event.register_attendee(attendee)
    is_attending = event.is_attending(attendee)

    # Assertions
    assert is_attending is True, f"Expected {attendee} to be registered as attending"


# Test multiple attendees in list
@pytest.mark.unit
def test_get_attendees__multiple(event):

    # register 2 attendees
    attendee_1 = "Rick"
    attendee_2 = "Tom"
    event.register_attendee(attendee_1)
    event.register_attendee(attendee_2)

    # get list of attendees
    attendees = event.get_attendees()

    # Assertions
    assert len(attendees) == 2
    assert attendee_1 in attendees
    assert attendee_2 in attendees


@pytest.mark.unit
def test_register_new_member(event, mocker):

    ms = mocker.Mock(spec=MemberService)
    name = "Bill"

    event.register_new_member(name, ms)
    # get list of attendees
    attendees = event.get_attendees()

    assert name in attendees
    ms.register_new_member.assert_called()
