import pandas as pandita
import matplotlib.pyplot as tatplocito

datos = {
    'Producto': ['Televisor', 'Celular', 'Laptop', 'Tablet', 'Audífonos'],
    'Ventas': [150, 200, 250, 300, 100],
    'Precio': [750, 650, 900, 400, 120]
}
df = pandita.DataFrame(datos)

html_tabla = df.to_html(index=False, border=0, justify='center')
estadisticas = df.describe().to_html(border=0, justify='center')

tatplocito.figure(figsize=(7,5))
tatplocito.bar(df['Producto'], df['Ventas'], color='#a1cfff', edgecolor='black')
tatplocito.title('Ventas por Producto', fontsize=14, fontweight='bold')
tatplocito.xlabel('Producto')
tatplocito.ylabel('Ventas')
tatplocito.xticks(rotation=30)
tatplocito.grid(axis='y', linestyle='--', alpha=0.5)
tatplocito.tight_layout()
tatplocito.savefig("grafiquita.png")   # nuevo nombre
tatplocito.close()

html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Datos de Ventas</title>
<style>
  body {{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 40px;
    background: #ffd6e8;
    color: #333;
  }}
  h1 {{
    color: #c2185b;
    text-align: center;
  }}
  h2 {{
    color: #8b0051;
  }}
  table {{
    border-collapse: collapse;
    margin-bottom: 25px;
    width: 70%;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    background: #cfe9ff;
  }}
  th, td {{
    border: 1px solid #fff;
    padding: 10px;
    text-align: center;
  }}
  th {{
    background: #aee2ff;
    font-weight: bold;
  }}
  img {{
    display: block;
    margin: 10px auto;
    border-radius: 10px;
    width: 520px;
    border: 3px solid #fff;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
  }}
  pre {{
    font-size: 15px;
    color: #4a4a4a;
    line-height: 1.1;
    text-align: center;
  }}
</style>
</head>
<body>
<h1>Datos de Ventas</h1>
<h2>Tabla de Datos:</h2>
{html_tabla}
<h2>Estadísticas Descriptivas:</h2>
{estadisticas}
<h2>Gráfica de Ventas:</h2>
<img src="grafiquita.png" alt="Gráfica de Ventas">

<h2>Integrantes:</h2>
<pre>
♡ Nelson Alexander ♡        ♡ Emely Pamela ♡        ♡ Franklin Osmar ♡

 (\_/)                       (\_/)                       (\_/)
 (•ᴗ•)                       (•ᴗ•)                       (•ᴗ•)
 />💙                        />💗                       />💚
</pre>  
</body>
</html>"""

with open("tabla.html", "w", encoding="utf-8") as f:
    f.write(html)

print("-------------------------------------------------")
print("tablitas creadas (con grafiquita bonita licenciada :3)")
print("-------------------------------------------------")
