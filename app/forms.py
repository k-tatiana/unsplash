from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    search = StringField('Поиск картинок', validators=[DataRequired()])
    submit = SubmitField('Найти')
