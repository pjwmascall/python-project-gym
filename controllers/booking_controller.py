from flask import Flask, Blueprint, render_template, request, redirect

from models.booking import Booking

import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository

bookings_blueprint = Blueprint('bookings', __name__)

@bookings_blueprint.route('/bookings', methods = ['GET'])
def show_all_bookings():
    bookings = booking_repository.select_all()
    return render_template('bookings/index.html', bookings = bookings)