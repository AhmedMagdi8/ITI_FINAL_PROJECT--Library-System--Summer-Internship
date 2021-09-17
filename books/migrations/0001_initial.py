# Generated by Django 3.2.7 on 2021-09-16 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('authors', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(max_length=200, null=True, upload_to='')),
                ('description', models.TextField(blank=True, null=True)),
                ('is_borrowed', models.BooleanField()),
                ('std_id', models.ForeignKey(default=1000, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
