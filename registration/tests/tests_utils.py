from django.test import TestCase
from ..utils import NewUserForm


class User_Form_Test(TestCase):
    """Tests registration form"""

    def test_UserForm_valid(self):
        """Tests registration form with valid data"""

        form = NewUserForm(data={"username": "Testuser",
                                 "first_name": "Martin",
                                 "last_name": "Paul",
                                 "email": "qqchose@mail.com",
                                 "password1": 'lfnedTTzpv244fjf',
                                 "password2": 'lfnedTTzpv244fjf'})
        self.assertTrue(form.is_valid())

    def test_UserForm_invalid(self):
        """Tests registration form with invalid data"""

        form = NewUserForm(data={"username": "Testuser2",
                                 "first_name": "Martine",
                                 "last_name": "Paule",
                                 "email": "",
                                 "password1": 'lfnedTTzpv244fjf',
                                 "password2": 'gfircfrhr'})
        self.assertFalse(form.is_valid())
