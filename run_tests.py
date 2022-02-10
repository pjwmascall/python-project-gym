import unittest

from tests.models.member_test import TestMember
from tests.models.gym_class_test import TestGymClass
from tests.models.booking_test import TestBooking

from tests.repositories.member_repository_test import TestMemberRepository
from tests.repositories.gym_class_repository_test import TestGymClassRepository
from tests.repositories.booking_repository_test import TestBookingRepository

# Database tables will be dropped and recreated when running repository tests

if __name__ == '__main__':
    unittest.main()