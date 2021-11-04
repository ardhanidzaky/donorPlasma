from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http.response import HttpResponse
from .models import Stok, StokB, StokAB, StokO
from .forms import StokForm, StokBForm, StokABForm, StokOForm

def index(request):
    stocks = Stok.objects.all()
    stockbs = StokB.objects.all()
    stockos = StokO.objects.all()
    stockabs = StokAB.objects.all()
    response = {'stocks':stocks, 'stockbs':stockbs, 'stockos':stockos, 'stockabs':stockabs,}
    return render(request, 'filterpage.html',response)

@login_required(login_url='/home/login')
def pilihgoldar(request):
    return render(request, 'pilihgoldar.html')

@login_required(login_url='/home/login?next=/informasiUDD/add')
def add_forms(request):
    context = {}
    response={}
    form = StokForm(request.POST or None)
    if form.is_valid():
        form.save()
        print("valid")
        if request.method == 'POST':
            return HttpResponseRedirect("/informasiUDD/")
    else:
        print(form.errors)
    context['form'] = form
    return render(request, "forms.html", response)

@login_required(login_url='/home/login?next=/informasiUDD/add')
def add_formsb(request):
    context = {}
    response={}
    form = StokBForm(request.POST or None)
    if form.is_valid():
        form.save()
        print("valid")
        if request.method == 'POST':
            return HttpResponseRedirect("/informasiUDD/")
    else:
        print(form.errors)
    context['form'] = form
    return render(request, "forms_b.html", response)

@login_required(login_url='/home/login?next=/informasiUDD/add')
def add_formso(request):
    context = {}
    response={}
    form = StokOForm(request.POST or None)
    if form.is_valid():
        form.save()
        print("valid")
        if request.method == 'POST':
            return HttpResponseRedirect("/informasiUDD/")
    else:
        print(form.errors)
    context['form'] = form
    return render(request, "forms_o.html", response)

@login_required(login_url='/home/login?next=/informasiUDD/add')
def add_formsab(request):
    context = {}
    response={}
    form = StokABForm(request.POST or None)
    if form.is_valid():
        form.save()
        print("valid")
        if request.method == 'POST':
            return HttpResponseRedirect("/informasiUDD/")
    else:
        print(form.errors)
    response = {
        'form':form
    }
    context['form'] = form
    return render(request, "forms_ab.html", response)


def delete_card(request):
    if (request.method == "POST"):
        id = request.POST.get("id")
        Stok.objects.filter(id=id).delete()
    return HttpResponseRedirect("/informasiUDD")

def delete_cardb(request):
    if (request.method == "POST"):
        id = request.POST.get("id")
        StokB.objects.filter(id=id).delete()
    return HttpResponseRedirect("/informasiUDD")

def delete_cardo(request):
    if (request.method == "POST"):
        id = request.POST.get("id")
        StokO.objects.filter(id=id).delete()
    return HttpResponseRedirect("/informasiUDD")

def delete_cardab(request):
    if (request.method == "POST"):
        id = request.POST.get("id")
        StokAB.objects.filter(id=id).delete()
    return HttpResponseRedirect("/informasiUDD")


def edit_card(request):
    if (request.method == "POST"):
        id = request.POST.get("id")
        namaUDD = request.POST.get("namaUDD")
        alamatUDD = request.POST.get("alamatUDD")
        nomorUDD = request.POST.get("nomorUDD")
        JumlahStok = request.POST.get("JumlahStok")

        stok = Stok.objects.get(id=id)
        stok.namaUDD = namaUDD
        stok.alamatUDD = alamatUDD
        stok.nomorUDD = nomorUDD
        stok.JumlahStok = JumlahStok
        stok.save()


    return HttpResponseRedirect("/informasiUDD")


def json(request):
    stocks = Stok.objects.all()
    data = serializers.serialize('json', Stok.objects.all())
    return HttpResponse(data, content_type="application/json")