# Generated by Django 3.2.12 on 2022-04-05 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_rename_activa_coupon_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='cede',
            new_name='code',
        ),
    ]