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

def buildpage(username="", email=""):
    header = """
        <!DOCTYPE=html>
        <html lang = "en">
        <head>
            <meta charset="utf-8">
            <title>User Signup | LC101</title>
        </head>
        <body>
            <h2>User Signup</h2>
            <form method="post">"""
    username = "<p><label>User Name<input type='text' name='username' value='" + username + "'>'</label><p>"
    password = "<p><label>Password<input type='password' name='password'></label</div></p>"
    verify = "<p><label>Verify Password<input type='password' name='verify'></label></p>"
    email = "<p><label>Email (optional)<input type='text' name='email' value='" + email +"'></label></p>"
    submission = "<input type='submit'/>"
    footer = "</form></body></html>"

    return (header + username + password + verify + email +
        submission + footer)

def buildwelcome(username):
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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = buildpage()
        self.response.write(content)

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")

        #content = buildpage(username, email)
        content = buildwelcome(username)
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
