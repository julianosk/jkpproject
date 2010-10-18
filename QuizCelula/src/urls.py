from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'views.index'),
    (r'^results$', 'views.results'),
    (r'^quests$', 'views.quests'),
)
