import unittest
import os

from repositories.gym_class_repository import *

class TestGymClassRepository(unittest.TestCase):

    def setUp(self):
        os.system('psql -d gym -f db/gym.sql')
        self.gym_class_1 = GymClass('Yoga', 'Judith', 'F11', 20, '2022-01-21', '09:30:00', '10:30:00', True)
        self.gym_class_2 = GymClass('Boxing', 'George', 'S09', 30, '2022-01-20', '15:30:00', '16:30:00', True)

    def test_can_save_gym_class(self):
        gym_class = save(self.gym_class_1)
        self.assertEqual(gym_class, self.gym_class_1)

    def test_can_select_all_gym_classes(self):
        gym_class_1 = save(self.gym_class_1)
        gym_class_2 = save(self.gym_class_2)
        gym_classes = select_all()
        self.assertEqual(gym_classes[0].class_name, gym_class_1.class_name)
        self.assertEqual(gym_classes[1].class_name, gym_class_2.class_name)

    def test_can_select_gym_class_by_id(self):
        gym_class = save(self.gym_class_1)
        selected_gym_class = select(gym_class.id)
        self.assertEqual(gym_class.class_name, selected_gym_class.class_name)

    def test_can_delete_all_members(self):
        save(self.gym_class_1)
        save(self.gym_class_2)
        delete_all()
        gym_classes = select_all()
        self.assertEqual(0, len(gym_classes))

    def test_can_delete_member_by_id(self):
        gym_class = save(self.gym_class_1)
        delete(gym_class.id)
        gym_classes = select_all()
        self.assertEqual(0, len(gym_classes))