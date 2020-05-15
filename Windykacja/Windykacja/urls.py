from django.contrib import admin
from django.urls import path
from main.views import sprawy, pomoc, windykatorzy, signup, edit_worker, sprawa, profil, delete_worker, delete_documents
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', profil, name="home"),
    path('sprawy/', sprawy),
    path('pomoc/', pomoc),
    path('windykatorzy/', windykatorzy),
    path('nowypracownik/', signup),
    path('editworker/<int:id>/', edit_worker),
    path('deleteworker/<int:id>/', delete_worker),
    path('deletedocument/<int:id>/', delete_documents),
    path('sprawa/<int:id>/', sprawa),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
