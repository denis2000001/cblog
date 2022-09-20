# Generated by Django 4.1.1 on 2022-09-16 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='stars',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.IntegerField(choices=[(1, 'Animals'), (2, 'Cars'), (3, 'Recipes'), (4, 'Nature'), (5, 'Other')], null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]