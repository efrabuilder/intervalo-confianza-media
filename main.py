"""
main.py
Programa de línea de comandos para calcular el intervalo de confianza
de la media poblacional, usando el estadístico Z:

    IC = x̄ ± z * (s / √n)

Al arrancar, se elige una de dos formas de ingresar los datos:
1) Resumidos: se conocen x̄, s y n (por ejemplo, de un enunciado
   o de un reporte que ya trae estos tres valores).
2) Lista completa de datos: el programa calcula x̄, s y n por vos.
"""

from ic import Z_NIVELES, intervalo_confianza_desde_datos, intervalo_confianza_media_z


def elegir_nivel_confianza():
    niveles_disponibles = sorted(Z_NIVELES)
    texto = ", ".join(f"{int(n * 100)}%" for n in niveles_disponibles)
    entrada = input(f"Nivel de confianza ({texto}) [95%]: ").strip()

    if not entrada:
        return 0.95

    entrada = entrada.replace("%", "")
    try:
        valor = float(entrada)
    except ValueError:
        print("Valor inválido, se usa 95% por defecto.")
        return 0.95

    if valor > 1:
        valor = valor / 100

    if valor not in Z_NIVELES:
        print("Nivel no soportado, se usa 95% por defecto.")
        return 0.95

    return valor


def mostrar_resultado(resultado):
    print("\n--- Intervalo de confianza para la media (Z) ---")
    print(f"Media (x̄):            {resultado['media']:.4f}")
    print(f"Desviación estándar:   {resultado['desviacion_estandar']:.4f}")
    print(f"n:                     {resultado['n']}")
    print(f"Nivel de confianza:    {int(resultado['nivel_confianza'] * 100)}%")
    print(f"z:                     {resultado['z']}")
    print(f"Error estándar (EE):   {resultado['error_estandar']:.4f}")
    print(f"Margen de error (E):   {resultado['margen_error']:.4f}")
    print(
        f"\nIC = {resultado['media']:.4f} ± {resultado['margen_error']:.4f} = "
        f"({resultado['limite_inferior']:.4f}, {resultado['limite_superior']:.4f})"
    )


def modo_resumen():
    try:
        media = float(input("Media muestral (x̄): "))
        desviacion = float(input("Desviación estándar (s): "))
        n = int(input("Tamaño de muestra (n): "))
    except ValueError:
        print("Error: ingresá solo números.")
        return

    if n <= 0:
        print("Error: n debe ser mayor que 0.")
        return

    nivel_confianza = elegir_nivel_confianza()
    resultado = intervalo_confianza_media_z(media, desviacion, n, nivel_confianza)
    mostrar_resultado(resultado)


def modo_datos():
    entrada = input("Ingresá los datos separados por espacio o coma: ")
    entrada = entrada.replace(",", " ")
    try:
        datos = [float(x) for x in entrada.split()]
    except ValueError:
        print("Error: asegurate de ingresar solo números.")
        return

    if len(datos) < 2:
        print("Error: se necesitan al menos 2 datos.")
        return

    nivel_confianza = elegir_nivel_confianza()
    resultado = intervalo_confianza_desde_datos(datos, nivel_confianza)
    mostrar_resultado(resultado)


def main():
    print("Intervalo de confianza para la media (estadístico Z)")
    print("¿Cómo querés ingresar los datos?")
    print("1) Ya tengo x̄, s y n (datos resumidos)")
    print("2) Tengo la lista completa de datos")
    opcion = input("Elegí 1 o 2 [1]: ").strip() or "1"

    if opcion == "2":
        modo_datos()
    else:
        modo_resumen()


if __name__ == "__main__":
    main()
