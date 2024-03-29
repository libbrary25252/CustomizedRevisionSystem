import uuid
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    role_id = models.ForeignKey(
        "Role", on_delete=models.CASCADE)
    info_id = models.ForeignKey(
        "UserInfo", on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)


class UserInfo(models.Model):
    info_id = models.CharField(max_length=6, default='')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    # password = models.CharField(max_length=50)
    phone_no = PhoneNumberField(blank=True)
    create_date = models.DateField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Role(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.description


class Question(models.Model):
    # def img_directory_path(folder, filename):
    #     return os.path.join(folder, filename)
    #     ext = filename.split('.')[-1]
    #     filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    #     return os.path.join(instance.question_id, "img", filename)
    QID = models.BigIntegerField(primary_key=True)
    parentQID = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True)
    statement = models.TextField(blank=True, null=True)
    string = models.TextField()
    # year = models.IntegerField(blank=True, null=True)

    # define type of question
    LONG = 'LQ'
    MULTIPLECHOICES = 'MC'
    TYPE_CHOICES = [(LONG, 'Long Question'),
                    (MULTIPLECHOICES, 'Multiple Choice')]
    Qtype = models.CharField(
        max_length=2, choices=TYPE_CHOICES, default=MULTIPLECHOICES)

    def is_upperclass(self):
        return self.type in {self.LONG, self.MULTIPLECHOICES}  # type: ignore

    image = models.ImageField(
        upload_to="uploads\\images\\", height_field=None, width_field=None, max_length=100, blank=True, null=True)  # name it by qid
    description = models.TextField(null=True, blank=True)
    options = models.TextField(null=True, blank=True)

    CATER_CHOICE = (
        ('ALGO', 'Algorithm Design'),
        ('BMO', 'Basic Machine Organisation'),
        ('COM', 'Computer System'),
        ('DM', 'Data Manipulation and Analysis'),
        ('DO', 'Data Organisation and Data Control'),
        ('ELEWEB', 'Elementary Web Authoring'),
        ('HEALTH', 'Health and Ethical Issues'),
        ('INFO', 'Information Processing'),
        ('IP', 'Intellectual Property'),
        ('NETSEV', 'Internet Services and Applications'),
        ('MEDIA', 'Multimedia Elements'),
        ('NETBAS', 'Networking and Internet Basics'),
        ('PROGRAM', 'Program Development'),
        ('SD', 'Spreadsheets and Databases'),
        ('THREAT', 'Threats and Security on the Internet'))
    category = MultiSelectField(
        choices=CATER_CHOICE, max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.QID)


class QuestionQuestion(models.Model):
    state_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    statement = models.TextField(blank=True, null=True)
    qid = models.ForeignKey(
        "Question", on_delete=models.CASCADE, null=True, blank=True)


class QuestionInput(models.Model):
    seq = models.CharField(max_length=100,
                           default='fuckyoula-2023032115364')
    uid = models.CharField(max_length=6, default="st0001")
    text = models.TextField()
    result = models.CharField(max_length=1000, null=True, blank=True)

# class Category(models.Model):
#     c_id = models.UUIDField(
#         primary_key=True, default=uuid.uuid4, editable=False)
#     c_name = models.CharField(max_length=30, default='c001')
#     description = models.TextField()
