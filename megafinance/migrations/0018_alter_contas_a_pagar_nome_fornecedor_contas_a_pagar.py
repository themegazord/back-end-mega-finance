# Generated by Django 4.0.4 on 2022-05-27 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('megafinance', '0017_alter_contas_a_pagar_nome_fornecedor_contas_a_pagar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contas_a_pagar',
            name='nome_fornecedor_contas_a_pagar',
            field=models.CharField(max_length=155, verbose_name='Nome fornecedor'),
        ),
    ]