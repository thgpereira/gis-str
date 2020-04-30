# DESAFIO GIS

A imagem analytic.tif é uma imagem de satélite multiespectral georreferenciada em formato GeoTIFF obtida pelo microsssatélite ID 0c0b da constelação PlanetScope em 7 de dezembro de 2016, às 15h19m53s UTC.

| Índice | Banda | Alcance Espectral (nm)  |
| ------ |:-----:| -----------------------:|
| 1      | Blue  | 455 - 515               |
| 2      | Green | 500 - 590               |
| 3      | Red   | 590 - 670               |
| 5      | NIR   | 780 - 860               |


O projeto efetua os seguintes cálculos: 

- Percentual de área da imagem que está coberto por algum tipo de vegetação
- Centróide geográfico da cena
- Área em quilômetros quadrados da cena
- Horário local da captura

# Aplicação
### Docker
docker build -t strider:latest ./
docker run -d -p 5000:5000 strider

Acessar http://localhost:5000/ ou http://127.0.0.1:5000/
