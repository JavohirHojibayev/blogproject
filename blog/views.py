from django.shortcuts import render
from blog.models import Blog


def bloglistview(request):
    blog = Blog.objects.all()

    context = {'blog': blog}

    return render ( request, "home.html", context=context )
