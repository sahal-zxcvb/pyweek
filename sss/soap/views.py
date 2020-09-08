from django.shortcuts import render

from .models import Certificate


def index(request):
    if request.method == "POST":
        email = request.POST["email"]
        bool = False
        try:
            a = Certificate.objects.get(email=email)
            name = a.name.replace(" ", "%20")
            url = "https://github.com/niranjanneeru/Pyweek-Temp/blob/master/assets/img/" + name + ".png?raw=true"
            bool = True
        except:
            url = "https://i.ytimg.com/vi/5MUzpVRqHCQ/maxresdefault.jpg"

        return render(request, 'soap/base.html', {"url": url, "bool": bool})

    return render(request, 'soap/hello.html')
