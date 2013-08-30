'''from django.contrib import admin
from polls.models import Poll

# admin.site.register(Poll)

class PollAdmin(admin.ModelAdmin):
	# fields = ['pub_date', 'question']

	fieldsets = [
		# First item in tuple is the title of the fieldset.
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date']}),
    ]


admin.site.register(Poll, PollAdmin)'''

from django.contrib import admin
from polls.models import Choice, Poll

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)