# Generated by Django 4.0.4 on 2022-05-31 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_photographeraccount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photographeraccount',
            old_name='doenloads',
            new_name='downloads',
        ),
        migrations.CreateModel(
            name='BoughtPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_number', models.IntegerField()),
                ('date', models.DateField()),
                ('phone_number', models.IntegerField(max_length=12)),
                ('total_amount', models.IntegerField()),
                ('noOfPhotos', models.IntegerField()),
                ('photographer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.photographer')),
            ],
        ),
    ]