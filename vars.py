from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor, CKEditorField, upload_fail, upload_success
import os
from flask_login import LoginManager, login_user, login_required, current_user, logout_user

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:11111111@localhost/congac'
app.config['SECRET_KEY'] = "aadadfasdasd"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:11111111@localhost/congac'
app.config['ALLOWED_CONTENT'] = True
app.config['CKEDITOR_FILE_UPLOADER'] = 'upload'
# app.config['CKEDITOR_ENABLE_CSRF'] = True  # if you want to enable CSRF protect, uncomment this line
app.config['UPLOADED_PATH'] = os.path.join(basedir, 'uploads')
app.config['CKEDITOR_PKG_TYPE'] = 'full'

db = SQLAlchemy(app) 
ckeditor = CKEditor(app)
#ckeditor.config['allowedContent'] = True

