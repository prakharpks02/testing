from django.shortcuts import render

# Create your views here.
def test_fn(request):
    a='Hello World'
    b='Hi'
    c='Yo'
    context = {'a':a, 'b':b, 'c':c }
    return render(request, 'test_html.html', context=context)