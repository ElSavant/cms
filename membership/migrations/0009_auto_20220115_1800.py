# Generated by Django 3.2.7 on 2022-01-15 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0008_auto_20220113_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='occupation',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='baptised',
            field=models.BooleanField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='mobile_number',
            field=models.CharField(max_length=15),
        ),
    ]