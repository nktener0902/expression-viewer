# Generated by Django 2.1.7 on 2019-03-10 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expression', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InputQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expression', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
