import unittest
from models.gym_class import *

class TestGymClass(unittest.TestCase):

    def setUp(self):
        self.test_gym_class = GymClass('Yoga', 'Judith', 'F11', 20, '2022-01-21', '09:30:00', '10:30:00', True)

    def test_gym_class_has_class_name(self):
        self.assertEqual('Yoga', self.test_gym_class.class_name)

    def test_gym_class_has_instructor(self):
        self.assertEqual('Judith', self.test_gym_class.instructor)

    def test_gym_class_has_room(self):
        self.assertEqual('F11', self.test_gym_class.room)

    def test_gym_class_has_capacity(self):
        self.assertEqual(20, self.test_gym_class.capacity)

    def test_gym_class_has_class_date(self):
        self.assertEqual('2022-01-21', self.test_gym_class.class_date)

    def test_gym_class_has_class_start(self):
        self.assertEqual('09:30:00', self.test_gym_class.class_start)

    def test_gym_class_has_class_end(self):
        self.assertEqual('10:30:00', self.test_gym_class.class_end)

    def test_gym_class_is_active(self):
        self.assertEqual(True, self.test_gym_class.is_active)

    def test_gym_class_has_no_id(self):
        self.assertEqual(None, self.test_gym_class.id)

    def test_gym_class_has_id(self):
        self.test_gym_class.id = 1
        self.assertEqual(1, self.test_gym_class.id)