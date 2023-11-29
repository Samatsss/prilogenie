from django.http import HttpResponse

def index(request):
    return HttpResponse('Я Саетгареев Самат Илдарович, Мне 16 лет, Я люблю кушать')

def about(request):
    return HttpResponse('Я приехал из уфы, у меня хорошая успеваемость, и я люблю учиться')

def contacts(request):
    return HttpResponse('https://github.com/Samatsss,' ' мой тг: @Rtrrrrtrr')