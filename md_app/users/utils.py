from flask import url_for
from md_app import mail
from flask_mail import Message


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password reset request', sender='noreply@demo.com', recipients=[user.email])
    msg.body = f'''
To reset your password, visit the following link:
{url_for('users.password_reset', token=token, _external=True)}
If you did not request this password reset email, please ignore this email and no changes will be made
    '''
    mail.send(msg)
