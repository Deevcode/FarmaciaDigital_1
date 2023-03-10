# Generated by Django 4.0.4 on 2023-03-06 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuariofarmacovigilancia',
            name='id_usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuariofarmacovigilancia',
            name='nombre_comercial',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to='app.medicamentos'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='MedicamentoFichaTecnica',
            fields=[
                ('id_ficha_medicamento', models.AutoField(primary_key=True, serialize=False)),
                ('url_ficha', models.CharField(max_length=700)),
                ('nombre_comercial', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.medicamentos')),
            ],
        ),
        migrations.CreateModel(
            name='FichaUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_nacimiento', models.DateField()),
                ('enfermades_cronicas', models.IntegerField(choices=[[0, 'Ninguna.'], [1, 'VIH/SIDA.'], [2, 'Insuficiencia Renal Crónica.'], [3, 'Hipertensión Arterial Primaria o Esencial en personas de 15 años y más.'], [4, 'Epilepsia no Refractaria en personas de 1 año y menores de 15 años.'], [5, 'Hemofilia.'], [6, 'Tratamiento médico en personas de 55 años y más con Artrosis de cadera y/o rodilla leve o moderada.'], [7, 'Fibrosis quística.'], [8, 'Artritis reumatoidea.'], [9, 'Diabetes Mellitus tipo 1.'], [10, 'Epilepsia en el adulto.'], [11, 'GPC Enfermedad de Parkinson.'], [12, 'Artritis idiopática juvenil/Artritis reumatoidea juvenil.'], [13, 'Esclerosis Multiple.'], [14, 'Diabetes Mellitus tipo 2.'], [15, 'Hipotiroidismo en personas de 15 años y más.'], [16, 'Hipertensión'], [17, 'Glaoucoma']])),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.usuario')),
                ('nombre_tipo_usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.tipo_usuario')),
            ],
        ),
    ]
