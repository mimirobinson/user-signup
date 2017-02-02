#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

def buildform():
    #Form that is used to collect data from the user;  Default username and email
    # is blank;  Form will redisplay with username and email if error has been
    #detected
    form = """
    <!DOCTYPE=html>
    <html lang = "en">
        <head>
            <meta charset="utf-8">
            <title>User Signup | LC101</title>
        </head>
        <body>
            <h2>User Signup</h2>
            <form method="post">
                <p>
                    <span><label>User Name:</span>
                    <span><input type='text' name='username' value='%(username)s'></label></span>
                    <span>%(name_error)s</span>
                </p>
                <p>
                    <span><label>Password:</span>
                    <span><input type='password' name='password' value='%(password)s'></label></span>
                    <span>%(password_error)s</span>
                </p>
                <p>
                    <span><label>Verify Password:</span>
                    <span><input type='password' name='verify' value='%(verify)s'></label></span>
                    <span>%(verify_error)s</span>
                </p>
                <p>
                    <span><label>Email(optional):</span>
                    <span><input type='text' name='email' value='%(email)s'></label></span>
                    <span>%(email_error)s</span>
                </p>
                <input type='submit'/>
            </form>
        </body>
    </html>
    """

    return (form)

def buildwelcome(username):
    #Welcome screen that is displayed once user information has been validated
    #and accepted.  Includes the text "Welcome, username"
    header = """
        <!DOCTYPE=html>
        <html lang = "en">
        <head>
            <meta charset="utf-8">
            <title>User Signup | LC101</title>
        </head>
        <body>
            <h2>User Signup</h2>
            <p>Welcome, """
    footer = """
            </p></body></html> """

    return (header + username + footer)

def valid_username(username):
    return USER_RE.match(username)

def valid_password(password):
    return PASSWORD_RE.match(password)

def valid_email(email):
    return EMAIL_RE.match(email)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = buildform()
        self.response.write(content % {"username": "", "name_error": "",
        "password": "", "password_error": "", "verify": "",
        "verify_error": "", "email": "", "email_error": ""})

    def post(self):
        error = ""
        name_error = ""
        password_error = ""
        verify_error = ""
        email_error = ""
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")

        if not valid_username(username):
            name_error = "This is not a valid username."
            error = "Y"
        if password == "":
            password_error = "A password is required."
            error = "Y"
        elif not valid_password(password):
            password_error = "This is an invalid password."
            error = "Y"
        if verify != password:
            verify_error = "The passwords do not match."
            error = "Y"
        if email != "" and not valid_email(email):
            email_error = "This is an invalid email."
            error = "Y"

        if error == "Y":
            password = ""
            verify = ""
            content = buildform()
        else:
            content = buildwelcome(username)

        self.response.write(content % {"username": username, "name_error": name_error,
        "password": password, "password_error": password_error, "verify": verify,
        "verify_error": verify_error, "email": email, "email_error": email_error})

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
