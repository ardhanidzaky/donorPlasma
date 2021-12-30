from django.http import response
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.core import serializers
from .forms import pendonor_form
from .models import pendonor
from django.contrib.auth.decorators import login_required
import json
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from cariDonor.models import Provinsi, Kota

# Create your views here.
@login_required(login_url='/home/login')
def form_pendonor(request):
    form = pendonor_form(request.POST,request.FILES or None)
    
    if(request.method=='POST' and form.is_valid()):
        user_now = request.user
        form_user = form.save(commit=False)
        form_user.user = user_now
        form_user.save()
        return HttpResponseRedirect('/pendonor')
    
    response = {'form' : form}
    return render(request,"form_pendonor.html",response)

@login_required(login_url='/home/login')
def informasi_pendonor(request):
    user_now = request.user
    data = None

    try:
        data = pendonor.objects.get(user = user_now)
    except :
        return HttpResponseRedirect('/pendonor/daftar')

    response = {'data' : data}

    return render(request,'informasi_pendonor.html',response)

def data_pendonor():
    data = serializers.serialize('json',pendonor.objects.all())
    return HttpResponse(data,content_type='application/json')

def get_pendonor(request):
    user_now  = request.user
    data = pendonor.objects.get(user = user_now)
    response = serializers.serialize('json',[data])
    return HttpResponse(response,content_type = "application/json")
    # return JsonResponse({'status':'berhasil'})

@login_required(login_url='/home/login')
def update_pendonor(request):
    user_now = request.user
    obj = get_object_or_404(pendonor,user = user_now)
    form = pendonor_form(request.POST, request.FILES, instance = obj)
    
    if(request.method=='POST' and form.is_valid()):
        form.save()
        return HttpResponseRedirect('/pendonor')

    response = {'form' : form}
    return render(request,'form_pendonor.html',response)

@login_required(login_url='/home/login')
def delete_pendonor(request):
    user_now = request.user
    obj = get_object_or_404(pendonor, user = user_now)
    obj.delete()
    return HttpResponseRedirect("/home/")

def info_donor(request):
    orang = request.GET.get("nama")
    data = pendonor.objects.get(nama=orang)
    response = serializers.serialize('json',[data])
    return HttpResponse(response,content_type= "application/json")

@csrf_exempt
def daftar_donor(request):
    print(request.method)
    print(request.body)
    data = json.loads(request.body)
    form = pendonor()
    form.nama = data["nama"]
    form.NIK = data["nik"]
    data["nik"] = data["nik"]
    form.tanggal_lahir = datetime.strptime(data["tl"], '%d/%m/%y')
    form.golongan_darah = data["goldar"]
    form.rhesus = data["rhesus"]
    form.provinsi = Provinsi.objects.get(nama=data["prov"])
    form.kota = Kota.objects.get(nama=data["kota"])
    form.nomor_hp = data["hp"]
    form.bukti_swab_negatif = data["lsn"]
    form.bukti_swab_positif = data["lsp"]
    form.tanggal_sembuh = datetime.strptime(data["ts"], '%d/%m/%y')
    form.tanggal_terakhir_mendonor = datetime.strptime(data["tm"], '%d/%m/%y')
    form.save()
    return JsonResponse({'status':'berhasil'})