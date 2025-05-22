from note.views import *
from note.views2 import *
from django.urls import path

urlpatterns = [
    path('show/', show, name='show'),
    path('note/', shownote, name='shownote'),
    path('post/', post, name='post'),
    path('add/', add, name='add'),
    path('update/<int:student_id>/', update, name='update'),
    path('noteupdate/<int:student_id>/', noteupdate, name='noteupdate'),
    path('delete/<int:student_id>/', delete, name='delete'),
    path('deletenote/<int:student_id>/', deletenots, name='deletenote'),
    path('getnote/<int:student_id>/', getnote , name='getnote'),
    path('get/<int:student_id>/', get , name='get'),

]