import unittest

from models.member import *
from models.gym_class import *
from models.booking import *

class TestBooking(unittest.TestCase):

    def setUp(self):
        self.member = Member('Jon', 'Snow', '123 Street Avenue', 'Standard', True, 1)
        self.gym_class = GymClass('Yoga', 'Judith', 'F11', 20, '2022-01-21', '09:30:00', '10:30:00', True, 1)
        self.booking = Booking(self.member, self.gym_class, True)

    def test_booking_has_member(self):
        self.assertEqual(self.booking.member, self.member)

    def test_booking_has_gym_class(self):
        self.assertEqual(self.booking.gym_class, self.gym_class)

    def test_booking_has_attended_True(self):
        self.assertEqual(True, self.booking.attended)

    def test_booking_has_attended_False(self):
        self.booking.attended = False
        self.assertEqual(False, self.booking.attended)

    def test_booking_has_no_id(self):
        self.assertEqual(None, self.booking.id)

    def test_booking_has_id(self):
        self.booking.id = 1
        self.assertEqual(1, self.booking.id)