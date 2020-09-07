from django.db import models


class Category(models.Model):
	category = models.CharField(max_length=128)

	def __str__(self):
		return self.name

class State(models.Model):
	state = models.CharField(max_length=25)

	def __str__(self):
		return self.name


class Region(models.Model):
	region = models.CharField(max_length=25)

	def __str__(self):
		return self.region

class Iso(models.Model):
	iso = models.CharField(max_length=5)

	def __str__(self):
		return self.iso

class Site(models.Model):
	name = models.CharField(max_length=128)
	year = models.IntegerField(null=True)
	area = models.FloatField(null=True)
	describe = models.TextField(max_length=500)
	justify = models.TextField(max_length=500, null=True)
	longitude = models.TextField(max_length=25)
	latitude = models.TextField(max_length=25)

	#one to many field
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	state = models.ForeignKey(State, on_delete=models.CASCADE)
	region = models.ForeignKey(Region, on_delete=models.CASCADE)
	iso = models.ForeignKey(Iso, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
