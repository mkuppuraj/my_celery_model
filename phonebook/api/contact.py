

class Contact(object):
    """
    This API provides interface to the contact model.
    """

    def __init__(self, session):
        self.session = session

    def make_new_contact(self, **contact_info):
        pass

    def update_existing_contact(self, contact_name, **contact_info):
        pass

    def remove_existing_contact(self, contact_name):
        pass

    def add_phones_to_contact(self, contact_name, phone_number_details = []):
        pass

    def remove_phones_from_contacts(self, contact_name, phone_numbers):
        pass

    def list_phones_for_contact(self, contact_name):
        pass

    def list_matching_contacts(self, pattern):
        """
        The pattern either matches to contact name or the phone number.
        """
