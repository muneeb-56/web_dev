from django.urls import path
from . import views

urlpatterns={
    path('xyz',views.fun_1),
    path('s',views.fun_2 ),
    path('html',views.fun_3)
}