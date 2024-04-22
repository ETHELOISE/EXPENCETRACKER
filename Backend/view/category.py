from flask import Blueprint

# category controller
from controllers.category import *

category_view = Blueprint("category" ,__name__ ,url_prefix="/category")

@category_view.route("/get-all-category" ,methods=['get'])
def get_all_category():
    return get_category()

@category_view.route("/create-category" ,methods=['post'])
def create_category():
    return "create category"

@category_view.route("/delete_category" ,methods=['delete'])
def delete_category():
    return "delte category"