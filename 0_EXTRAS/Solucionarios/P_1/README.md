<table align="center">
  <tr>
    <td rowspan="4">
      <img src="../Img/Escudouatf.png" alt="Escudo" width="100" align="center">
    </td>
    <td colspan="7" align="center">
      <h1> UNIVERSIDAD AUTÓNOMA “TOMÁS FRÍAS”<br>
      INGENIERÍA DE SISTEMAS</h1>
    </td>
  </tr>

  <tr>
    <td colspan="1"><b>ESTUDIANTE:</b></td>
    <td colspan="3"></td>
    <td colspan="1"><b>C.I.:</b></td>
    <td colspan="1"></td>
  </tr>
  
  <tr>
    <td colspan="1"><b>DOCENTE:</b></td>
    <td colspan="2">Ing. Clever Bravo Villafuerte</td>
    <td colspan="1"><b>MATERIA:</b></td>
    <td colspan="1">SIS-110 G1</td>
    <td colspan="1" rowspan="2" style="text-align: center;"><b>PRÁCTICA<br>N°1</b></td>
  </tr>

  <tr>
    <td colspan="1"><b>AUXILIAR:</b></td>
    <td colspan="2">Univ. Gabriel Alejandro Garvizu Salas</td>
    <td colspan="1"><b>FECHA:</b></td>
    <td colspan="1">02/04/2025</td>
  </tr>

</table>

## PREGUNTAS Y RESPUESTAS/SOLUCIONES:
> - CADA PREGUNTA TIENE UN VALOR DE 6.67PTS, SUMANDO LAS 15 UN TOTAL DE 100PTS.

**1.** Un volcán ha entrado en erupción recientemente en Geldingadalur, Islandia. Afortunadamente, esta erupción es relativamente pequeña y, a diferencia de la infame erupción del Eyjafjallajökull, no se espera que cause retrasos en los vuelos internacionales o indignación mundial. Existe cierta preocupación por el gas magmático que se ha liberado como parte de la erupción, ya que podría representar un peligro para las poblaciones humanas en los alrededores. Los científicos han estimado la cantidad total de gas emitido que, debido a la falta de viento, se ha distribuido uniformemente en un área circular alrededor del centro del volcán. Las autoridades han evacuado el área y ahora quisieran cerrarla rodeando el perímetro con cinta de barrera y tu labor es: dado el área total cubierta por gas en metros cuadrados calcular la longitud total de cinta de barrera necesaria para rodear el área cubierta por gas en metros.

### Solución
**Datos:** Área $A$ (m²) distribuida en un círculo.
**Objetivo:** calcular el perímetro $(\text{longitud de cinta})$.

* Si el área es $A$, el radio es

$$
r = \sqrt{\frac{A}{\pi}}
$$

* El perímetro de un círculo es

$$
P = 2\pi r = 2\pi \sqrt{\frac{A}{\pi}} = 2\sqrt{\pi A}.
$$

**Respuesta:**

$$
\boxed{2\,\sqrt{\pi\,A}\text{ metros de cinta}}
$$

---

**2.** En el extenso mundo de los números existen variedad de ellos que tiene cualidades especiales, únicas, curiosas, etc.; por ejemplo, tenemos al número 542.986.731, ¿Puedes decirnos por qué o qué hace que este número sea tan especial o único en su clase?

### Solución
Ese número es **pandigital**: contiene exactamente una vez cada dígito del 1 al 9 (no incluye el 0) y además es **primo**. Esa combinación (ser primo y pandigital de nueve dígitos) lo hace muy raro en teoría de números.

---

**3.** Si el pasado mañana de ayer es jueves, ¿qué día será el anteayer, del ayer del mañana?

### Solución
* “Pasado mañana de ayer” = dos días después de “ayer”.
* Si “ayer” + 2 = jueves ⇒ “ayer” = martes ⇒ hoy = miércoles.

Luego:

> “el anteayer, del ayer del mañana”

1. “mañana” = jueves, porque hoy es miércoles.
2. “ayer del mañana” = miércoles (el día antes de jueves).
3. “anteayer” de ese miércoles = **lunes**.

**Respuesta:** Lunes.

---

