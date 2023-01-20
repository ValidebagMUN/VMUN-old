# Generated by Django 4.1.5 on 2023-01-19 15:51

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution',
                 models.CharField(blank=True, help_text='Institution hosting the conference', max_length=100,
                                  verbose_name='Institution')),
                ('name', models.CharField(help_text='Name of the conference', max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(help_text='Slug of the conference', verbose_name='Slug')),
                ('email', models.EmailField(blank=True, help_text='Contact email of the conference', max_length=254,
                                            verbose_name='Email')),
                ('website', models.CharField(blank=True, help_text='Website of the conference', max_length=100,
                                             verbose_name='Website')),
                ('start_date', models.DateField(blank=True, help_text='Start date of the conference', null=True,
                                                verbose_name='Start date')),
                ('end_date', models.DateField(blank=True, help_text='End date of the conference', null=True,
                                              verbose_name='End date')),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'conference',
                'verbose_name_plural': 'conferences',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('number', models.PositiveSmallIntegerField(help_text='Number of the session', verbose_name='Number')),
                ('start_time', models.TimeField(blank=True, help_text='Expected start time of the session', null=True,
                                                verbose_name='Start time')),
                ('end_time', models.TimeField(blank=True, help_text='Expected end time of the session', null=True,
                                              verbose_name='End time')),
            ],
            options={
                'verbose_name': 'session',
                'verbose_name_plural': 'sessions',
            },
        ),
    ]
