from django.urls import path
from . import views
from django.contrib import admin
from .views import check_auth


if check_auth:
    print(check_auth)
else:
    print(check_auth)



urlpatterns = [
    # path('adminpage/login/?next=/adminpage/', views.adminlogin, name="admin"),
    path('admin/', views.adminlogin, name="admin"),
    path('', views.adminlogin, name="admin"),
    path('adminpage/', admin.site.urls),
    path('extranet/services/verificarisultaticandidato.aspx', views.student_page, name="student_page"),
]