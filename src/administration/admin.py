from django.contrib import admin
from .models import Caroussel, Actualite


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('id','titre', 'contenu',)
    prepopulated_fields = {'slug': ('titre',)}


class ActualiteAdmin(admin.ModelAdmin):
    list_display = ('id','titre', 'contenu',)


# Register your models here.

# Panneau défilant
admin.site.register(Caroussel, CarouselAdmin)

# Articles
admin.site.register(Actualite, ActualiteAdmin)