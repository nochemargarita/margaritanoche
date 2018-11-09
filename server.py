from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """Homepage."""
    return render_template('homepage.html')

@app.route('/about')
def about_me():
    """Display about Margarita."""

    return render_template('about.html')

if __name__ == "__main__":

    app.debug = False

    # make sure templates, etc. are not cached in debug mode
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.jinja_env.auto_reload = app.debug

    # disable intercept redirects
    # app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    # Use the DebugToolbar
    DebugToolbarExtension(app)



    app.run(host="0.0.0.0")