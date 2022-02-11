from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.member import Member

import repositories.member_repository as member_repository

members_blueprint = Blueprint('members', __name__)

@members_blueprint.route('/members', methods = ['GET'])
def show_members():
    members = member_repository.select_all()
    return render_template('members/index.html', members = members)

@members_blueprint.route('/members/<id>', methods = ['GET'])
def show_member(id):
    member = member_repository.select(id)
    return render_template('members/show.html', member = member)

@members_blueprint.route('/members/new', methods = ['GET'])
def new_member():
    return render_template('members/new.html')

@members_blueprint.route('/members', methods=['POST'])
def create_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    home_address = request.form['home_address']
    membership_type = request.form['membership_type']
    is_active = request.form['is_active']
    member = Member(first_name, last_name, home_address, membership_type, is_active)
    member_repository.save(member)
    return redirect('/members')

@members_blueprint.route('/members/<id>/edit', methods = ['GET'])
def edit_member(id):
    member = member_repository.select(id)
    return render_template('members/edit.html', member = member)