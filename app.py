import os
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# print(os.environ['APP_SETTINGS'])


@app.route("/")
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/upload-image')
def upload_show():
    return render_template("upload_image.html")


@app.route('/upload-image', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        image = request.files['image']
        target = os.path.join(APP_ROOT, 'image_uploads/')
        print(target)
        destination = "/".join([target, image.filename])
        print(destination)
        image.save(destination)
        print('Image saved')
    return render_template("uploaded.html")


if __name__ == '__main__':
    app.run()
