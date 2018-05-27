from rest_framework.routers import DefaultRouter
from mainapp.views import GroupsListView, ElementsListView


router = DefaultRouter()

router.register('groups', GroupsListView)
router.register('elements', ElementsListView)