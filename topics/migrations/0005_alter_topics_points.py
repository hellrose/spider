# Generated by Django 5.0.7 on 2024-07-16 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0004_alter_topics_difficulty_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topics',
            name='points',
            field=models.TextField(blank=True, default='暂未更新考点', help_text='本题的考点'),
        ),
    ]
