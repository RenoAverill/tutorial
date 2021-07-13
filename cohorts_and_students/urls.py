from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('', views.cohorts_list, name='cohorts_list'),
    path('<int:cohort_id>', views.cohort_detail, name='cohort_detail'),
    path('<int:cohort_id>/delete', views.cohort_delete, name='cohort_delete'),
    path('new', views.cohort_new, name='cohort_new'),
    # path('<int:cohort_id>/edit', views.cohort_edit, name='cohort_edit'),
]
