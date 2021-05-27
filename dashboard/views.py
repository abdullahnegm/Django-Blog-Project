from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from dashboard.forms import BadwordsForm
from posts.models import Badwords

# Create your views here.


def home(request):
    context = {
        "admin": "admin dashboard",
    }
    return render(request, 'auth/dashboard/home.html', context)


def all_badwords(request):
    badwords = Badwords.objects.all()
    context = {"data": badwords}
    return render(request, 'auth/dashboard/badwords/badwords.html', context)


def badwords_details(request, badword_id):
    badword = Badwords.objects.get(id=badword_id)
    context = {"data": badword}
    return render(request, 'auth/dashboard/badwords/badwords_details.html', context)


def add_badwords(request):
    badwords_form = BadwordsForm()
    if request.method == 'POST':
        badwords_form = BadwordsForm(request.POST)
        if badwords_form.is_valid():
            badwords_form.save()
            return HttpResponseRedirect("/auth/badwords")

    context = {"badwords_form": badwords_form}
    return render(request, 'auth/dashboard/badwords/badwords_form.html', context)


def edit_badwords(request, badword_id):
    badwords = Badwords.objects.get(id=badword_id)
    badwords_form = BadwordsForm(instance=badwords)
    if request.method == 'POST':
        badwords_form = BadwordsForm(request.POST, instance=badwords)
        if badwords_form.is_valid():
            badwords_form.save()
            return HttpResponseRedirect('/auth/badwords')

    context = {'badwords_form': badwords_form}
    return render(request, 'auth/dashboard/badwords/badwords_form.html', context)


def delete_badwords(request, badword_id):
    badwords = Badwords.objects.get(id=badword_id)
    badwords.delete()
    return HttpResponseRedirect("/auth/badwords")
