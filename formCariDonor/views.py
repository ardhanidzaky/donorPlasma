from django.shortcuts import render, redirect
from .forms import CariDonorForm
from .models import CariDonor
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http.response import HttpResponse

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
    context = {
        'nama': nama,
        'nik': nik,
        'dob': dob[1:-1],
        'provinsi': provinsi[1:-1],
        'kota': kota[1:-1],
        'nohp': nohp,
        'goldar': goldar,
        'idnya': idnya.id
    }
    return render(request, 'submit.html', context)

def editdata(request, pk):
    data = get_object_or_404(CariDonor, id=pk)
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
    return redirect("/FormCariDonor/")

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