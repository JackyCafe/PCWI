from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import UserProfile, Department, Consult, MedicationStyle, MedicationNotice


class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)


    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        '''
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        '''
        if commit:
            user.save()
        return  user


class UserProfileForm(ModelForm):
    FIRST_CAREER = forms.CharField(required=False)
    LAST_CAREER = forms.CharField(required=False)
    ROOM = forms.CharField(required=False)

    class Meta:
        model = UserProfile
        fields = ('CARD_ID','NAME','BIRTHDAY','BLOOD','ADDRESS','TEL','MOBILE'
                  ,'CONTACT','CONTACT_TEL','CONTACT_RELATION','FIRST_CAREER','LAST_CAREER',
                  'ROOM','IS_STAFF',)



class DepartmentForm(ModelForm):

    class Meta:
        model = Department
        fields = '__all__'


class ConsultForm(ModelForm):

    class Meta:
        model = Consult
        fields = '__all__'

    def save(self, commit=True):
        consult = super().save(commit=False)

        if commit:
            consult.save()
        return  consult


# 用藥方式
class MedicationStyleForm(ModelForm):
    class Meta:
        model = MedicationStyle
        fields = '__all__'

#用藥須知
class MedicationNoticeForm(ModelForm):
    class Meta:
        model = MedicationNotice
        fields = '__all__'

    def save(self, commit=True):
        medicationnotice = super().save(commit=False)
        if commit:
            medicationnotice.save()
            print(medicationnotice)

        return  medicationnotice