from django.urls import path
from .import views
from .views import CustomLoginView, RegisterPage
from .views import logout_view

urlpatterns = [

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    # Маршруты 
    path('', views.index, name='index'), # общий маршрут

    path('manufacturer_list/', views.manufacturer_list, name='manufacturer_list'),
    path('display_manufacturers/', views.display_manufacturers, name='display_manufacturers'),
    path('add_manufacturer/', views.add_manufacturer, name='add_manufacturer'), 
    path('manufacturer/<int:pk>/', views.manufacturer_detail, name='manufacturer_detail'),  
    path('delete_manufacturer/<int:pk>/', views.delete_manufacturer, name='delete_manufacturer'),  

    path('product_list/', views.product_list, name='product_list'),
    path('display_laptops/', views.display_laptops, name='display_laptops'),
    path('add_laptop/', views.add_laptop, name='add_laptop'),
    path('laptop/<int:pk>/detail/', views.laptop_detail, name='laptop_detail'),
    path('edit_laptop/<int:pk>/', views.edit_laptop, name='edit_laptop'),
    path('delete_laptop/<int:pk>/', views.delete_laptop, name='delete_laptop'),

    path('display_desktops/', views.display_desktops, name='display_desktops'),
    path('add_desktop/', views.add_desktop, name='add_desktop'),
    path('desktop/<int:pk>/detail/', views.desktop_detail, name='desktop_detail'),
    path('edit_desktop/<int:pk>/', views.edit_desktop, name='edit_desktop'),
    path('delete_desktop/<int:pk>/', views.delete_desktop, name='delete_desktop'),

    path('display_mobiles/', views.display_mobiles, name='display_mobiles'),    
    path('add_mobile/', views.add_mobile, name='add_mobile'),        
    path('mobile/<int:pk>/detail/', views.mobile_detail, name='mobile_detail'),
    path('edit_mobile/<int:pk>/', views.edit_mobile, name='edit_mobile'),
    path('delete_mobile/<int:pk>/', views.delete_mobile, name='delete_mobile'),

]
