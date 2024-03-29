from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "timestamp", "updated"]
	list_display_links = ["updated"]
	list_filter = ["timestamp"]
	list_editable = ["title"]
	search_fields = ["content", "title"]
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)