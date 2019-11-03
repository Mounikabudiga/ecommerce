from django.urls import path
from . import views

urlpatterns = [
	path('data/',views.data,name='data'),
    path('products/', views.products,name='products'),
    path('data1/',views.data1,name='data1'),
    path('single/<id>',views.single,name="single"),
    path('destroy/<id>',views.destroy,name='destroy'),
    # path('update_form/',views.update_form,name="update_form"),
    path('single_user/<id>',views.single_user,name="single_user"),
    path('user/',views.user,name="user"),
    # path('buyed/',views.buyed,name="buyed"),
]
