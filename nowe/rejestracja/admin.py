from django.contrib import admin
from ankieta.models import Vote,Choice,AnkietaModel
from rejestracja.models import Usr
# Register your models here.
class ChoiceAdmin(admin.ModelAdmin):
    list_display =('nazwa','autor','ankieta')

class AnkietaAdmin(admin.ModelAdmin):
    list_display =('nazwa', 'data_z', 'autor')

class VoteAdmin(admin.ModelAdmin):
    list_display =('wybor', 'Usr')

class UsrAdmin(admin.ModelAdmin):
    list_display = ('username','date_joined','is_active','is_staff','is_superuser')
    list_filter = ('is_staff','is_superuser','is_active')


admin.site.register(Vote, VoteAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(AnkietaModel, AnkietaAdmin)
admin.site.register(Usr, UsrAdmin)

