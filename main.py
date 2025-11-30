from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

#setting up flask stuff
app = Flask(__name__)
app.config['SECRET_KEY'] = 'joemamadeeznutz'

#flask form class stuff
class InfoForm(FlaskForm):
    link = StringField("Please enter your item link", validators=[DataRequired()])
    email = StringField("Please enter your email", validators=[DataRequired(), Email()])
    submit = SubmitField()

@app.route('/', methods=['GET', 'POST'])
def index():
    link = None
    email = None
    form = InfoForm()
    if form.validate_on_submit():
        link = form.link.data
        email = form.email.data
        form.link.data = ''
        form.email.data = ''
    return render_template('index.html', link=link, email=email, form=form)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/test')
def test():
    yo = 'Whats up'
    return render_template("test.html", yo=yo)

if __name__ == '__main__':
    app.run(debug=True)