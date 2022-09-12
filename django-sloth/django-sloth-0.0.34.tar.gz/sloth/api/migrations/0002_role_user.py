# Generated by Django 3.2.8 on 2021-11-16 09:50

from django.db import migrations, models
import django.db.models.deletion
import sloth.core.base


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
                'proxy': True,
                'fieldsets': {'Dados Gerais': (('first_name', 'last_name'), 'username', 'email'), 'Dados de Acesso': 'is_superuser'},
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('scope_key', models.CharField(max_length=50, null=True, verbose_name='Escopo', blank=True)),
                ('scope_value', models.IntegerField(null=True, verbose_name='Valor do Escopo', blank=True)),
                ('scope_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name='Tipo do Escopo', blank=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='api.user', verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Papel',
                'verbose_name_plural': 'Papéis',
            },
            bases=(models.Model, sloth.core.base.ModelMixin),
        ),
    ]
