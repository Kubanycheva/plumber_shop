from .models import Services, СompanyProfile, Master, GlavnyiImage
from modeltranslation.translator import TranslationOptions, register


@register(Services)
class ServicesTranslationOptions(TranslationOptions):
    fields = ('services_name', 'description')


@register(СompanyProfile)
class СompanyProfileTranslationOptions(TranslationOptions):
    fields = ('company_name', 'description')


@register(Master)
class MasterTranslationOptions(TranslationOptions):
    fields = ('master_name', 'description')


@register(GlavnyiImage)
class GlavnyiImageTranslationOptions(TranslationOptions):
    fields = ('work_name', 'description')
