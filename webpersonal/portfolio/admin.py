from django.contrib import admin
from .models import Portfolio,Categoria

# Register your models here.
class PortfolioAdmin(admin.ModelAdmin):
    readonly_fields = ('created' , 'updated')


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Categoria, PortfolioAdmin)

