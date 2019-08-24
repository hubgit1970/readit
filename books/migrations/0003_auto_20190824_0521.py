# Generated by Django 2.2.4 on 2019-08-24 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20190824_0456'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Use pen name, not real name!', max_length=70, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='books', to='books.Author'),
        ),
    ]
