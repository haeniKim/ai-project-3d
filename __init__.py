from flask import Flask
from views import main_views, tutor_views

app = Flask(__name__)

app.register_blueprint(main_views.bp)
#app.register_blueprint(tutor_views.bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, debug = True)