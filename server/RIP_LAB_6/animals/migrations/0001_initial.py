# Generated by Django 3.2.9 on 2021-11-22 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_type', models.CharField(max_length=50, verbose_name='Вид животного')),
                ('animal_name', models.CharField(max_length=50, verbose_name='Кличка животного')),
                ('animal_photo', models.URLField(verbose_name='Фото жифотного')),
            ],
            options={
                'verbose_name': 'Животное',
                'verbose_name_plural': 'Животные',
            },
        ),
    ]
