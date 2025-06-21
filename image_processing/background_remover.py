from rembg import remove
from PIL import Image

input_path  = r"C:\Users\Al-arab\Pictures\Screenshots\eren1.png"
output_path = r"C:\Users\Al-arab\Pictures\Screenshots\output.png"
The_image   = Image.open(input_path)
The_output  = remove(The_image)
The_output.save(output_path)