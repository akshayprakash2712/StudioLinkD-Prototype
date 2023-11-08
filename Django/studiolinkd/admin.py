from django.contrib import admin
from .models import UserType,Artist,Client,TvChannel,RadioChannel
# Register your models here.

class TypeUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'TYPE_CHOICES')
    list_filter = ('username','TYPE_CHOICES')
    search_fields = ('username',)

admin.site.register(UserType, TypeUserAdmin)
admin.site.register(Artist)
admin.site.register(Client)
admin.site.register(TvChannel)
admin.site.register(RadioChannel)