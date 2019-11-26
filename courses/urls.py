from django.urls import path

from . import views

urlpatterns = [
    path('', views.CoursesAdminListView.as_view(), name='courses_admin_list'),
    path('new/',
         views.CoursesAdminCreateView.as_view(), name='courses_admin_new'),
    path('<int:pk>/edit/',
         views.CoursesAdminUpdateView.as_view(), name='courses_admin_edit'),
    path('<int:pk>/',
         views.CoursesAdminDetailView.as_view(), name='courses_admin_detail'),
    path('<int:pk>/delete/',
         views.CoursesAdminDeleteView.as_view(), name='courses_admin_delete'),
]
