from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.pk, filename)


# Create your models here.
class Employee(models.Model):
    """
    Employee Profile Model
    Links to User model
    """

    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    picture             = models.ImageField('Profile Picture', upload_to=user_directory_path)
    temporary_address   = models.CharField('Temporary Address', max_length=200)
    permanent_address   = models.CharField('Permanent Address', max_length=200)
    linkedin            = models.CharField(max_length=50)

    father_name         = models.CharField(max_length=50)
    father_cnic         = models.CharField(max_length=13)
    fathers_phone_no    = models.CharField(max_length=11, default="0000000")


