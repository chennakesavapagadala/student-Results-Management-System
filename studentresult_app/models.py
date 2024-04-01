from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class SscResult(models.Model):
    name        = models.OneToOneField(User, on_delete=models.CASCADE)
    hall_ticket = models.IntegerField()
    telugu      = models.IntegerField(default=0)
    hindi       = models.IntegerField(default=0)
    english     = models.IntegerField(default=0)
    maths       = models.IntegerField(default=0)
    science     = models.IntegerField(default=0)
    social      = models.IntegerField(default=0)
    total      = models.IntegerField(default=0)

    def __str__(self):
        return f" {self.name.first_name} Result"

class InterResult1(models.Model):
    name        = models.OneToOneField(User, on_delete=models.CASCADE)
    hall_ticket = models.IntegerField()
    sanskrit    = models.IntegerField(default=0)
    english     = models.IntegerField(default=0)
    maths_A     = models.IntegerField(default=0)
    maths_B     = models.IntegerField(default=0)
    physics     = models.IntegerField(default=0)
    chemistry   = models.IntegerField(default=0)
    practicals  = models.IntegerField(default=0)
    total       = models.IntegerField(default=0)

    def __str__(self):
        return f" {self.name.first_name} Result"

class InterResult2(models.Model):
    name        = models.OneToOneField(User, on_delete=models.CASCADE)
    hall_ticket = models.IntegerField()
    sanskrit    = models.IntegerField(default=0)
    english     = models.IntegerField(default=0)
    maths_A     = models.IntegerField(default=0)
    maths_B     = models.IntegerField(default=0)
    physics     = models.IntegerField(default=0)
    chemistry   = models.IntegerField(default=0)
    practicals  = models.IntegerField(default=0)
    total       = models.IntegerField(default=0)

    def __str__(self):
        return f" {self.name.first_name} Result"


class DegreeResult1(models.Model):
    name        = models.OneToOneField(User, on_delete=models.CASCADE)
    hall_ticket = models.IntegerField()
    telugu    = models.IntegerField(default=0)
    english     = models.IntegerField(default=0)
    mathematics     = models.IntegerField(default=0)
    physics     = models.IntegerField(default=0)
    computer_science   = models.IntegerField(default=0)
    practicals  = models.IntegerField(default=0)
    total       = models.IntegerField(default=0)

    def __str__(self):
        return f" {self.name.first_name} Result"

class DegreeResult2(models.Model):
    name        = models.OneToOneField(User, on_delete=models.CASCADE)
    hall_ticket = models.IntegerField()
    mathematics_I    = models.IntegerField(default=0)
    mathematics_II   = models.IntegerField(default=0)
    physics_I     = models.IntegerField(default=0)
    physics_II    = models.IntegerField(default=0)
    computer_science_I  = models.IntegerField(default=0)
    computer_science_II = models.IntegerField(default=0)
    practicals  = models.IntegerField(default=0)
    total      = models.IntegerField(default=0)

    def __str__(self):
        return f" {self.name.first_name} Result"

class DegreeResult3(models.Model):
    name        = models.OneToOneField(User, on_delete=models.CASCADE)
    hall_ticket = models.IntegerField()
    mathematics_V_theory    = models.IntegerField(default=0)
    mathematics_V_practical     = models.IntegerField(default=0)
    mathematics_VI_Theory    = models.IntegerField(default=0)
    mathematics_VI_practical     = models.IntegerField(default=0)
    computer_science   = models.IntegerField(default=0)
    physics = models.IntegerField(default=0)
    practicals  = models.IntegerField(default=0)
    total      = models.IntegerField(default=0)

    def __str__(self):
        return f" {self.name.first_name} Result"

class BtechResult1(models.Model):
    name        = models.OneToOneField(User, on_delete=models.CASCADE)
    hall_ticket = models.IntegerField()
    english    = models.IntegerField(default=0)
    applied_physics     = models.IntegerField(default=0)
    mathematics_I    = models.IntegerField(default=0)
    mathematics_II     = models.IntegerField(default=0)
    cit   = models.IntegerField(default=0)
    data_processing = models.IntegerField(default=0)
    C_data_structures  = models.IntegerField(default=0)
    total      = models.IntegerField(default=0)

    def __str__(self):
        return f" {self.name.first_name} Result"

class BtechResult2(models.Model):
    name        = models.OneToOneField(User, on_delete=models.CASCADE)
    hall_ticket = models.IntegerField()
    computer_organization    = models.IntegerField(default=0)
    operating_systems    = models.IntegerField(default=0)
    oops    = models.IntegerField(default=0)
    data_communications    = models.IntegerField(default=0)
    operations_research   = models.IntegerField(default=0)
    system_rogramming = models.IntegerField(default=0)
    total      = models.IntegerField(default=0)

    def __str__(self):
        return f" {self.name.first_name} Result"


class BtechResult3(models.Model):
    name        = models.OneToOneField(User, on_delete=models.CASCADE)
    hall_ticket = models.IntegerField()
    computer_architecture    = models.IntegerField(default=0)
    ds_and_algorithms     = models.IntegerField(default=0)
    data_mining    = models.IntegerField(default=0)
    wireless_network     = models.IntegerField(default=0)
    ai   = models.IntegerField(default=0)
    computer_graphics = models.IntegerField(default=0)
    total      = models.IntegerField(default=0)

    def __str__(self):
        return f" {self.name.first_name} Result"

class BtechResult4(models.Model):
    name        = models.OneToOneField(User, on_delete=models.CASCADE)
    hall_ticket = models.IntegerField()
    se    = models.IntegerField(default=0)
    cc     = models.IntegerField(default=0)
    jp    = models.IntegerField(default=0)
    ip     = models.IntegerField(default=0)
    nn   = models.IntegerField(default=0)
    mc = models.IntegerField(default=0)
    total      = models.IntegerField(default=0)

    def __str__(self):
        return f" {self.name.first_name} Result"
