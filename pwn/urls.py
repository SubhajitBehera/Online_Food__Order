from django.conf.urls.static import static
from django.urls import path

from OnlineFood import settings
from pwn import views

urlpatterns = [
path('',views.showIndex,name='pwn_main'),
    path('pwn_login_check/', views.pwn_login_check, name='pwn_login_check'),
    path('welcome/', views.welcome, name='welcome'),
    path('state/', views.openState, name='state'),
    path('city/', views.openCity, name='city'),
    path('cuisine/', views.openCusine, name='cuisine'),
    path('vendor/', views.openVendor, name='vendor'),
    path('resports/', views.openReporsts, name='reports'),
    path('logout/', views.pwn_login_check, name='logout'),
    path('addstate/', views.addstate, name='addstate'),
    path('addcity/', views.addCity, name='addcity'),
    path('update/', views.update, name='update'),
    path('updatestate/', views.updatestate, name='updatestate'),
    path('delete/', views.delete, name='delete'),
    path('deletecity/', views.deleteCity, name='deletecity'),
    path('update_c/', views.updateC, name='update_c'),
    path('update_city/', views.updateCity, name='update_city'),
    path('addcuisine/', views.addCuisine, name='addcuisine'),
    path('updatecuisine/', views.updatecuisine, name='updatecuisine'),
    path('updatecuisinetype/', views.cuisineTypeUpdate, name='updatecuisinetype'),
    path('deletecuisine/', views.deletecuisine, name='deletecuisine')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

