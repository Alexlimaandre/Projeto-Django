from django.contrib import admin
from django.urls import path
from todos import views # ou from todos.views import nome_da_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.TodoHomeView.as_view(), name="home"),
    path("lista/", views.TodoListView.as_view(), name="todo_list"),
    path("criar/", views.TodoCreateView.as_view(), name="todo_create"),
    path("atualizar/<int:pk>/", views.TodoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>/", views.TodoDeleteView.as_view(), name="todo_delete"),
    path("concluir/<int:pk>/", views.TodoCompleteView.as_view(), name="todo_complete")
]
