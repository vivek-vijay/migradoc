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
    events = db.relationship('HeadacheEvent', backref='migraineur', lazy=True)
    # medicalHx = db.relationship('MedicalHx', backref='migraineur', lazy=True)

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
        return f"User('{self.username}', '{self.email}')"


"""
class MedicalHx(db.Model):
    pass
    id = db.Column(db.Integer, primary_key=True)
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
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
"""


class HeadacheEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    startDate = db.Column(db.DateTime, nullable=True)
    endDate = db.Column(db.DateTime, nullable=True)
    pain = db.Column(db.Integer)
    nv = db.Column(db.String)
    phonophoto = db.Column(db.String)
    adls = db.Column(db.String)
    period = db.Column(db.String)
    # Null if User.gender = 1 (Male)
    acutetx1 = db.Column(db.String(40), nullable=True)
    acutetx2 = db.Column(db.String(40), nullable=True)
    acutetx3 = db.Column(db.String(40), nullable=True)
    acutetxSuccess = db.Column(db.Integer, nullable=True)
    prophylactic = db.Column(db.String(40), nullable=True)
    prophylacticDose = db.Column(db.String(10), nullable=True)
    triggers = db.Column(db.String(40), nullable=True)
    notes = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"HeadacheEvent('{self.pain}')"


"""
class AcuteTx(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    acutetx = db.Column(db.String)
    dose = db.Column(db.Integer)

    def __repr__(self):
        return f"AcuteTx('{self.acutetx}: {self.dose}')"


class Prophylactic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prophylactic = db.Column(db.String)
    dose = db.Column(db.Integer)

    def __repr__(self):
        return f"Prophylactic('{self.prophylactic}: {self.dose}')"


class PsychScores(db.Model):
    pass
"""
