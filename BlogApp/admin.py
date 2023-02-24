from django.contrib import admin
from BlogApp.models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug', 'author', 'publish', 'created', 'updated','status']
    list_filter=('status','created','publish','author')
    search_fields=('title','body')
    prepopulated_fields={"slug":('title',)}
    raw_id_fields=('author',)
    ordering=['status','publish']

admin.site.register(Post, PostAdmin)



#model-based-form for comments
from django import forms
from BlogApp.models import Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','email','body')
