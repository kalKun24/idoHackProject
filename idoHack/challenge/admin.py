from django.contrib import admin

# Register your models here.
from .models import CategoryModel, ExerciseModel, ChallengeModel

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']

class ExerciseAdmin(admin.ModelAdmin):

    fieldsets = [
        ("基本情報", {"fields": ["exercise_title", "exercise_number","category", "visible"]}),
        ("演習の説明", {"fields": ["exercise_discription"]}),
        ("教科書・解説URL", {"fields": ["textbook_url" , "explanation_url"]}),
        ("その他情報", {"fields": ["created_at", "updated_at"]}),
    ]

    list_display = ['exercise_title', 'exercise_number', 'visible', 'category']
    list_filter = ['exercise_title','visible', 'category']
    search_fields = ['exercise_title']
    ordering = ['category', 'exercise_number']
    readonly_fields = ['created_at', 'updated_at']


class ChallengeAdmin(admin.ModelAdmin):
    
        fieldsets = [
            ("基本情報", {"fields": ["challenge_title", "challenge_number", "category", "exercise_title", "score", "flag", "visible", "is_practice"]}),
            ("課題の問題文", {"fields": ["problem"]}),
            ("ヒント", {"fields": ["hint_one", "hint_two", "hint_three"]}),
            ("その他情報", {"fields": ["created_at", "updated_at"]}),
        ]
    
        list_display = ['challenge_title', 'challenge_number', 'score', 'category', 'exercise_title', 'visible']
        list_filter = ['challenge_title', 'visible', 'category', 'exercise_title']
        search_fields = ['challenge_title']
        ordering = ['exercise_title' ,'challenge_number']
        readonly_fields = ['created_at', 'updated_at']

admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(ExerciseModel, ExerciseAdmin)
admin.site.register(ChallengeModel, ChallengeAdmin)

#TODO: 検証