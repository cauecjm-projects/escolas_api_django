from django.contrib import admin

from apps.escola.models import Curso, Matricula


class CursosAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'nome', 'nivel')
    list_display_links = ('nome', 'codigo_curso')
    search_fields = ('nome', 'codigo_curso')
    list_per_page = 20

admin.site.register(Curso, CursosAdmin)


class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('aluno',)
    search_fields = ('aluno__nome', 'curso__nome')
    list_per_page = 20

admin.site.register(Matricula, MatriculaAdmin)
