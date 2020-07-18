from django.urls import path
# , reverse
# from django.http import HttpResponse

from . import views

app_name = 'polls'

# def abc(reqeust):
#     url =  reverse('polls:votes', kwargs={'question_id': 4})
#     return HttpResponse('asdlfjsld: ' + url)

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),    
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='votes'),
    # path('xyz', abc)

]
