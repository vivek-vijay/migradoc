from datetime import date
from md_app import db, login_manager
from flask import current_app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serialiser


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    # age = db.Column(db.Integer, nullable=False, default=0)
    gender = db.Column(db.Integer, nullable=False, default=0)
    diagnosis = db.Column(db.Integer, nullable=False, default=0)
    # 0=no confirmed dx, 1=episodic migraine w/ aura etc., as dropdown?
    diagnosisDate = db.Column(db.DateTime, nullable=True)
    # ageOnset = db.Column(db.Integer, nullable=False, default=age)
    acuteTherapy = db.Column(db.Integer, nullable=False, default=0)
    # 0=none, 1=paracetamol only, 2=NSAID only etc. as a check-box?
    prophylacticCurrent = db.Column(db.Integer, nullable=False, default=0)
    # Dropdown list each associated with an integer e.g. none=0, amitript=1
    prophylacticStart = db.Column(db.DateTime, nullable=True)
    prophylacticPast = db.Column(db.String(20), nullable=True)
    # amitriptyline = 1 etc. able to select multiple (e.g. check-box) and
    # stored as string of integers?
    comorbidities = db.Column(db.Integer, nullable=False, default=0)
    # 0 = nil, chronic pain conditions = 1, chronic medical conditions = 3,
    # psychiatric co-morbidities = 2. Check-box and stored as string?
    smoker = db.Column(db.Integer, nullable=False, default=0)
    # 0 = non/ex-smoker, 1 = current smoker
    familyhx = db.Column(db.Integer, nullable=False, default=0)
    # 0 = no fhx, 1 = positive fhx
    events = db.relationship('HeadacheEvent', backref='migraineur', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serialiser(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serialiser(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.diagnosis}')"


class HeadacheEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=date.today)
    pain = db.Column(db.Integer, nullable=False)
    # 0-10 scale
    nv = db.Column(db.String, nullable=False)
    # 0 = neither, 1 = nausea, 2 = vom, 3 = both
    phonophoto = db.Column(db.String, nullable=False)
    # 0 = neither, 1 = phono, 2 = photo, 3 = both
    adls = db.Column(db.String, nullable=False, default="Able to continue with activities")
    # 0 = not affected, 1 = interrupted
    period = db.Column(db.String, nullable=True, default="Not within -2 to +3 days of start of period")
    # Null if User.gender = 1 (Male)
    # 0 = , 1 = within
    acutetx = db.Column(db.String, nullable=False)
    # 0=none, 1=paracetamol only, 2=NSAID only etc. as a dropdown?
    prophylactic = db.Column(db.String, nullable=False, default=0)
    # default=User.prophylacticCurrent
    prophylacticDose = db.Column(db.Integer, nullable=True)
    triggers = db.Column(db.Integer, nullable=False)
    # Potential triggers, 0=nil, 1=disturbed sleep etc.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"HeadacheEvent('{self.date}')"
