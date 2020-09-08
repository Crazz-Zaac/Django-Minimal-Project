import csv 

#python3 manage.py runscript many_load

from unesco.models import Site, Iso, Category, Region, States

def run():
	fhand = open('unesco/load.csv')
	reader = csv.reader(fhand)
	next(reader)

	Category.objects.all().delete()
	Iso.objects.all().delete()
	Region.objects.all().delete()
	States.objects.all().delete()

	Site.objects.all().delete()

	for row in reader:
	
		nm= row[0]
		dsc = row[1]
		jst = row[2]
		lng = row[4]
		lat = row[5]
		area = row[6]

		try:
			area = float(row[6])
		except:
			area = 0.0

		try:
			year = int(row[3])
		except:
			year = None

		#create objects only for tables in a relation
		
		category, created = Category.objects.get_or_create(name=row[7])
		states, created = States.objects.get_or_create(name=row[8])
		region, created = Region.objects.get_or_create(name=row[9])
		iso, created = Iso.objects.get_or_create(name=row[10])

		
		st = Site(category=category, states=states, region=region, iso=iso, 
					name=nm, year=year, area_hectares=area, describe=dsc, justify=jst, longitude=lng, latitude=lat)
		st.save()