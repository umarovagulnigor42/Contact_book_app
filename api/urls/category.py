from rest_framework.routers import DefaultRouter

import api.views.category as views

router= DefaultRouter()
router.register("category", views.CategoryModelViewSet)

urlpatterns = router.urls