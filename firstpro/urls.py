from django.contrib import admin
from django.urls import path, include

from .import views

urlpatterns = [
    path('',views.home),
    path('about',views.about),
    # path('register',views.register),
    # path('formsave',views.formsave),
    path('registration',views.registration),
    path('saveform',views.saveform),
    path('viewdata',views.viewdata),
    # path('delete_data/<int:id>',views.delete_data),
    # path('edit_data/<int:id>',views.edit_data),
    path('delete_data',views.delete_data),
    path('edit_data',views.edit_data),
    path('update_data',views.update_data),
    path('login',views.login),
    path('login_check',views.login_check),
    path('dashboard',views.dashboard),
    path('logout',views.logout),
    path('addcookie',views.addcookie),
    path('viewcookie',views.viewcookie),
    path('file',views.file),
    path('filesave',views.filesave), 
]