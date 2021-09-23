from django.shortcuts import render
import random

def fristpage(request):
    return render(request,'genrator/fristpage.html')

def password(request):
    ch_pass = list("abcdefghijklmnopwquerstyz")
    if request.GET.get('upper'):
        ch_pass.extend(list('ABCDEFGHIJKLMNOPQUERSTWXZ'))
    if request.GET.get('symbol'):
        ch_pass.extend(list('!@#$%^&*()_+-'))
    if request.GET.get('numbers'):
        ch_pass.extend(list('1234567890'))
    
    the_password = ""
    lenght = int(request.GET.get('Length'))
    for i in range(lenght):
        the_password += random.choice(ch_pass)
        
    return render(request,'genrator/password.html',{'the_password':the_password})