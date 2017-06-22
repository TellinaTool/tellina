from django.contrib import admin

from .models import Annotation, NLRequest, Translation, URL, URLTag, User

admin.site.register(URL)
admin.site.register(User)
admin.site.register(NLRequest)
admin.site.register(Translation)
admin.site.register(Annotation)
admin.site.register(URLTag)