from django.core.mail import send_mail
from udemy.celery import app


@app.task    
def send_act_code(email, code):
    link = f'http://localhost:8000/api/v1/account/activate/{code}'
    send_mail(
        'Your user activation code',
        f'Tap this -> {link}',
        'dcabatar@gmail.com',
        [email]    
    )
    

@app.task    
def send_mentor_act_code(email, code):
    link = f'http://localhost:8000/api/v1/account/mentor/activate/{code}'
    send_mail(
        'Your mentor activation code',
        f'Tap this -> {link}',
        'dcabatar@gmail.com',
        [email]    
    )
    
    
@app.task    
def send_password_confirm_code(email):
    full_link = 'http://localhost:8000/api/v1/account/forgot_password_finish/'
    send_mail(
        'Password recovery',
        f'Tap this link-> {full_link}',
        'dcabatar@gmail.com',
        [email],
    )
