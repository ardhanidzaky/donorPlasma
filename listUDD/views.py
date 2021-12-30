from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from .models import Stok, StokB, StokAB, StokO
from .forms import StokForm, StokBForm, StokABForm, StokOForm
from django.views.decorators.csrf import csrf_exempt
import json

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


def stock_json(request):
    
    response = {
        'stocks': list(Stok.objects.values()),
        'stocksb': list(StokB.objects.values()),
        'stockso': list(StokO.objects.values()),
        'stocksab': list(StokAB.objects.values()),
    }

    return HttpResponse(json.dumps(response), content_type="application/json")

@csrf_exempt
def add_uddA(request):
    if (request.method == "POST"):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        namaUDD_new = body['nama']
        alamatUDD_new = body['alamat']
        nomorUDD_new = body['notelp']
        goldar_new = body['goldar']
        JumlahStok_new = body['stok']

        try: #kiri dari model, kanan dari variabel diatas
            stok = Stok(namaUDD=namaUDD_new, alamatUDD=alamatUDD_new, nomorUDD=nomorUDD_new, goldar=goldar_new, JumlahStok=JumlahStok_new)
            stok.save()
            return HttpResponse("Successful", status=200)
        except Stok.DoesNotExist:
            print("An error occurred")
            return HttpResponse("An error occurred", status=400, content_type="text/plain")
    return HttpResponse("Must use POST Method", status=405, content_type="text/plain")   

@csrf_exempt
def add_uddA(request):
    if (request.method == "POST"):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        namaUDD_new = body['nama']
        alamatUDD_new = body['alamat']
        nomorUDD_new = body['notelp']
        goldar_new = body['goldar']
        JumlahStok_new = body['stok']

        try: #kiri dari model, kanan dari variabel diatas
            stok = Stok(namaUDD=namaUDD_new, alamatUDD=alamatUDD_new, nomorUDD=nomorUDD_new, goldar=goldar_new, JumlahStok=JumlahStok_new)
            stok.save()
            return HttpResponse("Successful", status=200)
        except Stok.DoesNotExist:
            print("An error occurred")
            return HttpResponse("An error occurred", status=400, content_type="text/plain")
    return HttpResponse("Must use POST Method", status=405, content_type="text/plain") 

@csrf_exempt
def add_uddB(request):
    if (request.method == "POST"):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        namaUDD_new = body['nama']
        alamatUDD_new = body['alamat']
        nomorUDD_new = body['notelp']
        goldar_new = body['goldar']
        JumlahStok_new = body['stok']

        try: #kiri dari model, kanan dari variabel diatas
            stokb = StokB(namaUDD=namaUDD_new, alamatUDD=alamatUDD_new, nomorUDD=nomorUDD_new, goldar=goldar_new, JumlahStok=JumlahStok_new)
            stokb.save()
            return HttpResponse("Successful", status=200)
        except StokB.DoesNotExist:
            print("An error occurred")
            return HttpResponse("An error occurred", status=400, content_type="text/plain")
    return HttpResponse("Must use POST Method", status=405, content_type="text/plain") 

@csrf_exempt
def add_uddO(request):
    if (request.method == "POST"):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        namaUDD_new = body['nama']
        alamatUDD_new = body['alamat']
        nomorUDD_new = body['notelp']
        goldar_new = body['goldar']
        JumlahStok_new = body['stok']

        try: #kiri dari model, kanan dari variabel diatas
            stoko = StokO(namaUDD=namaUDD_new, alamatUDD=alamatUDD_new, nomorUDD=nomorUDD_new, goldar=goldar_new, JumlahStok=JumlahStok_new)
            stoko.save()
            return HttpResponse("Successful", status=200)
        except StokO.DoesNotExist:
            print("An error occurred")
            return HttpResponse("An error occurred", status=400, content_type="text/plain")
    return HttpResponse("Must use POST Method", status=405, content_type="text/plain") 

@csrf_exempt
def add_uddAB(request):
    if (request.method == "POST"):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        namaUDD_new = body['nama']
        alamatUDD_new = body['alamat']
        nomorUDD_new = body['notelp']
        goldar_new = body['goldar']
        JumlahStok_new = body['stok']

        try: #kiri dari model, kanan dari variabel diatas
            stokab = StokAB(namaUDD=namaUDD_new, alamatUDD=alamatUDD_new, nomorUDD=nomorUDD_new, goldar=goldar_new, JumlahStok=JumlahStok_new)
            stokab.save()
            return HttpResponse("Successful", status=200)
        except StokAB.DoesNotExist:
            print("An error occurred")
            return HttpResponse("An error occurred", status=400, content_type="text/plain")
    return HttpResponse("Must use POST Method", status=405, content_type="text/plain")         