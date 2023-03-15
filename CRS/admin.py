from django.contrib import admin
from .models import User, Role, Question, QuestionQuestion
# Register your models here.
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Question)
# admin.site.register(Category)
admin.site.register(QuestionQuestion)
