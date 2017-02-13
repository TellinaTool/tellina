from django.contrib import admin

from .models import NLRequest, Translation, NLRequestIPAddress

admin.site.register(NLRequest)
admin.site.register(Translation)
admin.site.register(NLRequestIPAddress)