from django.contrib import admin

from unesco.models import Site, Category, Iso, Region, State

admin.site.register([Site, Category, Iso, Region, State])
