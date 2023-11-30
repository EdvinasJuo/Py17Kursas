# Generated by Django 4.2.7 on 2023-11-23 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postit_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumreviewcomment',
            name='album_review_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='postit_api.albumreview'),
        ),
    ]