import unittest
import os

from repositories.member_repository import *

class TestMemberRepository(unittest.TestCase):

    def setUp(self):
        os.system('psql -d gym -f db/gym.sql')
        self.member_1 = Member('Jon', 'Snow', '123 Street Avenue', 'Standard', True)
        self.member_2 = Member('Joe', 'Bloggs', '123 Boulevard Crescent', 'Premium', True)

    def test_can_save_member(self):
        member = save(self.member_1)
        self.assertEqual(member, self.member_1)

    def test_can_select_all_members(self):
        member_1 = save(self.member_1)
        member_2 = save(self.member_2)
        members = select_all()
        self.assertEqual(members[0].first_name, member_1.first_name)
        self.assertEqual(members[1].first_name, member_2.first_name)      

    def test_can_select_member_by_id(self):
        member = save(self.member_1)
        selected_member = select(member.id)
        self.assertEqual(member.first_name, selected_member.first_name)

    def test_can_delete_all_members(self):
        save(self.member_1)
        save(self.member_2)
        delete_all()
        members = select_all()
        self.assertEqual(0, len(members))

    def test_can_delete_member_by_id(self):
        member = save(self.member_1)
        delete(member.id)
        members = select_all()
        self.assertEqual(0, len(members))