# Generated by Django 2.1.5 on 2019-02-20 10:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitdetail',
            name='visit_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='blood_group',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-"')], max_length=3),
        ),
        migrations.AlterField(
            model_name='visitdetail',
            name='weight',
            field=models.IntegerField(),
        ),
    ]
