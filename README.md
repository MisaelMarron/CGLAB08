# Laboratorio de Procesamiento de Imágenes 08

Este proyecto contiene una serie de ejercicios prácticos de procesamiento de imágenes utilizando Python y la librería OpenCV.

## Requisitos Previos

Asegúrate de tener Python instalado en tu sistema. Luego, instala las dependencias necesarias.

## Cómo instalar dependencias

Abre una terminal o consola y ejecuta el siguiente comando en la raíz de este proyecto:

```bash
pip install -r requirements.txt
```

## Cómo colocar las imágenes

1. Navega a la carpeta `imagenes/`.
2. Coloca tres imágenes con los nombres exactos: `imagen1.jpg`, `imagen2.jpg` y `imagen3.jpg`.
3. Es recomendable que al menos una imagen (`imagen1.jpg`) sea de una persona o animal para observar correctamente el ejercicio 05.

*(Nota: Si no las colocas, los scripts mostrarán un mensaje indicando que no encuentran el archivo y evitarán que el programa falle).*

## Cómo ejecutar cada archivo

Abre tu terminal (por ejemplo, en VS Code) en la carpeta raíz del proyecto (`Lab_Procesamiento_Imagenes`) y ejecuta los scripts uno a uno en el siguiente orden:

```bash
python scripts/ejercicio_01_redimensionar.py
python scripts/ejercicio_02_combinar_canales.py
python scripts/ejercicio_03_negativo_grises.py
python scripts/ejercicio_04_visualizador_canales.py
python scripts/ejercicio_05_dibujar_circulo_texto.py
python scripts/ejercicio_06_umbral_binario.py
python scripts/ejercicio_07_dibujo_interactivo.py
```

## Qué resultado genera cada ejercicio

- **Ejercicio 01:** Encuentra la imagen más grande, redimensiona las demás manteniendo su proporción y les agrega bordes negros para que todas queden exactamente del mismo tamaño. Genera archivos en la carpeta `resultados/`.
- **Ejercicio 02:** Toma las tres imágenes del ejercicio 1 y crea una nueva imagen utilizando el canal rojo de la primera, el verde de la segunda y el azul de la tercera.
- **Ejercicio 03:** Genera el negativo de la imagen combinada del ejercicio 02, y posteriormente crea una versión en escala de grises del negativo.
- **Ejercicio 04:** Lanza un visualizador interactivo donde puedes activar/desactivar los canales (Rojo, Verde, Azul) utilizando las teclas `r`, `g`, y `b`. Con `s` guardas la imagen.
- **Ejercicio 05:** Dibuja un círculo y un texto descriptivo sobre `imagen1.jpg`.
- **Ejercicio 06:** Convierte `imagen2.jpg` a escala de grises y aplica un umbral binario para separar objetos del fondo (convierte la imagen a blanco y negro puro).
- **Ejercicio 07:** Abre un lienzo interactivo para dibujar libremente utilizando el mouse. Las teclas `l`, `r` y `c` cambian entre línea, rectángulo y círculo. La tecla `u` deshace el último trazo y `s` guarda el dibujo final.
