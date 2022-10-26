"""General page routes."""
from flask import Blueprint
from flask import render_template
import requests


# Blueprint Configuration
home_bp = Blueprint(
    "home_bp", __name__, template_folder="templates", static_folder="static"
)


@home_bp.route("/", methods=["GET"])
def home():
    """Home."""

    data = requests.get(url='https://statsapi.mlb.com/api/v1/teams?leagueIds=104').json()

    return render_template(
        "home.jinja2",
        title="Home",
        # subtitle="Beta in action.",
        template="home-template",
        data=data['teams']        
    )