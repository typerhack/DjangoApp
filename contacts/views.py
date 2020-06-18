from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.
def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_id = request.POST['user_id']
        phone = request.POST['phone']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['messagetxt']

        contact_temp = Contact(first_name=first_name, last_name=last_name, phone=phone, email=email, subject=subject,
                               message=message, user_id=user_id)

        contact_temp.save()

        # Send notification mail to user
        send_mail(
            f'اطلاعات فرم تماس موضوع: {subject}',
            f'سلام،\nدرخواست شما ثبت شده است. بزودی از طرف کارشناسان ما با شما تماس گرفته خواهد شد\n.'
            f'----------------------------------------------\n'
            f'متن پیام:\n'
            f'{message}',
            'hybevo@gmail.com',
            [email],
            fail_silently=False,
        )

        send_mail(
            f'اطلاعات فرم تماس موضوع: {subject}',
            f'سلام،\nدرخواست تماس با مشخصات زیر ثبت شده است. لطفا پیگیری بفرمایید.\n.'
            f'----------------------------------------------\n'
            f'فرستنده: {first_name} {last_name}\n'
            f'متن پیام:\n'
            f'{message}',
            'hybevo@gmail.com',
            ['hybevo@gmail.com'],
            fail_silently=False,
        )

        # Send notification mail to staff

        messages.success(request, 'پیام شما دریافت شد. در اسرع وقت با شما تماس خواهیم گرفت')
        return redirect('contact')
    else:
        return render(request, 'contacts/contact.html')
