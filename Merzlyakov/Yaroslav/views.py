







































































































































































from django.shortcuts import render
from django.http import HttpResponse

def index(request,full_name,age,interests):
    return HttpResponse(f'''
    <h2>Я {full_name}</h2>
    <p>Мне {age} лет</p>
    <p>И мне нравиться {interests}</p>
    <a href = '/about/'>Обо мне</a>    
    <a href = '/contacts/'>Мои контакты</a>    

    ''')
def about(request,arrived, performance,desire):
    return HttpResponse(f'''
    <h2>Я приехал из{arrived}</h2>
    <p>Моя успеваемость {performance}</p>
    <p>Я {desire} учиться</p>
    <a href = '../'>Назад</a>    

    ''')
def contacts(request, git,telegram):
        return HttpResponse(f'''
    <h2>Мои контакты</h2>
    <a href = '{git}'>Моя GitHub</a>
    <a href = '{telegram}'>Мой Telegram</a>    
    <a href = '../'>Назад</a>    

    ''')
