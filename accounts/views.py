from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']
        email = request.POST['email']
        mobile = request.POST['mobile']
        job = request.POST['job']
        degree = request.POST['degree']
        major = request.POST['major']
        university = request.POST['university']
        student_id_card = request.POST['student-id-card']
        newsletter = request.POST.get('newsletter', '') == 'on'
        student = request.POST.get('student', '') == 'on'

        # Check if passwords match
        if password == repassword:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'این نام کاربری قبلا استفاده شده است.')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'این ایمیل قبلا استفاده شده است.')
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username, email=email, password=password,
                                                    first_name=first_name, last_name=last_name)
                    # ------------------------- Log in after register
                    # auth.login(request, user)
                    # messages.success(request, 'شما وارد شدید')
                    # return redirect('index')
                    # -------------------------
                    user.save()
                    messages.success(request, 'شما عضو شدید')
                    return redirect('login')
        else:
            messages.error(request, "رمز عبور با تکرار آن همخوانی ندارد")
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'شما با موفقیت وارد شدید')
            return redirect('dashboard')
        else:
            messages.error(request, 'نام کاربری یا رمز عبور شما مطابقت ندارد.')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "شما از فضای کاربری خارج شدید")
        return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
