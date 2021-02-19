from core import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^api/dapau$', views.dapau),
    url(r'^api/login$', views.login),
    url(r'^api/logout$', views.logout),
    url(r'^api/whoami$', views.whoami),

    url(r'^api/add_todo$', views.add_todo),
    url(r'^api/list_todos$', views.list_todos),
    url(r'^api/cadastro$', views.cadastro),
    url(r'^api/listaranimais$', views.listaranimais),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
