# Cuestionario de Laboratorio 08

**1. ¿Qué otros modelos de colores existen para las imágenes?**

Existen múltiples modelos y espacios de colores, entre los más comunes en el procesamiento de imágenes están:
- **HSV (Hue, Saturation, Value):** Es excelente para la segmentación por colores, ya que separa el tinte (color puro) de la saturación y del brillo (luz), lo que lo hace menos sensible a sombras que el modelo RGB.
- **CMYK (Cyan, Magenta, Yellow, Key/Black):** Modelo sustractivo utilizado principalmente para impresoras y artes gráficas.
- **YCrCb / YUV:** Muy usado en transmisiones de televisión y compresión de video (como JPEG). Separa la luminancia (Y, brillo) de la crominancia (color).
- **Grayscale (Escala de Grises):** Utiliza un solo canal que indica la intensidad de la luz (típicamente de 0 a 255).
- **RGBA:** Es el modelo RGB tradicional, pero incluye un cuarto canal llamado "Alpha" que define la opacidad/transparencia del píxel.

**2. ¿Qué otros cambios se pueden realizar a las imágenes con OpenCV?**

Con la librería OpenCV se puede aplicar una inmensa cantidad de transformaciones matemáticas y visuales, como por ejemplo:
- **Transformaciones Geométricas:** Rotación, traslación, escalado, transformaciones afines y de perspectiva (útiles para enderezar documentos).
- **Filtros Espaciales:** Diferentes tipos de difuminado o desenfoque (Blur, Gaussiano, Mediana) para reducir ruido, o filtros de enfoque para afinar detalles.
- **Detección de Bordes:** Algoritmos como Canny y Sobel que encuentran los cambios bruscos de intensidad para delinear objetos.
- **Morfología Matemática:** Operaciones de erosión, dilatación, apertura y cierre, fundamentales para limpiar imperfecciones o ruidos en imágenes binarizadas.
- **Detección de Características y Objetos:** Algoritmos para encontrar líneas y círculos (Transformada de Hough), reconocimiento de rostros (Haar Cascades), o encontrar puntos clave (SIFT, ORB).
- **Corrección de Histogramas:** Ecualización para mejorar globalmente o localmente el contraste de imágenes oscuras.

**3. ¿Cuál sería el uso del binary threshold en el procesamiento de imágenes?**

El umbral binario (binary threshold) es una técnica esencial utilizada principalmente para la **segmentación** de imágenes. Sus usos principales incluyen:
- **Separación de objeto y fondo:** Al convertir una imagen en blanco y negro puro, permite separar los objetos de interés del fondo del escenario.
- **Paso previo obligatorio:** Muchos algoritmos como la búsqueda de contornos (findContours) o las operaciones morfológicas requieren de imágenes binarias puras para funcionar de manera óptima.
- **Extracción de texto (OCR):** Limpiar y binarizar el documento facilita enormemente que los algoritmos de reconocimiento óptico de caracteres identifiquen las letras sin ser afectados por manchas o sombras en el papel.
- **Detección de defectos industriales:** En automatización de fábricas, simplificar la imagen a dos colores ayuda a inspeccionar rápidamente si hay fisuras, cortes o piezas faltantes.
