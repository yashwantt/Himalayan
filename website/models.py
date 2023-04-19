
from django.db import models


class Popular_Destination(models.Model):
    title = models.CharField(max_length = 30)
    main_img = models.ImageField()
    front_img = models.ImageField(null = True)
    def __str__(self):
        return self.title



class Image(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Location")
    img = models.ImageField()
    # city = models.ForeignKey(Popular_Destination, on_delete = models.CASCADE)
    to_be_shown = models.BooleanField(default = False)

    def __str__(self):
        return self.title



class Package(models.Model):
    title = models.CharField(max_length = 200)
    starting_from = models.CharField(max_length = 100, null = True)
    desc = models.TextField(null = True)
    days = models.SmallIntegerField(default = 3)
    nights = models.SmallIntegerField(default = 3)
    front_img = models.ImageField(null = True, default = "default.jpg")
    main_img = models.ImageField(default = "default.jpg")
    cities = models.ManyToManyField(Popular_Destination)
    category = models.CharField(max_length = 100, null = True)
    volvo = models.BooleanField(default = False)
    top_package = models.BooleanField(default = False)

    def __str__(self):
        return self.title + f"({self.days}D-{self.nights}N) ({self.starting_from})"


class Inclusions(models.Model):
    title = models.CharField(max_length = 50)


class Pack_Desc(models.Model):

    def defaultImg(self):
        return Image.objects.first()


    day = models.IntegerField(default = 1)
    title = models.CharField(max_length = 100)
    desc = models.TextField(null = True, default = None)
    img = models.URLField(null = True)
    package = models.ForeignKey(Package, on_delete = models.CASCADE)

    def __str__(self):
        return self.package.title +" "+ self.title +" Day "+ str(self.day)


fuel = (
    ("Diesel", "Diesel"),
    ("Petrol", "Petrol"),
)

cats = (
    ("Sedan Cabs", "Sedan Cabs"),
    ("MUV Cabs", "MUV Cabs"),
    ("SUV Cabs", "SUV Cabs"),
    ("Minibus Cabs", "Minibus Cabs"),
    ("Rental Vehicles", "Rental Vehicles"),
    ("Rental Bikes", "Rental Bikes"),
)



class Cab(models.Model):
    title = models.CharField(max_length = 200)
    img = models.ImageField()
    price = models.IntegerField()
    ac = models.BooleanField(default = True)
    fuel = models.CharField(max_length = 20, choices = fuel, default = "Diesel")
    seats = models.SmallIntegerField(default = 4)
    popular = models.BooleanField(default = False)
    cat = models.CharField(max_length=30, default = "Rental Vehicles", choices = cats)

    def __str__(self):
        return self.title
