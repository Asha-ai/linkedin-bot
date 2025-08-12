from flask import Flask, request, redirect
import requests
import os

app = Flask(__name__)

CLIENT_ID = os.getenv("LINKEDIN_CLIENT_ID")
CLIENT_SECRET = os.getenv("LINKEDIN_CLIENT_SECRET")
REDIRECT_URI = os.getenv("LINKEDIN_REDIRECT_URI")

@app.route("/")
def home():
    return f'<a href="https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope=r_liteprofile%20r_emailaddress%20w_member_social">Login with LinkedIn</a>'

@app.route("/callback")
def callback():
    code = request.args.get("code")
    token_url = "https://www.linkedin.com/oauth/v2/accessToken"
    payload = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    r = requests.post(token_url, data=payload)
    return r.json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
