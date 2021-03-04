# Automata celulares

__Alumno:__ _Edgar Quiroz_

## Preguntas

1. ¿Qué es la complejidad?
    Es una propiedad que puede tener un sistema. Significa que el comportamiento del sistema no se puede explicar únicamente con el comportamiento de sus partes. Es decir, la interacción entre las diferentes partes juega un papel muy importante en el comportamiento general.
2. ¿Cuándo se usa el concepto de autoorganización en un sistema?
    Cuando de forma macroscópica un sistema posee diferentes partes coordinadas que realizan cierta acción pero no hay ningún tipo de control centralizado. Cada parte actúa de forma independiente interactuando con su ambiente local.
3. ¿Qué es una propiedad emergente?
    Es alguna propiedad que tiene un sistema que no tienen sus partes. Como estructura u organización. Algo que emerge al juntar todo. Todo sistema complejo tiene propiedades emergentes.
4. ¿Qué es la fractalidad?
    Es una propiedad de los objetos geométricos. Intuitivamente, un objeto es fractal si es autocontenido. Es decir, si una sección de él es estructuralemente similar a la figura completa. Formalmente, un objeto es fractal si su dimensión fractal es mayor a su dimensión topológica.

## Autómata celular elemental

1. Explore algunas de las 256 reglas del autómata celular a partir de la implementación de su programa con condiciones de frontera periódicas, mínimo 100 tiempos de evolución y condiciones iniciales aleatorias. Identifique el tipo de dinámica que presenta y a que clase pertenece según las cuatro categorías de la Clasificación de Wolfram. Muestre dos representaciones de cada clase junto con una captura de pantalla de cada una.

    - Clase I: estable

    Convergen siempre a un mismo estado independientemente de la entrada.

    Regla 168

    @import "168.png"

    Regla 40

    @import "40.png"

    - Clase II: periódica

    Se repiten cada cierta cantidad de pasos.

    Regla 51

    @import "51.png"

    Regla 73

    @import "73.png"

    - Clase III: caótica

    EL resultado depende fuertemente de la entrada y pequeñas variacones afectan mucho el resultado.

    Regla 105

    @import "105.png"

    Reglo 90

    @import "90.png"

    - Clase IV: compleja

    Muestran emergencia, como patrones sin periodo. La salida depende de la entrada, pero patrones similares se encuentran sin importar la entrada.

    Regla 106

      @import "106.png"

    Regla 41

      @import "41.png"

2. Después de visualizar las 256 reglas con el programa que implementaste ¿Cuál crees que sea la clase más frecuente?

    Me parece que las clases periódicas son las más frecuentes. En especial las de periodo igual a toda la longitud de la celda o de periodo 1.

    Patrones muy comunes son el recorrer todas las celdas a la izquierda o derecha, o converger a un estado dependiente de la entrada. Ambos patrones son periódicos.

3. Con base en las observaciones hechas en clase y con su programa, encuentre 3 autómatas de clase IV. Adjuntar en el documento las capturas de pantalla.

    En la pregunta 1 se propusieron dos de ellas. La regla 106 parece producir montañas diagonales. No parece tener periodo pero las estrucuturas encontraras son bastante autosemenjantes. La regla 41 produce desplazamientos pero no parece tener un periodo.

    Otra regla que siempre produce patrones sin periodo es la regla 110. Esta produce el mismo tipo de triángulos en diferentes escalas. Pero la distribución de los triángulos parece aleatoria.

    @import "110.png"

4. Encuentre un autómata de clase III, perturbe la condición inicial aleatoria por un bit, evolucione y trate de ver las diferencias entre el autómata perturbado y el normal. ¿La sensibilidad a las condiciones iniciales es una propiedad suficiente para catalogar la dinámica como caótica? Explique. Adjunte las imágenes del ACE perturbado, sin perturbar y la diferencia de estados.

    Se ejecutó al regla 90 (que es de clase III) con condiciones iniciales. Luego, copiaron esas mismas condiciones (en azul) excepto un autómata al que se invirtió el estado (en rojo).

    Finalmente, se calcularon los estados diferentes en verde.

    @import "90caos.png"

    Se puede apreciar que esta diferencia es el mismo comportamiento que la regla 90 con un solo autómata vivo como condición inicias.

    Entonces se podría considerar que para que una regla sea caótica, aún debe tener cierta regularidad en sus salidas. En este caso sería que una ejecución y su perturbación difieren exactamente en la ejeución de la diferente del estado inicial.

    Este tipo de propiedades no se observan directamente y hay que hacer un análisis más minicioso para encontrarlos.

5. ¿Qué poder de cómputo tiene la regla 132?

    Por observación, parece que las secuencias seguidas de células vivas forman triángulos. Si la longitud es par, el triángulo se concluye y los autómatas mueren. Si es impar, el autómata central quedará vivo.

    Parece que este comportamiento es el mismo sin importar la entrada, así que se podría conjeturar que puede computar la función constante que cuenta la cantidad de secuencias de autómatas vivos de longitud impar.

