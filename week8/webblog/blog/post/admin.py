from django.contrib import admin


from .models import Post, Tag, UserProfile, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status','created')
    list_filter = ('status','created','author')
    search_fields = ['title','body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_field = ('author',)
    date_hierachy = 'publish'
    ordering = ('status','publish')
    autocomplete_fields = ('tags',)


class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)


#class ProfileAdmin(admin.ModelAdmin):



admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile)
admin.site.register(Comment)