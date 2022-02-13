from db.run_sql import run_sql

from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository


def save(booking):
    sql = """
        INSERT INTO
        bookings (
            member_id,
            class_id,
            attended
            ) 
        VALUES (%s, %s, %s) 
        RETURNING id
        """
    values = [
        booking.member.id,
        booking.gym_class.id,
        booking.attended
        ]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking


def update(booking):
    sql = """
        UPDATE bookings 
        SET (
            member_id,
            class_id,
            attended
            )
        = (%s, %s, %s)
    WHERE id = %s
    """
    values = [
        booking.member.id,
        booking.gym_class.id,
        booking.attended,
        booking.id
        ]
    run_sql(sql, values)


def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for row in results:
        member = member_repository.select(row['member_id'])
        gym_class = gym_class_repository.select(row['class_id'])
        booking = Booking(
                member, 
                gym_class, 
                row['attended'], 
                row['id']
            )
        bookings.append(booking)
    return bookings


def select_all_bookings_by_gym_class(gym_class_id):
    bookings = []
    sql = """
    SELECT bookings.* FROM bookings
    WHERE class_id = %s
    """
    values = [gym_class_id]
    results = run_sql(sql, values)
    for row in results:
        member = member_repository.select(row['member_id'])
        gym_class = gym_class_repository.select(gym_class_id)
        booking = Booking(member, gym_class, row['attended'], row['id'])
        bookings.append(booking)
    return bookings


def select(id):
    booking = None
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        member = member_repository.select(result['member_id'])
        gym_class = gym_class_repository.select(result['class_id'])
        booking = Booking(
            member,
            gym_class,
            result['attended'],
            result['id']
        )
    return booking


def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)