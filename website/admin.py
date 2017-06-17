from django.contrib import admin

from .models import NLRequest, Translation

admin.site.register(NLRequest)
admin.site.register(Translation)