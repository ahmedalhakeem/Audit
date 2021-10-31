from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass
    def __str__(self):
        employer_position = models.CharField(max_length=64, blank=True)
        return f"{self.username}"
# الغرض من الزيارة جدول
class Visit_Purpose(models.Model):
    visit_purpose= models.CharField(max_length=64, null=True)

#  جدول تصنيف الموْسسة 
class Institute_Classification(models.Model):
    type = models.CharField(max_length=64)

# جدول الموسسات  
class Institutes(models.Model):
    institute_name = models.CharField(max_length=64, blank=True)
    delegated_person = models.CharField(max_length=64, blank=True)
    location = models.CharField(max_length=100, blank=True)
    email_address = models.EmailField()
    contact_number= models.PositiveIntegerField(blank=True)
    institute_type = models.ForeignKey(Institute_Classification, on_delete=models.CASCADE, null=True, blank=True)

# جدول المراجعات
class Transactions(models.Model):
    transaction_num = models.IntegerField()
    institute = models.ForeignKey(Institutes, on_delete=models.CASCADE, null=True, blank=True)
    visit_Purpose = models.ForeignKey(Visit_Purpose, on_delete=models.CASCADE, null=True, blank=True)
    visit_date = models.DateField(auto_now=False, blank=True)
    contact_no = models.PositiveIntegerField()
    email = models.EmailField()
    document = models.ImageField()
    notes = models.CharField(max_length=100, blank=True, null=True)

#جدول حالة المراجعة
class Transactction_Status(models.Model):
    transaction = models.ForeignKey(Transactions, on_delete=models.CASCADE, null=True, blank=True)
    status = models.BooleanField(default=False)
