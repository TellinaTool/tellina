from django.contrib import admin

from .models import Annotation, NLRequest, Translation, User

admin.site.register(User)
admin.site.register(NLRequest)
admin.site.register(Translation)
admin.site.register(Annotation)