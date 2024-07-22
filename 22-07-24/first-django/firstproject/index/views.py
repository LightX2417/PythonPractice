from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timedelta


def helloworld(request):
    html = "<html><body><h1>Hello World!</h1></body></html>"
    return HttpResponse(html)



# Create a web page which displays the current date and time offset by a certain number of hours. 
# The goal is to craft a site in such a way that the page /time/plus/1/ displays the date/time one hour into the future, 
# the page /time/minus/2/ displays the date/time two hours into the past, the page /time/plus/3/ displays the date/time 
# three hours into the future, the page /time/minus/5/ displays the date/time five hours into the past and so on.

def dynamicTime(request, operator, hours):
        now = datetime.now()
        if operator == 'plus':
            offset = now + timedelta(hours=int(hours))
        elif operator == 'minus':
            offset = now - timedelta(hours=int(hours))
        else:
            return HttpResponse(status=400)

        context = {"current_time": now, "offset_hours": hours, "offset_time": offset}
        return render(request, "index/timeoffset.html", context)
