from django.shortcuts import render, redirect
from .forms import CariDonorForm
from .models import CariDonor
from cariDonor.models import *
import json
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http.response import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response as Resp
from .serializers import *

def formcaridonor(request):
    form = CariDonorForm(request.POST or None)
    if request.is_ajax():
        if (form.is_valid() and request.method == 'POST'):   
            nama = form.cleaned_data["nama"]
            nik = form.cleaned_data["NIK"]
            dob = form.cleaned_data["tanggal_Lahir"]
            provinsi = form.cleaned_data["provinsi"]
            kota = form.cleaned_data["kota"]
            nohp = form.cleaned_data["nomor_Telepon"]
            goldar = form.cleaned_data["golongan_Darah"]
            request.session['nama'] = nama
            request.session['nik'] = nik
            request.session['dob'] = json.dumps(dob,indent=4, sort_keys=True, default=str)
            request.session['provinsi'] = json.dumps(provinsi,indent=4, sort_keys=True, default=str)
            request.session['kota'] = json.dumps(kota,indent=4, sort_keys=True, default=str)
            request.session['nohp'] = nohp
            request.session['goldar'] = goldar
            form.save()
            return JsonResponse({})
    context = {
        'form': form
    }
    return render(request, 'formcaridonor.html', context) 

def informasicaridonor(request):
    nama = request.session['nama']
    nik = request.session['nik']
    dob = request.session['dob']
    provinsi = request.session['provinsi']
    kota = request.session['kota']
    nohp = request.session['nohp']
    goldar = request.session['goldar']
    idnya = CariDonor.objects.filter(nama=nama, NIK=nik).last()
    if (idnya == None):
        return redirect("/home/")
    idnya = idnya.id
    context = {
        'nama': nama,
        'nik': nik,
        'dob': dob[1:-1],
        'provinsi': provinsi[1:-1],
        'kota': kota[1:-1],
        'nohp': nohp,
        'goldar': goldar,
        'idnya': idnya
    }
    return render(request, 'submit.html', context)

def editdata(request, pk):
    try:
        data = CariDonor.objects.get(id=pk)
    except CariDonor.DoesNotExist:
        return redirect("/FormCariDonor/")
    edit(pk)
    form = CariDonorForm(instance=data)
    if request.method == 'POST':
        form = CariDonorForm(request.POST, instance=data)
        if form.is_valid(): 
            form.save()
    context = {
        'form': form
    }
    return render(request, 'formcaridonor.html', context)

def edit(pk):
    idnya = CariDonor.objects.filter(id=pk)
    idnya.delete()

def deletedata(request, pk):
    idnya = CariDonor.objects.filter(id=pk)
    idnya.delete()
    return redirect("/home/")

@login_required(login_url='/home/login')
def listcaridonor(request):
    if request.user.is_superuser:
        data = CariDonor.objects.all()
        response = {'data': data}
        return render(request, 'listnya.html', response)
    else:
        return redirect("/home/")

def jsonnya(request):
    data = serializers.serialize('json', CariDonor.objects.all())
    return HttpResponse(data, content_type="application/json")

@api_view(['GET'])
def listt(request):
    caridonor = CariDonor.objects.all()
    data = CrDnr(caridonor, many=True)
    return Resp(data.data)

@api_view(['GET'])
def detailcaridonor(request, pk):
    caridonor = CariDonor.objects.filter(id=pk)
    data = CrDnr(caridonor, many=True)
    return Resp(data.data)

@api_view(['POST'])
def create(request):
    data = request.data 
    namaprov = Provinsi.objects.get(nama=data['provinsi'])
    namakota = Kota.objects.get(id=data['kota'])

    baru = CariDonor.objects.create(
        nama = data['nama'],
        NIK = data['NIK'],
        tanggal_Lahir = data['tanggal_Lahir'],
        provinsi = namaprov,
        kota = namakota,
        # provinsi = data['provinsi'],
        # kota = data['kota'],
        nomor_Telepon = data['nomor_Telepon'],
        golongan_Darah = data['golongan_Darah'],
    )
    datanya = CrDnr(baru, many=False)
    return Resp(datanya.data)

@api_view(['PUT'])
def update(request, pk):
    data = request.data 
    updatenya = CariDonor.objects.get(id=pk)
    namaprov = Provinsi.objects.get(nama=data['provinsi'])
    namakota = Kota.objects.get(id=data['kota'])
    provv = model_to_dict(namaprov)
    prov = json.dumps(provv) 
    kotaa = model_to_dict(namakota)
    kota = json.dumps(kotaa)
    print(prov)
    datanya = {
        'id': pk,
        'nama': data['nama'],
        'NIK': data['NIK'],
        'tanggal_Lahir': data['tanggal_Lahir'],
        'provinsi': data['provinsi'],
        'kota': data['kota'],
        'nomor_Telepon': data['nomor_Telepon'],
        'golongan_Darah': data['golongan_Darah'],
    }
    datanya = CrDnr(updatenya, data=datanya)
    print("gavalid")
    if datanya.is_valid():
        print("VALIDDDDDDDDD")
        datanya.save()
    else:
        print(datanya.errors)
    # datanya = CrDnr(baru, many=False)
    return Resp(datanya.data)

@api_view(['DELETE'])
def delete(request, pk):
    data = CariDonor.objects.get(id=pk)
    data.delete()
    return Resp('Deleted')
