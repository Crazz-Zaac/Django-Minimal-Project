from django.contrib import admin

from cats.models import Breed, Cat

admin.site.register([Breed, Cat])