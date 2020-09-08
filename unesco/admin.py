from django.contrib import admin

from unesco.models import Site, Category, Iso, Region, States

admin.site.register([Site, Category, Iso, Region, States])
