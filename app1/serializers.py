from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Department, Consult, MedicationStyle, MedicationNotice,MedicationRecord


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = '__all__'
        fields = ('username','password','email','url')


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields =  ('user','CARD_ID','NAME','BIRTHDAY','BLOOD','ADDRESS','TEL','MOBILE'
                  ,'CONTACT','CONTACT_TEL','CONTACT_RELATION','FIRST_CAREER','LAST_CAREER',
                  'ROOM','IS_STAFF','url')


#科別
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'



#回診日
class ConsultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consult
        fields = '__all__'


# 用藥方式
class MedicationStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationStyle
        fields = '__all__'

#用藥須知
class MedicationNoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationNotice
        fields = '__all__'


class MedicationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationRecord
        fields = '__all__'