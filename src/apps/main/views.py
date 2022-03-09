from shaggy_framework import render


def index(request):
    context = {
        "title": "Main page",
        "description": "Some text"
    }
    code = "200 OK"
    return code, render("index.html", context=context)
