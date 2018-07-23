# -*- coding: utf-8 -*-
from app import app, db
from flask import render_template, url_for, json, redirect, flash
from app.forms import SearchForm
import requests
from app.models import Images
from urllib.parse import unquote

#auth:
API_URL = 'https://api.unsplash.com'
ADD_URL = '/search/photos'
PER_PAGE = 100
ACCESS_KEY = '6bf8a59262a3b7b30b735c0abf99721529f1ecb028d04d10ea7a0468400a0816'
SECRET_KEY = '5b5604f792805ee3e5fe48770490d325114cacb6a243b689a0e895d2b8a65876'
URI = 'urn:ietf:wg:oauth:2.0:oob'


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        keyword = form.search.data
        if keyword is not None:
            return redirect(url_for('search_image', keyword=keyword))
        else:
            flash("No any keyword")
    form.search.data = ''
    return render_template('index.html', title='Unsplash search', form=form)


@app.route('/api/image/<string:keyword>', methods=['GET', 'POST'])
def search_image(keyword):
    headers = {'Authorization': 'Client-ID {access_token}'.format(access_token=ACCESS_KEY)}
    url = API_URL + ADD_URL + '?per_page=' + str(PER_PAGE) + '&query=' + keyword
    request_result = requests.get(url=url, headers=headers)
    result = request_result.json()  # или можно json.loads(request_result.text)
    response = app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )
    return render_template('keyword.html', title='Images', entries=result['results'])


@app.route('/api/image/favorites/add/<string:image_url>', methods=['GET', 'POST'])
def save_image(image_url):
    Images.add_image(image_url)
    db.session.commit()


@app.route('/api/image/favorites/delete', methods=['POST'])
def delete_image(image_url, charset='utf-8'):
    Images.remove_image(unquote(image_url))
    db.session.commit()


@app.route('/favorites')
def favorites():
    images = Images.favorites
    return render_template('favorites.html', favotites=images, title='Favorite images')


