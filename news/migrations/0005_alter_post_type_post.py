# Generated by Django 4.1 on 2022-09-04 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_post_type_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type_post',
            field=models.CharField(choices=[('NW', 'Новость'), ('AR', 'Статья')], max_length=2),
        ),
    ]
