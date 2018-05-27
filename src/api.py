from rest_framework.routers import DefaultRouter
from mainapp.views import GroupsViewSet, ElementsViewSet


router = DefaultRouter()

router.register('groups', GroupsViewSet)
router.register('elements', ElementsViewSet)
