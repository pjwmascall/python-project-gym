import unittest

from tests.models.booking_test import TestBooking
from tests.models.gym_class_test import TestGymClass
from tests.models.member_test import TestMember

from tests.repositories.member_repository_test import TestMemberRepository

# Database tables will be dropped and recreated when running repository tests

if __name__ == '__main__':
    unittest.main()