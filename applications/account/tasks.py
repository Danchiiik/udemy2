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
def send_password_confirm_code(email, code):
    send_mail(
        'Password recovery',
        f'Copy this code -> {code}',
        'dcabatar@gmail.com',
        [email],
    )