**4.** Después del concurso clasificatorio de programación, los jueces y concursantes van a comer una pizza al restaurante de Alfredo Los concursantes están muy hambrientos después de concursar durante 5 horas seguidas sin descanso. Para tenerlo preparado al momento, deciden ordenar una pizza gigante para todos en vez de muchos pequeños. Ellos se preguntan si será posible poner la pizza gigante rectangular en la superficie de una mesa redonda tal que los extremos no cuelguen del borde de la mesa.

Dado un entero R que es el radio de la superficie de la mesa redonda donde los concursantes están sentados y otros dos enteros W y L especificando el ancho y el largo de la pizza respectivamente, indicar si la pizza cabe o no en la mesa.

### Solución
* Mesa de radio $R$: diámetro $=2R$.
* Pizza de ancho $W$ y largo $L$: para que quepa sin colgar, su **diagonal**
  $\sqrt{W^2+L^2}$ debe ser ≤ $2R$.

**Respuesta:**

* **Cabe** si $\sqrt{W^2+L^2}\le2R$.
* **No cabe** si $\sqrt{W^2+L^2}>2R$.

---

**5.** Una madre tiene 40 años y su hijo tiene recién cumplidos sus 10 años. El niño es bastante listo y disfruta mucho de los juegos con números, su madre para entretenerle le hizo una pregunta: ¿Cuántos años deberían de pasar para que mi edad sea el triple de la edad de que tengas tú?

### Solución
* Ahora:
  * madre = 40
  * hijo = 10.

* Dentro de $x$ años:

  $$
  40 + x = 3\,\bigl(10 + x\bigr)
  \quad\Longrightarrow\quad
  40 + x = 30 + 3x
  \quad\Longrightarrow\quad
  10 = 2x
  \quad\Longrightarrow\quad
  x = 5.
  $$

**Respuesta:** en **5 años**.

---

**6.** José es un niño que tiene un gusto gigante por los dulces, pero... no podemos decir lo mismo que por las matemáticas, es la materia que más se le complica; cierto día en su escuela hubo una competencia de matemáticas en la cual el premio sería una gran cantidad de dulces, era obvio de que José trataría de ganar, a pesar de no ser muy bueno en matemáticas. Sorpresivamente José fue respondiendo bien casi todas las preguntas que se dieron en el concurso hasta el punto de llegar a la ultima pregunta que definiría si se lleva el jugoso premio o no, la pregunta era: si un niño de 12 años en promedio consume 550 gramos de pan al día. ¿Cuál será el consumo diario en kilos de un comedor entero compuesto por 214 niños?. Ayuda a José a ganarse sus tan ansiados dulces.

### Solución
* Un niño consume 550 g/día.
* Para 214 niños:

  $$
  214\times550 = 117\,700 g = 117,7 kg.
  $$


---

**7.** Dos amigos aburridos una tarde deciden jugar a las adivinanzas para pasar el rato y entretenerse un poco, uno de ellos le plantea la siguiente pregunta al otro: “Antes de ayer, mi hermana tenía 15 años. El año que viene tendrá 18. ¿Qué día crees que es hoy?”. Ayuda a su amigo a encontrar la respuesta correcta a la adivinanza y ganar el juego.

### Solución
“Antes de ayer mi hermana tenía 15; el año que viene tendrá 18.”

* Eso solo es posible si hoy es **1 de enero**, y su cumpleaños es el 31 de diciembre.

**Respuesta al enigma (¿qué día es hoy?):** 1 de enero.

---

**8.** Los 52 alumnos del grupo A, los 40 alumnos del grupo B, y los 32 alumnos del grupo C, presentan examen parcial de matemáticas I. En el grupo A, aprueban 36 y reprueban 16; en el grupo B, aprueban 28 y reprueban 12; en el grupo C, aprueban 24 y reprueban 8. ¿Qué grupo tiene mayor nivel de aprobación?

### Solución
| Grupo | Alumnos | Aprobados | Tasa (%)        |
| ----- | ------- | --------- | --------------- |
| A     | 52      | 36        | $36/52=69{,}2$% |
| B     | 40      | 28        | $28/40=70$%     |
| C     | 32      | 24        | $24/32=75$%     |

