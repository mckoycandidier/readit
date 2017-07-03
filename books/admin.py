# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Author, Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	fieldset = [
		("Book Details", {"fields": ["title", "authors"]}),
		("Review", {"fields": ["is_favourite", "review", "date_reviewed"]})
	]
	#remove date output option to timezone
	readonly_fields = ("date_reviewed",)
	
	#adding relational view with other data
	def book_authors(self, obj):
		return obj.list_authors()
		
	
	#adding or editing the title of list item
	book_authors.short_description = "Author(s)"
	
	
	#adding admin list view or table view
	#traverse field by adding double uderscore __ exmaple book_authors
	list_display = ("title", "book_authors", "is_favourite", "date_reviewed",)
	list_display_links =("date_reviewed",)
	list_editable = ("title", "is_favourite",)
	list_filter = ("title",)
	search_fields = ("title", "author__name")
	
# Register your models here.
admin.site.register(Author)

# the code below chnage by @admin.register(Book)
#admin.site.register(Book, BookAdmin)
