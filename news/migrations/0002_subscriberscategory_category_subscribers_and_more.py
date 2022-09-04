from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SubscribersCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="category",
            name="subscribers",
            field=models.ManyToManyField(
                through="news.SubscribersCategory", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="subscriberscategory",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="news.category"
            ),
        ),
        migrations.AddField(
            model_name="subscriberscategory",
            name="subscriber",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
