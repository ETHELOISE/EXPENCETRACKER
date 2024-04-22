from flask import Blueprint ,request
import json

# importing the user controller
from controllers.user import *

user_view = Blueprint("user" ,__name__ ,url_prefix="/user")

@user_view.route("/get-all-user" ,methods=['get'])
def get_all_user():
    return get_user()

@user_view.route("/get-user/<id>" ,methods=['get'])
def get_one_user(id):
    return get_user(id)

@user_view.route("/create-user" ,methods=['POST'])
def create_user():
    print(json.loads(request.data.decode())['name'])
    return "create user"

@user_view.route("/delete_user/<id>" ,methods=['delete'])
def delete_user(id=None):
    return "delte user"