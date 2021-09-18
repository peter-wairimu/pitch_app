from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class ReviewForm(FlaskForm):

 title = StringField('Review title',validators=[Required()])

 review = TextAreaField('Movie review')

 submit = SubmitField('Submit')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Who are You?.',validators = [Required()])
    submit = SubmitField('submit')

class PitchForm(FlaskForm):
  title = StringField('Pitch title',validators=[Required()])
  category = SelectField("Choose Category",choices=[('Gr8','Gr8'),('Products','Products'),('Production','Production')])
  pitch = TextAreaField('Your Pitch',validators=[Required()])
  submit = SubmitField('Submit')


class CommentForm(FlaskForm):
  comment = TextAreaField('Your Comment',validators=[Required()])
  submit = SubmitField('Submit') 