from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About
from .models import CollaborateRequest

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    list_display = ('title','created_on',)
    search_fields = ['title','content']
    list_filter = ('created_on',)
    # prepopulated_fields = {'slug':('title',)}
    summernote_fields = ('content',)

# Register your models here.
# admin.site.register(Post)
# admin.site.register(About)

# Note: admin.ModelAdmin is the standard way of registering
#       our model with the admin panel. We do it differently
#       above because we are supplying Summernote fields.
#       If you want to customise the admin panel view in your
#       own projects, then inherit from admin.ModelAdmin like
#       we do below.
@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)