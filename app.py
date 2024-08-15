from flask import Flask, render_template, request, redirect
# from flask_sslify import SSLify

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='')
# sslify = SSLify(app)

# If you have SSL
"""
@app.before_request
def force_https():
    if not request.is_secure:
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)
"""


@app.route('/')
def hello_world():  # put application's code here
    return render_template("ui.html")


if __name__ == '__main__':
    app.run()
