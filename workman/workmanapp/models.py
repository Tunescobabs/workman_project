from django.db import models


# Create your models here.
class artisan(models.Model):
    artisan_id =  models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=120, default='', blank=True, null=True)
    service_type_choices = (
        ('Mechanic', 'Mechanic'), ('Plumber', 'Plumber'), ('Barber','Barber'), ('Tailor', 'Tailor'),
        ('Electrician', 'Electrician'), ('Hairdresser', 'Hairdresser')
    )
    service_type = models.CharField(max_length=50, default='', blank=True, null=True, choices=service_type_choices)
    date_of_birth = models.DateTimeField(auto_now=False, auto_now_add=False)
    nigerian_states_choices = (  ('Abia', 'Abia'), ('Adamawa', 'Adamawa'), ('Akwa Ibom', 'Akwa Ibom'), ('Anambra', 'Anambra'), 

     ('Bauchi','Bauchi'), ('Bayelsa', 'Bayelsa'), ('Benue', 'Benue'), ('Borno', 'Borno'), ('Cross River', 'Cross River'), ('Delta', 'Delta'),
     ('Ebonyi', 'Ebonyi'), ('Edo', 'Edo'), ('Ekiti', 'Ekiti'), ('Enugu', 'Enugu'), ('Gombe', 'Gombe'), ('Imo', 'Imo'),
     ('Jigawa', 'Jigawa'), ('Kaduna', 'Kaduna'), ('Kano', 'Kano'), ('Katsina', 'Katsina'), ('Kebbi', 'Kebbi'), ('Kogi', 'Kogi'), 
     ('Kwara', 'Kwara'), ('Lagos', 'Lagos'), ('Nasarawa', 'Nasarawa'), ('Niger', 'Niger'), ('Ogun', 'Ogun'), ('Ondo', 'Ondo'), ('Osun', 'Osun'),
     ('Oyo', 'Oyo'), ('Plateau', 'Plateau'), ('Rivers', 'Rivers'), ('Sokoto', 'Sokoto'), ('Taraba', 'Taraba'), ('Yobe', 'Yobe'), ('Zamfara', 'Zamfara')
    
    )
    state = models.CharField(max_length=50, default='', blank=True, null=True, choices=nigerian_states_choices)
    def __str__(self):
        return self.first_name+' '+self.last_name