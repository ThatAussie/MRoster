class Marshal:

    def __init__(self, Name, HeadMarshal, RegularMarshal, GreyLeader):
        self.Name = Name
        self.HeadMarshal = HeadMarshal
        self.RegularMarshal = RegularMarshal
        self.GreyLeader = GreyLeader

    def get_name(self):
        return self.Name

    def is_headmarshal(self):
        return self.HeadMarshal

    def is_marshal(self):
        return self.RegularMarshal

    def is_greyleader(self):
        return self.GreyLeader