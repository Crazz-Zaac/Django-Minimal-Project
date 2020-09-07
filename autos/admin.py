from django.contrib import admin

from autos.models import Auto, Make

admin.site.register([Auto, Make])
