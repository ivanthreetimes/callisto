from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.db import models
from PIL import Image

from callisto.users_app.managers import AppUsersManager


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'

    objects = AppUsersManager()


class Profile(models.Model):  # TODO - image name -> f'{user.email}...'
    FIRST_NAME_MIN_LENGTH = 3
    FIRST_NAME_MAX_LENGTH = 30

    LAST_NAME_MIN_LENGTH = 3
    LAST_NAME_MAX_LENGTH = 30

    GENDERS = [(x, x) for x in ('Male', 'Female', 'Other')]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
        ),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
        ),
    )

    gender = models.CharField(
        max_length=max([len(x) for x, _ in GENDERS]),
        choices=GENDERS,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    profile_picture = models.ImageField(
        default='default.jpg',
        upload_to='profile_pics'
    )

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
    )

    def save(  # TODO -> return super().save()...
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        """
        Reduces the size of the photo => fewer data used
        """
        super().save()
        img = Image.open(self.profile_picture.path)

        if img.height > 300 or img.width:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)

    def __str__(self):
        return f'{self.user.email} Profile'
