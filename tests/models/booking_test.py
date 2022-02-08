import unittest
from models.booking import *
from models.member import *
from models.gym_class import *

class TestBooking(unittest.TestCase):

    def setUp(self):
        self.test_member = Member('Jon', 'Snow', '123 Street Avenue', 'Standard', True, 1)
        self.test_gym_class = self.test_gym_class = GymClass('Yoga', 'Judith', 'F11', 20, '2022-01-21', '09:30:00', '10:30:00', True, 1)
        self.test_booking = Booking(self.test_member, self.test_gym_class)

    def test_booking_has_member(self):
        self.assertEqual(self.test_booking.member, self.test_member)

    def test_booking_has_gym_class(self):
        self.assertEqual(self.test_booking.gym_class, self.test_gym_class)

    def test_booking_has_attended_None(self):
        self.assertEqual(None, self.test_booking.attended)

    def test_booking_has_attended_True(self):
        self.test_booking.attended = True
        self.assertEqual(True, self.test_booking.attended)

    def test_booking_has_attended_False(self):
        self.test_booking.attended = False
        self.assertEqual(False, self.test_booking.attended)

    def test_booking_has_no_id(self):
        self.assertEqual(None, self.test_booking.id)

    def test_booking_has_id(self):
        self.test_booking.id = 1
        self.assertEqual(1, self.test_booking.id)