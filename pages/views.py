from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse('<h1>Hello World</h1>')
    return render(request, 'home.html', {})

def contact_view(request, *args, **kwargs):
    my_context = {
        'my_text': 'dasdad'
        'my_number': 123124,
        'my_list': [324, 345,3, 43535, 234]
    }
    return render(request, 'contact.html', my_context)
