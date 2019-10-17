from django.contrib import admin
from .models import UserProfile,Department,Consult,MedicationStyle,MedicationNotice,MedicationRecord
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Department)
admin.site.register(Consult)
admin.site.register(MedicationStyle)
admin.site.register(MedicationNotice)
admin.site.register(MedicationRecord)