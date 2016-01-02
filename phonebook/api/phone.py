

class Phone(object):
    """
    This API provides interface to the phone model.
    """

    def __init__(self, session):
        self.session = session

    def make_new_phone(self, **phone_info):
        pass

    def modify_existing_phone(self, phone_number, **phone_info):
        pass

    def remove_existing_phone(self, phone_number):
        pass
