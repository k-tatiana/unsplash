# -*- coding: utf-8 -*-
from app import app, db
from flask import render_template, url_for, json, redirect, flash
from app.forms import SearchForm
from app.models import Images, User
from urllib.parse import unquote
import requests
import config

#auth:
API_URL = 'https://api.unsplash.com'
ADD_URL = '/search/photos'
PER_PAGE = 100
ACCESS_KEY = '6bf8a59262a3b7b30b735c0abf99721529f1ecb028d04d10ea7a0468400a0816'
SECRET_KEY = '5b5604f792805ee3e5fe48770490d325114cacb6a243b689a0e895d2b8a65876'
URI = 'urn:ietf:wg:oauth:2.0:oob'
config.FAVORITE = Images.query.all()


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
    config.SEARCH_RESULT = result['results']
    config.SEARCH_HIST.append(config.SEARCH_RESULT)

    print(config.FAVORITE)
    id_list = []
    for entry in config.FAVORITE:
        id_list.append(entry.image_id)
    print(id_list)
    return render_template('keyword.html', title='Images',
                           entries=config.SEARCH_RESULT, favorite=id_list)


@app.route('/api/image/favorites/add', methods=['POST', 'GET'])
def save_image():
    """Получаем запрос на добавление картинки, добавляем в базу новую картинку,
    отрисовываем фронт с изменением текста кнопки"""
    from flask import request
    img = {'image_id': request.form['image_id'], 'image_url': request.form['image_url'],
           'image_desc': request.form['description'], 'image_full': request.form['image_full']}
    imgs = Images(**img)
    db.session.add(imgs)
    db.session.commit()
    config.FAVORITE = Images.query.all()
    return render_template('keyword.html',
                           title='Images',
                           entries=config.SEARCH_RESULT,
                           favorite=config.FAVORITE)


@app.route('/api/image/favorites/delete', methods=['POST'])
def delete_image():
    from flask import request
    img = Images.query.filter_by(image_url=request.form['image_url']).first_or_404()
    db.session.delete(img)
    db.session.commit()
    favorite = Images.query.all()
    return render_template('keyword.html', title='Images', entries=config.SEARCH_RESULT, favorite=config.FAVORITE['image_url'])


@app.route('/favorites')
def favorites():
    images = Images.query.all()
    return render_template('favorites.html', title='Favorites', images=images)

@app.route('/last_search')
def last_search():
    return render_template('keyword.html', title='Images', entries=config.SEARCH_RESULT)

@app.route('/login')
def login():
    return redirect('portfolio.html'#, form=form
                    )
