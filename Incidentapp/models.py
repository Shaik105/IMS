from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        
        if not email:
            raise ValueError(("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)

class role(models.Model):
    role_id=models.AutoField(primary_key=True)
    role_name=models.CharField(max_length=20)

class CustomUser(AbstractUser):
    username=None
    role=models.ForeignKey(role,on_delete=models.CASCADE,null=True)
    email=models.EmailField(unique=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    object=CustomUserManager()

    def __str__(self):
        return self.email


class Incident_ticket(models.Model):
    id=models.AutoField(primary_key=True)
    reporter=models.ForeignKey('employee',on_delete=models.CASCADE)
    report_type=models.ForeignKey('report_type',on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    location=models.CharField(max_length=40)
    description=models.CharField(max_length=100,null=True)
    department=models.ForeignKey('department',on_delete=models.CASCADE)
    assigned_pocs=models.ForeignKey('POCs',on_delete=models.CASCADE,null=True)
    risk_level=models.CharField(max_length=10,null=True)
    potential_severity=models.CharField(max_length=50,null=True)
    likelihood_of_Recurrence=models.CharField(max_length=50,null=True)
    contributing_factor=models.ManyToManyField('contributing_factor',db_table="IncidentFactor")
    witnesses=models.ManyToManyField("employee",db_table="Witness",related_name="wit")
    individual_involved=models.ManyToManyField("employee",db_table="IndividualInvolved",related_name="indi")
    recommendation=models.ManyToManyField("employee",through="Recommendations",related_name="recomm",null=True)
    follow_up_actions=models.ManyToManyField("employee",through="FollowUpActions",related_name="follow",null=True)
    status=models.ManyToManyField("Status",through="Statustaken",related_name="sta",null=True)

    
    
class ImmediateAction(models.Model):
    immediate_id=models.AutoField(primary_key=True)
    description=models.CharField(max_length=100)
    incident_id=models.ForeignKey("Incident_ticket",on_delete=models.CASCADE, null = True , related_name="immediateactions")
    emp_id=models.ManyToManyField("employee", db_table="Immediate_action_employee", related_name="action")


    
class Recommendations(models.Model):
    recomm_id=models.AutoField(primary_key=True)
    actions=models.CharField(max_length=100)
    emp_id=models.ForeignKey("employee",on_delete=models.CASCADE)
    id=models.ForeignKey("Incident_ticket",on_delete=models.CASCADE)



class FollowUpActions(models.Model):
    follow_id=models.AutoField(primary_key=True)
    actions_title=models.CharField(max_length=100)
    date_Completed=models.DateField(auto_now_add=True)
    responsible_emp_id=models.ForeignKey("employee",on_delete=models.CASCADE)
    id=models.ForeignKey("Incident_ticket",on_delete=models.CASCADE)

class Status(models.Model):
    status_id=models.AutoField(primary_key=True)
    status=models.CharField(max_length=50)

class Statustaken(models.Model):
    statustaken_id=models.AutoField(primary_key=True)
    date=models.DateTimeField(auto_now_add=True)
    status_id=models.ForeignKey("Status",on_delete=models.CASCADE)
    id=models.ForeignKey("Incident_ticket",on_delete=models.CASCADE)


class IncidentEvidence(models.Model):
    evidence_id=models.AutoField(primary_key=True)
    file=models.FileField(upload_to="file/")
    id=models.ForeignKey("Incident_ticket",on_delete=models.CASCADE,related_name="evi")



class employee(models.Model):
    emp_id=models.AutoField(primary_key=True)
    job_title=models.CharField(max_length=20)
    contact=models.BigIntegerField(null=True)
    desig_id=models.ForeignKey('designation',on_delete=models.CASCADE,related_name="designations")
    user_id=models.ForeignKey('CustomUser',on_delete=models.CASCADE,related_name="employee")


class department(models.Model):
    dept_id=models.AutoField(primary_key=True)
    dept_name=models.CharField(max_length=20)

class designation(models.Model):
    desig_id=models.AutoField(primary_key=True)
    desig_name=models.CharField(max_length=20 )
    dept_id=models.ForeignKey('department',on_delete=models.CASCADE)

class report_type(models.Model):
    rep_id=models.AutoField(primary_key=True)
    rept_type=models.CharField(max_length=100)
    dept_id=models.ForeignKey('department',on_delete=models.CASCADE)

    
class contributing_factor(models.Model):
    contrib_id=models.AutoField(primary_key=True)
    contrib_name=models.CharField(max_length=50)

class POCs(models.Model):
    pocs_id=models.AutoField(primary_key=True)
    dept_id=models.ForeignKey('department',on_delete=models.CASCADE,related_name="poc")
    emp_id=models.ForeignKey('employee',on_delete=models.CASCADE)


class stake_holder(models.Model):
    stake_id=models.AutoField(primary_key=True)
    user_id=models.OneToOneField(CustomUser,on_delete=models.CASCADE)