**Respuesta:** el **grupo C** tiene el mayor nivel de aprobación (75 %).

---

**9.** Hay un tablero de ajedrez de 8x8 en el que se han cortado dos esquinas diagonalmente opuestas. Te dan 31 fichas de dominó, una ficha de dominó puede cubrir exactamente dos cuadrados. ¿Puedes usar las 31 fichas de dominó para cubrir todo el tablero? Demuestre su respuesta (proporcionando un ejemplo o mostrando por qué es imposible).

### Solución
Al quitar dos esquinas opuestas de un tablero de ajedrez 8×8, quedan 62 casillas. Pero siempre se quitan dos esquinas del **mismo color** (ambas negras o ambas blancas). Un dominó cubre una casilla negra y una blanca:

* Para cubrir 62 casillas harían falta 31 dominós, pero entonces se necesitarían 31 casillas de cada color.
* Al quitar dos del mismo color, quedan 32 de un color y 30 del otro ⇒ **no es posible** cubrir.

**Respuesta:** imposible, por la desigualdad de casillas blancas/negras.

---

**10.** En uno de tus tantos viajes por el mundo por mala suerte te atrapa una fuerte lluvia, ¡y peor aún te terminaste enfermando muy severamente!, pero no todo está perdido para ti y tus viajes, una amiga que hiciste en el sitio te recomendó un remedio casero, mencionando que funciona en 15 de cada 60 personas que lo probaron. ¿Qué probabilidades tienes de que funcione y puedes continuar con tus viajes?

### Solución
Funciona en 15 de cada 60 personas ⇒

$$
P = \frac{15}{60} = 0{,}25 = 25\%.
$$

---

**11.** Pedro y Nicol están enamorados y deciden tener una cita por primera vez, Nicol cita a Pedro a las 8 p.m. sin saber que Pedro tiene el reloj 15 minutos adelantado y Nicol olvida el detalle que el suyo lo trae 15 minutos atrasado. Si Pedro llega a la cita 15 minutos antes según su reloj y Nicol llega 15 minutos retrasada según su reloj. ¿Cuánto tiempo tuvo que esperar Pedro?

### Solución
* Nicol atrasa 15 min; su reloj marca $t_{\rm real} - 15$.
* Pedro adelanta 15 min; su reloj marca $t_{\rm real} + 15$.
* Pedro llega cuando su reloj marca las 7:45 (15 min antes de la cita “8:00” en su reloj) ⇒ hora real = 7:30.
* Nicol llega cuando su reloj marca las 8:15 (15 min tarde en su reloj) ⇒ hora real = 8:30.
* Tiempo de espera = 8:30 − 7:30 = **1 hora (60 minutos)**.

---

**12.** Guillermo es un amante de los gatos, en su casa vive junto a 4 gatos de diferentes colores cada uno y necesita alimentarlos, sin embargo, cierto día le entró una duda, ¿cuál de sus gatos es el que come menos? Lo único que sabe por ahora es que: El gato negro come más que el naranja, el gato blanco come más que el naranja y menos que el gato plomo, pero el gato plomo come más que el gato negro. ¿Qué gato es el que come menos?

### Solución
Condiciones:

* Negro > Naranja
* Blanco > Naranja
* Blanco < Plomo
* Plomo > Negro

De esto se deduce:

$$
\text{Plomo} > \text{Blanco} > \text{Negro} > \text{Naranja}.
$$

**Respuesta:** el **gato naranja** es el que come menos.

---

**13.** Cuatro jugadores de futbol americano entran en un ascensor que puede trasportar un máximo de 380 kilos, si se excede dicho limite sonará una alarma y se detendrá el ascensor dejándolos atrapados.

Para que no suene la alarma, tienes que ayudarles a calcular su peso total entre los cuatro, pero, ¿Cuánto pesa cada jugador? He aquí los datos:
- Pablo es quien pesa más: si cada uno de los otros pesara tanto como el, la alarma detendría el
ascensor.
- Carlos es el más ligero: ¡el ascensor podría subir a cinco como el sin problema alguno!
- Renato pesa 14 kilos menos que Pablo, y solo seis menos que Jesús.
- Jesús pesa 17 kilos más que Carlos. Los pesos de Pablo y de Carlos son múltiplos de cinco.

