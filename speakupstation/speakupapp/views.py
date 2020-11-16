from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
from django.core.paginator import Paginator, EmptyPage
# Create your views here.


def home(request):
    result = homePage1.objects.all()
    return render(request, 'html Files/homePage.html', {'result': result})


def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['conpassword']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'html Files/logAndSign.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password'])
                return redirect(home)
        else:
            return render(request, 'html Files/logAndSign.html', {'error': 'password does not matched'})
    else:
        return render(request, 'html Files/logAndSign.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect(home)
        else:
            return render(request, 'html Files/logAndSign.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'html Files/logAndSign.html')


def logout(request):
    auth.logout(request)
    return redirect(home)


def tologAndSign(request):
    return render(request, 'html Files/logAndSign.html')


def myCourse(request):
    return render(request, 'html Files/myCourses.html')


def profile(request):
    return render(request, 'html Files/profile.html')


def settings(request):
    return render(request, 'html Files/settings.html')


def allCourses(request):
    return render(request, 'html Files/allCourses.html')


def coursePage1(request):
    res1 = coursePage.objects.all()
    res2 = seperateId.objects.all()
    coursesName = homePage1.objects.all()
    return render(request, 'html Files/coursePage.html', {'fetcher1': res1, 'fetcher2': res2, 'fetcher3': coursesName})


def showlesson(request):
    # res = lesson1.objects.all()

    # aka1 = lesson1.objects.values_list("translator_sentence", flat=True)
    # akac1 = list(aka1)
    # aka2 = lesson1.objects.values_list("translated_sentence", flat=True)
    # akac2 = list(aka2)

    catCat1 = category1.objects.all()
    sptID = seperateId.objects.all()
    res = lesson1.objects.all()
    p = Paginator(res, 1)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    return render(request, 'html Files/lesson.html', {'fetcher4': page, 'fetcher5': catCat1, 'fetcher6': sptID})
