from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) # one to one Relation
    CARD_ID = models.CharField(max_length=10,null=False,verbose_name='身分證號碼')
    NAME = models.CharField(max_length=10,null=False,verbose_name='姓名')
    USERNAME = models.CharField(max_length=16,null=False,verbose_name='帳號')
    PASSWORD = models.CharField(max_length=256,null=False,verbose_name='密碼')
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





class Department(models.Model):
    DEPARTMENT = models.CharField(max_length=10,verbose_name='科別')
    DOCTOR = models.CharField(max_length=10,null=True,verbose_name='醫師')

    def __str__(self):
       return self.DEPARTMENT


class Consult(models.Model):
    Department = models.ForeignKey(Department,related_name='Department',on_delete=models.CASCADE,verbose_name='科別')
    date1 = models.DateField(null=True, verbose_name='回診日')
    number = models.IntegerField(null=False,verbose_name='回診號碼')
    date2 = models.DateField(null=True,verbose_name='第二次處方簽領藥日')
    date3 = models.DateField(null=True,verbose_name='第三次處方簽領藥日')

    def __str__(self):
       return self.Department.DEPARTMENT+","+self.Department.DOCTOR
