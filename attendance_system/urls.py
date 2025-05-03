from django.contrib import admin
from django.urls import path
from face_recognition_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('admin_portal/', views.admin_portal, name='admin_portal'),
    path('admin/view-students/', views.view_all_students, name='view_students'),
    path('admin/sync-attendance/', views.sync_attendance, name='sync_attendance'),
    path('admin/daily-report/', views.generate_daily_report, name='generate_daily_report'),
    path('register/', views.register, name='register'),
    path('students/', views.students, name='students'),
    path('attendance/', views.attendance, name='attendance'),
    path('details/', views.attendance_details, name='details'),
    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('edit_student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('filter_attendance/', views.filter_attendance, name='filter_attendance'),
    path('export_attendance/', views.export_attendance, name='export_attendance'),

]
