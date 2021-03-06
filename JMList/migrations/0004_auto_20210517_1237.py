# Generated by Django 3.1.6 on 2021-05-17 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('JMList', '0003_auto_20210501_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DeptName', models.TextField(default='')),
                ('DeptHead', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(default='')),
                ('Gender', models.TextField(default='')),
                ('Address', models.TextField(default='')),
                ('Birthday', models.DateField(default='')),
                ('PhoneNumber', models.CharField(default='', max_length=11)),
                ('EmailAddress', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeesHealth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EHealth', models.TextField(default='')),
                ('Maintenance', models.TextField(default='')),
                ('EmpID', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='JMList.employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeesStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ETestDate', models.DateField(default='')),
                ('EStatus', models.TextField(default='')),
                ('Comments', models.TextField(default='')),
                ('Prescription', models.TextField(default='', max_length=200)),
                ('Doctor', models.TextField(default='')),
                ('EmployeeId', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='JMList.employee')),
            ],
        ),
        migrations.CreateModel(
            name='ValidID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ValID', models.TextField(default='')),
                ('ValNum', models.TextField(default='')),
                ('ValDate', models.DateField(default='')),
                ('EmpID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='JMList.employee')),
            ],
        ),
        migrations.CreateModel(
            name='WorkHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company', models.TextField(default='')),
                ('DeptAssigned', models.TextField(default='')),
                ('Location', models.TextField(default='')),
                ('Contact', models.CharField(default='', max_length=11)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='List',
        ),
        migrations.AddField(
            model_name='department',
            name='EmpID',
            field=models.ManyToManyField(default=None, to='JMList.Employee'),
        ),
    ]
