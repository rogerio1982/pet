from django.contrib import admin

from .models import *


#admin
class ServicoInline(admin.TabularInline):
    model = Servico

class VendasAdmin(admin.ModelAdmin):
    list_display = ('status','pet',)
    inlines = [
        ServicoInline,
    ]

admin.site.register(Produtos)
admin.site.register(Cliente)
admin.site.register(Pet)
#admin.site.register(Servico)
admin.site.register(Vendas,VendasAdmin)

