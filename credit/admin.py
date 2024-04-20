from django.contrib import admin

from .models import CreditPackage, Transaction

# Register your models here.
admin.site.register(CreditPackage)
admin.site.register(Transaction)
