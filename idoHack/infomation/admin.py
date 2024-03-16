from django.contrib import admin
from .models import InfomationModel, FrequentlyAskedQuestionModel

class InfomationAdmin(admin.ModelAdmin):
    list_display = ['title', 'infomation_category', 'created_at', 'updated_at']
    list_filter = ['infomation_category']
    search_fields = ['title']
    ordering = ['created_at']
    readonly_fields = ['created_at', 'updated_at']

class FrequentlyAskedQuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'created_at', 'updated_at']
    search_fields = ['question']
    ordering = ['created_at']
    readonly_fields = ['created_at', 'updated_at']

admin.site.register(InfomationModel, InfomationAdmin)
admin.site.register(FrequentlyAskedQuestionModel, FrequentlyAskedQuestionAdmin)