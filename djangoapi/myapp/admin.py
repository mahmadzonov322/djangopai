from django.contrib import admin
from .models import PortfolioProject,News,Trending

# Register your models here.
# @admin.register(PortfolioProject)
# class PortfolioProjectAdmin(admin.ModelAdmin):
#     list_display = ('nomi', 'category','narxi', )
#     list_filter = ('category',)
#     search_fields = ('nomi', 'description')

    
#     fieldsets = (
#         (None, {
#             'fields': ('nomi', 'category', 'description', 'rasmi', 'texnologiya','narxi')
#         }),
        
#     )

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'game_name', 'release_date', 'is_published', 'created_at')
    list_filter = ('is_published', 'release_date')
    search_fields = ('title', 'description', 'game_name')
    readonly_fields = ('created_at', 'updated_at')
admin.site.register(PortfolioProject)
@admin.register(Trending)
class TrendingAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'categoriya', 'id')
    list_filter = ('categoriya',)
    search_fields = ('nomi',)
    ordering = ('-id',)
    