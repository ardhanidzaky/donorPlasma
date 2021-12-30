from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import CariDonor
from cariDonor.models import *

class provinsiserializer(ModelSerializer):
    class Meta:
        model = Provinsi
        fields = '__all__'

class kotaserializer(ModelSerializer):
    provinsi = provinsiserializer(many=False)
    class Meta:
        model = Kota
        fields = ('id', 'nama', 'provinsi')
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['provinsi'] = provinsiserializer(context=self.context).to_representation(instance.provinsi)
        return ret

class CrDnr(ModelSerializer):
    # provinsi = provinsiserializer(many=False, read_only=True)
    # kota = kotaserializer(many=False, read_only=True)
    provinsi = serializers.PrimaryKeyRelatedField(queryset=Provinsi.objects.all())
    kota = serializers.PrimaryKeyRelatedField(queryset=Kota.objects.all())
    class Meta:
        model = CariDonor
        fields = ('id', 'nama', 'NIK', 'tanggal_Lahir', 'provinsi', 'kota', 'nomor_Telepon', 'golongan_Darah')
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['provinsi'] = provinsiserializer(context=self.context).to_representation(instance.provinsi)
        ret['kota'] = kotaserializer(context=self.context).to_representation(instance.kota)
        return ret
