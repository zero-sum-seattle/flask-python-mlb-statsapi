"""General page routes."""
from flask import Blueprint
# from flask import current_app as app
from flask import render_template
import requests


# Blueprint Configuration
beta_bp = Blueprint(
    "beta_bp", __name__, template_folder="templates", static_folder="static"
)


@beta_bp.route("/", methods=["GET"])
def home():
    """beta."""

    data = requests.get(url='https://statsapi.mlb.com/api/v1/teams?leagueIds=104').json()

    return render_template(
        "index.jinja2",
        title="Flask Beta Demo",
        subtitle="Beta in action.",
        template="beta-template",
        data=data['teams']        
    )