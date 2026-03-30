class MemberService():

    def __init__(self):
        self.members = []

    def register_new_member(self, name):
        self.members.append(name)

    def is_registered(self, name) -> bool:
        return name in self.members
