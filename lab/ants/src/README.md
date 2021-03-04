# Modelos basados en agentes

## Installar dependencias

El projecto se manejó con [`poetry`](https://python-poetry.org/). Para instalar
dependencias basta correr

``` console
$ poetry install
```

En caso de no usar `poetry`, se incluyó un dump de las dependencias en
`requirements.txt`. Para instalarlas, basta con correr

``` console
$ pip install -r requirements.txt
```

## Correr

El script `launch.py` corre el modelo indicado. Este se indica con su nombre. Es
decir, con poetry,

``` shell
$ poetry run python launch.py <modelo>
```

o sin poetry,

``` shell
$ python launch.py <modelo>
```

donde `<modelo>` es 'termites', 'langton', 'ants' o 'schelling'.

Inmediatamente se abre la ventaca con la visualización del modelo.

## Análisis

El modelo de hormigas y el de segregación requirieron análisis más a fondo que
el dado en las visualizaciones. Estos análisis se hicieron en los cuadernos de
`AntAnalysis.ipynb` y `SchellingAnalysis.ipynb`. Las dependencias extra para los
análisis ya están en el proyecto.
