from django.contrib import admin

# Register your models here.

from .models import Question,CdpQuestion,MathsQuestion,EnglishQuestion,HindiQuestion


admin.site.register(Question)

admin.site.register(CdpQuestion)

admin.site.register(MathsQuestion)

admin.site.register(EnglishQuestion)

admin.site.register(HindiQuestion)

