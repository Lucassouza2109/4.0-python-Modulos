# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python 😂


from pathlib import Path

from PIL import Image
# PIL = de Pillow. 

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'original.JPG'
NEW_IMAGE = ROOT_FOLDER / ' new.JPG'

pil_image = Image.open(ORIGINAL) # ABRI A IMAGEM ORIGINAL. 
width, height = pil_image.size   # LARGURA | ALTURA
exif = pil_image.info['exif']    # INFORMACOES SOBRE IMAGENS. 

# width     new_width
# height    ??
new_width = 640 # NOVA LARGURA
new_height = round(height * new_width / width) # NOVA ALTURA

new_image = pil_image.resize(size=(new_width, new_height))
# RESIZE = Redimensionar. 

# Abaixo, modo de salvar. 
new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=70,
    # exif=exif,
)

