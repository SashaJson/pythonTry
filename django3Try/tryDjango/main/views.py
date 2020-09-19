from django.shortcuts import render


def index(request):
    data = {
        'title': 'Main page',
        'values': ['some', 'hello'],
        'obj': {
            'asap': 11
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
