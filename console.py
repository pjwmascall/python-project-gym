# import pdb
import os

from models.member import Member
from models.gym_class import GymClass
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.booking_repository as booking_repository

os.system('psql -d gym -f db/gym.sql')

member_1 = Member('Jon', 'Snow', '123 Street Avenue', 'Standard', True)
member_2 = Member('Joe', 'Bloggs', '123 Boulevard Crescent', 'Premium', True)
member_repository.save(member_1)
member_repository.save(member_2)

gym_class_1 = GymClass('Yoga', 'Judith', 'F11', 20, '2022-01-21', '09:30:00', '10:30:00', True)
gym_class_2 = GymClass('Boxing', 'George', 'S09', 30, '2022-01-20', '15:30:00', '16:30:00', True)
gym_class_3 = GymClass('Yoga', 'Judith', 'F11', 20, '2023-02-12', '09:30:00', '13:30:00', False)
gym_class_repository.save(gym_class_1)
gym_class_repository.save(gym_class_2)
gym_class_repository.save(gym_class_3)

booking_1 = booking_repository.Booking(member_1, gym_class_1, True)
booking_2 = booking_repository.Booking(member_2, gym_class_2, False)
booking_repository.save(booking_1)
booking_repository.save(booking_2)

# pdb.set_trace()