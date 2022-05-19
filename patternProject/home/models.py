from secrets import choice
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True
    # 일반 user 생성
    def create_user(self, email, id, name, password=None):
        if not email:
            raise ValueError('must have user email')
        if not name:
            raise ValueError('must have user name')
        user = self.model(
            email = self.normalize_email(email),
            id = id,
            name = name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # 관리자 user 생성
    def create_superuser(self, email, id, name, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            id = id,
            name = name,
            password = password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    # 헬퍼 클래스 사용
    objects = UserManager()
    
    id = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=100)
    name = models.CharField(default='', max_length=10, null=False, blank=False)
    email = models.EmailField(default='',max_length=100, null=False, blank=False, unique=True)
    
    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # last_login = models.BooleanField(default=True)
    
    

    # 사용자의 username field는 name으로 설정
    USERNAME_FIELD = 'id'
    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = ['name','email']

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return True

    def has_perms(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    def __str__(self):
        return self.id
    
    
# class webcam(models.Model):
#     cam_idx = models.AutoField(primary_key=True)
#     lec = models.ForeignKey("Lecture", related_name="lec", on_delete=models.CASCADE, db_column="lec")
    