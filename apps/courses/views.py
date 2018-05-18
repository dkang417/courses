# from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from .models import Course 
from django.contrib import messages

def index(request):
	
	if request.method == "POST":
		errors = Course.objects.basic_validator(request.POST)
		if len(errors):
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags=tag)
				return redirect("/")
		else:
			Course.objects.create(name=request.POST["name"], description=request.POST["description"])
			return redirect("/")
	else:
		context = {
			"courses" : Course.objects.all()
		}	
		return render(request,'courses/index.html', context)

def show_or_destroy(request,course_id):
	if request.method == "POST":
		Course.objects.get(id=course_id).delete()
		return redirect('/')
	else:
		context = {
		"course": Course.objects.get(id=course_id)
	}
		return render(request, 'courses/delete.html', context)



