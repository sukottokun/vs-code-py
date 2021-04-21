from django.shortcuts import render
import os


def frontpage(request):
    return render(request, "core/frontpage.html")
