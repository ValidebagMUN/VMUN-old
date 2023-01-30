from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

from institution.models import Institution
from committee.models import Committee
from importer.models import Delegation
# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password = None):
        if not email or len(email) <= 0: 
            raise  ValueError("Email field is required!")
        if not password:
            raise ValueError("Password is necessary!")
          
        user = self.model(
            email = self.normalize_email(email), 
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(
            email = self.normalize_email(email), 
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    class Types(models.TextChoices):
        CHAIRPERSON = 'chairperson', 'Chairperson'
        ASSISTANT = 'assistant', 'Assistant'
        DELEGATE = 'delegate', 'Delegate'
        ADMIN = 'admin', 'Admin'
        STAFF = 'staff', 'Staff'

    name = models.CharField(max_length=40)
    type = models.CharField(max_length = 15, choices = Types.choices, default = Types.DELEGATE)
    email = models.EmailField(max_length = 200, unique = True)
    phone = models.CharField(max_length = 20, unique = True, null = True)
    is_active = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
      
    # special permission which define that
    # the new user is teacher or student 
    is_delegate = models.BooleanField(default = False)
    is_chairperson = models.BooleanField(default = False)
    is_assistant = models.BooleanField(default = False)
      
    USERNAME_FIELD = "email"
      
    # defining the manager for the UserAccount model
    objects = UserAccountManager()
      
    def __str__(self):
        return str(self.name)

    def has_perm(self , perm, obj = None):
        return self.is_admin
      
    def has_module_perms(self , app_label):
        return True
      
    def save(self , *args , **kwargs):
        if not self.type or self.type == None : 
            self.type = UserAccount.Types.DELEGATE
        return super().save(*args , **kwargs)


class DelegateManager(models.Manager):
    def create_user(self , email , password = None):
        if not email or len(email) <= 0 : 
            raise  ValueError("Email field is required !")
        if not password :
            raise ValueError("Password is necessary!")
        email  = email.lower()
        user = self.model(
            email = email
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def get_queryset(self , *args,  **kwargs):
        queryset = super().get_queryset(*args , **kwargs)
        queryset = queryset.filter(type = UserAccount.Types.DELEGATE)
        return queryset  

class DelegateProxy(UserAccount):
    is_delegate = True
    class Meta :
        proxy = True
    objects = DelegateManager()
      
    def save(self  , *args , **kwargs):
        self.type = UserAccount.Types.DELEGATE
        self.is_teacher = True
        return super().save(*args , **kwargs)

class Delegate(DelegateProxy):
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE, help_text='Committee of the delegate')
    delegation = models.ForeignKey(Delegation, on_delete=models.CASCADE, help_text='Delegation of the delegate', blank=True, null=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, help_text='Institution of the delegate')
    country = models.CharField(max_length=40, help_text='Country allocation of the delegate', blank=True, null=True)

    def isInCommittee(self, *args, **kwargs):
        return self.committee.slug == kwargs['committee_slug']
  

class AssistantManager(models.Manager):
    def create_user(self , email , password = None):
        if not email or len(email) <= 0 : 
            raise  ValueError("Email field is required !")
        if not password :
            raise ValueError("Password is necessary!")
        email  = email.lower()
        user = self.model(
            email = email
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
      
    def get_queryset(self , *args,  **kwargs):
        queryset = super().get_queryset(*args , **kwargs)
        queryset = queryset.filter(type = UserAccount.Types.ASSISTANT)
        return queryset  

class AssistantProxy(UserAccount):
    is_assistant = True
    class Meta :
        proxy = True
    objects = AssistantManager()
      
    def save(self  , *args , **kwargs):
        self.type = UserAccount.Types.ASSISTANT
        self.is_teacher = True
        return super().save(*args , **kwargs)

class Assistant(AssistantProxy):
    committee = models.OneToOneField(Committee, on_delete=models.CASCADE, help_text='Committee of the academic assistant')

    def isInCommittee(self, *args, **kwargs):
        return self.committee.slug == kwargs['committee_slug']


class ChairPersonManager(models.Manager):
    def create_user(self , email , password = None):
        if not email or len(email) <= 0 : 
            raise  ValueError("Email field is required !")
        if not password :
            raise ValueError("Password is must !")
        email  = email.lower()
        user = self.model(
            email = email
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
      
    def get_queryset(self , *args,  **kwargs):
        queryset = super().get_queryset(*args , **kwargs)
        queryset = queryset.filter(type = UserAccount.Types.CHAIRPERSON)
        return queryset  

class ChairPersonProxy(UserAccount):
    is_chairperson = True
    class Meta :
        proxy = True
    objects = ChairPersonManager()
      
    def save(self  , *args , **kwargs):
        self.type = UserAccount.Types.CHAIRPERSON
        self.is_teacher = True
        return super().save(*args , **kwargs)

class ChairPerson(ChairPersonProxy):
    committee = models.OneToOneField(Committee, on_delete=models.CASCADE, blank=True, null=True)
    Institution = models.ForeignKey(Institution, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Chairperson'
        verbose_name_plural = 'Chairpeople'

    def isCommitteeChair(self, *args, **kwargs):
        return Committee.objects.get(slug=kwargs['committee_slug']) == self.committee