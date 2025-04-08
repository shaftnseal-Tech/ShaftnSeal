from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager,User
from .manager import CustomUserManager
import uuid
from datetime import datetime, timezone

# import uuid
from django.core.validators import RegexValidator
import random
import string



# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email=None, phone_no=None, password=None):
        if not email and not phone_no:
            raise ValueError('Users must have an email or phone number.')

        user = self.model(
            email=self.normalize_email(email) if email else None,
            phone_no=phone_no,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_no, password):
        user = self.create_user(email, phone_no, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Custom User Model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True, blank=True)

    # ✅ Adding phone number field with validation
    phone_regex = RegexValidator(
        regex=r'^[6-9]\d{9}$',
        message="Phone number must be a valid 10-digit Indian number starting with 6-9."
    )
    phone_no = models.CharField(
        validators=[phone_regex],
        max_length=10,
        unique=True,
        null=True,
        blank=True
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'   # You can change this to 'phone_no' if you prefer
    REQUIRED_FIELDS = ['phone_no']

    class Meta:
        db_table = 'Customers_auth'

    def __str__(self):
        return self.email or self.phone_no

# Customer Profile Model
class CustomerProfile(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE, related_name='profile')

    customer_name = models.CharField(max_length=100)
    address = models.TextField()
    pincode = models.CharField(max_length=6)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    gst_no = models.CharField(max_length=15, blank=True, null=True, unique=True)
    customer_no = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'Customers'

    def __str__(self):
        return f"{self.customer_name} ({self.customer_no})"

    def save(self, *args, **kwargs):
        if not self.customer_no:
            self.customer_no = self.generate_customer_no()

        if not self.gst_no:
            self.gst_no = self.generate_gst_no()

        super().save(*args, **kwargs)

    @staticmethod
    def generate_customer_no():
        prefix = "CUST"
        unique_id = uuid.uuid4().hex[:6].upper()
        return f"{prefix}-{unique_id}"

    @staticmethod
    def generate_gst_no():
        state_code = '27'
        pan_letters = ''.join(random.choices(string.ascii_uppercase, k=5))
        pan_digits = ''.join(random.choices(string.digits, k=4))
        pan_last = random.choice(string.ascii_uppercase)
        pan = f"{pan_letters}{pan_digits}{pan_last}"

        entity_code = str(random.randint(1, 9))
        default_z = 'Z'
        checksum = random.choice(string.ascii_uppercase + string.digits)

        gst_no = f"{state_code}{pan}{entity_code}{default_z}{checksum}"

        # Ensure uniqueness
        if CustomerProfile.objects.filter(gst_no=gst_no).exists():
            return CustomerProfile.generate_gst_no()

        return gst_no

