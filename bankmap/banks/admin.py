from django.contrib import admin
from .models import Bank, Workload, Types

admin.site.register(Bank)
admin.site.register(Workload)
admin.site.register(Types)
