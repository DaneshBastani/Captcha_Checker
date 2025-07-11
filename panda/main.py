from captcha.image import ImageCaptcha
from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
import random

app = Flask(__name__)
app.config['SECRET_KEY']='secret_key'

#Codefor Captcha
code =['Python123','ALex456','Intro789']
generated_code = random.choice(code)
image = ImageCaptcha(width=200,height=100)
img = image.create_captcha_image(generated_code,color='white',background='black')
img.save('static/image/Python456.jpg')

#Creating the Form
class info(FlaskForm):
    Text = StringField('Enter the Captcha Here')
    Submit = SubmitField('Enter')


@app.route('/',methods=['GET','POST'])
def home():
    form = info()
    return render_template('index.html',form=form)
# img.show()


@app.route('/Login',methods=['GET','POST'])
def login():
    form =info()
    valid = form.Text.data

    if generated_code==valid:

        return render_template('Login.html')
    return 'Please Try Again'
if __name__=='__main__':
    app.run(debug=True)