from django.contrib.auth.base_user import BaseUserManager


# Define User manager
class UserManager(BaseUserManager):
    use_in_migrations = True

    # Define user creation method
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set!')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    

    # User creation callback method
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)


    # Superuser creation method
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        return self._create_user(email, password, **extra_fields)