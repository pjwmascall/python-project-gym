# import pdb
import os

from models.member import Member
from models.gym_class import GymClass
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.booking_repository as booking_repository

os.system('psql -d gym -f db/gym.sql')

member_1 = Member('Jon', 'Snow', '123 Street Avenue', 'Premium', True)
member_2 = Member('Joe', 'Bloggs', '123 Boulevard Crescent', 'Premium', True)
member_3 = Member('Jack', 'Jackson', '1 Address Street', 'Premium', False)
member_4 = Member('Jason', 'Smith', '2 Address Street', 'Premium', True)
member_5 = Member('Jessica', 'Jameson', '1 Place Place', 'Standard', True)
member_repository.save(member_1)
member_repository.save(member_2)
member_repository.save(member_3)
member_repository.save(member_4)
member_repository.save(member_5)

gym_class_1 = GymClass('Yoga', 'Judith', 'F11', 20, '2022-01-21', '09:30:00', '10:30:00', True)
gym_class_2 = GymClass('Boxing', 'George', 'S09', 30, '2022-01-20', '15:30:00', '16:30:00', True)
gym_class_3 = GymClass('Yoga', 'Judith', 'F11', 20, '2023-02-12', '09:30:00', '13:30:00', False)
gym_class_4 = GymClass('Swimming', 'Michael', 'Main Pool', 10, '2022-01-21', '09:30:00', '10:30:00', True)
gym_class_5 = GymClass('Pilates', 'Rachel', 'B10', 5, '2022-01-21', '10:30:00', '11:30:00', True)
gym_class_6 = GymClass('Personal Training', 'Jordan', 'B10', 1, '2022-01-21', '12:30:00', '13:30:00', True)
gym_class_7 = GymClass('Crossfit', 'Lee', 'F11', 20, '2022-01-20', '18:00:00', '19:00:00', False)
gym_class_repository.save(gym_class_1)
gym_class_repository.save(gym_class_2)
gym_class_repository.save(gym_class_3)
gym_class_repository.save(gym_class_4)
gym_class_repository.save(gym_class_5)
gym_class_repository.save(gym_class_6)
gym_class_repository.save(gym_class_7)

booking_1 = booking_repository.Booking(member_1, gym_class_1, True)
booking_2 = booking_repository.Booking(member_1, gym_class_2, False)
booking_3 = booking_repository.Booking(member_1, gym_class_3, False)
booking_4 = booking_repository.Booking(member_2, gym_class_1, False)
booking_5 = booking_repository.Booking(member_3, gym_class_2, True)
booking_6 = booking_repository.Booking(member_4, gym_class_6, True)
booking_7 = booking_repository.Booking(member_5, gym_class_2, True)
booking_repository.save(booking_1)
booking_repository.save(booking_2)
booking_repository.save(booking_3)
booking_repository.save(booking_4)
booking_repository.save(booking_5)
booking_repository.save(booking_6)
booking_repository.save(booking_7)

# pdb.set_trace()