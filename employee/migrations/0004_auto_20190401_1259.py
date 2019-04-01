# Generated by Django 2.1.7 on 2019-04-01 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20190401_1246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='linkedin',
        ),
        migrations.AddField(
            model_name='employee',
            name='facebook_url',
            field=models.URLField(blank=True, max_length=60, verbose_name='Facebook URL'),
        ),
        migrations.AddField(
            model_name='employee',
            name='github_url',
            field=models.URLField(blank=True, max_length=60, verbose_name='Github URL'),
        ),
        migrations.AddField(
            model_name='employee',
            name='linkedin_url',
            field=models.URLField(default='https://google.com/', max_length=60, verbose_name='Linkdin URL'),
            preserve_default=False,
        ),
    ]