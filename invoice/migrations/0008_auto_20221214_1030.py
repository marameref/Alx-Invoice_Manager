# Generated by Django 3.1.7 on 2022-12-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0007_auto_20210912_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='contact',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='invoice',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='customer',
            field=models.TextField(default=''),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
