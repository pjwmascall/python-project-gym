class Member:

    def __init__(
        self, 
        first_name, 
        last_name, 
        home_address, 
        membership_type, 
        is_active, 
        id = None
        ):
        self.first_name = first_name
        self.last_name = last_name
        self.home_address = home_address
        self.membership_type = membership_type
        self.is_active = is_active
        self.id = id
