"""
test_ic.py
Pruebas unitarias para las funciones de ic.py
Ejecutar con: python -m unittest test_ic.py
"""

import unittest

from ic import (
    calcular_desviacion_estandar,
    calcular_error_estandar,
    calcular_margen_error,
    calcular_media,
    intervalo_confianza_desde_datos,
    intervalo_confianza_media_z,
    valor_critico_z,
)


class TestValorCriticoZ(unittest.TestCase):

    def test_niveles_soportados(self):
        self.assertEqual(valor_critico_z(0.90), 1.645)
        self.assertEqual(valor_critico_z(0.95), 1.96)
        self.assertEqual(valor_critico_z(0.99), 2.576)

    def test_nivel_no_soportado(self):
        with self.assertRaises(ValueError):
            valor_critico_z(0.80)


class TestMediaYDesviacion(unittest.TestCase):

    def test_media(self):
        self.assertAlmostEqual(calcular_media([4, 8, 15, 16, 23, 8]), 12.3333, places=4)

    def test_media_lista_vacia(self):
        with self.assertRaises(ValueError):
            calcular_media([])

    def test_desviacion_estandar(self):
        self.assertAlmostEqual(calcular_desviacion_estandar([2, 4, 6, 8]), 2.5820, places=4)

    def test_desviacion_estandar_un_solo_dato(self):
        with self.assertRaises(ValueError):
            calcular_desviacion_estandar([5])


class TestErrorEstandarYMargen(unittest.TestCase):

    def test_error_estandar(self):
        self.assertAlmostEqual(calcular_error_estandar(2, 25), 0.4)

    def test_error_estandar_n_invalido(self):
        with self.assertRaises(ValueError):
            calcular_error_estandar(2, 0)

    def test_margen_error(self):
        self.assertAlmostEqual(calcular_margen_error(2, 25, 0.95), 0.784)


class TestIntervaloConfianzaMediaZ(unittest.TestCase):
    """Caso de referencia: 25 llamadas, x̄ = 8.4 min, s = 2 min, 95% de confianza."""

    def test_llamadas_empresa(self):
        resultado = intervalo_confianza_media_z(8.4, 2, 25, 0.95)

        self.assertEqual(resultado["z"], 1.96)
        self.assertAlmostEqual(resultado["error_estandar"], 0.4)
        self.assertAlmostEqual(resultado["margen_error"], 0.784)
        self.assertAlmostEqual(resultado["limite_inferior"], 7.616)
        self.assertAlmostEqual(resultado["limite_superior"], 9.184)

    def test_nivel_confianza_por_defecto_es_95(self):
        resultado = intervalo_confianza_media_z(8.4, 2, 25)
        self.assertEqual(resultado["nivel_confianza"], 0.95)

    def test_otro_nivel_de_confianza(self):
        resultado = intervalo_confianza_media_z(8.4, 2, 25, 0.99)
        self.assertEqual(resultado["z"], 2.576)
        self.assertAlmostEqual(resultado["margen_error"], 1.0304)


class TestIntervaloConfianzaDesdeDatos(unittest.TestCase):

    def test_desde_lista_de_datos(self):
        datos = [4, 8, 15, 16, 23, 8]
        resultado = intervalo_confianza_desde_datos(datos, 0.95)

        self.assertAlmostEqual(resultado["media"], 12.3333, places=4)
        self.assertAlmostEqual(resultado["desviacion_estandar"], 6.9474, places=4)
        self.assertEqual(resultado["n"], 6)
        self.assertEqual(resultado["z"], 1.96)
        self.assertLess(resultado["limite_inferior"], resultado["media"])
        self.assertGreater(resultado["limite_superior"], resultado["media"])

    def test_menos_de_dos_datos_lanza_error(self):
        with self.assertRaises(ValueError):
            intervalo_confianza_desde_datos([5])


if __name__ == "__main__":
    unittest.main()
