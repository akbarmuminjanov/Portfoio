from django.db import models

Languages_CHOISES = (
    ("nt","native"),
    ("fl","fluent")
)

# Create your models here.
class Resume(models.Model):
    photo = models.ImageField(upload_to="profile")
    about_me = models.TextField()
    full_name = models.CharField(max_length=150)
    area = models.CharField(max_length=150)
    birthday = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    mail = models.EmailField()
    location = models.CharField(max_length=70)
    resume_file = models.FileField(upload_to="file")

    def __str__(self):
        return self.full_name
        

class Languages(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    languages = models.CharField(max_length=60)
    languages_choises = models.CharField(max_length=60, choices=Languages_CHOISES)


    def __str__(self):
        return self.languages
    
class Interests(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    interests = models.CharField(max_length=150)

    def __str__(self):
        return self.interests
    
    