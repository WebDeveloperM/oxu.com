from django.db import models

# Create your models here.


class Info(models.Model):
    title = models.CharField(max_length=100)
    count = models.IntegerField()

    def __str__(self):
        return self.title


class Announcement(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title


class Direction(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title


class Support(models.Model):
    name = models.CharField(max_length=50)
    surename = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    is_payment = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.surename}"


class Contract(models.Model):
    name = models.CharField(max_length=50)
    surename = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    second_phone = models.CharField(max_length=20)
    age = models.CharField(max_length=50, null=True, blank=True)
    contract_type = models.CharField(max_length=50)
    stady_lang = models.CharField(max_length=50)
    stady_type = models.CharField(max_length=50)
    education_form = models.CharField(max_length=50)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    payment_check = models.ImageField()
    is_payment = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.surename}"
