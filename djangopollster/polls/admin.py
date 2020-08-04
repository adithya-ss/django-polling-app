from django.contrib import admin

# Register your models here.

from .models import Questions, Choice

admin.site.site_header = "Poll Admin"
admin.site.site_title = "Poll Admin Area"
admin.site.index_title = "Hello. Welcome to the admin area."

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionsAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['question_text']}),
    ('Date Information', {'fields':['publish_date'], 'classes':['collapse']}),]
    inlines = [ChoiceInline]

# admin.site.register(Questions)
# admin.site.register(Choice)
admin.site.register(Questions, QuestionsAdmin)
