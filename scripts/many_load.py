import csv 

#python3 manage.py runscript many_load

from unesco.models import Site, Category, Iso, Region, State

def run():
	fhand = open('unesco/load.csv')
	reader = csv.reader(fhand)
	next(reader)

	
	Category.objects.all().delete()
	Iso.objects.all().delete()
	Region.objects.all().delete()
	State.objects.all().delete()

	Site.objects.all().delete()


	for row in reader:
		# print(row)
		# print (len(row))

		nm, created = Site.objects.get_or_create(name=row[0])
		dsc, created = Site.objects.get_or_create(describe=row[1])
		jst, created = Site.objects.get_or_create(justify=row[2])
		yr, created = Site.objects.get_or_create(year=row[3])
		lng, created = Site.objects.get_or_create(longitude=row[4])
		lat, created = Site.objects.get_or_create(latitude=row[5])
		area, created = Site.objects.get_or_create(latitude=row[6])

		
		# c, created = Category.objects.get_or_create(category=row[7])
		# c.save()
		# i, created = Iso.objects.get_or_create(iso=row[10]) #iso is field name in the model ISO
		# i.save()
		# r, created = Region.objects.get_or_create(region=row[9]) #region is field name in the model Region 
		# r.save()
		# s, created = State.objects.get_or_create(state=row[8])
		# s.save()

		# r = Membership.Leader
		# if row[1] == 'I':
		# 	r = Membership.INSTRUCTOR
		
		st = Site(category=row[7], state=row[8], region=row[9], iso=row[10], 
					name=nm, area=area, describe=dsc, justify=jst, longitude=lng, latitude=lat)
		st.save()