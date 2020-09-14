from django.contrib import admin

from ads.models import Ad, Comment

admin.site.register([Ad, Comment])
