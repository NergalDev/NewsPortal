from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0002_subscriberscategory_category_subscribers_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="type_post",
            field=models.CharField(
                choices=[("NW", "Новость"), ("AR", "Статья")], max_length=2
            ),
        ),
    ]
