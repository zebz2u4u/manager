from django.urls import path

from . import views
urlpatterns = [
    path('', views.home, name='home'),

    #     path('register', views.register, name="register"),
        
    #     path('login', views.login, name="login"),

    #     path('logout', views.logout, name="logout"),

    #     path('dashboard', views.dashboard, name="dashboard"),

    #     path('admin-dashboard', views.adminDashboard, name="admin-dashboard"),

    #     path('admin-updates/<int:pk>', views.adminUpdateRequest, name='admin-updates'),

    #     path('create-record', views.createRecord, name="create-record"),

    #     path('update-record/<int:pk>/', views.updateRecord, name="update-record"),
        
    #     path('request/<int:pk>', views.viewRecord, name="view-request"),

    #     path('delete-record/<int:pk>', views.deleteRecord, name="delete-record"),
]