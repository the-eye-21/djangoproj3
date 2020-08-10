from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

# Create your views here.
from .models import *

def home(request):
	pps = post.objects.order_by('-time')

	context = {'posts':pps}

	return render(request, 'home.html', context)


def writepost(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		f = createpost(request.POST)
		# check whether it's valid:
		if f.is_valid():
			# process the data in form.cleaned_data as required
			p=f.save(commit=False)
			p.user=request.user
			p.save()
			# redirect to a new URL:
			return HttpResponseRedirect('/')

	else:
		form=createpost()

	return render(request,'writepost.html',{'form':form})



def cppost(request, nice):
	p = post.objects.get(id=nice)
	c = comment.objects.filter(post = p)
	
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		f = writecomment(request.POST)
		# check whether it's valid:
		if f.is_valid():
			obj = f.save(commit=False)
			# process the data in form.cleaned_data as required
	
			obj.post = p
			obj.user = request.user
			obj.save()
			# redirect to a new URL:
			return HttpResponseRedirect('')

	else:
		form=writecomment()

	u = (request.user==p.user)
	context = {'pa':p,'comments':c,'form':form,'la':u}	
	return render(request,'post.html',context)



	


def updatepost(request, nice):
	
	p=post.objects.get(id=nice)
	# if this is a POST request we need to process the form data
	if (request.method == 'POST'):
		# create a form instance and populate it with data from the request:
		f = createpost(request.POST, instance=p)
		# check whether it's valid:
		if f.is_valid():
			# process the data in form.cleaned_data as required
			p=f
			p.save()
			# redirect to a new URL:
			return HttpResponseRedirect('/')
	else:
		
		form=createpost(instance=p)

	return render(request,'writepost.html',{'form':form})



def registeracc(request):
	form = UserCreationForm
	context = {'form':form}
	if request.method =='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')

	return render(request,'register.html',context)

def loginpage(request):

	if request.method == 'POST':
		uname = request.POST.get('username')
		pword = request.POST.get('password')

		user = authenticate(request,username=uname, password=pword)

		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/')

	context={}

	return render(request,'login.html',context)
	


def logoutuser(request):
	logout(request)
	return HttpResponseRedirect('/')
