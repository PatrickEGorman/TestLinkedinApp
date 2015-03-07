import os
import requests
from flask import redirect, request, url_for
from flask.ext.login import current_user
from mako.template import Template
from ..exceptions import InvalidStateVariableException


def authorization_request():
    get_data = {
        "response_type": "code",
        "client_id": os.environ["API_KEY"],
        "redirect_uri": "http://127.0.0.1:5000/linkedin",
        "state": os.environ["STATE"]
    }
    get_request = requests.get('https://www.linkedin.com/uas/oauth2/authorization', data=get_data)
    return redirect(url_for('/share', get_request=get_request))


def get_token():
    code = request.args.get('code')
    state = request.args.get('state')
    if state == os.environ["STATE"]:
        post_data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": "http://127.0.0.1:5000/linkedin",
            "client_id": os.environ["API_KEY"],
            "client_secret": os.environ["API_SECRET"]
        }
        post_request = requests.post("https://www.linkedin.com/uas/oauth2/accessToken", data=post_data)
        return redirect(url_for('/share', post_request=post_request))
    raise InvalidStateVariableException


def share_comment():
    if request.method == "POST":
        comment = request.form["comment"]
        share_post_request = {
            "Host": "api.linkedin.com",
            "Connection": "Keep-Alive",
            "Authorization": current_user.access_token,
            "content":{
                "title": "test share",
                "description": "linkedin app test by Patrick Gorman"
            },
            "comment": comment,
            "visibility": {
                "code": "anyone"
            }
        }
        share_post = requests.post("https://api.linkedin.com/v1/people/~/shares?format=json", data=share_post_request)
        return share_post.text
    return Template("addon/templates/simple_share.mako").render()