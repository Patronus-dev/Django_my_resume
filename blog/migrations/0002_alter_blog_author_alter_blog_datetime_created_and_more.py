# Generated by Django 5.0.6 on 2024-07-03 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(max_length=50, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='datetime_modified',
            field=models.DateTimeField(auto_now=True, verbose_name='date edited'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='blog/blog_cover/', verbose_name='blog Image'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('pub', 'published'), ('drf', 'draft')], max_length=3, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=models.TextField(max_length=1000, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
    ]