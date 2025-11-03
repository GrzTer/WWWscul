from django.contrib import admin
from grzybyapp.models import Grzyby, Rodzina, Potrawy

admin.site.register(Rodzina)
admin.site.register(Potrawy)
admin.site.register(Grzyby)

