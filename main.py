from flask import Flask, render_template
from flask_login import LoginManager, login_required, current_user

from data import db_session
from data.input_data import InputData

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(InputData).get(user_id)

@app.route('/home', methods=['GET', 'POST'])
@login_required
def home_screen():
    global var
    if current_user.level_of_access == 0:
        var = current_user._get_current_object().input_data_buyer[0].id
    elif current_user.level_of_access == 1:
        var = current_user._get_current_object().input_data_seller[0].id
    return render_template('home.html', title='Главная страница')