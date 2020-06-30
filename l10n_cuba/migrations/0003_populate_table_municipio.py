# Generated by Django 3.0 on 2020-06-25 00:18
import sys
from django.db import migrations, transaction
from l10n_cuba.data.municipios import get_provincia


def populate(apps, schema_editor):
    if schema_editor.connection.alias != 'default':
        return

    Municipio = apps.get_model('l10n_cuba', 'Municipio')
    p = get_provincia(apps=apps)
    MUNICIPIOS = [
        # Pinar del Rio
        {'nombre': 'Sandino', 'provincia': p['pr']},
        {'nombre': 'Mantua', 'provincia': p['pr']},
        {'nombre': 'Minas de Matahambre', 'provincia': p['pr']},
        {'nombre': 'Viñales', 'provincia': p['pr']},
        {'nombre': 'La Palma', 'provincia': p['pr']},
        {'nombre': 'Los Palacios', 'provincia': p['pr']},
        {'nombre': 'Consolación del Sur', 'provincia': p['pr']},
        {'nombre': 'Pinar del Río', 'provincia': p['pr']},
        {'nombre': 'San Luis', 'provincia': p['pr']},
        {'nombre': 'San Juan y Martínez', 'provincia': p['pr']},
        {'nombre': 'Guane', 'provincia': p['pr']},

        # Artemisa
        {'nombre': 'Bahía Honda', 'provincia': p['art']},
        {'nombre': 'Mariel', 'provincia': p['art']},
        {'nombre': 'Guanajay', 'provincia': p['art']},
        {'nombre': 'Caimito', 'provincia': p['art']},
        {'nombre': 'Bauta', 'provincia': p['art']},
        {'nombre': 'San Antonio de los Baños', 'provincia': p['art']},
        {'nombre': 'Güira de Melena', 'provincia': p['art']},
        {'nombre': 'Alquízar', 'provincia': p['art']},
        {'nombre': 'Artemisa', 'provincia': p['art']},
        {'nombre': 'Candelaria', 'provincia': p['art']},
        {'nombre': 'San Cristóbal', 'provincia': p['art']},

        # La Habana
        {'nombre': 'Playa', 'provincia': p['lh']},
        {'nombre': 'Plaza de la Revolución', 'provincia': p['lh']},
        {'nombre': 'Centro Habana', 'provincia': p['lh']},
        {'nombre': 'La Habana Vieja', 'provincia': p['lh']},
        {'nombre': 'Regla', 'provincia': p['lh']},
        {'nombre': 'La Habana del Este', 'provincia': p['lh']},
        {'nombre': 'Guanabacoa', 'provincia': p['lh']},
        {'nombre': 'San Miguel del Padrón', 'provincia': p['lh']},
        {'nombre': 'Diez de Octubre', 'provincia': p['lh']},
        {'nombre': 'Cerro', 'provincia': p['lh']},
        {'nombre': 'Marianao', 'provincia': p['lh']},
        {'nombre': 'La Lisa', 'provincia': p['lh']},
        {'nombre': 'Boyeros', 'provincia': p['lh']},
        {'nombre': 'Arroyo Naranjo', 'provincia': p['lh']},
        {'nombre': 'Cotorro', 'provincia': p['lh']},

        # Mayabeque
        {'nombre': 'Bejucal', 'provincia': p['may']},
        {'nombre': 'San José de las Lajas', 'provincia': p['may']},
        {'nombre': 'Jaruco', 'provincia': p['may']},
        {'nombre': 'Santa Cruz del Norte', 'provincia': p['may']},
        {'nombre': 'Madruga', 'provincia': p['may']},
        {'nombre': 'Nueva Paz', 'provincia': p['may']},
        {'nombre': 'San Nicolás', 'provincia': p['may']},
        {'nombre': 'Güines', 'provincia': p['may']},
        {'nombre': 'Batabanó', 'provincia': p['may']},
        {'nombre': 'Quivicán', 'provincia': p['may']},
        {'nombre': 'Melena del Sur', 'provincia': p['may']},

        # Matanzas
        {'nombre': 'Matanzas', 'provincia': p['mtz']},
        {'nombre': 'Cárdenas', 'provincia': p['mtz']},
        {'nombre': 'Martí', 'provincia': p['mtz']},
        {'nombre': 'Colón', 'provincia': p['mtz']},
        {'nombre': 'Perico', 'provincia': p['mtz']},
        {'nombre': 'Jovellanos', 'provincia': p['mtz']},
        {'nombre': 'Pedro Betancourt', 'provincia': p['mtz']},
        {'nombre': 'Limonar', 'provincia': p['mtz']},
        {'nombre': 'Unión de Reyes', 'provincia': p['mtz']},
        {'nombre': 'Ciénaga de Zapata', 'provincia': p['mtz']},
        {'nombre': 'Jagüey Grande', 'provincia': p['mtz']},
        {'nombre': 'Calimete', 'provincia': p['mtz']},
        {'nombre': 'Los Arabos', 'provincia': p['mtz']},

        # Villa Clara
        {'nombre': 'Corralillo', 'provincia': p['vcl']},
        {'nombre': 'Quemado de Güines', 'provincia': p['vcl']},
        {'nombre': 'Sagua la Grande', 'provincia': p['vcl']},
        {'nombre': 'Encrucijada', 'provincia': p['vcl']},
        {'nombre': 'Camajuaní', 'provincia': p['vcl']},
        {'nombre': 'Caibarién', 'provincia': p['vcl']},
        {'nombre': 'Remedios', 'provincia': p['vcl']},
        {'nombre': 'Placetas', 'provincia': p['vcl']},
        {'nombre': 'Santa Clara', 'provincia': p['vcl']},
        {'nombre': 'Cifuentes', 'provincia': p['vcl']},
        {'nombre': 'Santo Domingo', 'provincia': p['vcl']},
        {'nombre': 'Ranchuelo', 'provincia': p['vcl']},
        {'nombre': 'Manicaragua', 'provincia': p['vcl']},

        # Cienfuegos
        {'nombre': 'Abreus', 'provincia': p['cfg']},
        {'nombre': 'Aguada de Pasajeros', 'provincia': p['cfg']},
        {'nombre': 'Cienfuegos', 'provincia': p['cfg']},
        {'nombre': 'Cruces', 'provincia': p['cfg']},
        {'nombre': 'Cumanayagua', 'provincia': p['cfg']},
        {'nombre': 'Lajas', 'provincia': p['cfg']},
        {'nombre': 'Palmira', 'provincia': p['cfg']},
        {'nombre': 'Rodas', 'provincia': p['cfg']},

        # Sancti Spiritus
        {'nombre': 'Yaguajay', 'provincia': p['ssp']},
        {'nombre': 'Jatibonico', 'provincia': p['ssp']},
        {'nombre': 'Taguasco', 'provincia': p['ssp']},
        {'nombre': 'Cabaiguán', 'provincia': p['ssp']},
        {'nombre': 'Fomento', 'provincia': p['ssp']},
        {'nombre': 'Trinidad', 'provincia': p['ssp']},
        {'nombre': 'Sancti Spíritus', 'provincia': p['ssp']},
        {'nombre': 'La Sierpe', 'provincia': p['ssp']},

        # Ciego de Avila
        {'nombre': 'Chambas', 'provincia': p['cav']},
        {'nombre': 'Morón', 'provincia': p['cav']},
        {'nombre': 'Bolivia', 'provincia': p['cav']},
        {'nombre': 'Primero de Enero', 'provincia': p['cav']},
        {'nombre': 'Ciro Redondo', 'provincia': p['cav']},
        {'nombre': 'Florencia', 'provincia': p['cav']},
        {'nombre': 'Majagua', 'provincia': p['cav']},
        {'nombre': 'Ciego de Ávila', 'provincia': p['cav']},
        {'nombre': 'Venezuela', 'provincia': p['cav']},
        {'nombre': 'Baraguá', 'provincia': p['cav']},

        # Camaguey
        {'nombre': 'Carlos Manuel de Céspedes', 'provincia': p['cmg']},
        {'nombre': 'Esmeralda', 'provincia': p['cmg']},
        {'nombre': 'Sierra de Cubitas', 'provincia': p['cmg']},
        {'nombre': 'Minas', 'provincia': p['cmg']},
        {'nombre': 'Nuevitas', 'provincia': p['cmg']},
        {'nombre': 'Sibanicú', 'provincia': p['cmg']},
        {'nombre': 'Florida', 'provincia': p['cmg']},
        {'nombre': 'Camagüey', 'provincia': p['cmg']},
        {'nombre': 'Vertientes', 'provincia': p['cmg']},
        {'nombre': 'Jimaguayú', 'provincia': p['cmg']},
        {'nombre': 'Santa Cruz del Sur', 'provincia': p['cmg']},
        {'nombre': 'Guáimaro', 'provincia': p['cmg']},
        {'nombre': 'Najasa', 'provincia': p['cmg']},

        # Las Tunas
        {'nombre': 'Manatí', 'provincia': p['ltu']},
        {'nombre': 'Puerto Padre', 'provincia': p['ltu']},
        {'nombre': 'Jesús Menéndez', 'provincia': p['ltu']},
        {'nombre': 'Majibacoa', 'provincia': p['ltu']},
        {'nombre': 'Las Tunas', 'provincia': p['ltu']},
        {'nombre': 'Jobabo', 'provincia': p['ltu']},
        {'nombre': 'Colombia', 'provincia': p['ltu']},
        {'nombre': 'Amancio', 'provincia': p['ltu']},

        # Holguin
        {'nombre': 'Gibara', 'provincia': p['hlg']},
        {'nombre': 'Rafael Freyre', 'provincia': p['hlg']},
        {'nombre': 'Banes', 'provincia': p['hlg']},
        {'nombre': 'Antilla', 'provincia': p['hlg']},
        {'nombre': 'Báguanos', 'provincia': p['hlg']},
        {'nombre': 'Holguín', 'provincia': p['hlg']},
        {'nombre': 'Calixto García', 'provincia': p['hlg']},
        {'nombre': 'Cacocum', 'provincia': p['hlg']},
        {'nombre': 'Urbano Noris', 'provincia': p['hlg']},
        {'nombre': 'Cueto', 'provincia': p['hlg']},
        {'nombre': 'Mayarí', 'provincia': p['hlg']},
        {'nombre': 'Frank País', 'provincia': p['hlg']},
        {'nombre': 'Sagua de Tánamo', 'provincia': p['hlg']},
        {'nombre': 'Moa', 'provincia': p['hlg']},

        # Granma
        {'nombre': 'Río Cauto', 'provincia': p['grm']},
        {'nombre': 'Cauto Cristo', 'provincia': p['grm']},
        {'nombre': 'Jiguaní', 'provincia': p['grm']},
        {'nombre': 'Bayamo', 'provincia': p['grm']},
        {'nombre': 'Yara', 'provincia': p['grm']},
        {'nombre': 'Manzanillo', 'provincia': p['grm']},
        {'nombre': 'Campechuela', 'provincia': p['grm']},
        {'nombre': 'Media Luna', 'provincia': p['grm']},
        {'nombre': 'Niquero', 'provincia': p['grm']},
        {'nombre': 'Pilón', 'provincia': p['grm']},
        {'nombre': 'Bartolomé Masó', 'provincia': p['grm']},
        {'nombre': 'Buey Arriba', 'provincia': p['grm']},
        {'nombre': 'Guisa', 'provincia': p['grm']},

        # Santiago de Cuba
        {'nombre': 'Contramaestre', 'provincia': p['scu']},
        {'nombre': 'Mella', 'provincia': p['scu']},
        {'nombre': 'San Luis', 'provincia': p['scu']},
        {'nombre': 'Segundo Frente', 'provincia': p['scu']},
        {'nombre': 'Songo - La Maya', 'provincia': p['scu']},
        {'nombre': 'Santiago de Cuba', 'provincia': p['scu']},
        {'nombre': 'Palma Soriano', 'provincia': p['scu']},
        {'nombre': 'Tercer Frente', 'provincia': p['scu']},
        {'nombre': 'Guamá', 'provincia': p['scu']},

        # Guantanamo
        {'nombre': 'El Salvador', 'provincia': p['gtm']},
        {'nombre': 'Manuel Tames', 'provincia': p['gtm']},
        {'nombre': 'Yateras', 'provincia': p['gtm']},
        {'nombre': 'Baracoa', 'provincia': p['gtm']},
        {'nombre': 'Maisí', 'provincia': p['gtm']},
        {'nombre': 'Imías', 'provincia': p['gtm']},
        {'nombre': 'San Antonio del Sur', 'provincia': p['gtm']},
        {'nombre': 'Caimanera', 'provincia': p['gtm']},
        {'nombre': 'Guantánamo', 'provincia': p['gtm']},
        {'nombre': 'Niceto Pérez', 'provincia': p['gtm']},

        # Isla de la Juventud
        {'nombre': 'Isla de la Juventud', 'provincia': p['isj']},
    ]
    with transaction.atomic():
        for municipio in MUNICIPIOS:
            mun = Municipio.objects.create(nombre=municipio['nombre'], provincia=municipio['provincia'])
            mun.save()


def reverse_populate(apps, schema_editor):
    Municipio = apps.get_model('l10n_cuba', 'Municipio')
    municipios = Municipio.objects.all()
    municipios.delete()


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('l10n_cuba', '0002_populate_table_provincia'),
    ]

    operations = [
        migrations.RunPython(populate, reverse_populate)
    ]