### Solución
Datos resumidos:

1. Si los otros tres (Carlos, Renato, Jesús) pesaran lo mismo que Pablo, sumarían $4P>380$.
2. Carlos es el más ligero: $5C\le380$.
3. Renato = $P - 14$ y Renato = $J - 6$ ⇒ $J = P - 8$.
4. Jesús = $C + 17$ ⇒ $P - 8 = C + 17$ ⇒ $P = C + 25$.
5. $P$ y $C$ son múltiplos de 5.

Resolviendo:

* De $5C\le380$ ⇒ $C\le76$, múltiplo de 5 ⇒ $C=75$.
* Entonces $P = 75 + 25 =100$.
* $J = P - 8 = 92$.
* $R = P -14 = 86$.

**Respuesta:**

* Pablo = 100 kg
* Carlos = 75 kg
* Jesús = 92 kg
* Renato = 86 kg

---

**14.** Explique y/o demuestre como podría generar la siguiente secuencia de números: **`1 1 2 3 5 8...`**

### Solución
Es la **sucesión de Fibonacci**, donde:

$$
F_1 = 1,\quad F_2 = 1,\quad
F_n = F_{n-1} + F_{n-2}\quad(n\ge3).
$$

---

**15.** Armando, Basilio, Carlos y Dionisio fueron, con sus mujeres, a comer. En el restaurante, se sentaron en una mesa redonda, de forma que:
- Ninguna mujer se sentaba al lado de su marido.
- Enfrente de Basilio se sentaba Dionisio.
- A la derecha de la mujer de Basilio se sentaba Carlos.
- No había dos mujeres juntas.

¿Quién se sentaba entre Basilio y Armando? 

### Solución
**Pareja:**

* Basilio (B) ⇔ esposa\_B
* Armando (A) ⇔ esposa\_A
* Carlos (C) ⇔ esposa\_C
* Dionisio (D) ⇔ esposa\_D

**Condiciones**:

1. Mesa redonda de 8 sillas.
2. No hay dos mujeres juntas ⇒ debe alternarse hombre–mujer.
3. Ninguna mujer junto a su esposo.
4. Enfrente de Basilio (B) se sienta Dionisio (D) ⇒ están a 4 sillas de distancia.
5. A la derecha (inmediata, sentido horario) de la esposa de Basilio se sienta Carlos (C).

**Solución paso a paso**:

1. **Ubicamos a los hombres fijos**:

   * Seat 0: Basilio (B)
   * Seat 4 (opuesto): Dionisio (D)

2. **Patrón de género** (alternado): hombres en asientos pares (0,2,4,6), mujeres en impares (1,3,5,7).

3. **Colocamos a Carlos**:

   * Sabemos que “a la derecha de esposa\_B” (si esposa\_B está en *i*, Carlos va en *(i+1) mod 8*).
   * Además, esposa\_B **no puede** sentarse en asientos 1 o 7 (son vecinos de Basilio en 0), ni en 3 (porque entonces Carlos caería en el opuesto 4 que ya ocupa D).
   * La única opción es poner esposa\_B en el asiento 5 ⇒ Carlos en el 6.

4. **Queda libre el asiento 2 para el último hombre**: Armando (A).

5. **Ahora asignamos las demás esposas** a 1, 3 y 7, respetando que no queden junto a su propio esposo:

   * esposa\_A no puede ir junto a Armando (seat 2 ⇒ no asientos 1 ni 3) ⇒ debe ir al 7.
   * esposa\_D no puede ir junto a Dionisio (seat 4 ⇒ no asientos 3 ni 5) ⇒ queda en 1.
   * esposa\_C ocupa el asiento restante, 3.

**Configuración final** (números = asiento, sentido horario):

```
0: Basilio (B)
1: esposa_D
2: Armando (A)
3: esposa_C
4: Dionisio (D)
5: esposa_B
6: Carlos (C)
7: esposa_A
```

**Pregunta:** ¿Quién se sienta **entre** Basilio (0) y Armando (2)?

**Respuesta:** Entre Basilio y Armando se sienta **la esposa de Dionisio**.
