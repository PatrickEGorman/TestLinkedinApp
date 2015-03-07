# Example routing rule
# api_routes = {
#     'rules': [
#         ##### Node settings #####
#         Rule(
#             ['urls'],
#             'request type',
#             methods,
#             json_renderer,
#             additional arguments
#         )
#     ]
# }


import requests
from . import app, login_manager
from .model import User, users
from .utils import valid_user_input_check
from .views import auth
from bson.objectid import ObjectId
from flask import request, redirect
from flask.ext.login import login_user, current_user
from mako.template import Template


#redirect user to sign into account
@app.route("/link_account")
def link_account():
    return auth.authorization_request()


#get user token used for authenticated requests
@app.route("/linkedin/", methods=["GET", "POST"])
def linkedin():
    return auth.get_token()


@app.route("/share/<post_request>", methods=["GET", "POST"])
def share(post_request):
    access_token = post_request.args.get('access_token')
    current_user.set_access_token(access_token)
    return auth.share_comment()


#Settup for test app


@login_manager.user_loader
def load_user(userid):
    return users.find_one({"_id": ObjectId(userid)})


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if request.form["type"] == "login":
            validity_check = valid_user_input_check(request.form["username"], request.form["password"])
            if validity_check:
                return Template(filename='addon/templates/linkedin_home.mako').render(
                    flashed_messages=validity_check)
            else:
                user = User(
                    username=request.form["username"],
                    password=request.form["password"])
                login_user(user)
                return redirect("/link_account")
        elif request.form["type"] == "create":
            validity_check = valid_user_input_check(request.form["username"], request.form["password"])
            if validity_check:
                return Template(filename='addon/templates/linkedin_home.mako').render(
                    flashed_messages=validity_check)
            else:
                user = User(
                    username=request.form["username"],
                    password=request.form["password"])
                user.add_to_db()
                login_user(user)
                return redirect("/link_account")
    return Template(filename='addon/templates/linkedin_home.mako').render()