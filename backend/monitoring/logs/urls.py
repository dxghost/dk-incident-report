from rest_framework import routers
from logs.views import LogsViewset


router = routers.SimpleRouter()
router.register("", LogsViewset, "logs")
