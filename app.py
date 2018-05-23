import os

from flask import Flask, jsonify
from proveedor import GoogleLogin, LinkedInLogin, FacebookLogin





os.environ["GOOGLE_LOGIN_CLIENT_ID"] = "364672633912-hbhtatjd9kbkbeaocn0902pivum4t0cd.apps.googleusercontent.com"
os.environ["GOOGLE_LOGIN_CLIENT_SECRET"] = "b_HGPbqiY-gBHSCBuS38fVau"

os.environ["LINKEDIN_LOGIN_CLIENT_ID"] = "-"
os.environ["LINKEDIN_LOGIN_CLIENT_SECRET"] = "-"

os.environ["FACEBOOK_LOGIN_CLIENT_ID"] = "-"
os.environ["FACEBOOK_LOGIN_CLIENT_SECRET"] = "-"




app = Flask(__name__)
app.config.update(
  SECRET_KEY="x34sdfm34",
)



for config in (
  "GOOGLE_LOGIN_CLIENT_ID",
  "GOOGLE_LOGIN_CLIENT_SECRET",
  "LINKEDIN_LOGIN_CLIENT_ID",
  "LINKEDIN_LOGIN_CLIENT_SECRET",
  "FACEBOOK_LOGIN_CLIENT_ID",
  "FACEBOOK_LOGIN_CLIENT_SECRET"

):app.config[config] = os.environ[config]




google_login = GoogleLogin(app)
linkedin_login = LinkedInLogin(app)
facebook_login = FacebookLogin(app)




@app.route("/")
def index():
  return """
<html>
<a href="{}">Login con con cuenta de Google </a><br>
<a href="{}">Login con Linkedin</a> <br>
<a href="{}">Login con Facebook</a> <br>
""".format(google_login.authorization_url(), linkedin_login.authorization_url(), facebook_login.authorization_url())


@google_login.login_success
def login_success(token, profile):
  return jsonify(token=token, profile=profile)

@google_login.login_failure
def login_failure(e):
  return jsonify(error=str(e))

@linkedin_login.login_success
def login_success(token, profile):
  return jsonify(token=token, profile=profile)

@linkedin_login.login_failure
def login_failure(e):
  return jsonify(error=str(e))
  
@facebook_login.login_success
def login_success(token, profile):
  return jsonify(token=token, profile=profile)

@facebook_login.login_failure
def login_failure(e):
  return jsonify(error=str(e))


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
