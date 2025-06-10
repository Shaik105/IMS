from django.shortcuts import render
from Incidentapp.models import *
from Incidentapp.serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class RoleViewset(viewsets.ModelViewSet):
    queryset=role.objects.all()
    serializer_class=roleSerializer

class DepartmentViewset(viewsets.ModelViewSet):
    queryset=department.objects.all()
    serializer_class=departmentSerializer

class DesignationViewset(viewsets.ModelViewSet):
    queryset=designation.objects.all()
    serializer_class=designationSerializer

class reportViewset(viewsets.ModelViewSet):
    queryset=report_type.objects.all()
    serializer_class=reportSerailizer

class ContribViewset(viewsets.ModelViewSet):
    queryset=contributing_factor.objects.all()
    serializer_class=contribSerializer

        
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    serializer_class = EmployeeSerializer

        
class POCsViewset(viewsets.ModelViewSet):
    queryset = POCs.objects.all()
    serializer_class = pocsSerializer


class StakeholderViewset(viewsets.ModelViewSet):
    queryset = stake_holder.objects.all()
    serializer_class = stakeholderSerializer

class ImmediateViewset(viewsets.ModelViewSet):
    queryset = ImmediateAction.objects.all()
    serializer_class = immediateSerializer

class RecommendationViewset(viewsets.ModelViewSet):
    queryset = Recommendations.objects.all()
    serializer_class = recommSerializer

class FollowUpViewset(viewsets.ModelViewSet):
    queryset = FollowUpActions.objects.all()
    serializer_class = followSerializer
    
class StatusViewset(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = statusSerializer

class StatustakenViewset(viewsets.ModelViewSet):
    queryset = Statustaken.objects.all()
    serializer_class = statustakenSerializer

class IncidentevidenceViewset(viewsets.ModelViewSet):
    queryset = IncidentEvidence.objects.all()
    serializer_class = evidenceSerializer

class RaisetktViewset(viewsets.ModelViewSet):
    queryset = Incident_ticket.objects.all()
    serializer_class = IncidentSerializer
 
        




# class finalViewset(viewsets.ModelViewSet):
#     queryset=Incident_evidence.objects.all()
#     serializer_class=Incidentprofile1


    