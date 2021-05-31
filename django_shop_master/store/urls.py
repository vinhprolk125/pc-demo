from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.index),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

	path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),

	path('vga/', views.vga, name='vga'),
    path('cpu/', views.cpu, name='cpu'),
	path('mainboard/', views.mainboard, name='mainboard'),
	path('ram/', views.ram, name='ram'),
	path('psu/', views.psu, name='psu'),
	path('case/', views.case, name='case'),
	path('ssd/', views.ssd, name='ssd'),
	path('hdd/', views.hdd, name='hdd'),
	path('man_hinh/', views.man_hinh, name='man_hinh'),
	path('chuot/', views.chuot, name='chuot'),
	path('ban_phim/', views.ban_phim, name='ban_phim'),
	path('tai_nghe/', views.tai_nghe, name='tai_nghe'),
	path('ghe_gaming/', views.ghe_gaming, name='ghe_gaming'),
	path('phu_kien/', views.phu_kien, name='phu_kien'),
	path('store/', views.store, name='store'),

    path('item/', views.item, name='item'),
    path('login/',auth_views.LoginView.as_view(template_name='store/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='/'), name='logout'),
   
    path('vga/<slug:slug>/', views.item, name='item'),
    path('cpu/<slug:slug>/', views.item, name='item'),
	path('mainboard/<slug:slug>/', views.item, name='item'),
	path('ram/<slug:slug>/', views.item, name='item'),
	path('psu/<slug:slug>/', views.item, name='item'),
	path('case/<slug:slug>/', views.item, name='item'),
	path('ssd/<slug:slug>/', views.item, name='item'),
	path('hdd/<slug:slug>/', views.item, name='item'),
	path('man_hinh/<slug:slug>/', views.item, name='item'),
	path('chuot/<slug:slug>/', views.item, name='item'),
	path('ban_phim/<slug:slug>/', views.item, name='item'),
	path('tai_nghe/<slug:slug>/', views.item, name='item'),
	path('ghe_gaming/<slug:slug>/', views.item, name='item'),
	path('phu_kien/<slug:slug>/', views.item, name='item'),
	path('store/<slug:slug>/', views.item, name='item'),



	

	path('results/<slug:slug>/', views.item, name='item'),
	
    path('results/', views.SearchView.as_view(), name='search'),


]