# Generated by Django 4.2.5 on 2023-10-04 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComicBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('publish', models.BooleanField(default=False, verbose_name='Опубликовать')),
            ],
            options={
                'verbose_name': 'Комикс',
                'verbose_name_plural': 'Комиксы',
                'ordering': ['-date_of_creation'],
            },
        ),
        migrations.CreateModel(
            name='ComicBookPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='comicbook_pages/', verbose_name='Изображение')),
                ('comic_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comics.comicbook', verbose_name='Комикс')),
            ],
            options={
                'verbose_name': 'Страница комикса',
                'verbose_name_plural': 'Страницы комиксов',
                'ordering': ['-id'],
            },
        ),
    ]