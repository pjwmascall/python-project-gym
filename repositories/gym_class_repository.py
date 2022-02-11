from db.run_sql import run_sql

from models.gym_class import GymClass


def save(gym_class):
    sql = """
        INSERT INTO
        gym_classes (
            class_name,
            instructor,
            room,
            capacity,
            class_date,
            class_start,
            class_end,
            is_active
            )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id
        """
    values = [
        gym_class.class_name,
        gym_class.instructor, 
        gym_class.room,
        gym_class.capacity,
        gym_class.class_date,
        gym_class.class_start,
        gym_class.class_end,
        gym_class.is_active
        ]
    results = run_sql(sql, values)
    gym_class.id = results[0]['id']
    return gym_class


def update(gym_class):
    sql = """
        UPDATE gym_classes 
        SET (
            class_name,
            instructor,
            room,
            capacity,
            class_date,
            class_start,
            class_end,
            is_active
            )
        = (%s, %s, %s, %s, %s, %s, %s, %s)
    WHERE id = %s
    """
    values = [
        gym_class.class_name,
        gym_class.instructor, 
        gym_class.room,
        gym_class.capacity,
        gym_class.class_date,
        gym_class.class_start,
        gym_class.class_end,
        gym_class.is_active,
        gym_class.id
        ]
    run_sql(sql, values)


def select_all():
    gym_classes = []
    sql = "SELECT * FROM gym_classes"
    results = run_sql(sql)
    for row in results:
        gym_class = GymClass(
            row['class_name'],
            row['instructor'],
            row['room'],
            row['capacity'],
            row['class_date'],
            row['class_start'],
            row['class_end'],
            row['is_active'],
            row['id']
        )
        gym_classes.append(gym_class)
    return gym_classes


def select(id):
    gym_class = None
    sql = "SELECT * FROM gym_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        gym_class = GymClass(
            result['class_name'],
            result['instructor'],
            result['room'],
            result['capacity'],
            result['class_date'],
            result['class_start'],
            result['class_end'],
            result['is_active'],
            result['id']
        )
    return gym_class


def delete_all():
    sql = "DELETE FROM gym_classes"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM gym_classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)