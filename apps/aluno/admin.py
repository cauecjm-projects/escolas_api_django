from django.contrib import admin

from apps.aluno.models import Aluno


class AlunosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('nome',)
    search_fields = ('nome', 'cpf', 'email')
    list_per_page = 20
    ordering = ('nome',)

admin.site.register(Aluno, AlunosAdmin)
