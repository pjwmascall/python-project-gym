import unittest
import os

import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.booking_repository as booking_repository

class TestBookingRepository(unittest.TestCase):

    def setUp(self):
        os.system('psql -d gym -f db/gym.sql')
        self.member_1 = member_repository.Member('Jon', 'Snow', '123 Street Avenue', 'Standard', True)
        self.member_2 = member_repository.Member('Joe', 'Bloggs', '123 Boulevard Crescent', 'Premium', True)
        member_1 = member_repository.save(self.member_1)
        member_2 = member_repository.save(self.member_2)
        self.gym_class_1 = gym_class_repository.GymClass('Yoga', 'Judith', 'F11', 20, '2022-01-21', '09:30:00', '10:30:00', True)
        self.gym_class_2 = gym_class_repository.GymClass('Boxing', 'George', 'S09', 30, '2022-01-20', '15:30:00', '16:30:00', True)
        gym_class_1 = gym_class_repository.save(self.gym_class_1)
        gym_class_2 = gym_class_repository.save(self.gym_class_2)
        self.booking_1 = booking_repository.Booking(member_1, gym_class_1, True)
        self.booking_2 = booking_repository.Booking(member_2, gym_class_2, False)
        
    def test_can_save_booking(self):
        booking_1 = booking_repository.save(self.booking_1)
        self.assertEqual(booking_1, self.booking_1)

    def test_can_select_all_bookings(self):
        booking_1 = booking_repository.save(self.booking_1)
        booking_2 = booking_repository.save(self.booking_2)
        bookings = booking_repository.select_all()
        self.assertEqual(bookings[0].member.id, booking_1.member.id)
        self.assertEqual(bookings[0].gym_class.id, booking_1.gym_class.id)
        self.assertEqual(bookings[1].member.id, booking_2.member.id)
        self.assertEqual(bookings[1].gym_class.id, booking_2.gym_class.id)      

    def test_can_select_booking_by_id(self):
        booking = booking_repository.save(self.booking_1)
        selected_booking = booking_repository.select(booking.id)
        self.assertEqual(booking.member.id, selected_booking.member.id)
        self.assertEqual(booking.gym_class.id, selected_booking.gym_class.id)

    def test_can_delete_all_bookings(self):
        booking_repository.save(self.booking_1)
        booking_repository.save(self.booking_2)
        booking_repository.delete_all()
        bookings = booking_repository.select_all()
        self.assertEqual(0, len(bookings))

    def test_can_delete_booking_by_id(self):
        booking = booking_repository.save(self.booking_1)
        booking_repository.delete(booking.id)
        bookings = booking_repository.select_all()
        self.assertEqual(0, len(bookings))