from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.gym_class import GymClass

import repositories.gym_class_repository as gym_class_repository

gym_classes_blueprint = Blueprint('gym_classes', __name__)

@gym_classes_blueprint.route('/classes', methods = ['GET'])
def show_gym_classes():
    gym_classes = gym_class_repository.select_all()
    return render_template('classes/index.html', gym_classes = gym_classes)

@gym_classes_blueprint.route('/classes/<id>', methods = ['GET'])
def show_gym_class(id):
    gym_class = gym_class_repository.select(id)
    return render_template('classes/show.html', gym_class = gym_class)

@gym_classes_blueprint.route('/classes/new', methods = ['GET'])
def new_gym_class():
    return render_template('classes/new.html')

@gym_classes_blueprint.route('/classes', methods = ['POST'])
def create_gym_class():
    class_name = request.form['class_name']
    instructor = request.form['instructor']
    room = request.form['room']
    capacity = request.form['capacity']
    class_date = request.form['class_date']
    class_start = request.form['class_start']
    class_end = request.form['class_end']
    is_active = request.form['is_active']
    gym_class = GymClass(class_name, instructor, room, capacity, class_date, class_start, class_end, is_active)
    gym_class_repository.save(gym_class)
    return redirect('/classes')

@gym_classes_blueprint.route('/classes/<id>/edit', methods = ['GET'])
def edit_gym_class(id):
    gym_class = gym_class_repository.select(id)
    return render_template('classes/edit.html', gym_class = gym_class)

@gym_classes_blueprint.route('/classes/<id>', methods = ['POST'])
def update_gym_class(id):
    class_name = request.form['class_name']
    instructor = request.form['instructor']
    room = request.form['room']
    capacity = request.form['capacity']
    class_date = request.form['class_date']
    class_start = request.form['class_start']
    class_end = request.form['class_end']
    is_active = request.form['is_active']
    gym_class = GymClass(class_name, instructor, room, capacity, class_date, class_start, class_end, is_active, id)
    gym_class_repository.update(gym_class)
    return redirect('/classes')

@gym_classes_blueprint.route('/classes/<id>/delete', methods = ['POST'])
def delete_gym_class(id):
    gym_class_repository.delete(id)
    return redirect('/classes')