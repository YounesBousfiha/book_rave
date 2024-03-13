from django.urls import path
from .views import all_comments, get_comment, remove_comment, add_comment, update_comment

urlpatterns = [
    path('<int:review_id>/comments', all_comments),
    path('getcomment/<int:comment_id>', get_comment),
    path('deletecomment/<int:comment_id>', remove_comment),
    path('addcomment/<int:review_id>', add_comment),
    path('update/<int:comment_id>', update_comment),
]