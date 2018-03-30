##
 # base/urls.py:
 #
 # St: 2018-03-09 Fri 12:18 PM
 # Up: 2018-03-09 Fri 12:18 PM
 #
 # Author: SPS
 ##

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='base-index'),
    path('menu/', views.displayMenu, name='base-menu'),
    path('order/', views.order, name='base-order'),
    path('contact/', views.contact, name='base-contact'),
    path('reviews/', views.ReviewListView.as_view(), name='base-reviews'),
    path('reviews/create/', views.ReviewCreate.as_view(), name='base-reviews-create'),
    path('reservation/', views.reservation, name='base-reservation'),
]