6. Considere la regla 22. Explique la dinámica usando como ejemplo la evolución con una condición simple (una sola celda) y aleatoria.

    Podrías ser que de cada celda viva se crean un triángulo. En cuanto dos triángulos se encuentran, tal vez se destruyan o se fusionen de una manera no homogénea.

    Así, cuando inicialmente solo hay un autómata vivo, el resultado es un triágnulo de Sierpinski. Pero cuando hay más de uno, las interaciones entre ellos generan y destruyen triángulos de tal manera que no se generan estrucuturas grandes y no hay periodos.

7. Si el autómata estuviera definido con un alfabeto de 3 estados considerando sus primeros vecinos, ¿cuántas posibles reglas hay?

    Como se consideran los vecinos, entonces la función recibe tres estados. Cada uno de estos estados puede tener tres valores. Así que hay $3^3$ posibles entradas para la función de transición. Luego, cada entrada se puede mapear a uno de tres estados. Lo que da un total de $3^{3^3}=19683$ posibles funciones.

## Juego de la vida

1. Inicie aletatoriamente las células con una densidad de 0.5 ¿En cuánto tiempo se estabiliza la cantidad de células vivas?¿Es lo mismo para toda configuración?

    En varias ejecuciones se obtuvieron los siguiente resultados

    | Ticks |
    | ----- |
    | 1725  |
    | 1500  |
    | 1300  |
    | 1575  |
    | 750   |
    | 2500  |
    | 975   |
    | 4000  |
    | 1500  |
    | 800   |

    En general están al rededor de 1500 ticks, pero hay casos donde tarda 4000 y 750, que varia mucho del promedio.

    Se incluyen las imágenes de la instancia con 4000 ticks

    @import "4000.png"
    @import "4000.jpeg"

    En general, como el juego de la vida es computacionalmente equivalente a una máquina de Turing, determinar cuando se estabiliza la cantidad de células vivas podría formulzarse en términos de la ejecución de un programa. Como existen programas que nunca terminan, debe existir una condición inicial que nunca se estabiliza.

    Encontrarla al azar podría ser complicado, pero debe existir. Así que en general no se puede saber nada sobre la cantidad de ticks para que una configuración se estabilice.

2. ¿Qué pasa con una densidad de 0.85?

    Con una densidad tan alto hay un problema de sobrepoblación. La gran mayor parte de las células muere de inmediato por tener demasiados vecinos, en menos de 5 ticks en la mayoría de los casos. Así que la cantidad rápidamente se estabiliza en un número muy bajo de células que encuentras un equilibrio local.

    Por ejemplo la siguiente que se estabilizó en 5 ticks.

    @import "5cells.png"
    @import "5cells.jpeg"

    Aún así, hay casos excepcionales, como el siguiente

    @import "1300cells.png"
    @import "1300cells.jpeg"

    Tardó aproximadamente 1300 ticks en estabilizarse y autmentó en gran medida su cantidad de células antes de estabilizarse.

    Probablemente haya alguna configuración con densidad 0.85 que nunca se estabilice. Pero por la sobrepoblación, en general estas configuraciones se estabilizan rápido.

3. Usando _Gosper's Gun_, _Slider_ e _Eater_ simula los operadores _AND_, _OR_ y _NOT_. Para cada circuito incluya imágenes de la condición inicial, de alguna colisión y del resultado. Explique porqué funcionan.

    - _NOT_

    Configuración inicial con la señal de entrada (gosler izquierdo) y la salida (gosler derecho).

    @import "not_init.png"

    Un gosler (el de la derecha) interfiere la señal de entrada (el gosler de la izquierda).

    @import "not_final1.png"

    Si no hay señal de entrada (si la entrada es 0), entonces la señal del gosler derecho pasa sin problemas. Al haber salida, esto es un 1.

    @import "not_coll2.png"

    Cuando hay señal de entrada (cuando la entrada es 1) los gliders se cancela y no hay salida, que representa un cero.

    - _AND_

    Hay dos señales de entrada (los dos gosler de la izquierda) y una señal de interferencia (el gosler de la derecha).

    @import "and_init.png"

    Si ambas señales están presentes, una de ellas es destruida por la señal de interferencia, y la otra es visible, lo que simboliza un uno.

    @import "and_final.png"

    Si alguna de las señales de entrada está bloqueada, entonces la señal de interferencia detruirá la otra y no habrá salida. Lo que es un cero.

    @import "and_final2.png"

    Entonces la salidad será uno solo si ambas entradas están presentes.

    - _OR_

    Hay dos señales de entrada (los gosler centrales), la señal de salida (el gosler izquierdo) y una señal de interferencia (el gosler derecho).

    @import "or_init.png"

    Si ambas señales están bloqueadas, la interferencia destruye la salida, y no hay nada. Esto simbolza un cero.

    @import "or_final1.png"

    Si al menos una señal está presente, esta se destruye junto con la interferencia, y la señal de salida no es destruida. Esto representa un uno.

    @import "or_final2.png"

    Entonces, si al menos una señal de entra está presente, la salida es uno.

4. ¿El juego de la vida es reversible?
    No. Esto es porque la función de transición para las células no es reversible. Es decir, en general dada una configuración, hay muchas posibles configuraciones que pudieron llevar a ella. Y como la única información que se tiene es el estado actual, no es pisble determinar el estado anterior.
