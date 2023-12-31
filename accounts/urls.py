from django.contrib.auth.views import LogoutView
from django.urls import path
from accounts.views import login_request, register_request, editar_request

urlpatterns = [
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
    path('registro/', register_request, name="Registro"),
    path('editar/', editar_request, name="Editar"),

]