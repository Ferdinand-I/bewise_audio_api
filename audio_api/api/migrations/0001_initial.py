# Generated by Django 4.2.1 on 2023-05-21 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, unique=True, verbose_name='Имя пользователя')),
                ('uuid_token', models.BinaryField(verbose_name='Токен доступа')),
            ],
            options={
                'ordering': ['pk'],
                'indexes': [models.Index(fields=['uuid_token'], name='uuid_token_idx')],
            },
        ),
    ]