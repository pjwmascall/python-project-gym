import unittest
from models.member import *

class TestMember(unittest.TestCase):

    def setUp(self):
        self.test_member = Member('Jon', 'Snow', '123 Street Avenue', 'Standard', True)

    def test_member_has_first_name(self):
        self.assertEqual('Jon', self.test_member.first_name)

    def test_member_has_last_name(self):
        self.assertEqual('Snow', self.test_member.last_name)

    def test_member_has_home_address(self):
        self.assertEqual('123 Street Avenue', self.test_member.home_address)

    def test_member_has_membership(self):
        self.assertEqual('Standard', self.test_member.membership_type)

    def test_member_is_active(self):
        self.assertEqual(True, self.test_member.is_active)

    def test_member_has_no_id(self):
        self.assertEqual(None, self.test_member.id)

    def test_member_has_id(self):
        self.test_member.id = 1
        self.assertEqual(1, self.test_member.id)