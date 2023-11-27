from django.urls import path

from mysite import settings
from . import views
from .views import OrdersByUsersUpdateView

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.cars, name='cars'),
    path('cars/<int:car_id>/', views.car, name ='car'),
    path('order/', views.OrderListView.as_view(), name='order'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order'),
    path('search/', views.search, name='search'),
    path('myorders/', views.OngoingWorkByUserListView.as_view(), name='my-orders'),
    path('register/', views.register, name='register'),
    path('profilis/', views.profilis, name='profilis'),
    path('myorders/', views.OrdersByUserListView.as_view(), name='my-orders'),
    path('myorders/<int:pk>', views.OrdersByUserDetailView.as_view(), name = 'my-orders'),
    path('my-order-new/', views.OrdersByUserCreateView.as_view(), name='my-order-new'),
    path('order_list/', views.OrderListView.as_view(), name='order-list'),
    path('myorders/<int:pk>/update/', OrdersByUsersUpdateView.as_view(), name='my-order-update'),
    path('myorder/<int:pk>/delete', views.OrderByUserDeleteView.as_view(),name='my-order-delete'),
]