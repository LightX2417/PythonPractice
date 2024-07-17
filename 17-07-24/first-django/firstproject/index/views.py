from django.http import HttpResponse

def helloworld(request):
    html = "<html><body><h1>Hello World!</h1></body></html>"
    return HttpResponse(html)
