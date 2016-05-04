from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from rest_framework_nested import routers
from authentication.views import AccountViewSet
from authentication.views import LoginView
from authentication.views import LogoutView
from django.conf.urls import patterns, url
from .views import IndexView


router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = patterns(
    '',
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),
    url(r'^.*$', IndexView.as_view(), name='index'),
)
