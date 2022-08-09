from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.core.validators import MaxValueValidator
from pyzipcode import ZipCodeDatabase

# Create your models here.

#------------------------------------------------------------------------------------------
#                               ** Profile Model **
# This model holds all of the relevant information from the user that comprises their
# personal profile. It includes the corresponding user, their avatar, their location, a bio, 
# and all the information pertinent to them as a musician.
#------------------------------------------------------------------------------------------
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='profile_images/default.jpg', upload_to='profile_pics')

    experience_level_choices = (
        ("Beginner","Beginner"),
        ("Intermediate","Intermediate"),
        ("Advanced","Advanced"),
        ("Professional","Professional"),
    )

    instrument_choices = (
        ("Guitar","Guitar"),
        ("Bass","Bass"),
        ("Drums","Drums"),
        ("Keyboard","Keyboard"),
    )

     # Create fields for the profile 
    instruments = models.TextField(choices = instrument_choices)
    singer = models.BooleanField(default=False)
    experience_level = models.TextField(choices = experience_level_choices)
    goals = models.TextField(max_length=300)
    music_production_experience = models.BooleanField(default=False)
    location = models.TextField(max_length=300)
    location_zip = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(99999)])
    associated_acts = models.TextField(max_length=300)
    profile_text = models.TextField(max_length=500)
    endorsements = models.ManyToManyField(User, related_name='endorsements')


    def __str__(self):
        return f'{self.user.username} Profile'

class ThreadModel(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
	receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')

class MessageModel(models.Model):
	thread = models.ForeignKey('ThreadModel', related_name='+', on_delete=models.CASCADE, blank=True, null=True)
	sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
	receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
	body = models.CharField(max_length=1000)
	date = models.DateTimeField(default=timezone.now)
    