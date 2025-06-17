import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('url', models.CharField(max_length=255, verbose_name='url')),
                ('named_url', models.CharField(max_length=100, verbose_name='именованный url')),
                ('menu_name', models.CharField(max_length=60, verbose_name='название меню')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='apps.menumodel')),
            ],
        ),
    ]
