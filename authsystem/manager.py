from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email , password = None , **other_fields):
        if email is None:
            raise ValueError("Error : Email number cannot be empty!")

        email = self.normalize_email(email)

        user = self.model(email = email, **other_fields)
        user.set_password(password)
        user.save( using = self.db )


        return user
        
    def create_superuser(self, email, password = None , **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        return self.create_user(email, password, **other_fields)