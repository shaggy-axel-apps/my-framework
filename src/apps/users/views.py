from shaggy_framework import render


def users(request):
    context = {"title": "Users", "description": "List of Users"}
    code = "200 OK"
    return code, render("index.html", context=context)
