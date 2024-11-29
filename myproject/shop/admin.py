from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin


class ContactInfoInline(admin.TabularInline):
    model = ContactInfo
    extra = 1


class СompanyProfileImageInline(admin.TabularInline):
    model = СompanyProfileImage
    extra = 1


class Contact_InfoInline(admin.TabularInline):
    model = Contact_Info
    extra = 1


class GlavnyiImageInline(admin.TabularInline):
    model = GlavnyiImage
    extra = 1


@admin.register(СompanyProfile)
class СompanyProfileAdmin(TranslationAdmin):
    inlines = [ContactInfoInline, СompanyProfileImageInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Services)
class ServicesAdmin(TranslationAdmin):

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Master)
class MasterAdmin(TranslationAdmin):
    inlines = [Contact_InfoInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Gallery)
class GlavnyiImageAdmin(TranslationAdmin):
    inlines = [GlavnyiImageInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class CartItemInlines(admin.TabularInline):
    model = CartItem
    extra = 1


class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInlines]


admin.site.register(User)
admin.site.register(Catalog)
admin.site.register(Review)
admin.site.register(Cart, CartAdmin)
