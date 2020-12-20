from django.urls import path
from . import views

urlpatterns=[
    path('',views.review_list),
    path('new_review/',views.new_review),
    path('create_review/',views.create_review),
    path('review_detail/<int:review_id>',views.review_detail)
    ]