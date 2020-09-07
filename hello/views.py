from django.shortcuts import render, HttpResponse

def cookie(request):
	print(request.COOKIES)
	oldval = request.COOKIES.get('val', None)
	resp = HttpResponse('In a view - the cookie value is '+str(oldval))
	resp.set_cookie('dj4e_cookie', 'ad47a008', max_age=1000)
	return resp

def sessfun(request):
	num_visits = request.session.get('num_visits', 0) + 1 
	request.session['num_visits'] = num_visits
	if num_visits > 4:
		del(request.session['num_visits'])
	return HttpResponse('view count='+str(num_visits))