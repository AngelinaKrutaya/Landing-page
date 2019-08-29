from django.contrib import admin
from .models import Image
from .models import Objects
from .models import Certificate

admin.site.register(Image)
admin.site.register(Objects)
admin.site.register(Certificate)
# Register your models here.
