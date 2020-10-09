from django.contrib import admin

from ads.models import Ad, Comment, Fav

admin.site.register([Ad, Comment, Fav])
