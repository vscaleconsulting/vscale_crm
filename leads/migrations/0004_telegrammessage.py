# Generated by Django 3.2.4 on 2021-06-20 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_user_twitter_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.IntegerField()),
                ('sender_ph', models.IntegerField()),
                ('from_id', models.IntegerField()),
                ('peer_id', models.IntegerField()),
                ('datetime', models.DateTimeField()),
                ('message', models.TextField()),
                ('out', models.BooleanField()),
            ],
        ),
    ]
