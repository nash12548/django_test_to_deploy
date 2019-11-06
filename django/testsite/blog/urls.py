from django.urls import path
from .views import about_page, home_page, contact_page, blog_create_view, blog_delete_view, blog_detail_view, \
    blog_list_view, blog_update_view, test_page, test2_page, test3_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('about/', about_page, name='about_page'),
    path('contact/', contact_page, name='contact_page'),
    path('list/', blog_list_view),
    path('test/', test_page),
    path('test2/', test2_page),
    path('test3/', test3_page),
    path('create/', blog_create_view),
    path('list/<str:slug>/edit/', blog_update_view, name='edit'),
    path('list/<str:slug>/delete/', blog_delete_view, name='delete'),
    path('list/<str:slug>/', blog_detail_view, name='detail'),

]
