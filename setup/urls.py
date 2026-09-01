from django.contrib import admin
from django.urls import path
from todos import views # ou from todos.views import nome_da_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("lista/", views.todo_list, name="todo_list")
]
