# Generated by Django 4.2.1 on 2023-05-25 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_alter_message_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avator',
            field=models.CharField(default='https://img1.imgtp.com/2023/05/07/8NKt5JEn.png', max_length=1000, null=True),
        ),
    ]