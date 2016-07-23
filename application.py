from flask import Flask, render_template, request
# from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route("/")
def index_page():
    """Show an index page."""

    return "<html><body>This is the homepage.</body></html>"


@app.route("/application-form")
def form_page():
    """Show application form."""

    return render_template("application-form.html")


@app.route("/application", methods=['POST'])
def submission_response():
    """Show form submission confirmation."""

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    salary = request.form.get('salary')
    job = request.form.get('job')

    return render_template("application-response.html",
                            job=job,
                            last_name=last_name,
                            salary=salary,
                            first_name=first_name)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(host="0.0.0.0", port=6969)
