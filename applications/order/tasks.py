from django.core.mail import send_mail
from udemy.celery import app

@app.task
def send_confirmation_code(email, code):
    full_link = f'Tap this -> http://localhost:8000/api/v1/order/confirm/{code}'      
    send_mail(
        f'Order confirm',
        f'Please click link to confirm order:  {full_link}',
        'dcabatar@gmail.com',
        [email]
    )
    
    