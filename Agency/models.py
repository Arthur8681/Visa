from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255)
    country_code = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class VisaType(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.country.name}"

class Employee(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.last_name} {self.name}"

class Client(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField()
    passport_data = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.last_name} {self.name}"

class Application(models.Model):
    date_of_submission = models.DateField()
    status = models.CharField(max_length=50)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    visa_type = models.ForeignKey(VisaType, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Application {self.id} for {self.client}"

class Payment(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    payment_date = models.DateField()
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField()  

    def __str__(self):
        return f"Payment {self.id} for Application {self.application.id}"

class Document(models.Model):
    name = models.CharField(max_length=255)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    required = models.BooleanField(default=True)
    verification_status = models.IntegerField() 

    def __str__(self):
        return f"{self.name} for Application {self.application.id}"