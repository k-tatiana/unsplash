from app import app
from flask import render_template, url_for, json, redirect, flash
from app.forms import SearchForm
import requests

#auth:
USER = 't1nka'
PASS = 'tinkaunsplash'
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
            return redirect(url_for('blog'))
        else:
            flash("No any keyword")
    else:
        flash('No validation')
    form.search.data = ''
    return render_template('index.html', title='Unsplash search', form=form)


@app.route('/api/image/<string:keyword>', methods=['GET'])
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
    return response


@app.route('/api/image/<int:id>', methods=['POST'])
def save_image():
    pass


@app.route('/login')
def login():
    pass

