from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet)

api_urlpatterns = router.urls