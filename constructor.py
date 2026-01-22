import os
import random

carpeta = r"todos_los_gifs"
carpeta_2 = r"gif_memes"
carpeta_3 = "fondos"

imagenes = os.listdir(carpeta)
imagenes_2 = os.listdir(carpeta_2)
imagenes_3 = os.listdir(carpeta_3)

textos = [
"Error 404", 
"Post overflow = 0", 
"インターネットのゴミ", 
"Rules 1 & 2: Do not talk about /b/.", 
"Desu desu desu.", 
"GOD Butthurt Dweller", 
"I am the one and only Christian Weston Chandler",
"Do a barrel roll!",
"U MAD?",
"( ͡° ͜ʖ ͡°)",
"чики-брики",
"""???????
????????
????!!%$↓
@@@@@
@@@"""
]

colores = [
    "#FF0000",  # Rojo
    "#FF7F00",  # Naranja
    "#FFFF00",  # Amarillo
    "#00FF00",  # Verde
    "#0000FF",  # Azul
    "#4B0082",  # Índigo
    "#8F00FF"   # Violeta
]



html = """
<!DOCTYPE html>
<html>
<body>
<style>
body {
  height: 2000px;
  width: 4000px;
  margin: 0;
  background-image: url("fondos/colorful-pixel-background-noise-signal-600nw-1913233048.webp");
}
</style>
<h1>xD.com</h1>
"""
for i in range(20): #Creador fondo
    for img in imagenes_3:
        html += f'<img src="{carpeta_3}/{img}" width = "{random.randint(1000, 1200)}" style="position: absolute; top: {random.randint(-100, 2000)}px; left: {random.randint(-1000, 6200)}px;">\n'
html += f'<img src="fondos\wp7848940.jpg" width = "2000px" style="position: absolute; top: 2800px; left: 0px;">\n'
html += f'<img src="fondos\wp7848940.jpg" width = "2000px" style="position: absolute; top: 2800px; left: 2000px;">\n'

for i in range(10): #Creador gifs (88x31)
    for img in imagenes:
        html += f'<img src="{carpeta}/{img}" width = "{random.randint(50, 300)}" style="position: absolute; top: {random.randint(-100, 4000)}px; left: {random.randint(-100, 7000)}px;">\n'

for i in range(30):
    for img in imagenes_2: #Creador memes
        html += f'<img src="{carpeta_2}/{img}" width = "{random.randint(50, 300)}" style="position: absolute; top: {random.randint(-100, 3550)}px; left: {random.randint(-100, 7000)}px;">\n'

for i in range(120):
    html += f'<p style="position: absolute; top: {random.randint(-100, 4000)}px; left: {random.randint(-100, 4000)}px; font-size: {random.randint(50, 100)}px; width: 3000px; color: {random.choice(colores)}">{random.choice(textos)}</p>\n'


html += """
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as file:
        file.write(html)

