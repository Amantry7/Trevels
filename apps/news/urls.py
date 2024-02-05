from rest_framework.routers import DefaultRouter

from apps.news.views import NewsAPI

router = DefaultRouter()

router.register('news', NewsAPI, 'api_news')

urlpatterns = router.urls

