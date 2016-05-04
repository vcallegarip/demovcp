from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.conf import settings


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, has_company=False, company_id=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username.')

        if has_company is True and not company_id:
            raise ValueError('You have to enter the your company code.')

        account = self.model(
            email=self.normalize_email(email),
            username=kwargs.get('username')
        )

        account.set_password(password)
        account.save()
        # account.id

        create_account(company_id, account.id)

        return account

    # def create_superuser(self, email, password, **kwargs):
    #     account = self.create_user(email, password, **kwargs)
    #
    #     account.is_admin = True
    #     account.save()
    #
    #     return account

    def create_account(self, company_id, user_id, **kwargs):
        account = Account.objects.create(company_id = company_id, user_id = user_id)
        account.save()
        return account


class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    has_company = models.BooleanField(default=False)
    InterjectUserID = models.CharField(max_length=40, blank=True)
    IsEmployee = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta(object):
        db_table = 'data_account'

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

    # @property
    # def is_superuser(self):
    #     return self.is_admin
    #
    # @property
    # def is_staff(self):
    #     return self.is_admin
    #
    # def has_perm(self, perm, obj=None):
    #     return self.is_admin
    #
    # def has_module_perms(self, app_label):
    #     return self.is_admin
