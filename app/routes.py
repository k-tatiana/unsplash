from app import app
from flask import render_template, url_for
from app.forms import SearchForm


@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    form = SearchForm()
    return render_template('index.html', title='Unsplash search', form=form)


@app.route('/image/<string:keyword>', methods=['GET'])
def search_image():
    pass


@app.route('/image/<int:id>', methods=['POST'])
def save_image():
    pass


