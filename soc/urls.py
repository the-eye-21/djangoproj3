from django.urls import path, include
from . import views

urlpatterns = [
	path('',views.home),
	path('ce/',views.writepost),
	path('p/<str:nice>/',views.cppost),
	path('ce/<str:nice>',views.updatepost),
	path('register/',views.registeracc),
	path('login/',views.loginpage),
	path('logout/',views.logoutuser)
]
