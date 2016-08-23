import webapp2
import cgi
from caesar import encrypt

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Caesar</title>
    <style type="text/css">
        .error {
            color: red;
        }
        form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
        textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        h1 {
                text-align: center;
            }
    </style>
</head>
<body>
    <h1>Caesar</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""
text=""
cypher_form = """
<form action="/" method="post">
    <label>
    Rotate by:
    </label>
    <input type="text" name="rot" value="0"/>
    <textarea type="text" name="text">{0}</textarea>
    <br>
    <input type="submit"/>
    </form>
"""

class Index(webapp2.RequestHandler):
    def get(self):
        response = page_header + cypher_form.format("") + page_footer
        self.response.write(response)

    def post(self):
        rotate = int(self.request.get("rot"))
        text = self.request.get("text")
        text_escaped = cgi.escape(text, quote=True)
        text_crypt = encrypt(text_escaped, rotate)
        response = page_header + cypher_form.format(text_crypt) + page_footer
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
