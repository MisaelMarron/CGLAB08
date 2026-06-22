import cv2
import os

def verificar_existencia(ruta):
    """Verifica si un archivo existe en la ruta dada."""
    if not os.path.exists(ruta):
        print(f"Error: No se encontró el archivo en la ruta '{ruta}'")
        return False
    return True

def cargar_imagen(ruta):
    """Carga una imagen y retorna el objeto de imagen."""
    if verificar_existencia(ruta):
        return cv2.imread(ruta)
    return None

def guardar_imagen(ruta, img):
    """Guarda una imagen en la ruta especificada."""
    # Crear directorio si no existe
    directorio = os.path.dirname(ruta)
    if directorio and not os.path.exists(directorio):
        os.makedirs(directorio)
    cv2.imwrite(ruta, img)
    print(f"Imagen guardada exitosamente en '{ruta}'")

def redimensionar_aspect_ratio(img, target_w, target_h):
    """Redimensiona una imagen manteniendo su relación de aspecto (aspect ratio)."""
    h, w = img.shape[:2]
    escala = min(target_w / w, target_h / h)
    nuevo_w = int(w * escala)
    nuevo_h = int(h * escala)
    # cv2.INTER_AREA es recomendado para reducir el tamaño de una imagen
    return cv2.resize(img, (nuevo_w, nuevo_h), interpolation=cv2.INTER_AREA)

def agregar_bordes_negros(img, target_w, target_h):
    """Agrega bordes negros a una imagen para alcanzar las dimensiones objetivo."""
    h, w = img.shape[:2]
    # Calcular bordes necesarios para centrar la imagen
    top = (target_h - h) // 2
    bottom = target_h - h - top
    left = (target_w - w) // 2
    right = target_w - w - left
    color_borde = [0, 0, 0] # Negro
    return cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color_borde)

def mostrar_imagen(titulo, img):
    """Muestra una imagen en una ventana."""
    cv2.imshow(titulo, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
