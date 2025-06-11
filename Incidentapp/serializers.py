from rest_framework import serializers
from Incidentapp.models import *
from rest_framework.serializers import *



# class incidentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Incident_ticket
#         fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name','password', 'email']


class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=employee
        fields="__all__"


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=CustomUser
#         fields="__all__"

class roleSerializer(serializers.ModelSerializer):
    class Meta:
        model=role
        fields="__all__"

class departmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=department
        fields="__all__"

class designationSerializer(serializers.ModelSerializer):
    class Meta:
        model=designation
        fields="__all__"

class reportSerailizer(serializers.ModelSerializer):
    class Meta:
        model=report_type
        fields="__all__"

class pocsSerializer(serializers.ModelSerializer):
    class Meta:
        model=POCs
        fields="__all__"

class contribSerializer(serializers.ModelSerializer):
    class Meta:
        model=contributing_factor
        fields="__all__"


class stakeholderSerializer(serializers.ModelSerializer):
    class Meta:
        model=stake_holder
        fields="__all__"




class recommSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recommendations
        fields=["actions","emp_id"]

class followSerializer(serializers.ModelSerializer):
    class Meta:
        model=FollowUpActions
        fields=["actions_title","responsible_emp_id"]

class evidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model=IncidentEvidence
        fields="__all__"

class statusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Status
        fields="__all__"

class statustakenSerializer(serializers.ModelSerializer):
    class Meta:
        model=Statustaken
        fields="__all__"


class Incidentprofile1(serializers.ModelSerializer):
    class Meta:
        model=Incident_ticket
        fields=["id"]
    def to_representation(self,instance):
        rep=super().to_representation(instance)
        rep["reporter"]={"name":instance.reporter.user_id.first_name + instance.reporter.user_id.last_name,
                        "designation":instance.reporter.desig_id.desig_name}
        rep["report_type"]=instance.report_type.rept_type
        rep["assigned_pocs"]=pocsSerializer(instance.assigned_pocs).data
        rep["department"]={"dep_id":instance.department.dept_id,"dept_name":instance.department.dept_name}
        rep["location"]=instance.location
        rep["date"]=instance.date
        if instance.assigned_pocs is not None:
            rep["assigned_pocs"]={"name":instance.assigned_pocs.emp_id.user_id.first_name}
        else:
            rep["assigned_pocs"]=""
        print(contribSerializer(instance.contributing_factor,many=True).data)
        rep["contributing_factor"]=[i["contrib_name"] for i in contribSerializer(instance.contributing_factor,many=True).data]
        print(rep)
        return rep
    
# class EmployeeSerializer(serializers.ModelSerializer):
#     first_name=serializers.CharField()
#     last_name=serializers.CharField()
#     email=serializers.CharField()
#     password=serializers.CharField()
#     department=serializers.CharField()
#     role=serializers.CharField()
#     class Meta:
#         model=employee
#         # fields=["job_title","emp_id","desig_id","contact"]
#     def create(self, validated_data):
#         # Yahan custom logic likho
#         instance = employee.objects.create(**validated_data)
#         return instance




class EmployeeSerializer(serializers.ModelSerializer):
    user_id=UserSerializer()

    class Meta:
        model = employee
        fields = "__all__"

    def create(self,validated_data):
        user=validated_data.pop("user_id")

        user=CustomUser.objects.create(**user)
        user.save()
        Employee=employee.objects.create(user_id=user,**validated_data)
        Employee.save()
        return Employee
    
class immediateSerializer(serializers.ModelSerializer):
    class Meta:
        model=ImmediateAction
        fields= ["emp_id","description"]



class IncidentSerializer(serializers.ModelSerializer):
    immediateactions = immediateSerializer(required =False,many=True)
    status=statusSerializer(required=False,many=True)
    Follow=followSerializer(required=False,many=True)
    Recommendations=recommSerializer(required=False,many=True)
 

    class Meta:
        model = Incident_ticket
        fields = ["id","reporter","report_type","location","department","description","contributing_factor","individual_involved","witnesses","immediateactions","assigned_pocs","status","Follow","Recommendations"]
          
        

    def create(self, validated_data):
        contributing_factor = validated_data.pop("contributing_factor")
        individual_involved = validated_data.pop("individual_involved")
        witnesses = validated_data.pop("witnesses")
        immediate_actions_data = validated_data.pop('immediateactions')
        FollowUpActions_data=validated_data.pop('Follow')
        Recommendations_data=validated_data.pop("Recommendations")

       
        
        depp=validated_data.get("department")
        pocss=depp.poc.first()
        validated_data["assigned_pocs"]=pocss
        print(validated_data["assigned_pocs"])

      
        ticket = Incident_ticket.objects.create(**validated_data)
        
        for i in contributing_factor:
            ticket.contributing_factor.add(i)
        for i in individual_involved:
            ticket.individual_involved.add(i)
        for i in witnesses:
            ticket.witnesses.add(i)
        for emp_data in FollowUpActions_data:
            FollowUpActions.objects.create(**emp_data, id=ticket)
        

        print(FollowUpActions_data)

        for recom_data in Recommendations_data:
            Recommendations.objects.create(id=ticket,**recom_data)
        


        for action_data in immediate_actions_data:
            employees = action_data.pop("emp_id")
            action = ImmediateAction.objects.create(incident_id=ticket,**action_data)
        for i in employees:
            action.emp_id.add(i)  
            # actionss.emp_id.set(employees)


        status_obj = Status.objects.get(status="Open")
        Statustaken.objects.create(status_id=status_obj, id=ticket)
        print(status_obj.status)

        
        return ticket





        
