from django.contrib import admin

# Register your models here.
from News.forms import AddNewsForm
from News.models import NewsTypeModel, NewsModel


class NewsAdminModel(admin.ModelAdmin):
    form = AddNewsForm

    def save_form(self, request, form, change):
        post = form.save(commit=False)
        post.author = request.user
        return super(NewsAdminModel, self).save_form(request, form, change)


admin.site.register(NewsTypeModel)
admin.site.register(NewsModel, NewsAdminModel)
