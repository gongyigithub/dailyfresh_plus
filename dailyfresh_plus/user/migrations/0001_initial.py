# Generated by Django 2.2.1 on 2019-05-27 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20, verbose_name='用户名')),
                ('upwd', models.CharField(max_length=30, verbose_name='密码')),
                ('uemail', models.CharField(max_length=20, verbose_name='邮箱')),
                ('uactive', models.BooleanField(default=False, verbose_name='是否激活')),
            ],
            options={
                'verbose_name': '账户',
                'verbose_name_plural': '账户',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='AddressInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ureceiver', models.CharField(default=None, max_length=10, verbose_name='收货人')),
                ('uaddress', models.CharField(default=None, max_length=300, verbose_name='收货地址')),
                ('ucode', models.CharField(default=None, max_length=6, verbose_name='邮编')),
                ('uphone', models.CharField(default=None, max_length=11, verbose_name='手机号')),
                ('isDefault', models.BooleanField(default=False, verbose_name='是否默认地址')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('uuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo', verbose_name='所属账户')),
            ],
            options={
                'verbose_name': '地址',
                'verbose_name_plural': '地址',
                'db_table': 'address',
            },
        ),
    ]
