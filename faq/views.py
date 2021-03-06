from django.shortcuts import render
from django.http import HttpResponseRedirect, response
from .models import faq
from .forms import FAQForm
from django.contrib.auth.decorators import login_required
from .forms import FAQForm
from django.core import serializers 
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    faqs = faq.objects.all()
    response = {'faqs':faqs}
    return render(request, 'faq.html', response)


@login_required(login_url='/home/login')
def add_forms(request):
    context ={}
    form = FAQForm(request.POST or None)
    if form.is_valid():
        form.save()
        if request.method == 'POST':
            return HttpResponseRedirect("/faq")
    context['form']= form
    return render(request, "formfaq.html", context)

def delete_question(request):
    if (request.method == "POST"):
        id = request.POST.get("id")
        faq.objects.filter(id=id).delete()
    return HttpResponseRedirect("/faq")


def json_faq(request):
    faqs = faq.objects.all()
    data = serializers.serialize('json', faqs)
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def add_faq(request):
    if (request.method == "POST"):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        question = body['question']
        answer = body["answer"]

        try:
            faqs = faq(question=question, answer=answer)
            faqs.save()
            return HttpResponse("Successful", status=200)
        except Exception :
           return HttpResponse("An error occurred", status=400, content_type="text/plain")
          
    
    return HttpResponse("Must use POST Method", status=405, content_type="text/plain")