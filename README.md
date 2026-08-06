# Intervalo de Confianza para la Media (Z)

Programa en Python que calcula el **intervalo de confianza para la media poblacional (μ)** usando el estadístico Z:

$$IC = \bar{x} \pm z \cdot \frac{s}{\sqrt{n}}$$

Se usa cuando la desviación estándar poblacional se conoce, o se aproxima con la desviación estándar muestral (por ejemplo, cuando n ≥ 30, o cuando el ejercicio así lo indica). Soporta los niveles de confianza más comunes: **90%** (z = 1.645), **95%** (z = 1.96) y **99%** (z = 2.576).

## Dos formas de empezar

1. **Ya tenés x̄, s y n** (datos resumidos de un enunciado o reporte) → los ingresás directamente.
2. **Tenés la lista completa de datos** → el programa calcula x̄, s y n por vos.

## Estructura del proyecto

```
intervalo-confianza-media/
├── main.py       # Programa de línea de comandos (con las dos opciones)
├── ic.py         # Funciones de cálculo del intervalo de confianza
├── test_ic.py    # Pruebas unitarias
├── index.html    # Demo interactiva en el navegador
└── README.md
```

## Requisitos

- Python 3.8 o superior (no requiere librerías externas)

## Uso

```bash
python main.py
```

**Opción 1 — datos resumidos:**

```
Intervalo de confianza para la media (estadístico Z)
¿Cómo querés ingresar los datos?
1) Ya tengo x̄, s y n (datos resumidos)
2) Tengo la lista completa de datos
Elegí 1 o 2 [1]: 1
Media muestral (x̄): 8.4
Desviación estándar (s): 2
Tamaño de muestra (n): 25
Nivel de confianza (90%, 95%, 99%) [95%]: 95

--- Intervalo de confianza para la media (Z) ---
Media (x̄):            8.4000
Desviación estándar:   2.0000
n:                     25
Nivel de confianza:    95%
z:                     1.96
Error estándar (EE):   0.4000
Margen de error (E):   0.7840

IC = 8.4000 ± 0.7840 = (7.6160, 9.1840)
```

**Opción 2 — lista de datos:**

```
Elegí 1 o 2 [1]: 2
Ingresá los datos separados por espacio o coma: 4, 8, 15, 16, 23, 8
Nivel de confianza (90%, 95%, 99%) [95%]:
```

## Usar las funciones en tu propio código

```python
from ic import intervalo_confianza_media_z, intervalo_confianza_desde_datos

# con datos ya resumidos
resultado = intervalo_confianza_media_z(media=8.4, desviacion_estandar=2, n=25, nivel_confianza=0.95)
print(resultado["limite_inferior"], resultado["limite_superior"])  # 7.616 9.184

# a partir de una lista de datos
resultado = intervalo_confianza_desde_datos([4, 8, 15, 16, 23, 8], nivel_confianza=0.95)
```

El diccionario que devuelven ambas funciones incluye: `media`, `desviacion_estandar`, `n`, `nivel_confianza`, `z`, `error_estandar`, `margen_error`, `limite_inferior` y `limite_superior`.

## Demo en el navegador

`index.html` ofrece las mismas dos opciones de entrada (pestañas arriba), un selector de nivel de confianza (90%/95%/99%) y muestra el procedimiento paso a paso una vez calculado el intervalo.

## Pruebas

```bash
python -m unittest test_ic.py
```

## Notas

- Requiere al menos 2 datos (o un n ≥ 2 en el modo resumido).
- Usa el estadístico Z, no la distribución t de Student.
- La desviación estándar se calcula de forma muestral (divide entre `n - 1`).

## Licencia

Este proyecto se distribuye bajo la licencia MIT.
