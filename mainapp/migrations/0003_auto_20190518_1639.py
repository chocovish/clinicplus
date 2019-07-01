# Generated by Django 2.2.1 on 2019-05-18 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20190220_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitdetail',
            name='bp',
        ),
        migrations.RemoveField(
            model_name='visitdetail',
            name='medicine',
        ),
        migrations.RemoveField(
            model_name='visitdetail',
            name='weight',
        ),
        migrations.AddField(
            model_name='patient',
            name='sex',
            field=models.CharField(choices=[('Male', 'M'), ('Female', 'F'), ('Other', 'O')], default='M', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visitdetail',
            name='remarks',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='visitdetail',
            name='report',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='visitdetail',
            name='treatment',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='visitdetail',
            name='disease_info',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]