from rest_framework import routers

from ads.views import AdViewSet, CommentViewSet

ads_router = routers.SimpleRouter()
ads_router.register("ads", AdViewSet)
ads_router.register("ads/(?P<ad_pk>[^/.]+)/comments", CommentViewSet)
