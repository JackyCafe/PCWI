
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) # one to one Relation
    CARD_ID = models.CharField(max_length=10,null=False,verbose_name='身分證號碼')
    NAME = models.CharField(max_length=10,null=False,verbose_name='姓名')
    USERNAME = models.CharField(max_length=16,null=True,verbose_name='帳號')
    PASSWORD = models.CharField(max_length=256,null=True,verbose_name='密碼')
    BIRTHDAY = models.DateField(null=False,verbose_name='生日')
    BLOOD = models.CharField(max_length=1,null=True,verbose_name='血型')
    ADDRESS = models.CharField(max_length=64,null=True,verbose_name='住址')
    TEL = models.CharField(max_length=10,null=True,verbose_name='聯絡電話')
    MOBILE = models.CharField(max_length=10,null=True,verbose_name='行動電話')
    CONTACT = models.CharField(max_length=10,null=True,verbose_name='緊急聯絡人')
    CONTACT_TEL = models.CharField(max_length=10,null=True,verbose_name='聯絡人電話')
    CONTACT_RELATION = models.CharField(max_length=10,null=True,verbose_name='聯絡人關係')
    FIRST_CAREER =models.CharField(max_length=10,null=True,verbose_name='第一份職業')
    LAST_CAREER =models.CharField(max_length=10,null=True,verbose_name='最後一份職業')
    ROOM = models.CharField(max_length=10,null = True,verbose_name='房號')
    IS_STAFF = models.BooleanField(verbose_name='職員')

    def __str__(self):
        return self.NAME




#定義科別
class Department(models.Model):
    DEPARTMENT = models.CharField(max_length=10,verbose_name='科別')
    DOCTOR = models.CharField(max_length=10,null=True,verbose_name='醫師')

    def __str__(self):
       return self.DEPARTMENT


#定義回診日
class Consult(models.Model):
    Department = models.ForeignKey(Department,related_name='ConsultDepartment',on_delete=models.CASCADE,verbose_name='科別')
    date1 = models.DateField(null=True, verbose_name='回診日')
    number = models.IntegerField(null=False,verbose_name='回診號碼')
    date2 = models.DateField(null=True,verbose_name='第二次處方簽領藥日' ,blank=True)
    date3 = models.DateField(null=True,verbose_name='第三次處方簽領藥日' ,blank= True)

    def __str__(self):
       return self.Department.DEPARTMENT+"/"+self.Department.DOCTOR


#用藥方式
class MedicationStyle(models.Model):
    style = models.CharField(max_length=30,verbose_name='用藥方式')
    pcs = models.CharField(max_length=5,verbose_name='劑量')

    def __str__(self):
        return  self.style +"/" +self.pcs


#用藥須知
class MedicationNotice(models.Model):
    Department = models.ForeignKey(Department,related_name='MedicationNoticeDepartment',on_delete=models.CASCADE,verbose_name='科別')
    Durg = models.CharField(max_length=50,null=False,verbose_name='藥名')
    MedicationStyle = models.OneToOneField(MedicationStyle,related_name='MedicationStyle',on_delete=models.CASCADE)

    def __str__(self):
        return self.Department.DEPARTMENT+"/"+ self.Durg+ "/"+self.MedicationStyle.style+"/"+self.MedicationStyle.pcs


#每日用藥紀錄
class MedicationRecord(models.Model):
    date1 = models.DateField(null=True ,blank=True,verbose_name='日期',auto_now=timezone.now)
    USERNAME = models.ForeignKey(UserProfile,related_name='MedicationRecordUSERNAME',on_delete=models.CASCADE)
    Durg = models.ForeignKey(MedicationNotice,related_name='MedicationRecordDrug',on_delete=models.CASCADE)
    MedicationTime = models.DateTimeField(verbose_name='用藥時間')

    def __str__(self):
        return self.USERNAME.NAME+"/"+self.Durg.Durg+"/"+self.MedicationTime.strftime("%m/%d/%Y, %H:%M:%S")