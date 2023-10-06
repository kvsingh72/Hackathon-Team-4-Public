import os
from flask import Flask, jsonify, Response, render_template


def create_app():
    app = Flask(__name__)

    # Error 404 handler
    @app.errorhandler(404)
    def resource_not_found(e):
        return jsonify(error=str(e)), 404

    # Error 405 handler
    @app.errorhandler(405)
    def resource_not_found(e):
        return jsonify(error=str(e)), 405

    # Error 401 handler
    @app.errorhandler(401)
    def custom_401(error):
        return Response("API Key required.", 401)

    @app.route("/")
    def home():
        return render_template('home.html')

    @app.route("/bronco_sport_2021_ignition")
    def bronco_sport_ignition():
        return render_template('bronco_sport_2021_ignition.html')

    return app


app = create_app()

if __name__ == "__main__":
    print(" Starting app...")
    app.run(host="0.0.0.0", port=5000)