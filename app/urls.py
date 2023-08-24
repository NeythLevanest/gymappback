from django.urls import path


from app.views import *

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns 



router = routers.SimpleRouter()

# router.register(r'users', UsersTableConfigViewSet)
router.register(r'user-type-client', UserTypeClientViewSet)
router.register(r'user-basic', UserBasicaViewSet)
router.register(r'sign-up', RegisterUserTableViewSet)
urlpatterns = router.urls