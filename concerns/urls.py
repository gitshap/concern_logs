from django.urls import path
from concerns.views import (create_concern, create_concern_form, concern_detail, update_concern,
                            delete_concern, home, empty, some_view, export_pdf, hello_view)

urlpatterns = [
    path('create_concern/', create_concern, name='create-concern'),
    path('home/', home, name='home'),
    path('hello/<str:name>/', hello_view, name='hello'),
    path('empty/', empty, name='empty'),
    path('csv/', some_view, name='csv'),
    path('pdf/', export_pdf, name='pdf'),
    path('htmx/create-book-form/', create_concern_form,
         name='create-concern-form'),
    path('htmx/concern/<pk>/', concern_detail, name="concern-detail"),
    path('htmx/concern/<pk>/update/', update_concern, name="update-concern"),
    path('htmx/concern/<pk>/delete/', delete_concern, name="delete-concern"),


]
