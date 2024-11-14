from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL, NumberRange


class CreateForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    map_url = StringField("map Url", validators=[DataRequired(), URL()])
    img_url = StringField("Image URL", validators=[DataRequired(), URL()])
    location = StringField("Location", validators=[DataRequired()])
    has_sockets = StringField("has sockets", validators=[DataRequired(), NumberRange(min=0, max=1)])
    has_toilet = StringField("has toilet", validators=[DataRequired(), NumberRange(min=0, max=1)])
    has_wifi = StringField("has wifi", validators=[DataRequired(), NumberRange(min=0, max=1)])
    can_take_calls = StringField("can take calls", validators=[DataRequired(), NumberRange(min=0, max=1)])
    seats = StringField("Seats", validators=[DataRequired()])
    coffee_price = StringField("coffee price", validators=[DataRequired()])
    submit = SubmitField("Submit Cafe")
