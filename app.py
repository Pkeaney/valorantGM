##Main script to start up the Flask process, will run on default port 5000

from flask import Flask

from extensions import db

from routes.simulation import sim_bp


def create_app():

    app = Flask(__name__)


##DATABASE CONFIGURATION

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "postgresql://postgres:pk123@localhost:5432/valorant_manager"
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


## INITIALISE EXTENSIONS and FLASK app

    db.init_app(app)

## REGISTER ROUTES (BLUEPRINTS)

    app.register_blueprint(sim_bp)

    return app


## RUN SERVER

if __name__ == "__main__":

    app = create_app()
    app.run(debug=True)
