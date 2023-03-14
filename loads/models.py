from django.db import models

class Loads(models.Model):
    
    LOAD_TYPES=[
        ("K", 'Complate'),
        ("P", 'Parsial'),
        ("KP", 'Copm-Pars'),
        
    ]

    load_name = models.CharField(max_length=30)
    load_type = models.CharField(max_length=2, choices=LOAD_TYPES, default="K")
    weight = models.IntegerField(blank=True, null=True)
    register_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    load_pic = models.ImageField(upload_to='profile_pics', blank=True)
    

    class Meta:
        # ordering = ['first_name']
        verbose_name_plural = "Yükler"

    def __str__(self):
        return f"{self.id} {self.load_name} {self.weight}"
    
class Owner(models.Model):
    owner_name = models.CharField(max_length=30)
    owners_load = models.OneToOneField(Loads, on_delete=models.CASCADE)

    class Meta:
        # ordering = ['first_name']
        verbose_name_plural = "Yük Sahibi"

    def __str__(self):
        return f"{self.owner_name} {self.owners_load}"


class Warehouse(models.Model):
    LOCATION=[
        ("IST", 'Istanbul'),
        ("ANK", 'Ankara'),
        ("IZM", 'Izmir'),
    ]
    warehouse_name = models.CharField(max_length=30)
    warehouse_location = models.CharField(max_length=3, choices=LOCATION, default="IST")
    included_loads = models.ManyToManyField(Loads)

    class Meta:
        # ordering = ['first_name']
        verbose_name_plural = "Depolar"

    def __str__(self):
        return f"{self.warehouse_name} {self.warehouse_location} {self.included_loads}"