from django.contrib import admin

from .models import Flat
from .models import Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['owner', 'town', 'address']
    readonly_fields = ['created_at']
    list_display = [
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
        'owners_phonenumber',
        'owners_pure_phonenumber',
    ]
    list_editable = ['new_building']
    list_filter = ['new_building']
    raw_id_fields = ['likes']


class ComplaintAdmin(admin.ModelAdmin):
    list_display = [
        'flat',
        'author',
        'body',
    ]
    raw_id_fields = [
        'author',
        'flat',
    ]

admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
