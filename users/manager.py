from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.
    """
    def create_user(self, email, first_name, 
                    last_name, middle_name='', password=None, commit=True):
        """
        Creates and saves a superuser with the given email, first name, last name and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last name')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
        )

        user.set_password(password)
        if commit:
            user.save(using=self._db)
        return user

    def create_superuser(
            self, email, first_name, last_name, password, middle_name=''):
        """
        Creates and saves a superuser with the given email, first name, last name and password
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            commit=False,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
