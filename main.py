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

def buildpage(submission_content):
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
    user_name_input = "<p><label>User Name<input type='text' name='user_name'></label><p>"
    password_input = "<p><label>Password<input type='password' name='password'></label</div></p>"
    password_verify = "<p><label>Verify Password<input type='password' name='password_v'></label></p>"
    email_input = "<p><label>Email (optional)<input type='text' name='email'></label></p>"
    submission = "<input type='submit'/>"
    footer = "</form></body></html>"

    return (header + user_name_input + password_input + password_verify + email_input +
        submission + footer)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = buildpage("")
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
