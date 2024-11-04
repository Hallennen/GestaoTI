from django.contrib import admin
from accounts.models import Unit, AcontUser, Position
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

@admin.register(AcontUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user','username','email', 'first_name','unit', 'cargo','ramal','active')

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display= ('name_unit','logradouro', 'adress', 'number_adress')

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display= ('position_name',)


# class UserAdmin(BaseUserAdmin):
#     # The forms to add and change user instances
#     form = UserAdminChangeForm
#     add_form = UserAdminCreationForm

#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ['email','user', 'admin']
#     list_filter = ['admin', 'staff', 'active']
#     fieldsets = (
#         (None, {'fields': ('user', 'password')}),
#         ('Personal info', {'fields': ('first_name','last_name','birthday','ramal','cargo','unit')}),
#         ('Permissions', {'fields': ('admin', 'staff', 'active',)}),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('user', 'password', 'password_2')}
#         ),
#     )
#     search_fields = ['email']
#     ordering = ['email']
#     filter_horizontal = ()

# admin.site.register(User, UserAdmin)
# Remove Group Model from admin. We're not using it.
# admin.site.unregister(Group)
