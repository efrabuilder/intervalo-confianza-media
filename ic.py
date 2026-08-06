"""
ic.py
Intervalo de confianza para la media poblacional (mu), usando el
estadístico Z: IC = x̄ ± z * (s / √n)

Se usa cuando la desviación estándar poblacional se conoce, o se
aproxima con la desviación estándar muestral (válido cuando n >= 30,
o cuando el ejercicio así lo indica).
"""

# Valores críticos z más comunes para intervalos de confianza de dos colas.
Z_NIVELES = {
    0.90: 1.645,
    0.95: 1.96,
    0.99: 2.576,
}


def valor_critico_z(nivel_confianza=0.95):
    """
    Devuelve el valor crítico z asociado a un nivel de confianza.
    Niveles admitidos: 0.90, 0.95, 0.99.
    """
    if nivel_confianza not in Z_NIVELES:
        niveles = ", ".join(str(n) for n in sorted(Z_NIVELES))
        raise ValueError(f"El nivel de confianza debe ser uno de: {niveles}.")
    return Z_NIVELES[nivel_confianza]


def calcular_media(datos):
    """Devuelve el promedio (media aritmética) de una lista de números."""
    if not datos:
        raise ValueError("La lista de datos no puede estar vacía.")
    return sum(datos) / len(datos)


def calcular_desviacion_estandar(datos):
    """Devuelve la desviación estándar muestral: s = √(Σ(xi - x̄)² / (n - 1))."""
    n = len(datos)
    if n < 2:
        raise ValueError("Se necesitan al menos 2 datos para calcular la desviación estándar.")
    media = calcular_media(datos)
    suma_cuadrados = sum((x - media) ** 2 for x in datos)
    return (suma_cuadrados / (n - 1)) ** 0.5


def calcular_error_estandar(desviacion_estandar, n):
    """Devuelve el error estándar de la media: s / √n."""
    if n <= 0:
        raise ValueError("El tamaño de muestra n debe ser mayor que 0.")
    if desviacion_estandar < 0:
        raise ValueError("La desviación estándar no puede ser negativa.")
    return desviacion_estandar / (n ** 0.5)


def calcular_margen_error(desviacion_estandar, n, nivel_confianza=0.95):
    """Devuelve el margen de error: E = z * (s / √n)."""
    z = valor_critico_z(nivel_confianza)
    error_estandar = calcular_error_estandar(desviacion_estandar, n)
    return z * error_estandar


def intervalo_confianza_media_z(media, desviacion_estandar, n, nivel_confianza=0.95):
    """
    Calcula el intervalo de confianza para la media poblacional (mu)
    usando el estadístico Z.

    Parámetros:
        media (float): media muestral (x̄)
        desviacion_estandar (float): desviación estándar (s o sigma)
        n (int): tamaño de la muestra
        nivel_confianza (float): 0.90, 0.95 o 0.99

    Devuelve un diccionario con z, error estándar, margen de error
    y los límites inferior y superior del intervalo.
    """
    z = valor_critico_z(nivel_confianza)
    error_estandar = calcular_error_estandar(desviacion_estandar, n)
    margen_error = z * error_estandar

    return {
        "media": media,
        "desviacion_estandar": desviacion_estandar,
        "n": n,
        "nivel_confianza": nivel_confianza,
        "z": z,
        "error_estandar": error_estandar,
        "margen_error": margen_error,
        "limite_inferior": media - margen_error,
        "limite_superior": media + margen_error,
    }


def intervalo_confianza_desde_datos(datos, nivel_confianza=0.95):
    """
    Calcula el intervalo de confianza para la media directamente a
    partir de una lista de datos (calcula x̄, s y n automáticamente).
    """
    media = calcular_media(datos)
    desviacion_estandar = calcular_desviacion_estandar(datos)
    n = len(datos)
    return intervalo_confianza_media_z(media, desviacion_estandar, n, nivel_confianza)
