# Generated by Django 4.0.4 on 2022-05-23 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('megafinance', '0005_alter_atualiza_estoque_producao_cod_producao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email_cliente',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail'),
        ),
    ]