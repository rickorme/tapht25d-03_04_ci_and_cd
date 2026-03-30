class Event:
    def __init__(self):
        self.attendees = []

    def register_attendee(self, attendee) -> None:
        self.attendees.append(attendee)
        return None

    def get_attendees(self) -> list:
        return self.attendees

    def is_attending(self, attendee) -> bool:
        attendee_in_list = attendee in self.attendees
        return attendee_in_list

    def register_new_member(self, name, ms):
        self.register_attendee(name)
        ms.register_new_member(name)
