from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators = [InputRequired()] ,)
    species = SelectField("Species", choices = [("Cat", "cat"), ("Dog", "dog"), ("Porcupine", "porcupine")],)
    photo_url = StringField("Photo URL", validators = [Optional(), URL()],)
    age = IntegerField("Age", validators = [Optional(), NumberRange(min=0, max=30)],)
    notes = TextAreaField("Notes", validators = [Optional(), Length(min = 20)],)

class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL", validators = [Optional(), URL()],)
    notes = TextAreaField("Notes", validators = [Optional(), Length(min = 20)],)
    available = BooleanField("Available")