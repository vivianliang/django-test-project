from django.contrib import admin
from polls.models import Question


# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]


admin.site.register(Question, QuestionAdmin)
