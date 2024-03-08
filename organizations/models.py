from django.db import models

# Create your models here.
class Organization(models.Model):
    
    ORGANIZATION_University = 'U'
    ORGANIZATION_Company = 'C'
    
    ORGANIZATION_TYPE = [
        (ORGANIZATION_University, 'University'),
        (ORGANIZATION_Company, 'Company'),
    ]
    
    name = models.CharField(max_length = 150)
    description = models.CharField(max_length = 250)
    country = models.CharField(max_length = 100) 
    city = models.CharField(max_length = 100)
    org_type = models.CharField(max_length = 1, choices = ORGANIZATION_TYPE, default = "University")
    website = models.URLField()
    logo_url = models.URLField()