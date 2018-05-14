from django.contrib import admin
from . import models
from myapp.models import Article
# Register your models here.
admin.site.register(models.Poem)



# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')


admin.site.register(Article, ArticleAdmin)
