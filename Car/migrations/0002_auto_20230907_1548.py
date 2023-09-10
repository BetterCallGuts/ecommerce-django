# Generated by Django 3.2.3 on 2023-09-07 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=2500)),
            ],
        ),
        migrations.RemoveField(
            model_name='car',
            name='Car_Type',
        ),
        migrations.AddField(
            model_name='car',
            name='Car_type',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Car.cartype'),
        ),
    ]
