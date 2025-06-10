from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework.settings import settings



router=DefaultRouter()
router.register(r"role",RoleViewset)
router.register(r"department",DepartmentViewset)
router.register(r"designation",DesignationViewset)
router.register(r"report",reportViewset)
router.register(r"poc",POCsViewset)
router.register(r"contrib",ContribViewset)
router.register(r"employee",EmployeeViewSet)
router.register(r"stake",StakeholderViewset)
router.register(r"immediate",ImmediateViewset)
router.register(r"incident",RaisetktViewset)
router.register(r"statustaken",StatustakenViewset)
# router.register(r"recomm",RecommendationViewset)
# router.register(r"follow",FollowUpViewset)
router.register(r"status",StatusViewset)
# router.register(r"evidence",IncidentevidenceViewset)


urlpatterns=[
    path("",include(router.urls)),
  
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)