# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-09-10 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payslip',
            name='relief',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='apf',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='basic_pay',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='ca',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='car_chr',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='comp_ad',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='con_adv',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='d_pay',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='da',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='ebf',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='elec_ch',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='f_adv',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='fc',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='gar_ch',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='gss',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='ha',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='hb_loan',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='hrc',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='i_relief',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='i_tax',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='lc',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='lic',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='m_loan',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='ma',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='misc',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='misc2',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='mo_inc',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='net_pay',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='nra',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='p_pay',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='pf',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='pf_loan',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='rop',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='s_all',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='s_pay',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='sbi_ln',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='soc_ln',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='total_ded',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='total_pay',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='uf',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='w_loan',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='wa',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='wc',
            field=models.FloatField(),
        ),
    ]
