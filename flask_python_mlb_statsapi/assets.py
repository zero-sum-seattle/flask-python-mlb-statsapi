"""Compile static assets."""
from flask import current_app as app
from flask_assets import Bundle


def compile_static_assets(assets):
    """Create stylesheet bundles."""
    assets.auto_build = True
    assets.debug = False
    # common_style_bundle = Bundle(
    #     "src/less/*.less",
    #     filters="less,cssmin",
    #     output="dist/css/style.css",
    #     extra={"rel": "stylesheet/less"},
    # )
    # beta_style_bundle = Bundle(
    #     "home_bp/less/home.less",
    #     filters="less,cssmin",
    #     output="dist/css/home.css",
    #     extra={"rel": "stylesheet/less"},
    # )
    
    # assets.register("beta_style_bundle", beta_style_bundle)
    # if app.config["FLASK_ENV"] == "development":
    #     common_style_bundle.build()
    #     beta_style_bundle.build()        
    return assets