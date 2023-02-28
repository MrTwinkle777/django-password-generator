from django.shortcuts import render
import random


# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters_list = list('abcdefghijklmnopqrstuvwxyz')
    upper_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    special_list = list('!@#$%^&*()_+')
    numbers_list = list('1234567890')

    if request.GET.get('uppercase'):
        characters_list.extend(upper_list)
    if request.GET.get('special'):
        characters_list.extend(special_list)
    if request.GET.get('numbers'):
        characters_list.extend(numbers_list)

    length = int(request.GET.get('length', 8))

    the_password = ''
    for x in range(length):
        the_password += random.choice(characters_list)

    while True:
        flag = True
        if request.GET.get('uppercase'):
            if set(upper_list).intersection(the_password):
                pass
            else:
                flag = False
        if request.GET.get('special'):
            if set(special_list).intersection(the_password):
                pass
            else:
                flag = False
        if request.GET.get('numbers'):
            if set(numbers_list).intersection(the_password):
                pass
            else:
                flag = False
        if flag:
            break
        the_password = ''
        for x in range(length):
            the_password += random.choice(characters_list)

    return render(request, 'generator/password.html', {'password': the_password})
