from flask import Flask, render_template, jsonify


def create_app():
    app = Flask(__name__)

    parts = {
        'lowpressure': {
            'name': 'Low Tire Pressure Warning',
            'image': 'lowpressure.jpg',
            'description': 'This illuminates when your tire pressure is low. If the lamp remains on with the engine '
                           'running or when driving, check your tire pressure as soon as possible. It will also '
                           'illuminate momentarily when you switch the ignition on to confirm the lamp is functional. '
                           'If it does not illuminate when you switch the ignition on, or begins to flash at any '
                           'time, have the system checked by your authorized dealer.'
        },
        'autolamps': {
            'name': 'Autolamps',
            'image': 'autolamps.jpg',
            'description': 'When the lighting control is in the autolamps position, the headlamps turn on in low '
                           'light situations, or when the wipers turn on. The headlamps remain on for a period of '
                           'time after you switch the ignition off. Use the information display controls to adjust '
                           'the period of time that the headlamps remain on.'
        },
        'meme': {
            'name': 'Meme',
            'image': 'meme.jpg',
            'description': 'The world\'s greatest meme, guaranteed.'
        }
    }

    # a simple response that returns OK
    @app.route('/')
    def send_ok():
        return render_template("index.html")

    @app.route('/qr')
    def qr():
        return render_template("qr.html")

    @app.route('/details')
    def details():
        return render_template("details.html")

    @app.route('/scans')
    def scans():
        return render_template("scans.html")

    @app.route('/parts/<part>', methods=['GET'])
    def disp(part):
        data = {
            'name': parts[part]["name"],
            'image': parts[part]["image"],
            'description': parts[part]["description"]
        }

        return jsonify(data)

    return app


app = create_app()

if __name__ == "__main__":
    print(" Starting app...")
    app.run(host="0.0.0.0", port=5000)