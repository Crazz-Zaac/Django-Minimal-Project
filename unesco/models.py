from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=128)

	def __str__(self):
		return self.name

class States(models.Model):
	name = models.CharField(max_length=25)

	def __str__(self):
		return self.name


class Region(models.Model):
	name = models.CharField(max_length=25)

	def __str__(self):
		return self.name

class Iso(models.Model):
	name = models.CharField(max_length=5)

	def __str__(self):
		return self.name

class Site(models.Model):
	name = models.CharField(max_length=128)
	year = models.IntegerField(null=True)
	area_hectares = models.CharField(max_length=15, null=True)
	describe = models.TextField(max_length=500)
	justify = models.TextField(max_length=500, null=True)
	longitude = models.TextField(max_length=25, null=True)
	latitude = models.TextField(max_length=25, null=True)

	#one to many field
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	states = models.ForeignKey(States, on_delete=models.CASCADE)
	region = models.ForeignKey(Region, on_delete=models.CASCADE)
	iso = models.ForeignKey(Iso, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
