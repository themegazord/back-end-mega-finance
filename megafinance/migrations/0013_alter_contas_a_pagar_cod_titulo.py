# Generated by Django 4.0.4 on 2022-05-24 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('megafinance', '0012_alter_fornecedor_email_fornecedor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contas_a_pagar',
            name='cod_titulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='megafinance.titulo', verbose_name='Código do Titulo'),
        ),
    ]