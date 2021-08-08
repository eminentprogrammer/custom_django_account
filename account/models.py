from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings

def upload_location(instance, filename):
    file_path = 'Clients/{client_id}/Photo/{filename}'.format(
        client_id=str(instance.username), filename=filename)
    return file_path


class MyAccountManager(BaseUserManager):
    def create_superuser(self, email, username, password):
        if not email:
            raise ValueError('Users must have a College email address') 
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            )
        user.is_student = True
        user.is_admin   = True
        user.is_staff   = True
        user.is_superuser = True
        user.save(using = self._db)
        return user
        
        
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('User enter a valid email address')
        elif not username:
            raise ValueError('User must enter a unique username')
        user = self.model(
                email=self.normalize_email(email),
                username=username,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user




class Account(AbstractBaseUser):
    image		 	= models.ImageField(upload_to=upload_location, null=True, blank=True)
    username        = models.CharField(max_length=150, unique=True)
    phone_number    = models.CharField(max_length=17, unique=True)
    email           = models.EmailField(verbose_name='email', max_length=254, unique=True)
    date_joined     = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active       = models.BooleanField(default=True)
    is_student      = models.BooleanField(default=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username",]
    objects = MyAccountManager()
    
    class Meta:
        verbose_name_plural = "Account"
    
    def __str__(self):
        return "%s %s" %(self.username, self.email)
    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True
