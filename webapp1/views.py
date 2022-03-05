from django.shortcuts import render, redirect
from .models import Verifica_Risultati_Candidato, Esami_sostenuti_e_relativi_esiti
# Create your views here.
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def check_auth(request):
    if request.user.is_authenticated:
        return True
    else:
        return False

def student_page(request):
    mtr = request.GET.get('mtr')
    get_student =  Verifica_Risultati_Candidato.objects.get(MATRICOLA=mtr)
    all_Esami_sostenuti_e_relativi_esiti  = Esami_sostenuti_e_relativi_esiti.objects.filter(Student = get_student)
    context = {'get_student':get_student, 'all_Esami_sostenuti_e_relativi_esiti':all_Esami_sostenuti_e_relativi_esiti}
    return render(request, 'student_page.html', context)



def adminlogin(request):
    if request.user.is_authenticated:
        return redirect('/adminpage/')
    else:
        if request.method == "GET":
            return render(request, 'loginpage.html')
        else:
            log_username = request.POST['username']
            log_password = request.POST['password']
            # this is for authenticate username and password for login
            user = authenticate(username=log_username, password=log_password)
            if user is not None:
                login(request, user)
                return redirect('/adminpage/')
            else:
                messages.error(request, "Invalid Credentials, Please Try Again !!")
                return render(request, 'loginpage.html')