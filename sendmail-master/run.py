# -*- coding: utf-8 -*-
from flask import Flask, flash, g, abort, render_template, session, request, redirect, url_for
from flask_mail import Message
from flask_mail import Mail
from threading import Thread
from flask import jsonify
from flask import json
import os

app = Flask(__name__)

app.config.update(
    MAIL_SERVER = 'smtp.qq.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = '2950393715',
    MAIL_PASSWORD = 'sblueiiknjsodhdf',
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]',
    FLASKY_MAIL_SENDER = '6760928269@qq.com',
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN'),
    MAIL_DEBUG = True
)
sblueiiknjsodhdf
#IMAP/SMTP授权码：avuxrmesrhvwdffc
#POP3/SMTP：sblueiiknjsodhdf

# app.config['MAIL_SERVER']='smtp.qq.com'
# app.config['MAIL_PORT']=25
# app.config['MAIL_PASSWORD']='**********'


# --- Common utility functions ------------------------------------------------

mail = Mail(app)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        data = json.loads(request.form.get('data'))
        msg = Message(data["name"],sender='676098269@qq.com',recipients=['2950493715@qq.com'])
        msg.body = ""
        msg.html = u"称呼：" + data["name"] + "<br>"+ u"专业："+ data["major"]+ "<br>"  + u"建议："+ data["message"]
        mail.send(msg)
    return render_template('contact.html')
@app.route('/form')
def form():
    return render_template('sign_up.html')
# --- Entry point -------------------------------------------------------------
	
if __name__ == '__main__':
	app.secret_key = os.urandom(24)
	app.run(debug = False)
