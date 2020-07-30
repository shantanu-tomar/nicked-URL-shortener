from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile
from .forms import UserRegisterForm
from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


class UserAdmin(UserAdmin):
    list_display = ('id', 'email', 'name', 'is_staff')
    search_fields = ('name', 'email')
    ordering = ('-id',)

    add_form = UserRegisterForm
    add_form_template = 'admin/add_form.html'

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': ('name',)}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


admin.site.register(Profile, ProfileAdmin)
admin.site.register(User, UserAdmin)
