from flask.ext.wtf import Form
from flask import session, request
from wtforms import StringField, SubmitField, PasswordField, TextAreaField 
from wtforms.validators import Required, Email, EqualTo, Length 

# Form on Home page (for email) 
class HomeSignUp(Form):
	BizEmail = StringField('Business/ Organization Email',\
		validators=[Required(), Email()])
	Submit = SubmitField('Register as a new User')

# Form on Sign Up page 
class SignUpForm(Form):
	BizEmail = StringField('Business/Organization Email',\
		validators=[Required(), Email()])
	BizName = StringField('What is the name of your \
		Business/ Organization?',validators=[Required(), \
		Length(min=1, max=60)]) 
	Password = PasswordField('Password', validators=[Required(), \
		EqualTo('ConfirmPassword', message='Passwords must match'), \
		Length(min=2)])
	ConfirmPassword = PasswordField('Re-type Password')
	Submit = SubmitField('Sign Up')
	#PicUpload(Form):

# Form on Request page 
class RequestPost(Form):
	Title = StringField('Give your request a title', \
		validators=[Required()])
	Comment = TextAreaField('Tell us more about your request...',\
		validators=[Required(), Length(min=1, max=1800)])
	# upload photo
	Submit = SubmitField('Post Request')