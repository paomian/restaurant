#coding=utf-8
from django import forms
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib import admin
from restaurant.menu.models import *
#admin.site.register(Customer)
#admin.site.register(Dish)
#admin.site.register(Desk)
#admin.site.register(Dishship)
#admin.site.register(MyUser)
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
def clean_password2(self):
    password1 = self.cleaned_data.get("password1")
    password2 = self.cleaned_data.get("password2")
    if password1 and password2 and password1 != password2:
        raise forms.ValidationError("Password don't match")
    return password2

def save(self, commit=True):
    user = super(UserCreationForm, self).save(commit=False)
    user.set_password(self.cleand_data["password1"])
    if commit:
        user.save()
    return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser

    def clean_password(self):
        return self.initial["password"]

class MyUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('name', 'email', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
            (None, {'fields':('name', 'password')}),
            ('User info', {'fields':('email',)}),
            ('Permissions',{'fields':('is_admin',)}),
            ('Important dates',{'fields':('last_login',)}),
            )
    add_fieldsets = (
            (None,{
                'classes':('wide',),
                'fields':('name','email','password1','password2')}
                ),
            )
    search_fields = ('name',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(MyUser, MyUserAdmin)
#admin.site.unregister(Group)
