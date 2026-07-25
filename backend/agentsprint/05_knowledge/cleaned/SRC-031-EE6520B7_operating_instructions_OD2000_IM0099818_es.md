BETRIEBSANLEITUNG


OD2000 Analog / IO-Link
sensor de desplazamiento

Producto descrito
                                   OD2000 Interfaz analógica / IO-Link

                                   Fabricante
                                   SICK AG
                                   Erwin-Sick-Str. 1
                                   79183 Waldkirch
                                   Alemania

                                   Información legal
                                   Este documento está protegido por la legislación sobre la propiedad intelectual. Los
                                   derechos derivados de ello son propiedad de SICK AG. Únicamente se permite la
                                   reproducción total o parcial de este documento dentro de los límites establecidos por
                                   las disposiciones legales sobre propiedad intelectual. Está prohibida la modificación,
                                   abreviación o traducción del documento sin la autorización expresa y por escrito de
                                   SICK AG.
                                   Las marcas mencionadas en este documento pertenecen a sus respectivos propieta‐
                                   rios.
                                   © SICK AG. Reservados todos los derechos.

                                   Documento original
                                   Este es un documento original de SICK AG.




                                                                                                                             NO

                                                                                                                         2006/42/EC
                                                                                                                           SAFETY




2   B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                     8026228/18SG/2024-12-16 | SICK
                                                                                                        Sujeto a cambio sin previo aviso

ÍNDICE


Índice
                                   1   Acerca de este documento..............................................................                                     5
                                       1.1     Información sobre las instrucciones de uso...........................................                               5
                                       1.2     Símbolos y convenciones utilizados en este documento.......................                                         5
                                       1.3     Información más detallada......................................................................                     5

                                   2   Para su seguridad.............................................................................                             7
                                       2.1     Uso conforme a lo previsto.......................................................................                   7
                                       2.2     Uso no conforme a lo previsto.................................................................                      7
                                       2.3     Ciberseguridad..........................................................................................            7
                                       2.4     Limitación de responsabilidad.................................................................                      7
                                       2.5     Cambios y modificaciones.......................................................................                     8
                                       2.6     Cualificación del personal........................................................................                  8
                                       2.7     Seguridad laboral y peligros especiales..................................................                           8
                                       2.8     Señales de advertencia en el dispositivo................................................                           10

                                   3   Descripción del producto................................................................. 11
                                       3.1     Volumen de suministro.............................................................................                 11
                                       3.2     Identificación del producto......................................................................                  11
                                               3.2.1      Identificación del producto con su SICK Product ID..............                                        11
                                               3.2.2      Clave de tipos...........................................................................               11
                                       3.3     Funcionamiento........................................................................................             12
                                               3.3.1      Principio de medición..............................................................                     12
                                               3.3.2      Salida de los valores medidos y parametrización.................                                        12
                                       3.4     Elementos de indicación y mando...........................................................                         13

                                   4   Transporte y almacenamiento........................................................ 15
                                       4.1     Transporte.................................................................................................        15
                                       4.2     Desembalaje.............................................................................................           15
                                       4.3     Inspección de transporte.........................................................................                  15
                                       4.4     Almacenamiento.......................................................................................              15

                                   5   Montaje............................................................................................... 16
                                       5.1     Indicaciones de montaje..........................................................................                  16
                                       5.2     Montar el dispositivo................................................................................              16

                                   6   Instalación eléctrica.......................................................................... 17
                                       6.1     Indicaciones de cableado........................................................................                   17
                                       6.2     Asignación de contactos..........................................................................                  17
                                       6.3     Conexión eléctrica del dispositivo...........................................................                      18

                                   7   Manejo................................................................................................ 19
                                       7.1     Manejo mediante teclas y pantalla.........................................................                         19
                                               7.1.1   Modo RUN................................................................................                   19
                                               7.1.2   Menú rápido.............................................................................                   19
                                               7.1.3   Menú principal.........................................................................                    21

8026228/18SG/2024-12-16 | SICK                                                                  B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link        3
Sujeto a cambio sin previo aviso

ÍNDICE


                                                                7.1.4     Ajuste de parámetros..............................................................                      21
                                                                7.1.5     Activación y desactivación del bloqueo de las teclas de
                                                                          mando......................................................................................             22
                                                    7.2         Manejo a través de IO-Link......................................................................                  22
                                                                7.2.1     Datos de proceso.....................................................................                   22
                                                                7.2.2     Datos del dispositivo...............................................................                    23
                                                    7.3         Manejo a través de SOPAS ET.................................................................                      23
                                                    7.4         Descripción de la función.........................................................................                24
                                                                7.4.1     Grupo de menús Medición......................................................                           24
                                                                7.4.2     Ajustes Q1 y Q2 / Qa...............................................................                     32
                                                                7.4.3     Grupo de menús Q1 Salida.......................................................                         34
                                                                7.4.4     Grupo de menús Q2 / Qa Salida............................................                               42
                                                                7.4.5     Grupo de menús Entrada IN......................................................                         44
                                                                7.4.6     Grupo de menús Dispositivo...................................................                           48
                                                                7.4.7     Grupo de menús Info...............................................................                      50

                                        8           Mantenimiento.................................................................................. 51
                                                    8.1         Limpieza....................................................................................................      51
                                                    8.2         Plan de mantenimiento............................................................................                 51

                                        9           Resolución de averías....................................................................... 52
                                                    9.1         Fallos.........................................................................................................   52
                                                    9.2         Información para el servicio.....................................................................                 52
                                                    9.3         Devolución.................................................................................................       52
                                                    9.4         Reparación................................................................................................        53
                                                    9.5         Eliminación................................................................................................       53

                                        10          Datos técnicos................................................................................... 54
                                                    10.1        Sistema mecánico y eléctrico..................................................................                    54
                                                    10.2        Rendimiento..............................................................................................         54
                                                    10.3        Interfaces..................................................................................................      56
                                                    10.4        Datos del entorno.....................................................................................            56
                                                    10.5        Rango de interferencia.............................................................................               57
                                                    10.6        Dibujo acotado..........................................................................................          63
                                                    10.7        Tamaño del spot.......................................................................................            63
                                                    10.8        Diagramas de linealidad..........................................................................                 65

                                        11          Accesorios.......................................................................................... 71

                                        12          Anexo................................................................................................... 72
                                                    12.1 Estructura del menú.................................................................................                     72
                                                         12.1.1 Estructura de los menús en el menú rápido..........................                                               72
                                                         12.1.2 Estructura del menú principal................................................                                     73
                                                    12.2 Declaraciones de conformidad y certificados........................................                                      74
                                                    12.3 Licencias...................................................................................................             74




4        B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                                                               8026228/18SG/2024-12-16 | SICK
                                                                                                                                                       Sujeto a cambio sin previo aviso

ACERCA DE ESTE DOCUMENTO 1


1                  Acerca de este documento
1.1                Información sobre las instrucciones de uso
                                   Lea detenidamente el manual de instrucciones antes de iniciar cualquier trabajo para
                                   familiarizarse con el producto y sus funciones.
                                   Las instrucciones de uso son parte integrante del producto y deberán conservarse
                                   de forma que estén siempre accesibles al personal. Cuando transmita el producto a
                                   terceros, entregue las instrucciones de uso con él.
                                   Las presentes instrucciones de uso no sirven para un manejo y funcionamiento segu‐
                                   ros de la máquina o del sistema en el que se integre el producto. La información a este
                                   respecto estará incluida en las instrucciones de uso de la máquina o del sistema.

1.2                Símbolos y convenciones utilizados en este documento
                                   Indicaciones de seguridad y otras indicaciones

                                   PELIGRO
                                   Indica una situación de peligro directa que produce lesiones graves o incluso la muerte
                                   si no se evita.


                                   ADVERTENCIA
                                   Indica una situación de peligro potencial que puede producir lesiones graves o incluso
                                   la muerte si no se evita.


                                   PECAUCIÓN
                                   Indica una situación de peligro potencial que puede producir lesiones leves o modera‐
                                   das si no se evita.


                                   IMPORTANTE
                                   Indica una situación de peligro potencial que puede producir daños materiales si no se
                                   evita.


                                   INDICACIÓN
                                   Destaca consejos útiles y recomendaciones, así como información para un funciona‐
                                   miento eficiente y libre de averías.

                                   Instrucciones de procedimiento
                                   ►    La flecha indica una instrucción de procedimiento.
                                   1.   Se muestra una secuencia numerada de instrucciones de procedimiento.
                                   2.   Respete las instrucciones de procedimiento numeradas en la secuencia indicada.
                                   ✓    La marca de verificación indica el resultado de una instrucción de procedimiento.

1.3                Información más detallada
                                   Encontrará la página del producto con más información a través de la SICK Product ID:
                                   pid.sick.com/{P/N}/{S/N}
                                   (véase "Identificación del producto con su SICK Product ID", página 11).
                                   En función del producto está disponible la siguiente información:
                                   • Este documento en todas las versiones lingüísticas disponibles
                                   • Hojas de datos

8026228/18SG/2024-12-16 | SICK                                                 B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link   5
Sujeto a cambio sin previo aviso

1 ACERCA DE ESTE DOCUMENTO

                                     •       Otras publicaciones
                                     •       Datos CAD de los esquemas y dibujos acotados
                                     •       Certificados (p. ej., la declaración de conformidad)
                                     •       Software
                                     •       Accesorios




6    B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                    8026228/18SG/2024-12-16 | SICK
                                                                                                        Sujeto a cambio sin previo aviso

PARA SU SEGURIDAD 2


2                  Para su seguridad
2.1                Uso conforme a lo previsto
                                   El sensor de medición de desplazamiento OD2000 es un sensor optoelectrónico y se
                                   utiliza para la determinación óptica de la distancia con los objetos sin contacto.
                                   SICK AG no se responsabiliza de las pérdidas directas o indirectas ni de los daños
                                   resultantes del uso del producto. Esto es aplicable en particular a un uso diferente
                                   del producto que no se corresponda con el uso previsto y que no se describa en la
                                   presente documentación.

2.2                Uso no conforme a lo previsto
                                   Cualquier otro uso que vaya más allá de los ámbitos mencionados, en particular, el uso
                                   que exceda las especificaciones técnicas y las del uso previsto se considerará un uso
                                   no conforme a lo previsto.
                                   •    El dispositivo no es un componente de seguridad a los efectos de las normas de
                                        seguridad en vigor para máquinas.
                                   •    El dispositivo no puede utilizarse en atmósferas potencialmente explosivas, en
                                        entornos corrosivos ni en condiciones ambiente extremas.
                                   •    El uso de accesorios que no han sido autorizados expresamente por SICK AG se
                                        efectúa por cuenta y riesgo propios.

                                   ADVERTENCIA
                                   Peligro debido a un uso no conforme a lo previsto
                                   Un uso no conforme a lo previsto puede provocar situaciones peligrosas.
                                   Por ese motivo debe observar las siguientes indicaciones:
                                   ■    Utilizar el producto únicamente según el uso conforme a lo previsto.
                                   ■    Respete rigurosamente todos los datos especificados en la documentación.
                                   ■    En caso de existir daños, poner el producto fuera de servicio de inmediato.


2.3                Ciberseguridad
                                   Resumen
                                   La protección contra las amenazas a la ciberseguridad requiere un concepto global
                                   de ciberseguridad de la empresa explotadora que debe ser revisado y mantenido con‐
                                   tinuamente. Un concepto adecuado consta de niveles de defensa organizativos, técni‐
                                   cos, de procedimiento, electrónicos y físicos, y tiene en cuenta las medidas adecuadas
                                   para los diferentes tipos de riesgo. Las medidas implementadas en este producto sólo
                                   pueden reforzar la protección contra las amenazas de ciberseguridad si el producto se
                                   utiliza en el contexto de este tipo de concepto.
                                   En www.sick.com/psirt encontrará más información, por ejemplo:
                                   • Información general sobre ciberseguridad
                                   • Opción de contacto para informar de los puntos débiles
                                   • Información sobre puntos débiles conocidos (Security Advisories)

2.4                Limitación de responsabilidad
                                   Toda la información e indicaciones de estas instrucciones se han elaborado teniendo
                                   en cuenta las normas y reglamentos vigentes, el estado de la técnica y nuestros
                                   conocimientos y experiencia de muchos años. El fabricante no asume responsabilidad
                                   alguna por daños debidos a las siguientes causas:



8026228/18SG/2024-12-16 | SICK                                                  B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link   7
Sujeto a cambio sin previo aviso

2 PARA SU SEGURIDAD

                                      ■       Incumplimiento de la documentación del producto (p. ej.,, instrucciones de uso)
                                      ■       Uso no conforme a lo previsto
                                      ■       Uso por parte de personal no capacitado
                                      ■       Modificaciones o reparaciones por cuenta propia
                                      ■       Modificaciones técnicas
                                      ■       Uso de recambios, piezas de desgaste y accesorios no autorizados

2.5           Cambios y modificaciones

                                     IMPORTANTE
                                     Los cambios y modificaciones en el dispositivo pueden provocar peligros imprevistos.

                                     En caso de realizar intervenciones o modificaciones en el dispositivo o en el software
                                     de SICK, quedará anulado cualquier derecho de garantía otorgado por SICK AG. Esto es
                                     válido, especialmente, si se abre la carcasa también dentro del marco de los trabajos
                                     de montaje e instalación eléctrica.

2.6           Cualificación del personal
                                     Todos los trabajos en el producto deben ser realizados únicamente por personal cualifi‐
                                     cado y autorizado.
                                     El personal cualificado es capaz de realizar el trabajo asignado y de reconocer y evitar
                                     de forma autónoma los posibles peligros. Esto requiere, por ejemplo:
                                      •       Formación profesional
                                      •       Experiencia
                                      •       Conocimiento de los reglamentos y normas pertinentes

2.7           Seguridad laboral y peligros especiales
                                     Observar las indicaciones de seguridad aquí especificadas y las indicaciones de adver‐
                                     tencia del resto de apartados de esta documentación del producto a fin de reducir los
                                     riesgos para la salud y evitar situaciones de peligro.

                                     Los peligros por radiación óptica son específicos de cada producto. En los datos técni‐
                                     cos se incluye información al respecto.

                                     PECAUCIÓN
                                     Radiación óptica, clase de láser 1
                                     La radiación accesible no es peligrosa ni siquiera cuando se mira directamente durante
                                     un tiempo de hasta 100 segundos. Puede existir peligro para los ojos y para la piel si
                                     no se usa conforme a lo previsto.
                                      ■       No abrir la carcasa. Incluso, el peligro puede aumentar al abrirla.
                                      ■       Tener en cuenta las disposiciones nacionales vigentes sobre protección láser.




8     B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                           8026228/18SG/2024-12-16 | SICK
                                                                                                                Sujeto a cambio sin previo aviso

PARA SU SEGURIDAD 2


                                   PECAUCIÓN
                                   Radiación óptica: clase de láser 2
                                   El ojo humano no sufre daños cuando la radiación dura poco tiempo (hasta 0,25
                                   segundos). Mirar durante mucho tiempo el haz láser puede provocar lesiones en la
                                   retina. La radiación láser no es peligrosa para la piel humana.
                                   ■    No mirar fijamente el haz láser de forma intencionada.
                                   ■    No dirigir el haz láser hacia los ojos de las personas.
                                   ■    Si no se puede evitar mirar directamente el haz láser, por ejemplo, durante los
                                        trabajos de puesta en servicio y mantenimiento, usar una protección adecuada
                                        para los ojos.
                                   ■    Evitar las reflexiones del haz láser en superficies reflectantes. Especialmente
                                        tenerlo en cuenta durante los trabajos de montaje y alineación.
                                   ■    No abrir la carcasa. Incluso, el peligro puede aumentar al abrirla.
                                   ■    Tener en cuenta las disposiciones nacionales vigentes sobre protección láser.

                                   Precaución – Usar dispositivos de ajuste o de manejo, o seguir otros pasos de trabajo
                                   distintos a los especificados, puede llevar a una exposición peligrosa a la radiación.
                                   No pueden excluirse completamente los efectos ópticos irritantes pasajeros, en parti‐
                                   cular en condiciones de luminosidad ambiente baja. Efectos ópticos irritantes son
                                   p. ej.: deslumbramiento, ceguera por destello, persistencia de las imágenes, epilepsia
                                   fotosensitiva o visión anómala del color.

                                   ADVERTENCIA
                                   ¡Tensión eléctrica!
                                   La tensión eléctrica puede provocar lesiones peligrosas o incluso la muerte.
                                   ■    Únicamente los electricistas profesionales pueden realizar trabajos en las instala‐
                                        ciones eléctricas.
                                   ■    Enchufar y desenchufar los conectores eléctricos solo en ausencia de tensión en
                                        el sistema.
                                   ■    Conectar el producto únicamente a una fuente de alimentación que cumpla los
                                        requisitos de las instrucciones de uso.
                                   ■    Respetar las normativas nacionales y locales.
                                   ■    Observar las normas de seguridad durante los trabajos en instalaciones eléctri‐
                                        cas.


                                   ADVERTENCIA
                                   ¡Peligro de lesiones y daños por corrientes equipotenciales!
                                   Una conexión a tierra incorrecta puede causar corrientes equipotenciales peligrosas y,
                                   por tanto, tensiones peligrosas en superficies metálicas, como, p. ej., la carcasa. La
                                   tensión eléctrica puede provocar lesiones peligrosas o incluso la muerte.
                                   ■    Únicamente los electricistas profesionales pueden realizar trabajos en las instala‐
                                        ciones eléctricas.
                                   ■    Respetar las indicaciones contenidas en las instrucciones de uso.
                                   ■    Efectúe la puesta a tierra del producto y de la instalación según las normativas
                                        nacionales y locales.




8026228/18SG/2024-12-16 | SICK                                                   B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link   9
Sujeto a cambio sin previo aviso

2 PARA SU SEGURIDAD

2.8           Señales de advertencia en el dispositivo
                                     Notas sobre el láser

                                     PECAUCIÓN
                                     Intervenciones, manipulaciones o un uso indebido pueden provocar una exposición
                                     peligrosa a la radiación láser.
                                     La radiación láser emitida no puede ser enfocada con ayuda de dispositivos ópticos
                                     adicionales.

                                     En el dispositivo está integrado un láser rojo visible. Según el tipo de dispositivo, el
                                     láser corresponde a la clase de láser 1 o a la clase de láser 2.
                                     La identificación de la clase de láser se encuentra en la impresión de la carcasa del
                                     sensor.


                                                                    LASER
                                                                      1

                                     Figura 1: Clase de láser 1

                                     El láser es seguro para la visión directa.
                                                  Laser
                                                    2

                                     Figura 2: Clase de láser 2


                                     PELIGRO
                                     RADIACIÓN LÁSER: No mirar al haz. Clase de láser 2

                                     Este dispositivo cumple las siguientes normas:
                                     • EN 60825-1:2014+A11:2021, IEC 60825-1:2014
                                     • Cumple con 21 CFR 1040.10 y 1040.11 excepto la conformidad con IEC 60825-1
                                          Ed. 3., como se describe a la nota sobre el láser N.º 56 del 8/5/2019.




10    B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                         8026228/18SG/2024-12-16 | SICK
                                                                                                              Sujeto a cambio sin previo aviso

DESCRIPCIÓN DEL PRODUCTO 3


3                  Descripción del producto
3.1                Volumen de suministro
                                   Tabla 1: Volumen de suministro
                                    Unida‐    Componente                          Observación
                                    des
                                    1         Dispositivo en la ejecución soli‐   Según la versión
                                              citada
                                    1         Notas de seguridad impresas,        Información abreviada e indicaciones generales de
                                              multilingües                        seguridad

                                   El volumen de suministro real puede ser diferente cuando se trata de versiones espe‐
                                   ciales, opciones de pedido adicionales o como consecuencia de nuevas modificaciones
                                   técnicas.

3.2                Identificación del producto

3.2.1              Identificación del producto con su SICK Product ID
                                   SICK Product ID
                                   La SICK Product ID identifica el producto de forma única. Sirve también como dirección
                                   de la página web con información sobre el producto.
                                   La SICK Product ID se compone del nombre de host pid.sick.com, la referencia (P/N) y
                                   el número de serie (S/N), todos ellos separados por guiones.
                                   La SICK Product ID en muchos productos está representada como texto y como código
                                   QR en la placa de características y/o en el embalaje.




                                   Figura 3: SICK Product ID


3.2.2              Clave de tipos
                                   Estructura de la clave de tipos
                                   OD2000 – a b c d e f
                                    Comodín       Descripción                     Expresión
                                    a             Centro del campo de medi‐       030: 25 mm ... 35 mm
                                                  ción                            050: 40 mm ... 60 mm
                                                                                  130: 60 mm ... 200 mm
                                                                                  245: 70 mm ... 420 mm
                                                                                  350: 100 mm ... 600 mm
                                                                                  700: 200 mm ... 1.200 mm
                                    b             Clase de láser                  1: Clase de láser 1
                                                                                  2: Clase de láser 2
                                    c             Geometría del spot              T: punto, redondo
                                    d             Interfaz                        1: I/U analógica 1), IO-Link
                                                                                  2: RS-485
                                    e             Tipo de conexión                5: Cable con conexión M12, 5 polos




8026228/18SG/2024-12-16 | SICK                                                         B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link   11
Sujeto a cambio sin previo aviso

3 DESCRIPCIÓN DEL PRODUCTO

                                        Comodín               Descripción                   Expresión
                                        f                     Tipo de dispositivo           “Vacío”: tipo estándar
                                                                                            S: dispositivo especial
                                       1)    No se aplica a dispositivos sin salida analógica.




3.3             Funcionamiento

3.3.1           Principio de medición
                                       El sensor de medición de desplazamiento determina la distancia a un objeto con ayuda
                                       del principio de triangulación.




                                       Figura 4: Principio de triangulación
                                       1           Receptor
                                       2           Óptica del receptor
                                       3           Objeto
                                       4           Emisor

                                       El principio de triangulación se basa en la medición de la distancia mediante el cálculo
                                       de ángulos. El dispositivo emite un haz de luz. Cuando el haz de luz emitida incide
                                       sobre un objeto, se refleja en la superficie de este. La luz reflejada por el objeto incide
                                       en el receptor sensible a la luz que hay en el dispositivo con un ángulo determinado
                                       en función de la distancia. A partir del ángulo entre las direcciones de los haces
                                       emisor y receptor, se determina la distancia al objeto mediante relaciones matemáticas
                                       triangulares.

3.3.2           Salida de los valores medidos y parametrización
                                       La distancia obtenida se transmite a través de la interfaz IO-Link. La salida de señal
                                       analógica convierte el valor de la distancia en una señal de salida proporcional a la
                                       distancia. El dispositivo señala a través de las salidas digitales si se han alcanzado los
                                       límites de conmutación y los valores de distancia parametrizables.
                                       La pantalla OLED permite consultar los datos de medición, de diagnóstico y de las
                                       unidades, así como realizar los ajustes de los parámetros. El dispositivo se puede
                                       parametrizar a través de la pantalla, la interfaz IO-Link y SOPAS ET.




12      B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                                   8026228/18SG/2024-12-16 | SICK
                                                                                                                          Sujeto a cambio sin previo aviso

DESCRIPCIÓN DEL PRODUCTO 3


3.4                Elementos de indicación y mando
                                   Resumen
                                                                  1

                                   5                  PWR
                                                                  Q2/QA

                                                                   Q1
                                                                            2
                                                                            3

                                                         4
                                   Figura 5: Elementos de control y visualización
                                   1       LED de estado PWR (verde)
                                   2       LED de estado Q2 / QA (naranja)
                                   3       LED de estado Q1 (naranja)
                                   4       Teclas de mando
                                   5       Pantalla

                                   LED de estado
                                   LED de estado                  Estado (color)          Descripción
                                   PWR (indicador de servicio) O (Verde)                  Fuente de alimentación disponible, dispositivo
                                                                                          operativo
                                                                  o (Verde)               Fuente de alimentación no disponible
                                                                  Ö (Verde)               Fuente de alimentación disponible, dispositivo
                                                                                          operativo, conexión a un IO-Link Master dispo‐
                                                                                          nible
                                   Q1 (indicador de salida)       O (Naranja)             Salida digital activa
                                                                  o (Naranja)             Salida digital no activa
                                   Q2 / QA (indicador de          O (Naranja)             Salida digital activa o valor medido dentro del
                                   salida)                                                rango de escala para la salida analógica
                                                                  o (Naranja)             Salida digital no activa o valor medido fuera
                                                                                          del rango de escala para la salida analógica

                                       O = se ilumina; Ö = parpadea; o = no se ilumina.

                                   Teclas de mando
                                   tecla      Función                         Descripción
                                              Abrir el menú, confirmar la     • Partiendo del modo RUN, se abre el menú rápido o el
                                              entrada                             menú principal.
                                                                              •   Confirmar la entrada.
                                                                              •   Cambiar al siguiente nivel de menú de una función
                                                                                  seleccionada.
                                                                              •   Mover el cursor hacia la derecha en la introducción
                                                                                  de números.
                                              Cancelar                        • En el menú rápido: cambiar al modo RUN.
                                                                              • Volver al nivel de menú anterior.
                                                                              • Mover el cursor hacia la izquierda en la introducción
                                                                                  de números.




8026228/18SG/2024-12-16 | SICK                                                            B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link   13
Sujeto a cambio sin previo aviso

3 DESCRIPCIÓN DEL PRODUCTO

                                     tecla           Función       Descripción
                                                     Navegación    • Paginación entre múltiples indicaciones de un nivel
                                                                      de menú.
                                                                   • Selección entre múltiples opciones.
                                                                   • Aumentar el valor de una entrada numérica.
                                                     Navegación    • Paginación entre múltiples indicaciones de un nivel
                                                                      de menú.
                                                                   • Selección entre múltiples opciones.
                                                                   • Disminuir el valor de una entrada numérica.




14   B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                  8026228/18SG/2024-12-16 | SICK
                                                                                                      Sujeto a cambio sin previo aviso

TRANSPORTE Y ALMACENAMIENTO 4


4                  Transporte y almacenamiento
4.1                Transporte

                                   IMPORTANTE
                                   Daños debidos a un transporte inadecuado
                                   ■   Embalar el producto a prueba de golpes y protegido contra la humedad.
                                   ■   Recomendación: utilizar el embalaje original.
                                   ■   Tener en cuenta los símbolos del embalaje.
                                   ■   No retirar el embalaje hasta el momento de iniciar el montaje.


4.2                Desembalaje
                                   •    Para proteger el dispositivo contra la condensación, antes de desembalarlo
                                        deberá esperarse a que alcance la temperatura ambiente.
                                   •    Manipular con cuidado el dispositivo y protegerlo de daños mecánicos.

4.3                Inspección de transporte
                                   Examinar la entrega en el momento de su recepción en la entrada de mercancías a
                                   fin de controlar la integridad de su contenido y comprobar si hay daños producidos
                                   por el transporte. Si se apreciaran externamente daños de transporte, proceder de la
                                   siguiente manera:
                                   •   No aceptar la entrega o hacerlo únicamente bajo condiciones.
                                   •   Hacer constar el alcance del daño en los documentos de transporte o en el
                                       albarán de entrega del transportista.
                                   •   Presentar una reclamación.

                                   INDICACIÓN
                                   Reclamar cualquier defecto, tan pronto como se haya detectado. Los derechos a
                                   indemnización por daños y perjuicios solo pueden reclamarse dentro de los plazos
                                   previstos para este fin.


4.4                Almacenamiento
                                   •   Colocar una tapa protectora en las conexiones eléctricas.
                                   •   No debe almacenarse en el exterior.
                                   •   Almacenar en un lugar protegido de la humedad y sin polvo.
                                   •   Recomendación: utilizar el embalaje original.
                                   •   No guardar el dispositivo en recipientes estancos para que la posible humedad
                                       residual pueda salir.
                                   •   Evitar la exposición a sustancias agresivas.
                                   •   Proteger contra la radiación solar.
                                   •   Evitar sacudidas mecánicas.
                                   •   Temperatura de almacenamiento: véase "Datos técnicos"
                                   •   Si el almacenamiento es superior a 3 meses, controlar periódicamente el estado
                                       general de todos los componentes y del embalaje.




8026228/18SG/2024-12-16 | SICK                                                 B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link   15
Sujeto a cambio sin previo aviso

5 MONTAJE


5             Montaje
5.1           Indicaciones de montaje
                                      •       Deben cumplirse los datos técnicos.
                                      •       Proteja el sensor contra la radiación directa.
                                      •       Para evitar la formación de agua condensada, no exponga el dispositivo a un
                                              cambio brusco de temperatura.
                                      •       El lugar de montaje debe poder soportar el peso del dispositivo.
                                      •       Para evitar mediciones erróneas durante la instalación de varios dispositivos,
                                              debe asegurarse que el spot de un dispositivo no se encuentre en la zona de
                                              interferencia de otro dispositivo.
                                      •       El elemento de ventilación no debe quedar herméticamente cerrado durante el
                                              montaje.

5.2           Montar el dispositivo
                                     Procedimiento
                                     1.       Monte el dispositivo utilizando los orificios de fijación previstos para tal fin. Debe
                                              respetarse el par de apriete máximo admitido de los tornillos (0,8 Nm).
                                     2.       Lleve a cabo la conexión eléctrica. Coloque y apriete el cable sin tensión.
                                     3.       Conecte la tensión de alimentación.
                                     ✓        El LED de estado PWR se ilumina en verde.
                                     4.       Alinee el spot para que el dispositivo mida sobre el objeto deseado.

                                     Temas relacionados
                                      •       Dibujo acotado
                                      •       Asignación de contactos




16    B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                             8026228/18SG/2024-12-16 | SICK
                                                                                                                  Sujeto a cambio sin previo aviso

INSTALACIÓN ELÉCTRICA 6


6                  Instalación eléctrica
6.1                Indicaciones de cableado

                                   INDICACIÓN
                                   Los cables premontados se encuentran en la página del producto.
                                   El acceso se realiza a través de la SICK Product ID: pid.sick.com/{P/N}/{S/N}
                                   {P/N} es la referencia del producto, véase la placa de características.
                                   {S/N} es el número de serie del producto, véase la placa de características (indicación
                                   opcional).


                                   IMPORTANTE
                                   Fallos durante el funcionamiento y defectos en el dispositivo o la instalación
                                   Un cableado inadecuado puede causar fallos durante el funcionamiento y defectos.
                                   ■         Deben seguirse exactamente las indicaciones de cableado.

                                   El grado de protección indicado en los datos técnicos solo se alcanza con un conector
                                   atornillado o una tapa protectora.
                                   Los circuitos eléctricos conectados al dispositivo deben ser circuitos ES1 o circuitos
                                   SELV (Safety Extra Low Voltage = baja tensión de seguridad). La fuente de tensión debe
                                   cumplir los requisitos conforme aES1 y PS2 (EN 62368-1) o SELV y LPS (EN 60950-1).
                                   Los cables de conexión deben conectarse sin tensión. La tensión de alimentación solo
                                   debe activarse después de la instalación y conexión completas de todos los cables de
                                   conexión al dispositivo y al controlador.

6.2                Asignación de contactos
                                   Resumen
                                   El diagrama de conexiones y la información sobre las entradas y salidas se encuentran
                                   en la placa lateral del dispositivo.

                                   Requisitos
                                   •         Observe las indicaciones de cableado, véase "Indicaciones de cableado",
                                             página 17.

                                   Asignación de contactos
                                   2                      1

                                                          5

                                   3                      4

                                   Figura 6: Conector macho M12 de 17 polos, codificación A

                                       brn    1
                                                  L+
                                       wht    2
                                                  Q2/QA
                                       blu    3
                                                  M
                                       blk    4
                                                  Q1/C
                                       gra    5
                                                  In1

                                   Figura 7: Diagrama de conexiones, conector macho de 5 polos



8026228/18SG/2024-12-16 | SICK                                                     B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link   17
Sujeto a cambio sin previo aviso

6 INSTALACIÓN ELÉCTRICA

                                      Contacto               Denominación      Color del conduc‐ Descripción
                                                                               tor
                                      1                      L+                Marrón             Tensión de alimentación, véase "Datos
                                                                                                  técnicos", página 54
                                      2                      Q2 / QA 1)        Blanco             Salida 2: salida digital 2 (nivel push-pull),
                                                                                                  salida analógica 1)
                                      3                      M                 Azul               Tensión de alimentación: 0 V
                                      4                      Q1 / C            Negro              Salida 1: salida digital 1 (nivel push-pull),
                                                                                                  IO-Link
                                      5                      In1               Gris               Entrada 1
                                     1)    QA no se aplica a dispositivos sin salida analógica.

                                     El diagrama de conexiones y la información sobre las entradas y salidas se encuentran
                                     en la placa lateral del dispositivo.

6.3           Conexión eléctrica del dispositivo
                                     Requisitos
                                      •       Observe las indicaciones de cableado.

                                     Procedimiento
                                     1.       Verifique la ausencia de tensión.
                                     2.       Conecte el dispositivo según el diagrama de conexiones.
                                     3.       Establezca la tensión de alimentación.

                                     Temas relacionados
                                      •       Indicaciones de cableado
                                      •       Asignación de contactos




18    B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                                    8026228/18SG/2024-12-16 | SICK
                                                                                                                         Sujeto a cambio sin previo aviso

MANEJO 7


7                  Manejo
7.1                Manejo mediante teclas y pantalla

7.1.1              Modo RUN
                                   En cuanto el dispositivo recibe tensión, la pantalla muestra el valor medido actual. El
                                   dispositivo se encuentra en modo RUN.
                                   Para cambiar entre las pantallas en modo RUN y abrir el menú rápido o el menú
                                   principal del dispositivo, utilice las teclas de mando del mismo. Para volver al modo
                                   RUN, pulse la tecla de mando          hasta que la pantalla muestre el valor medido actual.
                                                           1                         1
                                                             RUN mode                 RUN mode

                                   3                  >3s                        2
                                        Quick menu                                   Main menu

                                   Figura 8: Estructura del menú
                                   1          Modo RUN
                                   2          Menú principal
                                   3          Menú rápido

                                   Tabla 2: Indicación en modo RUN
                                    Indicación                          Descripción
                                    Distancia                           Muestra la distancia sin la desviación del valor medido.
                                    Distancia (relativa)                Muestra la distancia con la desviación del valor medido.
                                    Distancia (bar)                     Muestra la distancia actual y los límites de Q1 y Q2 / QA en forma
                                                                        de indicador de barras.
                                    Valor analógico1)                   Muestra el valor analógico.
                                                                        El valor de salida actual sólo se muestra con la salida analógica
                                                                        activada.
                                    Modo                                Visualiza el modo establecido.
                                    Captura                             Inicia la captura de datos y su análisis.
                                   1)     No se aplica a dispositivos sin salida analógica.


7.1.2              Menú rápido

7.1.2.1            Funciones del menú rápido
                                   Funciones en resumen
                                   Partiendo de las pantallas en modo RUN, se puede acceder rápidamente a cada
                                   función del menú principal a través del menú rápido. Mientras que en el menú principal
                                   todas las funciones están disponibles, a través del menú rápido solo pueden ajustarse
                                   las funciones seleccionadas.
                                    Función                       Punto de partida del           Descripción
                                                                  modo RUN
                                    Aprendizaje de los            Distancia                      Selección del modo de salida.
                                    puntos de conmuta‐                                           Aprendizaje de los puntos de conmutación
                                    ción                                                         SP1 y SP2 1).
                                    Aprendizaje punto             Distancia (rel.)               Aprendizaje de la distancia como punto cero
                                    cero                                                         (punto de referencia).



8026228/18SG/2024-12-16 | SICK                                                                   B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link   19
Sujeto a cambio sin previo aviso

7 MANEJO

                                          Función                            Punto de partida del         Descripción
                                                                             modo RUN
                                          Mostrar la curva de                Distancia (bar)              Visualización de la distribución cualitativa de
                                          distribución de la luz                                          la intensidad luminosa en el elemento recep‐
                                                                                                          tor.
                                                                                                          La curva de distribución de la luz se divide
                                                                                                          en cuatro zonas en la pantalla. El dispositivo
                                                                                                          cambia automáticamente al rango donde se
                                                                                                          encuentra el máximo.
                                          Aprendizaje de los      Valor analógico                         Aprendizaje de los valores límite superior e
                                          valores analógicos,                                             inferior de la curva característica analógica.
                                          escalar la curva carac‐                                         Genera un escalado de la curva característica
                                          terística analógica 2)                                          analógica.
                                          Ajuste del modo                    Modo                         Seleccionar entre los modos Precisión, Velocidad
                                                                                                          y Específico del cliente .
                                                                                                          Realizar los ajustes previos necesarios en fun‐
                                                                                                          ción de la aplicación.
                                          Captura de datos                   Arrancando                   Para iniciar la captura de datos se pulsa breve‐
                                                                                                          mente la tecla      . Para detener la captura se
                                                                                                          pulsa de nuevo brevemente la tecla        .
                                                                                                          Al iniciar una captura, se borra automática‐
                                                                                                          mente la captura realizada anteriormente.
                                          Análisis de los datos              Arrancando                   Para visualizar los resultados de la captura,
                                                                                                          pulse la tecla     durante más de 3 segundos.
                                         1)    SP2 sólo está disponible en la ventana del modo de salida.
                                         2)    La función sólo está disponible si la salida está configurada como salida analógica en el menú principal.
                                               No se aplica a tipos de productos sin salida analógica.

                                         Función Ajuste del modo
                                          Modo                                        Parámetro                           Ajuste de fábrica
                                          Precisión                                   Tiempo de ciclo                     Auto
                                                                                      Filtro de valor medio               512
                                                                                      Filtro de mediana                   31
                                          Velocidad                                   Tiempo de ciclo                     133 μs
                                                                                      Filtro de valor medio               Apagado
                                                                                      Filtro de mediana                   Apagado
                                          Específico del cliente        1)
                                                                                      Tiempo de ciclo                     Auto
                                                                                      Filtro de valor medio               128
                                                                                      Filtro de mediana                   31
                                         1)    Si cambia parámetros manualmente, el dispositivo cambia automáticamente al modo Específico del
                                               cliente.
                                               Si establece el modo Específico del cliente los ajustes de fábrica se corresponden con el estado de
                                               suministro.

                                         Temas relacionados
                                          •       Estructura de los menús en el menú rápido

7.1.2.2           Abrir el menú rápido
                                         1.       Abra la indicación requerida en modo RUN como punto de partida.
                                         2.       Pulse la tecla    durante más de 3 segundos.
                                         ✓        La pantalla muestra la función correspondiente.



20        B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                                              8026228/18SG/2024-12-16 | SICK
                                                                                                                                       Sujeto a cambio sin previo aviso

MANEJO 7


7.1.3              Menú principal

7.1.3.1            Funciones en el menú principal
                                   Funciones en resumen
                                   Grupos de menús
                                   • Medición
                                   • Q1 Salida
                                   • Q2 / Qa Salida
                                   • Entrada IN
                                   • Dispositivo
                                   • Info
                                   • Volver a RUN
                                   Temas relacionados
                                   •    Descripción de la función (Información sobre los grupos de menús individuales)
                                   •    Estructura del menú principal

7.1.3.2            Abrir el menú principal
                                   Abrir el grupo de menús
                                   1. Para abrir el menú principal, en modo RUN pulse brevemente la tecla                                  breve‐
                                        mente en el modo RUN.
                                   2. Seleccione un grupo de menús con las teclas     y    .
                                   3. Confirme la selección con la tecla   .
                                   ✓ La pantalla muestra el grupo de menús correspondiente.

7.1.4              Ajuste de parámetros
                                   Selección de parámetros
                                   1.   Seleccione el parámetro deseado dentro de un grupo de menú con las teclas                                   y
                                           .
                                   2.   Confirme la selección con la tecla .

                                   Seleccionar opción
                                   1.   Seleccione los parámetros.
                                   2.   Seleccione la opción deseada con las teclas       y     .
                                   3.   Siga uno de estos pasos:
                                        ■    Para guardar el ajuste, pulse la tecla    .
                                        ■    Para cancelar la operación, pulse la tecla     .
                                   4.   Para volver a la visualización del valor medido, pulse la tecla                     hasta que
                                        aparezca el valor medido.

                                   Aprendizaje del valor
                                   1.   Seleccione los parámetros.
                                   ✓    La pantalla muestra el valor medido actual.
                                   2.   Alinee el dispositivo a la distancia deseada.
                                   3.   Para el aprendizaje del valor, pulse la tecla    .
                                   ✓    El valor se ajusta a la distancia actual en el momento de pulsar el botón. El valor
                                        está aprendido.

                                   Ajuste del valor
                                   1.   Seleccione los parámetros.
                                   ✓    Se muestra el valor actual del parámetro. La primera cifra de la izquierda parpa‐


8026228/18SG/2024-12-16 | SICK                                                   B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link        21
Sujeto a cambio sin previo aviso

7 MANEJO

                                                dea.
                                       2.       Ajuste la cifra que parpadea con las teclas      y     .
                                       3.       Para confirmar la cifra y pasar a la siguiente, pulse la tecla  .
                                       ✓        La siguiente cifra parpadea.
                                       4.       Ajuste las demás cifras de la forma descrita.
                                       5.       Para volver a la cifra anterior, pulse la tecla  .
                                       6.       Ajuste la última cifra. Confirme la entrada con la tecla     .
                                       ✓        Se ha establecido el valor del parámetro.
                                       7.       Para volver a la visualización del valor medido, pulse la tecla   hasta que
                                                aparezca el valor medido.
                                       Temas relacionados
                                       • Elementos de indicación y mando

7.1.5           Activación y desactivación del bloqueo de las teclas de mando
                                       Para evitar un manejo accidental, bloquee y desbloquee las teclas de mando mediante
                                       la selección rápida de teclas.
                                       ►        Mantenga pulsadas las teclas       y     simultáneamente durante > 3 segundos.
                                       ✓        Cuando se activa el bloqueo de teclas, en la pantalla aparece Bloqueo. Cuando se
                                                desactiva el bloqueo de las teclas, en la pantalla aparece Desbloqueo .

7.2             Manejo a través de IO-Link
                                       El dispositivo puede intercambiar datos de proceso y parámetros a través de IO-Link.
                                       Para ello, el dispositivo se conecta con un IO-Link Master adecuado.
                                       Tabla 3: Propiedades de la interfaz IO-Link
                                        Especificación IO-Link                 V 1.1
                                        Tiempo de ciclo mínimo                 0,7 ms (COM3)
                                        Velocidad de transmisión               COM3 (230,4 kbaudios)
                                        Ancho de datos de proceso              48 bits de salida (del dispositivo al IO-Link Master)
                                        Tipo de datos de proceso               Record
                                        Función de servidor de parametriza‐    Sí
                                        ción (Data storage)
                                        Tipo de perfil                         SSP 3.2, 0x000B, Measuring Sensor high resolution
                                                                               (DMS)
                                                                               0x4000, Identification and Diagnosis
                                        Clase de función                       0x800B, Measurement Data Channel, (high resolution)
                                                                               0x8000, DeviceIdentification
                                                                               0x8002, ProcessDataMapping
                                                                               0x8003, DeviceDiagnosis
                                                                               0x8100, ExtendedIdentification


7.2.1           Datos de proceso
                                       Datos del telegrama de datos de proceso (ajuste de fábrica)
                                       • Valor de la distancia medida (unidad: nanómetro, 32 bits con signo)
                                       • Estado Q1 (1 bit)
                                       • Estado Q2 / QA (1 bit)
                                       Mediante la parametrización del dispositivo, se puede modificar el formato de los datos
                                       de proceso y la desviación del valor de distancia.




22      B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                              8026228/18SG/2024-12-16 | SICK
                                                                                                                     Sujeto a cambio sin previo aviso

MANEJO 7


                                   Tabla 4: Formatos de datos de proceso
                                    N.º                                 Descripción
                                    Estructura de datos de pro‐ PDI48.INT32_INT8
                                    ceso 1 1)                   Bit 0 = Q1
                                                                Bit 1 = Q2
                                                                Bit 2 … 7 = vacío
                                                                Bit 8 ... 15 = Scale
                                                                Bit 16 … 47 = Distance 2)
                                    Estructura de datos de pro‐ Bit 0 = Q1
                                    ceso 2                      Bit 1 = Q2
                                                                Bit 2 … 15 = vacío
                                                                Bit 16 ... 47 = Nivel de señal
                                    Estructura de datos de pro‐ Bit 0 = Q1
                                    ceso 3                      Bit 1 = Q2
                                                                Bit 2 … 15 = vacío
                                                                Bit 16 … 47 = Timer
                                    Estructura de datos de pro‐ Bit 0 = Q1
                                    ceso 4                      Bit 1 = Q2
                                                                Bit 2 … 15 = vacío
                                                                Bit 16 … 47 = Altura de bordes
                                    Estructura de datos de pro‐ Bit 0 = Q1
                                    ceso 5                      Bit 1 = Q2
                                                                Bit 2 … 7 = peak width
                                                                Bit 8 ... 15 = Scale
                                                                Bit 16 … 47 = Distance 2)
                                    Estructura de datos de pro‐ Bit 0 = Q1
                                    ceso 6                      Bit 1 = Q2
                                                                Bit 2 … 7 = peak width
                                                                Bit 8 ... 15 = Scale
                                                                Bit 16 … 47 = Distance (absolute) 3)
                                   1)     Ajuste de fábrica
                                   2)     Valor relativo de distancia
                                   3)     Valor absoluto de distancia


7.2.2              Datos del dispositivo
                                   Los datos del dispositivo (parámetros, datos de identificación, información de diagnós‐
                                   tico) pueden transmitirse desde y hacia el dispositivo. Para ello, es necesario un
                                   archivo de descripción del dispositivo específico del producto (archivo IODD) en el
                                   IO-Link Master.
                                   Hay disponible un paquete de descarga con el archivo IODD y documentación comple‐
                                   mentaria en la página del producto en Internet.

7.3                Manejo a través de SOPAS ET
                                   El software SOPAS Engineering Tool (SOPAS ET) a partir de la versión 2021.2 puede
                                   utilizarse para la parametrización del dispositivo y con fines de servicio y diagnóstico.
                                   En SOPAS ET se pueden visualizar los valores medidos y ajustarse y comprobarse
                                   todas las funciones del dispositivo. Los cambios en parámetros a través de SOPAS ET
                                   son adoptados inmediatamente por el dispositivo y almacenados de forma permanen‐
                                   temente. No es necesario llamar a una función separada para esto.
                                   SOPAS ET es especialmente adecuado para parametrizar las funciones de Region of
                                   Interest (ROI) y de salto de altura del borde.




8026228/18SG/2024-12-16 | SICK                                                        B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link   23
Sujeto a cambio sin previo aviso

7 MANEJO

                                         Requisitos
                                         ■   Ordenador con el software SOPAS ET instalado y una conexión libre compatible
                                             con USB 2.0
                                             La versión actual del software SOPAS ET puede descargarse desde
                                             www.sick.com/SOPAS_ET. Allí se indican también los requisitos correspondientes
                                             del sistema para la instalación de SOPAS ET.
                                         ■   SICK SiLink2 Master (disponible como accesorio)
                                         ■   Cable de conexión con conector macho M12 y conector hembra M12 de 5 polos
                                             (disponible como accesorio)
                                         ■   Archivo de descripción de dispositivo (SDD)
                                             La versión actual del archivo SDD está disponible para su descarga en la página
                                             de Internet del producto.
                                             Puede acceder a la página del producto con la SICK Product ID:
                                             pid.sick.com/{P/N}/{S/N}
                                             {P/N} es la referencia del producto, véase la placa de características.
                                             {S/N} es el número de serie del producto, véase la placa de características (si se
                                             indica).
                                         Establecimiento de conexión
                                         1. Conecte el dispositivo al SiLink2 Master mediante el conector macho o un cable
                                             de conexión adicional.
                                         2. Conecte el SiLink2 Master al ordenador utilizando el cable USB adjunto.
                                         3. Conecte el ordenador y arránquelo.
                                         4. Para garantizar un suministro de energía suficiente al dispositivo, conecte adi‐
                                             cionalmente la fuente de alimentación enchufable que se entrega junto con el
                                             SiLink2 Master.
                                         ✓ Después de la correcta inicialización, el LED de estado PWR parpadea en verde.
                                             El dispositivo está listo para funcionar y se establece la conexión con el SiLink2
                                             Master.
                                         Instale el archivo SDD a través del catálogo de dispositivos en SOPAS ET. Tras la
                                         instalación, el dispositivo puede seleccionarse en el catálogo de dispositivos y añadirse
                                         a un proyecto. Por medio de la interfaz de comunicación se establece una conexión con
                                         el dispositivo. Para la transmisión de datos, la conexión debe estar activada (online).

7.4               Descripción de la función

7.4.1             Grupo de menús Medición


7.4.1.1           Menú Tiempo de ciclo
                                         El tiempo de ciclo define el intervalo en el que el dispositivo realiza una medición. El
                                         tiempo de ciclo se corresponde con la velocidad de salida de los valores medidos.




24        B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                        8026228/18SG/2024-12-16 | SICK
                                                                                                                 Sujeto a cambio sin previo aviso

MANEJO 7


                                   •    Modo auto: el dispositivo se ajusta a la velocidad máxima con la que puede
                                        conseguir una medición estable en función de la superficie del objeto. En el modo
                                        auto, el tiempo de ciclo se ajusta dinámicamente para que la velocidad de salida
                                        de los valores medidos pueda variar con el tiempo.
                                   •    Ajuste fijo: independientemente de la superficie del objeto, el dispositivo utiliza
                                        el tiempo de ciclo máximo establecido. La velocidad de salida de los valores
                                        medidos se corresponde con el valor definido y permanece constante.
                                        INDICACIÓN
                                        Si las propiedades de reflexión difusa del objeto no son suficientes para realizar
                                        una medición válida, el dispositivo emite el valor de una medición errónea, véase
                                        "Menú Modo de error", página 31.
                                        Para mostrar una lectura válida para objetos oscuros, es posible aumentar el
                                        tiempo de ciclo.


                                   Ajuste del tiempo de ciclo

                                       > Medición >      > Tiempo de ciclo >       > Seleccionar opción >

                                   Parámetro                    Valor                                             Ajuste de fábrica
                                   Tiempo de ciclo              Auto, 133 µs, 150 µs, 200 µs, 300 µs,             Auto
                                                                500 µs, 1 ms, 2 ms, 5 ms


7.4.1.2            Menú Filtro de valores medidos
                                   Los filtros de valores medidos optimizan el desarrollo de la señal. Los filtros facilitan la
                                   evaluación por parte del controlador, por ejemplo, para las tareas de regulación.
                                   Filtro de valores medidos
                                   • Filtro de valor medio: el filtro de promedios o filtro de valor medio efectúa un
                                         cálculo de valor promedio de los valores medidos. Esto mejora la repetibilidad
                                         temporal de la medición. El filtro de promedios es adecuado para suavizar una
                                         curva de señal temporalmente con ruido.
                                   • Filtro de mediana: el filtro deslizante de mediana clasifica los valores medidos
                                         según su tamaño. A continuación, el filtro selecciona el valor medio. El filtro de
                                         mediana es adecuado para excluir los valores atípicos individuales del cálculo de
                                         un valor medio.
                                   Ambos tipos de filtros afectan al tiempo de respuesta del sensor de distancia.




8026228/18SG/2024-12-16 | SICK                                                       B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link   25
Sujeto a cambio sin previo aviso

7 MANEJO

                                    Output signal




                                                           1            2                                    4



                                                                              3




                                                                                                                                        Time t




                                                     1 Real distance
                                                     2 Measured value with median (Avg: 63)
                                                     3 Measured value with averaging (Avg: 64)
                                                     4 Measured value without averaging (Avg: OFF)
                                    Figura 9: Efecto de los filtros de valores medidos en la señal de salida mediante una curva
                                    temporal de valores de distancia
                                    1           Señal de salida
                                    2           distancia real
                                    3           Valor medido sin filtro de valores medidos
                                    4           Valor medido con filtro de valor medio
                                    5           Valor medido con filtro de mediana
                                    6           Tiempo t

                                    Ajuste del filtro de valor medio

                                            > Medición >           > Filtro de promedios >        > Seleccionar opción >

                                     Parámetro                           Valor                                    Ajuste de fábrica
                                     Filtro de promedios                 Desact., 4, 8, 16, 32, 64, 128, 256, 512 128

                                    Ajuste del filtro de mediana

                                            > Medición >           > Filtro de mediana >         > Seleccionar opción >

                                     Parámetro                           Valor                                    Ajuste de fábrica
                                     Filtro de mediana                   Desact., 3, 7, 15, 31                    31




26   B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                                       8026228/18SG/2024-12-16 | SICK
                                                                                                                           Sujeto a cambio sin previo aviso

MANEJO 7


7.4.1.3            Menú Dirección de medición
                                   La función Dirección de medición cambia el signo del valor de distancia relativo. El
                                   cambio de signo depende de la dirección de la distancia al centro del campo de
                                   medición (posición cero).
                                   •    Positivo: se asigna un signo positivo a las distancias superiores a la posición
                                        cero definida para el dispositivo. A las distancias menores se les asigna un signo
                                        negativo.
                                   •    Negativo: se asigna un signo negativo a las distancias superiores a la posición
                                        cero definida para el dispositivo. A las distancias menores se les asigna un signo
                                        positivo.

                                   Ajuste de la dirección de medición

                                        > Medición >      > Dirección de medición >           > Seleccionar opción >

                                   Parámetro                    Valor                                               Ajuste de fábrica
                                   Dirección de medición        Positivo                                            Positivo
                                                                Negativo


7.4.1.4            Menú Desviación del valor medido
                                   La desviación del valor medido desplaza el punto cero del valor de la distancia relativa.
                                   El valor de la salida analógica a esta distancia se encuentra en el centro del rango de
                                   valores analógicos. Con la ayuda de la desviación del valor medido se pueden medir los
                                   cambios de distancia con respecto a una distancia de referencia individual.

                                   INDICACIÓN
                                   Al ajustar la desviación del valor medido, la pendiente actual de la curva característica
                                   analógica no se modifica.

                                   En el menú principal puede ajustarse manualmente la desviación del valor medido.
                                   En el menú rápido puede realizarse el aprendizaje del punto cero y reiniciarse. La
                                   distancia actual se aprende como nuevo punto cero (punto de referencia). Información
                                   de la ruta de menú, véase "Estructura de los menús en el menú rápido", página 72.
                                   El valor de la distancia que emite el dispositivo y que se evalúa en las funciones de
                                   conmutación tiene en cuenta la desviación definida del valor medido. A través de la
                                   comunicación IO-Link sólo se transmiten los valores relativos de distancia que indican
                                   el valor medido incluyendo su desviación.
                                   Tabla 5: Desviación del valor medido (ejemplo, tipo de dispositivo OD2000-700)
                                                       Distancia (abso‐      Distancia (rela‐        Salida analógica              Offset definido
                                                       luta)                 tiva)
                                   En los ajustes de   0700,0 mm             0000,0 mm               12,00 mA                      0000,0 mm
                                   fábrica
                                   Con desviación      0700,0 mm             -0100,0 mm              10,40 mA                      0100,0 mm
                                   del valor medido
                                   +100,0 mm

                                   Tabla 6: Cambio de la señal de corriente analógica debido al cambio de distancia (ejemplo, tipo
                                   de dispositivo OD2000-700)
                                   Campo de medición                                   200 mm ... 1.200 mm
                                   Salida analógica de corriente                       4 mA ... 20 mA
                                   Variación de la distancia                           100,0 mm
                                   Modificación de la salida analógica de              1,6 mA
                                   corriente por variación en la distancia


8026228/18SG/2024-12-16 | SICK                                                         B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link   27
Sujeto a cambio sin previo aviso

7 MANEJO


                                         Ajuste de Desviación del valor medido

                                                 >>           > Desviación del valor medido >   > Ajuste del valor >

                                          Parámetro                             Valor                                  Ajuste de fábrica
                                          Desviación del valor medido           -1.000,0 mm ... +1.000,0 mm            0,000 mm


7.4.1.5           Menú Calibración
                                         En la medición, diferentes características de superficie del objeto de medición y el de
                                         referencia, así como errores de alineación o angulares durante el montaje, pueden pro‐
                                         vocar desviaciones de los valores medidos. La calibración corrige las desviaciones de
                                         los valores medidos. La desviación de la linealidad especificada en los datos técnicos
                                         no varía.
                                         Es posible realizar el aprendizaje de la calibración o bien ajustarse manualmente. La
                                         calibración se realiza para ambos puntos de calibración en dos pasos. Primero se
                                         realiza el aprendizaje o el ajuste del valor actual. A continuación se define el valor de
                                         ajuste como valor nominal.

                                         Aprendizaje de la calibración
                                         Para el aprendizaje de la calibración, el dispositivo debe ser capaz de medir. La distan‐
                                         cia al objeto no debe cambiar durante el aprendizaje. El objeto debe estar dentro del
                                         campo de medición.
                                         Parámetros de aprendizaje
                                         • 1er punto
                                         • 2º punto
                                         Aprendizaje de la calibración
                                         1. Abrir el menú:       > Medición >     > Calibración (auto)>
                                         ✓ La pantalla muestra el valor medido actual.
                                         2. Ponga el punto de calibración 1er punto a la distancia actual, véase "Aprendizaje
                                             del valor", página 21.
                                         3. Ajuste el punto de calibración 1er punto manualmente con el valor de ajuste (valor
                                             nominal), véase "Ajuste del valor", página 21.
                                         4. Repita la operación para el punto de calibración 2º punto.

                                         Ajuste de la calibración
                                         Parámetros ajustables
                                         • 1er punto valor actual
                                         • 1er punto valor de ajuste
                                         • 2º punto valor actual
                                         • 2º punto valor de ajuste
                                         Ajuste de la calibración
                                         1. Abrir el menú:         > Medición >     > Calibración (manual)>
                                         2. En el 1er punto valor actual, defina el valor de distancia actual, véase "Ajuste del
                                              valor", página 21.
                                         3. En el 1er punto valor de ajuste, defina el valor de ajuste (valor nominal), véase "Ajuste
                                              del valor", página 21.
                                         4. Repita la operación para el segundo punto de calibración 2º punto valor actual y 2º
                                              punto valor de ajuste.




28        B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                                     8026228/18SG/2024-12-16 | SICK
                                                                                                                              Sujeto a cambio sin previo aviso

MANEJO 7


7.4.1.6            Menú Region of Interest (ROI)
                                   La Region of Interest (ROI) puede utilizarse para definir un área de evaluación en la que
                                   el dispositivo mide las distancias de los objetos. Todas las áreas circundantes quedan
                                   cegadas. Para el ajuste, tenga en cuenta que, con el uso, debe respetarse un rango
                                   de tolerancia de 15 mm fuera de los límites definidos del rango de distancia. En este
                                   rango de tolerancia no se garantiza un cegado seguro ni la detección de objetos.
                                   Ejemplos de aplicación
                                   • Cegar la pantalla protectora transparente entre el objeto y el dispositivo.
                                   • El segundo pico de intensidad desplaza el valor medido de forma indeseada.
                                                       Blanking 1                        Detection 2                                      Blanking 1


                                                       Transparent
                                                       screen 8                      Measuring object 3




                                                                                  Region of Interest (ROI) 4
                                                                            ROI Near 8                           ROI Far 5

                                                              15 mm (0,59 inch)                                        15 mm (0,59 inch)
                                                             Tolerance window 6                                       Tolerance window 6
                                                                                  Max. measuring range 7

                                   Figura 10: Cegado de una pantalla protectora transparente
                                   1      Cegado
                                   2      Detección
                                   3      Objeto de medición
                                   4      Region of Interest (ROI)
                                   5      ROI cercano
                                   6      ROI lejano
                                   7      Ventana de tolerancia
                                   8      Campo de medición máximo
                                   9      Disco transparente

                                   Límites de la Region of Interest (ROI)
                                   Los valores ROI cercano y ROI lejano son las distancias en milímetros que definen los
                                   límites del rango de evaluación. Los límites pueden estar fuera del campo de medición
                                   especificado.
                                   La ROI puede definirse a través de SOPAS ET, véase "Manejo a través de SOPAS ET",
                                   página 23.

                                   Ajuste de ROI cercano y ROI lejano

                                       > Medición >       > ROI cercano >      > Ajuste del valor >

                                       > Medición >       > ROI lejano >     > Ajuste del valor >




8026228/18SG/2024-12-16 | SICK                                                           B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link   29
Sujeto a cambio sin previo aviso

7 MANEJO

                                          Parámetro                     Valor                          Ajuste de fábrica
                                          ROI cercano                   Ajuste del punto de conmuta‐   ROI cercano:
                                                                        ción                           OD2000-030: -5,04 mm
                                                                        OD2000-030:                    OD2000-050: -10,10 mm
                                                                        -5,04 mm ... +5,75 mm          OD2000-130: -70,70 mm
                                                                        OD2000-050:                    OD2000-245: -176,75 mm
                                                                        -10,10 mm ... +11,50 mm        OD2000-350: -252,50 mm
                                                                        OD2000-130:                    OD2000-700: -505,00 mm
                                                                        -70,70 mm … +76,00 mm
                                          ROI lejano                                                   ROI lejano:
                                                                        OD2000-245:
                                                                        -176.75 mm ... +189.00 mm      OD2000-030: +5,75 mm
                                                                        OD2000-350:                    OD2000-050: +11,50 mm
                                                                        -252.50 mm ... +271.00 mm      OD2000-130: +76,00 mm
                                                                        OD2000-700                     OD2000-245: +189,00 mm
                                                                        : -505,00 mm ... +550,00 mm    OD2000-350: +271,00 mm
                                                                                                       OD2000-700: +550,00 mm


7.4.1.7           Menú Selección del pico
                                         En la medición de la distancia, un haz de luz incide sobre el receptor que hay en el
                                         dispositivo. En el receptor se forma entonces un pico de señal. La posición del pico de
                                         señal se utiliza para la determinación de la distancia.
                                         En condiciones de aplicación desfavorables, pueden producirse variaciones del efecto
                                         del haz de luz con la superficie del objeto, así como efectos de reflexión o interferen‐
                                         cias. Esto influye sobre la forma del pico de señal, o bien se generan picos de señal
                                         dobles.

                                         Auto
                                         Método de evaluación del pico e señal para la mayoría de las aplicaciones. La curva
                                         de distribución de la luz sobre el receptor muestra un pico de señal bien definido, cuya
                                         intensidad difiere claramente de los rangos de los receptores contiguos.

                                         1er pico remoto demasiado cerca
                                         Método de evaluación para determinar el pico de evaluación cuando se dan más de un
                                         pico de señal válido en la curva de distribución de la luz. Se evalúa el primer pico de
                                         señal válido partiendo del final del campo de medición.

                                         2º pico remoto demasiado cerca
                                         Método de evaluación para determinar el pico de evaluación cuando se dan más de un
                                         pico de señal válido en la curva de distribución de la luz. Se evalúa el segundo pico de
                                         señal válido partiendo del final del campo de medición.

                                         1er pico cercano demasiado lejos
                                         Método de evaluación para determinar el pico de evaluación cuando se dan más de un
                                         pico de señal válido en la curva de distribución de la luz. Se evalúa el primer pico de
                                         señal válido partiendo del principio del campo de medición.

                                         2º pico cercano demasiado lejos
                                         Método de evaluación para determinar el pico de evaluación cuando se dan más de un
                                         pico de señal válido en la curva de distribución de la luz. Se evalúa el segundo pico de
                                         señal válido partiendo del principio del campo de medición.




30        B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                          8026228/18SG/2024-12-16 | SICK
                                                                                                                   Sujeto a cambio sin previo aviso

MANEJO 7


                                   Anchura de pico
                                   Método de evaluación para determinar el pico de evaluación con geometrías de pico
                                   desfavorables o con factores perturbadores en el entorno. Con la definición de la
                                   Anchura mín. de pico y la Anchura máx. de pico pueden suprimirse efectos perturbadores
                                   del entorno. Los parámetros Anchura mín. de pico y Anchura máx. de pico se muestran en el
                                   menú en cuanto se activa Anchura de pico.

                                   Ajuste de la selección del pico

                                        > Medición >      > Selección del pico >    > Ajuste del valor >

                                   Parámetro                      Valor                                      Ajuste de fábrica
                                   Selección del pico             Auto                                       Auto
                                                                  1er pico remoto demasiado cerca
                                                                  2º pico remoto demasiado cerca
                                                                  1er pico cercano demasiado lejos
                                                                  2º pico cercano demasiado lejos
                                                                  Anchura de pico

                                   Ajuste de Anchura mín. de pico y Anchura máx. de pico

                                        > Medición >      > Selección del pico >    > Anchura de pico >

                                        > Medición >      > Anchura de pico mín./máx. Anchura de pico >             > Ajuste de valor >

                                   Parámetro                      Valor                                      Ajuste de fábrica
                                   Anchura mín. de pico           0 píxeles … 100 píxeles                    4 píxeles
                                   Anchura máx. de pico           0 píxeles … 100 píxeles                    30 píxeles


7.4.1.8            Menú Modo de error
                                   Si el dispositivo no puede medir la distancia, se emite un valor sustitutivo. El comporta‐
                                   miento del dispositivo en caso de mediciones defectuosas puede ajustarse mediante
                                   varios parámetros.
                                   Posibles causas de error
                                   • Objeto de medición fuera del campo de medición
                                   • La señal luminosa recibida no es lo suficientemente fuerte
                                   • Emisor desconectado
                                   Parámetro
                                   • Modo de error > Valor definido por el usuario: si no es posible realizar ninguna medi‐
                                       ción, se muestra el Valor de sustitución definido y se mantiene hasta que vuelva a
                                       haber un valor medido válido.
                                   • Modo de error> Conservar el último valor: si no es posible realizar ninguna medición, se
                                       muestra el último valor medido válido y se mantiene hasta que vuelva a haber un
                                       valor medido válido.
                                   • Modo de error> Conservar últ. valor + tempor.: si no es posible realizar ninguna medi‐
                                       ción, se muestra el último valor medido válido y se mantiene durante el tiempo
                                       definido en el Tiempo de supresión de error. A continuación, se muestra el Valor de
                                       sustitución definido y se mantiene hasta que se vuelva a disponer de un valor
                                       medido válido.
                                   • Valor de sustitución: establezca un valor numérico como valor de sustitución. Si no
                                       es posible la medición, se emite el valor sustitutivo.
                                   • Tiempo de supresión de error: defina el tiempo durante el cual se muestra y mantiene
                                       el último valor medido válido. Para esta función, debe activarse el modo de error
                                       Conservar últ. valor + tempor..



8026228/18SG/2024-12-16 | SICK                                                         B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link   31
Sujeto a cambio sin previo aviso

7 MANEJO

                                         Ajuste de Modo de error

                                                 > Medición >           > Modo de error >      > Seleccionar opción >

                                          Parámetro                              Valor                                         Ajuste de fábrica
                                          Modo de error                          Valor definido por usuario                    Valor definido por usuario
                                                                                 Conservar el último valor
                                                                                 Conservar últ. valor + tempor.

                                         Ajuste de Valor de sustitución

                                                 > Medición >           > Valor de sustitución >      > Ajuste del valor >

                                          Parámetro                              Valor                                         Ajuste de fábrica
                                          Valor de sustitución                   -2.000.00 mm ... +2.000.00 mm                 +2.000,00 mm

                                         Ajuste de Tiempo de supresión de error

                                                 > Medición >           > Tiempo de supresión de error >          > Ajuste del valor >

                                          Parámetro                              Valor                                         Ajuste de fábrica
                                          Tiempo de supresión de error           1 ms ... 100.000 ms                           1 ms


7.4.2             Ajustes Q1 y Q2 / Qa


7.4.2.1           Menú Q1 / Q2 Lógica del punto de conmutación
                                         La lógica del punto de conmutación describe la relación entre el estado de conmuta‐
                                         ción (activo o inactivo) y el potencial aplicado a la salida digital (High o Low).
                                         Ajustes (en función del modo de salida)
                                         • High-active: la salida digital funciona como un contacto normalmente abierto. Si el
                                              valor cae por debajo del punto de conmutación programado, se emite una señal.
                                         • Low-active: la salida digital funciona como un contacto normalmente cerrado. Si se
                                              sobrepasa el punto de conmutación programado, se emite una señal.

                                         Ajuste de Q1 Lógica del punto de conmutación

                                                 > Salida Q1 >          > Q1 Lógica del punto de conmutación >           > Seleccionar opción >

                                          Parámetro                              Valor                                         Ajuste de fábrica
                                          Q1 Lógica del punto de conmu‐ High-active                                            High-active
                                          tación                        Low-active


7.4.2.2           Menú Q1 / Q2 Modo de temporizador
                                         El modo temporizador se utiliza para emitir los cambios de estado de conmutación con
                                         un retardo de tiempo o como un impulso de conmutación corto (Impulso (one shot)). El
                                         tiempo de retardo es ajustable.




32        B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                                              8026228/18SG/2024-12-16 | SICK
                                                                                                                                       Sujeto a cambio sin previo aviso

MANEJO 7



                                               Device               Device               Device                                  Device                      Device
                                           1                 1                       1                                    1                              1




                                   High
                                                            0.5 s                                           0.5 s        0.5 s                   0.5 s
                                   Low
                                                                                                                                                                          t
                                                        2                    3                    4                                       5                           6
                                   1        Dispositivo
                                   2        Desconexión inmediatamente después de que la distancia medida supere el punto de
                                            conmutación predeterminado, el estado de la salida digital cambia (ajuste de fábrica).
                                   3        Retardo de conexión: se produce un retardo en la transición de la salida digital del estado
                                            no activo al activo. La transición del estado activo al no activo se produce sin retardo.
                                   4        Retardo de desconexión: se produce un retardo en la transición de la salida digital del
                                            estado activo al no activo. La transición del estado no activo al activo se produce sin
                                            retardo.
                                   5        Retardo de conexión/desconexión: se produce retardo en ambas transiciones.
                                   6        Impulso (one shot): cuando se cumple la condición de conmutación, la salida digital pasa
                                            del estado no activo al activo. Independientemente de cuánto tiempo se cumple la condi‐
                                            ción de conmutación, el estado de conmutación permanece en el estado activo durante
                                            un tiempo predeterminado. Solo después vuelve el estado de conmutación al estado no
                                            activo. Otros cambios en las condiciones de conmutación no se tienen en cuenta durante
                                            este periodo.

                                   Ajuste de Q1 Modo de temporizador

                                   INDICACIÓN
                                   Cuando utilice el modo de temporizador, defina un tiempo de ciclo fijo (no Auto).
                                   Ajuste el Ajuste del temporizador al menos igual de extenso que el tiempo de ciclo.
                                   Cuando utilice el modo de temporizador Retardo de conexión/desconexión, ajuste el Ajuste
                                   del temporizador como mínimo con el doble de duración que el tiempo de ciclo.

                                          > Salida Q1 >      > Q1 Modo de temporizador >                       > Seleccionar opción >

                                   Parámetro                                 Valor                                                        Ajuste de fábrica
                                   Q1 Modo de temporizador                   Desconexión                                                  Desconexión
                                                                             Retardo de conexión
                                                                             Retardo de desconexión
                                                                             Retardo de conexión/desconexión
                                                                             Impulso (one shot)


7.4.2.3            Menú Q1 / Q2 Histéresis
                                   La histéresis es la diferencia de distancia entre el punto de conexión y el de descone‐
                                   xión. Si la distancia medida fluctúa en torno al punto de conmutación establecido, la
                                   histéresis es necesaria para un comportamiento de conmutación estable. Para conse‐
                                   guir un comportamiento de conmutación más preciso, defina un valor menor para la
                                   histéresis. Para conseguir un comportamiento de conmutación más estable, defina un
                                   valor mayor para la histéresis.

                                   Ajuste de Q1 Histéresis

                                          > Salida Q1 >      > Q1 Histéresis >                    > Ajuste del valor >



8026228/18SG/2024-12-16 | SICK                                                                           B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link      33
Sujeto a cambio sin previo aviso

7 MANEJO

                                          Parámetro                     Valor                          Ajuste de fábrica
                                          Q1 Histéresis                 0 mm ... 2.147,48 mm           OD2000-030: 0,1 mm
                                                                                                       OD2000-050: 0,2 mm
                                                                                                       OD2000-130: 0,3 mm
                                                                                                       OD2000-245: 0,5 mm
                                                                                                       OD2000-350: 1 mm
                                                                                                       OD2000-700: 1,5 mm


7.4.3             Grupo de menús Q1 Salida
                                         La salida Q1 es una salida digital. Además, cuando se utiliza la interfaz IO-Link, la
                                         salida sirve como línea de comunicación para la transmisión bidireccional de datos.
                                         La salida Q1 ofrece diferentes modos de salida. Cuando se selecciona un modo de
                                         salida, los ajustes necesarios se pueden establecer mediante aprendizaje o manual‐
                                         mente. Dependiendo del modo de salida seleccionado, hay diferentes parámetros
                                         disponibles.

7.4.3.1           Ajuste del punto de conmutación
                                         Un punto de conmutación puede establecerse mediante aprendizaje o manualmente.
                                         Para el aprendizaje de un punto de conmutación, el dispositivo debe ser capaz de
                                         medir. La distancia al objeto no debe cambiar durante el aprendizaje. El objeto debe
                                         estar dentro del campo de medición.
                                         El punto de conmutación SP2 sólo está disponible en el modo de salida Ventana. En el
                                         aprendizaje de una ventana de conmutación no debe programarse el mismo valor de
                                         distancia para la distancia cercana al sensor que para la lejana.

                                         Aprendizaje del punto de conmutación
                                         Ajuste el punto de conmutación a la distancia actual en el momento de pulsar la tecla,
                                         véase "Aprendizaje del valor", página 21.
                                         Parámetros de aprendizaje
                                         • Q1 Aprendizaje SP1 (auto)
                                         • Q1 Aprendizaje SP2 (auto)
                                         Ajuste manual del punto de conmutación
                                         Ajuste manual de la distancia del punto de conmutación, véase "Ajuste del valor",
                                         página 21. El valor del punto de conmutación puede ajustarse en función del número
                                         de decimales establecido.
                                         Parámetros ajustables
                                         • Q1 Aprendizaje SP1 (manual)
                                         • Q1 Aprendizaje SP2 (manual)

7.4.3.2           Menú Q1 Punto único (SP1:DtO)
                                         Ajuste un punto de conmutación. Si el valor de la distancia medida queda por debajo
                                         (contacto NA: punto de conmutación lógico High-active) o lo supera (contacto NC: punto
                                         de conmutación lógico Low-active), se emite una señal (cambio del nivel de salida).




34        B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                      8026228/18SG/2024-12-16 | SICK
                                                                                                               Sujeto a cambio sin previo aviso

MANEJO 7


                                                                                                 1


                                                                                                 0
                                        Minimum 1                2                        Maximum 3
                                   Figura 11: Distancia al objeto, punto de conmutación simple (contacto normalmente abierto:
                                   HIGH active, PNP)
                                   1      Mínimo
                                   2      Punto de conmutación
                                   3      Máximo


                                                                                                 1


                                                                                                 0
                                         Minimum 1               2                    Maximum 3
                                   Figura 12: Distancia al objeto, punto de conmutación simple invertido (contacto normalmente
                                   cerrado: LOW active, PNP)
                                   1      Mínimo
                                   2      Punto de conmutación
                                   3      Máximo

                                   Selección del modo de salida y ajuste de parámetros

                                       > Q1 Salida >      > Q1 Modo >      > Q1 Punto único (SP1: DtO) >

                                        > Q1 Salida >     > Parámetro >        > Seleccionar la opción, realizar aprendizaje o ajuste
                                   del valor

                                   Parámetro                     Valor                                              Ajuste de fábrica
                                   Q1 SP1 Aprendizaje (auto)     Ajuste del punto de conmutación                    0.00 mm
                                   Q1 SP1 Aprendizaje (manual)   OD2000-030:
                                                                 -5,04 mm ... +5,75 mm
                                                                 OD2000-050:
                                                                 -10,10 mm ... +11,50 mm
                                                                 OD2000-130:
                                                                 -70,70 mm … +76,00 mm
                                                                 OD2000-245:
                                                                 -176.75 mm ... +189.00 mm
                                                                 OD2000-350:
                                                                 -252.50 mm ... +271.00 mm
                                                                 OD2000-700
                                                                 : -505,00 mm ... +550,00 mm
                                   Q1 Lógica del punto de conmu‐ High-active                                        High-active
                                   tación                        Low-active
                                   Q1 Modo de temporizador       Desconexión                                        Desconexión
                                                                 Retardo de conexión
                                                                 Retardo de conexión/desconexión
                                                                 Retardo de desconexión
                                                                 Impulso (one shot)
                                   Q1 Ajuste del temporizador    1 ms ... 30.000 ms                                 1 ms




8026228/18SG/2024-12-16 | SICK                                                         B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link   35
Sujeto a cambio sin previo aviso

7 MANEJO

                                          Parámetro                           Valor                                    Ajuste de fábrica
                                          Q1 Histéresis                       0 mm ... 2.147,48 mm                     OD2000-030: 0,1 mm
                                                                                                                       OD2000-050: 0,2 mm
                                                                                                                       OD2000-130: 0,3 mm
                                                                                                                       OD2000-245: 0,5 mm
                                                                                                                       OD2000-350: 1 mm
                                                                                                                       OD2000-700: 1,5 mm


7.4.3.3           Menú Q1 Ventana (SP1,SP2:Ventana)
                                         Establezca un umbral de conmutación superior y otro inferior (dos puntos de conmuta‐
                                         ción). Si la distancia medida se encuentra dentro (contacto NA: punto de conmutación
                                         lógico High-active) o fuera (contacto NC: punto de conmutación lógico Low-active) de la
                                         ventana de conmutación, se emite una señal (cambio del nivel de salida).
                                                                                                           1


                                                                                                        0
                                                   Minimum 1              2             3          Maximum 4
                                         Figura 13: Ventana (contacto normalmente abierto: HIGH active, PNP)
                                         1           Mínimo
                                         2           Punto de conmutación cercano
                                         3           Punto de conmutación lejano
                                         4           Máximo


                                                                                                           1


                                                                                                        0
                                                 Minimum 1                2             3          Maximum 4
                                         Figura 14: Ventana (contacto normalmente cerrado: LOW active, PNP)
                                         1           Mínimo
                                         2           Punto de conmutación cercano
                                         3           Punto de conmutación lejano
                                         4           Máximo

                                         Selección del modo de salida y ajuste de parámetros

                                                 > Q1 Salida >          > Q1 Modo >     > Q1 Ventana (SP1,SP2: Ventana) >

                                               > Q1 Salida >            > Parámetro >       > Seleccionar la opción, realizar aprendizaje o ajuste
                                          del valor




36        B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                                       8026228/18SG/2024-12-16 | SICK
                                                                                                                                Sujeto a cambio sin previo aviso

MANEJO 7


                                   Parámetro                     Valor                                             Ajustes predeterminados
                                   Q1 SP1 Aprendizaje (auto)     Ajuste del punto de conmutación                   SP1: 0,00 mm
                                   Q1 SP1 Aprendizaje (manual)   OD2000-030:
                                                                 -5,04 mm ... +5,75 mm
                                   Q1 SP2 Aprendizaje (auto)     OD2000-050:                                       SP2:
                                   Q1 SP2 Aprendizaje (manual)   -10,10 mm ... +11,50 mm                           OD2000-030: +5 mm
                                                                 OD2000-130:                                       OD2000-050: +10 mm
                                                                 -70,70 mm … +76,00 mm                             OD2000-130: +70 mm
                                                                 OD2000-245:                                       OD2000-245: +175 mm
                                                                 -176.75 mm ... +189.00 mm                         OD2000-350: +250 mm
                                                                 OD2000-350:                                       OD2000-700: +500 mm
                                                                 -252.50 mm ... +271.00 mm
                                                                 OD2000-700
                                                                 : -505,00 mm ... +550,00 mm
                                   Q1 Lógica del punto de conmu‐ High-active                                       High-active
                                   tación                        Low-active
                                   Q1 Modo de temporizador       Desconexión
                                                                 Retardo de conexión
                                                                 Retardo de desconexión
                                                                 Retardo de conexión/desconexión
                                                                 Impulso (one shot)                                Desconexión
                                   Q1 Ajuste del temporizador    1 ms ... 30.000 ms                                1 ms
                                   Q1 Histéresis                 0 mm ... 2.147,48 mm                              OD2000-030: 0,1 mm
                                                                                                                   OD2000-050: 0,2 mm
                                                                                                                   OD2000-130: 0,3 mm
                                                                                                                   OD2000-245: 0,5 mm
                                                                                                                   OD2000-350: 1 mm
                                                                                                                   OD2000-700: 1,5 mm


7.4.3.4            Menú Q1 Ventana (SP1:ObSB)
                                   Establezca un fondo como referencia. Si no se detecta el fondo de referencia (contacto
                                   NA: punto de conmutación lógico High-active) o si se detecta el fondo de referencia
                                   (contacto NC: punto de conmutación lógico Low-active), se emite una señal. En el modo
                                   de salida ObSB se detectan todos los objetos que difieren del fondo. También se
                                   detectan los objetos que son reflectantes o negros.
                                                                   2
                                                                                                1


                                                                                                0
                                        Minimum 1                  4                  Maximum 3
                                   Figura 15: Objeto entre el dispositivo y el fondo (contacto NA: High-active, PNP)
                                   1      Mínimo
                                   2      Tolerancia en torno al punto de conmutación
                                   3      Máximo
                                   4      Punto de conmutación (fondo de referencia)




8026228/18SG/2024-12-16 | SICK                                                        B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link   37
Sujeto a cambio sin previo aviso

7 MANEJO

                                                                           2

                                                                                                    1


                                                                                                    0
                                              Minimum 1                    4                Maximum 3
                                    Figura 16: Objeto entre el dispositivo y el fondo (contacto NC: Low-active, PNP)
                                    1           Mínimo
                                    2           Tolerancia en torno al punto de conmutación
                                    3           Máximo
                                    4           Punto de conmutación (fondo de referencia)

                                    Selección del modo de salida y ajuste de parámetros

                                            > Q1 Salida >          > Q1 Modo >     > Q1 Ventana (SP1: ObSB) >

                                          > Q1 Salida >            > Parámetro >     > Seleccionar la opción, realizar aprendizaje o ajuste
                                     del valor

                                     Parámetro                           Valor                                  Ajuste de fábrica
                                     Q1 SP1 Aprendizaje (auto)           Ajuste del punto de conmutación        0.00 mm
                                     Q1 SP1 Aprendizaje (manual)         OD2000-030:
                                                                         -5,04 mm ... +5,75 mm
                                                                         OD2000-050:
                                                                         -10,10 mm ... +11,50 mm
                                                                         OD2000-130:
                                                                         -70,70 mm … +76,00 mm
                                                                         OD2000-245:
                                                                         -176.75 mm ... +189.00 mm
                                                                         OD2000-350:
                                                                         -252.50 mm ... +271.00 mm
                                                                         OD2000-700
                                                                         : -505,00 mm ... +550,00 mm
                                     Q1 Lógica del punto de conmu‐ High-active                                  High-active
                                     tación                        Low-active
                                     Q1 Modo de temporizador             Desconexión                            Desconexión
                                                                         Retardo de conexión
                                                                         Retardo de desconexión
                                                                         Retardo de conexión/desconexión
                                                                         Impulso (one shot)
                                     Q1 Ajuste del temporizador          1 ms ... 30.000 ms                     1 ms
                                     Q1 Histéresis                       0 mm ... 2.147,48 mm                   OD2000-030: 0,1 mm
                                                                                                                OD2000-050: 0,2 mm
                                                                                                                OD2000-130: 0,3 mm
                                                                                                                OD2000-245: 0,5 mm
                                                                                                                OD2000-350: 1 mm
                                                                                                                OD2000-700: 1,5 mm
                                     Q1 Tolerancia                       0 mm ... 2.147,48 mm                   OD2000-030: 1 mm
                                                                                                                OD2000-050: 1 mm
                                                                                                                OD2000-130: 2 mm
                                                                                                                OD2000-245: 4 mm
                                                                                                                OD2000-350: 4 mm
                                                                                                                OD2000-700: 4 mm




38   B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                                    8026228/18SG/2024-12-16 | SICK
                                                                                                                        Sujeto a cambio sin previo aviso

MANEJO 7


7.4.3.5            Menú Q1 Alarma
                                   Mientras no sea posible la medición, se emite una señal de conmutación constante en
                                   la salida. Esta función puede utilizarse, por ejemplo, para evaluar el valor medido en la
                                   salida analógica.

                                   Selección del modo de salida y ajuste de parámetros

                                       > Salida Q1 >      > Modo Q1 >      > Q1 Alarma >

                                       > Q1 Salida >      > Parámetros >        > Seleccionar opción >

                                   Parámetro                     Valor                                              Ajustes predeterminados
                                   Q1 Lógica del punto de conmu‐ High-active                                        High-active
                                   tación                        Low-active


7.4.3.6            Menú Q1 Advertencia de nivel
                                   Si el nivel de la señal cae por debajo de un valor de umbral, se emite un aviso a través
                                   de las salidas digitales Q1 y Q2. El umbral de la señal puede establecerse mediante
                                   aprendizaje o manualmente como valor numérico. El nivel de la señal es un valor
                                   específico del sensor sin unidad de medida. Se recomienda ajustar el nivel de la señal
                                   mediante mediciones de prueba específicas de la aplicación.

                                   Selección del modo de salida y ajuste de parámetros

                                       > Salida Q1 >      > Modo Q1 >      > Q1 Advertencia de nivel >

                                        > Q1 Salida >     > Parámetro >        > Seleccionar la opción, realizar aprendizaje o ajuste
                                   del valor

                                   Parámetro                     Valor                                              Ajustes predeterminados
                                   Q1 Umbral de señal (auto)     Ajuste del punto de conmutación                    1700
                                   Q1 Umbral de señal (manual)   0 ... 5000

                                   Q1 Lógica del punto de conmu‐ High-active                                        High-active
                                   tación                        Low-active
                                   Q1 Modo de temporizador       Desconexión
                                                                 Retardo de conexión
                                                                 Retardo de desconexión
                                                                 Retardo de conexión/desconexión
                                                                 Impulso (one shot)                                 Desconexión
                                   Q1 Ajuste del temporizador    1 ms ... 30.000 ms                                 1 ms


7.4.3.7            Menú Q1 Cambio altura de bordes
                                   Si se produce un salto de valor entre dos valores medidos, se emite una señal. Una
                                   aplicación típica es el recuento de copias o escalas en aplicaciones de impresión. El
                                   dispositivo se encarga de la compleja evaluación a través de su controlador.
                                   Ajustes para el uso de la función
                                   • Menú Q1 Mín./Máx. Cambio altura
                                   • Fijo Menú Tiempo de ciclo (recomendado)
                                        INDICACIÓN
                                        En el modo Auto, la fluctuación de los valores de reflectividad difusa de la superfi‐
                                        cie del objeto puede modificar el tiempo de ciclo del dispositivo. Esto significa que
                                        no se garantiza una detección fiable con altas velocidades de detección o con
                                        estructuras pequeñas.


8026228/18SG/2024-12-16 | SICK                                                         B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link   39
Sujeto a cambio sin previo aviso

7 MANEJO

                                        •       Filtro de valor medio desc. (recomendado)
                                        •       Menú Q1 / Q2 Histéresis (si es necesario)
                                        •       Menú Q1 Dirección del salto (si es necesario)
                                        •       Menú Q1 Desplazamiento de ciclos (si es necesario)

                                       Selección del modo de salida y ajuste de parámetros

                                               > Salida Q1 >          > Modo Q1 >      > Q1 Cambio altura de bordes >

                                             > Q1 Salida >            > Parámetro >      > Seleccionar la opción, realizar aprendizaje o ajuste
                                        del valor

                                        Parámetro                           Valor                          Ajustes predeterminados
                                        Q1 Salto de altura mínimo           0 mm ... 2.147,48 mm           OD2000-030/050: 0.50 mm
                                                                                                           OD2000-130: 5,00 mm
                                                                                                           OD2000-245/350/700: 10.00 mm
                                        Q1 Salto de altura máximo           0 mm ... 2147,48 mm            OD2000-030/050: 2.00 mm
                                                                                                           OD2000-130: 30,00 mm
                                                                                                           OD2000-245/350/700: 100.00 mm
                                        Q1 Dirección del salto              Positivo                       Ambas
                                                                            Negativo
                                                                            Ambas
                                        Q1 Desplazamiento de ciclos         1 ... 10.000                   50
                                        Q1 Lógica del punto de conmu‐ High-active                          High-active
                                        tación                        Low-active
                                        Q1 Modo de temporizador             Desconexión                  Desconexión
                                                                            Retardo de conexión
                                                                            Retardo de desconexión
                                                                            Retardo de conexión/descone‐
                                                                            xión
                                                                            Impulso (one shot)
                                        Q1 Ajuste del temporizador          1 ms ... 30.000 ms             1 ms
                                        Q1 Histéresis                       0 mm ... 2.147,48 mm           OD2000-030: 0,1 mm
                                                                                                           OD2000-050: 0,2 mm
                                                                                                           OD2000-130: 0,3 mm
                                                                                                           OD2000-245: 0,5 mm
                                                                                                           OD2000-350: 1 mm
                                                                                                           OD2000-700: 1,5 mm


7.4.3.7.1                  Menú Q1 Mín./Máx. Cambio altura
                                       Q1 Salto de altura mínimo y Q1 Salto de altura máximo definen la menor y mayor diferencia
                                       entre el valor medido actual y el valor de comparación en milímetros. Los dos valores
                                       medidos deben diferir en esta diferencia para que haya un cambio o salto de la altura
                                       del borde. La función sólo tiene en cuenta la diferencia entre dos valores medidos y es
                                       independiente de la distancia absoluta del objeto.

7.4.3.7.2                  Menú Q1 Dirección del salto
                                       La dirección del salto define la dirección en la que se detectan los saltos en los valores
                                       medidos.




40      B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                                      8026228/18SG/2024-12-16 | SICK
                                                                                                                             Sujeto a cambio sin previo aviso

MANEJO 7


                                   •    Positivo: sólo se detectan los saltos de valores medidos dentro de los límites
                                        establecidos con grandes distancias (descripción válida con el ajuste de fábrica).
                                   •    Negativo: sólo se detectan los saltos del valores medidos dentro de los límites esta‐
                                        blecidos con distancias pequeñas (descripción válida con el ajuste de fábrica).
                                   •    Ambas: se detectan todos los saltos de valores medidos dentro de los límites
                                        establecidos.

7.4.3.7.3                   Menú Q1 Desplazamiento de ciclos
                                   El desplazamiento de ciclos especifica qué valor medido anterior se compara con el
                                   valor medido actual.

7.4.3.7.4                   Ejemplos: la salida digital en el modo de cambio de altura de bordes




                                                                                1
                                                                        4   3   2   1   0
                                                                    4   3   2   1   0
                                                           2 4 43   3
                                                                    2
                                                                        2
                                                                        1
                                                                            1
                                                                            0
                                                                                0




                                          4                                 6                             7                                  6
                                   3
                                          5



                                          9


                                   8      ß


                                          à


                                                                                                                                                          t

                                   Figura 17: Cambio de altura del borde: la duración del salto del valor medido es mayor que el
                                   lapso de tiempo del desplazamiento de ciclo.
                                   1      Desplazamiento de ciclos: 4, sin filtro de valores medidos
                                   2      Tiempo de ciclo fijo, por ejemplo, 1 ms
                                   3      Desarrollo de la señal con distancia real
                                   4      Valor límite máx. de salto de altura del borde (mm)
                                   5      Valor límite mín. de salto de la altura del borde (mm)
                                   6      Salto de valor medido, de distancia grande a pequeña
                                   7      Salto de valor medido, de distancia pequeña a grande
                                   8      Desarrollo de la señal en salida digital
                                   9      Parámetro Dirección de salto > Ambas
                                   ß      Parámetro Dirección de salto > Negativo
                                   à      Parámetro Dirección de salto > Positivo




8026228/18SG/2024-12-16 | SICK                                                              B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link       41
Sujeto a cambio sin previo aviso

7 MANEJO




                                                                                            1
                                                                                    4   3   2   1   0
                                                                                4   3   2   1   0
                                                                        2 4 43 32   2
                                                                                    1
                                                                                        1
                                                                                        0
                                                                                            0




                                                     4                                  6 7                6      7 6                7
                                         3
                                                     5



                                                     9


                                         8           ß


                                                     à


                                                                                                                                               t

                                         Figura 18: Salto de altura del borde: la duración del salto del valor medido es menor que el lapso
                                         de tiempo del desplazamiento del ciclo.
                                         1           Desplazamiento de ciclos: 4, sin filtro de valores medidos
                                         2           Tiempo de ciclo fijo, por ejemplo, 1 ms
                                         3           Desarrollo de la señal con distancia real
                                         4           Valor límite máx. de salto de altura del borde (mm)
                                         5           Valor límite mín. de salto de la altura del borde (mm)
                                         6           Salto de valor medido, de distancia grande a pequeña
                                         7           Salto de valor medido, de distancia pequeña a grande
                                         8           Desarrollo de la señal en salida digital
                                         9           Parámetro Dirección de salto > Ambas
                                         ß           Parámetro Dirección de salto > Negativo
                                         à           Parámetro Dirección de salto > Positivo


7.4.3.8           Menú Q1 Desconexión
                                         Si el modo de salida Q1 Desconexión está activado, la salida Q1 no tiene función y se
                                         desactiva.

7.4.4             Grupo de menús Q2 / Qa Salida
                                         La salida Q2 / Qa puede configurarse como salida analógica o como salida digital.
                                         Los dispositivos sin salida analógica cuentan con una segunda salida digital, . Para
                                         estos dispositivos, la información sobre la salida analógica no es relevante.
                                         Cuando se selecciona un modo de salida, los ajustes necesarios se pueden establecer
                                         mediante aprendizaje o manualmente. Dependiendo del modo de salida seleccionado,
                                         hay diferentes parámetros disponibles.




42        B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                             8026228/18SG/2024-12-16 | SICK
                                                                                                                      Sujeto a cambio sin previo aviso

MANEJO 7


7.4.4.1            Ajuste del valor analógico
                                   Es posible realizar el aprendizaje de un valor analógico o bien ajustarlo manualmente.
                                   No debe programarse el mismo valor de distancia para las distancias de sensor cerca‐
                                   nas que para las lejanas.

                                   Aprendizaje del valor analógico
                                   Se establece el valor analógico de la distancia actual en el momento de pulsar el
                                   botón, véase "Aprendizaje del valor", página 21.
                                   Parámetros de aprendizaje
                                   • Qa 4 mA aprendizaje (auto)
                                   • Qa 20 mA aprendizaje (auto)
                                   • Qa 0 V aprendizaje (auto)
                                   • Qa 10 V aprendizaje (auto)
                                   Para el aprendizaje de un valor analógico, el dispositivo debe ser capaz de medir. La
                                   distancia al objeto no debe cambiar durante el aprendizaje. El objeto debe estar dentro
                                   del campo de medición.

                                   Ajuste manual del valor analógico
                                   Se ajusta el valor analógico manualmente, véase "Ajuste del valor", página 21.
                                   Parámetros ajustables
                                   • Qa 4 mA aprendizaje (manual)
                                   • Qa 20 mA aprendizaje (manual)
                                   • Qa 0 V aprendizaje (manual)
                                   • Qa 10 V aprendizaje (manual)

7.4.4.2            Menú Qa Analógica 4 mA ... 20 mA
                                   La salida Q2 es una salida de corriente analógica. El valor medido se emite en forma
                                   de valor de corriente linealmente proporcional.

                                   Selección del modo de salida y ajuste de parámetros

                                       > Salida Q2 / Qa >       > Modo Q2 >      > Qa Analógica 4 mA ... 20 mA >

                                       > Q2 / Qa Salida >       > Parámetros >      > Realizar aprendizaje o ajuste del valor >

                                   Parámetro                      Valor                                      Ajuste de fábrica
                                   Qa 4 mA aprendizaje (auto)    Ajuste del valor analógico                  OD2000-030: -5,00 mm
                                   Qa 4 mA aprendizaje (manual) OD2000-030:                                  OD2000-050: -10,00 mm
                                                                 -5,04 mm ... +5,75 mm                       OD2000-130: -70,70 mm
                                                                 OD2000-050:                                 OD2000-245: -175,00 mm
                                                                 -10,10 mm ... +11,50 mm                     OD2000-350: -250,00 mm
                                                                 OD2000-130:                                 OD2000-700: -500,00 mm
                                                                 -70,70 mm … +76,00 mm
                                   Qa 20 mA aprendizaje (auto)                                               OD2000-030: +5,00 mm
                                                                 OD2000-245:
                                   Qa 20 mA aprendizaje (manual) -176.75 mm ... +189.00 mm                   OD2000-050: +10,00 mm
                                                                                                             OD2000-130: +76,00 mm
                                                                 OD2000-350:
                                                                 -252.50 mm ... +271.00 mm                   OD2000-245: +175,00 mm
                                                                 OD2000-700                                  OD2000-350: +250,00 mm
                                                                 : -505,00 mm ... +550,00 mm                 OD2000-700: +500,00 mm


7.4.4.3            Menú Qa Analógica 0 V ... 10 V
                                   La salida Q2 es una salida de tensión analógica. El valor medido se emite en forma de
                                   valor de tensión linealmente proporcional.



8026228/18SG/2024-12-16 | SICK                                                         B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link   43
Sujeto a cambio sin previo aviso

7 MANEJO

                                         Selección del modo de salida y ajuste de parámetros

                                                 > Salida Q2 / Qa >      > Modo Q2 >      > Qa Analógica 0 V ... 10 V >

                                                 > Q2 / Qa Salida >      > Parámetros >       > Realizar aprendizaje o ajuste del valor >

                                          Parámetro                        Valor                                 Ajuste de fábrica
                                          Qa 0 V aprendizaje (auto)        Ajuste del valor analógico            OD2000-030: -5,00 mm
                                                                           OD2000-030:                           OD2000-050: -10,00 mm
                                          Qa 0 V aprendizaje (manual)
                                                                           -5,04 mm ... +5,75 mm                 OD2000-130: -70,70 mm
                                                                           OD2000-050:                           OD2000-245: -175,00 mm
                                                                           -10,10 mm ... +11,50 mm               OD2000-350: -250,00 mm
                                                                           OD2000-130:                           OD2000-700: -500,00 mm
                                                                           -70,70 mm … +76,00 mm
                                          Qa 10 V aprendizaje (auto)                                             OD2000-030: +5,00 mm
                                                                           OD2000-245:
                                                                                                                 OD2000-050: +10,00 mm
                                          Qa 10 V aprendizaje (manual)     -176,75 mm ... +189,00 mm
                                                                                                                 OD2000-130: +76,00 mm
                                                                           OD2000-350:
                                                                           -252,50 mm ... +271,00 mm             OD2000-245: +175,00 mm
                                                                           OD2000-700:                           OD2000-350: +250,00 mm
                                                                           -505,00 mm ... +550,00 mm             OD2000-700: +500,00 mm


7.4.4.4           Modo de salida Q2
                                         También se pueden configurar funciones de salida digital en lugar de los modos de
                                         salida analógica. La función y las opciones de ajuste son idénticas a las de la salida
                                         Q1, véase "Grupo de menús Q1 Salida", página 34.
                                         Además, la función Q2 Q2=Q1 no está disponible en Q2 (inversión de Q1). Con esta
                                         función, la señal de conmutación invertida de Q1 se emite a través de Q2. Por ejemplo,
                                         si Q1 emite la señal High, Q2 emite Low.

                                         Ajuste de la salida digital

                                                 > Q2 / Qa Salida >      > Q2 Modo >      > Seleccionar modo de salida (conmutación) >


7.4.5             Grupo de menús Entrada IN
                                         Para utilizar las funciones en la Entrada IN, la entrada debe estar activa (cualquier ajuste
                                         excepto Desconexión). El ajuste Desconexión desactiva la entrada y, por tanto, todas las
                                         funciones.

                                         INDICACIÓN
                                         La entrada sólo puede desactivarse a través de la pantalla, SOPAS ET o IO-Link, no a
                                         través de la propia entrada.

                                         El comportamiento de la entrada puede seleccionarse como contacto normalmente
                                         abierto(High-active, ajuste de fábrica) o contacto normalmente cerrado(Low-active).
                                         Cuando se utiliza Emisor desconectado , la lógica determina si la aplicación de una señal
                                         en la entrada hace que el emisor se apague (ajuste de fábrica) o se encienda.

7.4.5.1           Menú Función IN
                                         Funciones
                                         • Conectar y desconectar el emisor con tiempos definidos.
                                         • Activar las funciones del dispositivo.
                                         Transmisor desconectado: el emisor se apaga durante la duración de la señal aplicada.




44        B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                                     8026228/18SG/2024-12-16 | SICK
                                                                                                                              Sujeto a cambio sin previo aviso

MANEJO 7


                                   Ajuste de la Función IN

                                       > Entrada In1 >     > Función IN >     > Seleccionar opción >

                                   Parámetro                     Valor                                             Ajuste de fábrica
                                   Función IN                    Desconexión                                       Transmisor desconectado
                                                                 Retención
                                                                 Aprendizaje punto cero
                                                                 Transmisor desconectado


7.4.5.2            Menú Función de retención IN
                                   Menú Valor medido
                                   Retención del valor medido obtenido con el estado de entrada HIGH (flanco ascen‐
                                   dente).
                                                                    2
                                        1



                                   3 IN HIGH
                                   4 IN LOW
                                   1      Valor medido
                                   2      Valor de retención emitido
                                   3      Estado de entrada HIGH
                                   4      Estado de entrada LOW

                                   Menú Valor de pico
                                   Retención del mayor valor medido presente en el intervalo de tiempo entre el último
                                   flanco descendente y el estado de entrada HIGH (siguiente flanco ascendente).
                                                                         2
                                         1


                                           3
                                   4 IN HIGH
                                   5 IN LOW
                                   1      Valor medido
                                   2      Valor de retención emitido
                                   3      Intervalo de tiempo en el que se realiza el análisis.
                                   4      Estado de entrada HIGH
                                   5      Estado de entrada LOW

                                   Menú Valor de mínimo
                                   Retención del menor valor medido que esté presente en el intervalo de tiempo entre el
                                   último flanco descendente y el estado de entrada HIGH (siguiente flanco ascendente).




8026228/18SG/2024-12-16 | SICK                                                        B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link   45
Sujeto a cambio sin previo aviso

7 MANEJO


                                              1                            2




                                    4 IN HIGH              3                   3
                                    5 IN LOW
                                    1           Valor medido
                                    2           Valor de retención emitido
                                    3           Intervalo de tiempo en el que se realiza el análisis.
                                    4           Estado de entrada HIGH
                                    5           Estado de entrada LOW

                                    Menú Valor de pico a pico
                                    Retención del valor de la diferencia entre el menor y el mayor valor medido que está
                                    presente en el intervalo de tiempo entre el último flanco descendente y el estado de
                                    entrada HIGH (siguiente flanco ascendente).
                                                                       2
                                                              P(1)
                                               1                           P(1)-B(1)            P(2)

                                                                                          P(2)-B(2)
                                                        B(1)
                                                                                   B(2)
                                    4 IN HIGH              3                  3
                                    5 IN LOW
                                    1           Valor medido
                                    2           Valor de retención emitido
                                    3           Intervalo de tiempo en el que se realiza el análisis.
                                    4           Estado de entrada HIGH
                                    5           Estado de entrada LOW

                                    Menú Valor de pico auto
                                    Cuando un estado de entrada HIGH (siguiente flanco ascendente) está presente, rete‐
                                    ner el valor medido mayor.
                                                                                          3
                                           1                                              2



                                    4 IN HIGH
                                    5 IN LOW
                                    1           Valor medido
                                    2           Valor medido interno
                                    3           Valor de retención emitido
                                    4           Estado de entrada HIGH
                                    5           Estado de entrada LOW

                                    Menú Valor de mínimo auto
                                    Cuando un estado de entrada HIGH (siguiente flanco ascendente) está presente, rete‐
                                    ner el valor medido menor.



46   B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                        8026228/18SG/2024-12-16 | SICK
                                                                                                            Sujeto a cambio sin previo aviso

MANEJO 7


                                                                         2
                                       1
                                                                                 3



                                   4 IN HIGH
                                   5 IN LOW
                                   1       Valor medido
                                   2       Valor medido interno
                                   3       Valor de retención emitido
                                   4       Estado de entrada HIGH
                                   5       Estado de entrada LOW

                                   Menú Valor medio
                                   Retención del valor medio de todos los valores medidos que están presentes en el
                                   intervalo de tiempo entre el último flanco descendente y el estado de entrada HIGH
                                   (siguiente flanco ascendente).
                                                                  2
                                           1



                                           3
                                   4 IN HIGH
                                   5 IN LOW
                                   1       Valor medido
                                   2       Valor de retención emitido
                                   3       Intervalo de tiempo en el que se realiza el análisis.
                                   4       Estado de entrada HIGH
                                   5       Estado de entrada LOW

                                   Menú Normal
                                   Retención del valor medido hasta el siguiente flanco descendente.

                                                                      2 3
                                        1




                                   4 IN HIGH

                                   5 IN LOW
                                   1       Valor medido
                                   2       Valor medido interno
                                   3       Valor de retención emitido
                                   4       Estado de entrada HIGH
                                   5       Estado de entrada LOW



8026228/18SG/2024-12-16 | SICK                                                         B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link   47
Sujeto a cambio sin previo aviso

7 MANEJO

                                         Ajuste de la Función de retención IN
                                         Para utilizar la función de retención, ajuste la Función In en Retención.

                                                 > Entrada IN >          > Función IN >        > Retención >

                                         Ajuste la función de retención mediante el parámetro Función de retención IN .

                                              > Entrada IN >             > Función IN >        > Función de retención IN >         > Seleccionar
                                          opción >

                                          Parámetro                            Valor                                    Ajustes predeterminados
                                          Función de retención IN              Valor medido                             Valor medido
                                                                               Valor de pico
                                                                               Valor mínimo
                                                                               Valor de pico a pico
                                                                               Valor de pico auto
                                                                               Valor mínimo auto
                                                                               Promedio
                                                                               Normal


7.4.5.3           Menú Supresión de rebotes IN
                                         Cuando se activa el rebote, la señal de entrada debe estar constantemente presente
                                         en la entrada IN durante 100 ms. Las tolerancias de tiempo de las funciones de
                                         aprendizaje externas tienen en cuenta la activación y desactivación de la función de
                                         supresión de rebotes. No es necesario ajustar los tiempos.

                                         Ajuste de la supresión de rebotes IN

                                                 > Entrada IN >         > Supresión de rebotes IN >     > Seleccionar opción >

                                          Parámetro                            Valor                                    Ajuste de fábrica
                                          Supresión de rebotes IN              No                                       Sí
                                                                               Sí


7.4.5.4           Menú Lógica de entrada IN
                                         El comportamiento de la entrada puede seleccionarse como contacto normalmente
                                         abierto (High-active, ajuste de fábrica) o contacto normalmente cerrado (Low-active).

                                         Ajuste de la Lógica de entrada IN

                                                 > Entrada IN >         > Lógica de entrada IN >      > Seleccionar opción >

                                          Parámetro                            Valor                                    Ajuste de fábrica
                                          Lógica de entrada IN                 High-active                              High-active
                                                                               Low-active


7.4.6             Grupo de menús Dispositivo

7.4.6.1           Restaurar el dispositivo
                                         Vista general
                                         El dispositivo se puede restaurar a los ajustes de fábrica o a los ajustes almacenados
                                         por el cliente. Mientras se restaura el dispositivo, este y sus funciones no estarán
                                         disponibles durante un breve tiempo.
                                         Si se ha realizado alguna calibración, esta función no la restaurará, véase "Menú
                                         Restaurar calibración", página 49.


48        B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                                        8026228/18SG/2024-12-16 | SICK
                                                                                                                                 Sujeto a cambio sin previo aviso

MANEJO 7


                                   Restablecer el dispositivo a los ajustes de fábrica

                                        > Dispositivo >     > Restaurar Ajustes de fábrica >              > Seleccionar opción >

                                   Parámetro                      Valor                                             Ajuste de fábrica
                                   Restaurar Ajustes de           No                                                -
                                   fábrica                        Sí

                                   Restaurar el dispositivo a los ajustes de cliente

                                        > Dispositivo >     > Restaurar Ajustes del cliente >              > Seleccionar opción

                                   Parámetro                      Valor                                             Ajuste de fábrica
                                   Restaurar Ajustes del          No                                                -
                                   cliente                        Sí


7.4.6.2            Menú Restaurar calibración
                                   Resumen
                                   La calibración puede restaurarse a sus ajustes de fábrica. La función Restaurar disposi‐
                                   tivo no restaura las calibraciones ya realizadas.

                                   Restaurar calibración

                                        > Dispositivo >    > Restaurar calibración >     > Seleccionar opción >

                                   Parámetro                      Valor                                             Ajuste de fábrica
                                   Restaurar calibración          No                                                -
                                                                  Sí


7.4.6.3            Menú Guardar ajustes del cliente
                                   Los ajustes realizados pueden guardarse como ajustes de cliente. Estos ajustes pue‐
                                   den restaurarse en cualquier momento, véase "Restaurar el dispositivo", página 48.

                                        > Dispositivo >     > Guardar ajustes del cliente >             > Seleccionar opción >

                                   Parámetro                      Valor                                             Ajuste de fábrica
                                   Guardar ajustes del cliente No                                                   -
                                                               Sí


7.4.6.4            Menú Idioma
                                   Puede definirse el idioma de los textos de la pantalla.

                                        > Dispositivo >     > Idioma >

                                   Parámetro                      Valor                                             Ajuste de fábrica
                                   Idioma                         English                                           English
                                                                  German
                                                                  Spanish
                                                                  Japanese
                                                                  Chinese


7.4.6.5            Configuración de la pantalla
                                   Existen distintos ajustes para el comportamiento de la pantalla.

                                        > Dispositivo >    > Configuración de la pantalla >


8026228/18SG/2024-12-16 | SICK                                                         B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link   49
Sujeto a cambio sin previo aviso

7 MANEJO

                                          Parámetro                             Valor                                           Ajuste de fábrica
                                          Decimales en pantalla                 0, 0,1, 0,01                                    0,1
                                          Modo Eco                              Desc., 10 s, 20 s, 60 s, 300 s, 1.200 s,        300 s
                                                                                3.600 s
                                          Brillo de pantalla                    10%, 20%, 30%, 40%, 50%, 60%, 70%,              30%
                                                                                80%, 90%, 100%
                                          Girar pantalla                        0°, 180°                                        0°


7.4.6.6           Menú Emisor
                                         El emisor (láser de medición) puede desconectarse. No es posible realizar ninguna
                                         medición con el emisor apagado.
                                         El emisor también puede encenderse y apagarse a través de la entrada IN.

                                                 > Dispositivo >         > Emisor >        > Seleccionar opción >

                                          Parámetro                             Valor                                           Ajuste de fábrica
                                          Emisor                                Apagado                                         Encendido
                                                                                Encendido


7.4.6.7           Menú Salida PNP/NPN/PP
                                         La lógica de salida sólo puede ajustarse a través de la pantalla. El ajuste NPN es
                                         incompatible con la mayoría de los componentes IO-Link Master disponibles en el
                                         mercado.

                                                 > Dispositivo >         > Salida PNP/NPN/PP >         > Seleccionar opción >

                                          Parámetro                                Valor                                   Ajuste de fábrica
                                          Salida PNP/NPN/PP                        PNP                                     PP
                                                                                   NPN
                                                                                   PP


7.4.6.8           Menú Ajuste del Device-ID
                                         El dispositivo admite múltiples Device-ID a partir de la versión de firmware 0100_0042.
                                         La Device-ID puede definirse para garantizar la compatibilidad del dispositivo cuando
                                         este se integra en una aplicación existente.

                                                 > Dispositivo >         > Ajuste del Device-ID >      > Seleccionar opción >

                                          Parámetro                             Valor                                           Ajuste de fábrica
                                          Ajuste del Device-ID                  8389374                                         en función de la versión de
                                                                                8389425                                         firmware


7.4.7             Grupo de menús Info
                                         Información de estado
                                          • Referencia
                                          • Número de serie
                                          • Versión de firmware
                                          • Horas de trabajo sensor
                                          • Horas de funcionamiento emisor
                                          • Número de errores
                                          • Historial de fallos
                                                 > Info >           > Información de estado


50        B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                                                 8026228/18SG/2024-12-16 | SICK
                                                                                                                                          Sujeto a cambio sin previo aviso

MANTENIMIENTO 8


8                  Mantenimiento
8.1                Limpieza

                                   IMPORTANTE
                                   Daños en el dispositivo por una limpieza incorrecta
                                   Una limpieza incorrecta puede provocar daños en el dispositivo.
                                   ■    Utilice exclusivamente los equipos y productos de limpieza recomendados.
                                   ■    No utilizar objetos en punta para realizar la limpieza.

                                   ►    Limpieza en intervalos regulares y en caso de suciedad de la pantalla frontal con
                                        un paño para ópticas que no deje pelusas y detergente para plásticos. El intervalo
                                        de limpieza depende fundamentalmente de las condiciones del entorno.

8.2                Plan de mantenimiento
                                   El dispositivo trabaja en funcionamiento continuo sin necesidad de mantenimiento.
                                   En función del lugar de uso puede ser necesario realizar en el dispositivo en intervalos
                                   regulares los siguientes trabajos de mantenimiento preventivos:
                                   Tabla 7: Plan de mantenimiento
                                   Tarea de mantenimiento                Intervalo                                               Debe realizarse
                                                                                                                                 por
                                   Comprobar regularmente el disposi‐    En función de las condiciones del                       Personal especia‐
                                   tivo y los cables de conexión para    entorno y del clima.                                    lizado
                                   descartar daños.
                                   Limpiar la carcasa el visor de ven‐   En función de las condiciones del                       Personal especia‐
                                   tana.                                 entorno y del clima.                                    lizado
                                   Comprobar las uniones roscadas y      En función del lugar de uso, de las                     Personal especia‐
                                   las conexiones enchufables.           condiciones del entorno o de las                        lizado
                                                                         especificaciones operativas. Reco‐
                                                                         mendado: al menos cada 6 meses.
                                   Comprobar si todas las conexiones     En función de las condiciones del                       Personal especia‐
                                   no utilizadas están cerradas con      entorno y del clima. Recomendado:                       lizado
                                   tapas protectoras.                    al menos cada 6 meses.




8026228/18SG/2024-12-16 | SICK                                                       B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link   51
Sujeto a cambio sin previo aviso

9 RESOLUCIÓN DE AVERÍAS


9             Resolución de averías
9.1           Fallos
                                     En la siguiente tabla se describen los posibles fallos y las medidas para solucionarlos.
                                     Póngase en contacto con el servicio técnico de SICK en caso de que se produzcan
                                     fallos que no puedan ser subsanados según la siguiente descripción. Para ponerse en
                                     contacto con su representante competente, véase la última página de este documento.

                                     INDICACIÓN
                                     Para que la gestión se desarrolle con rapidez, antes de llamar por teléfono, anote los
                                     datos de la placa de características como la clave de tipos, el número de serie, etc.

                                     Los fallos generales se dividen en advertencias y errores. Si hay advertencias se siguen
                                     emitiendo los valores medidos actuales; si hay errores, ya no es posible la medición.

                                     Tabla 8: Preguntas y respuestas sobre la solución de problemas
                                      Pregunta / Estado                      Respuesta / Medidas correctivas
                                      El dispositivo no muestra una medi‐    • Emisor no activado: conecte el emisor, véase "Menú
                                      ción o la medición no es posible.          Emisor", página 50.
                                                                             • El spot láser no está dirigido al objeto: compruebe la
                                                                                 alineación del dispositivo y corríjala si es necesario.
                                                                             • Asegúrese de que el recorrido de la luz esté despe‐
                                                                                 jado.
                                                                             •   Asegúrese de que el objeto está dentro del campo de
                                                                                 medición.
                                                                             •   Asegúrese de que el elemento receptor del disposi‐
                                                                                 tivo recibe suficiente luz.
                                                                             •   Superficies reflectantes: compruebe el estado de la
                                                                                 superficie.
                                      Entorno perturbado por la compatibi‐ Recomendación: utilice la salida de datos a través de
                                      lidad electromagnética               IO-Link.
                                                                           Si los valores medidos deben emitirse a través de la
                                                                           salida analógica, utilice una salida de corriente analó‐
                                                                           gica. La salida de corriente analógica es mucho menos
                                                                           susceptible a las interferencias electromagnéticas que
                                                                           una salida de tensión.


9.2           Información para el servicio
                                     Si hay que ponerse en contacto con el servicio de SICK, recoja de antemano la
                                     siguiente información del dispositivo y anótela:
                                      •       Información sobre la versión de firmware
                                      •       Información del hardware
                                      •       Información de las horas de funcionamiento
                                     Estos datos pueden consultarse a través de la pantalla.

9.3           Devolución
                                     ►        No envíe los dispositivos sin haberlo consultado con el servicio técnico de SICK.
                                     ►        Envíe el dispositivo exclusivamente en el embalaje original o en un embalaje
                                              acolchado similar.




52    B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                               8026228/18SG/2024-12-16 | SICK
                                                                                                                    Sujeto a cambio sin previo aviso

RESOLUCIÓN DE AVERÍAS 9


                                   INDICACIÓN
                                   Para una gestión eficiente y una localización rápida de la causa, adjunte al envío de
                                   devolución lo siguiente:
                                   •    Datos de una persona de contacto
                                   •    descripción de la aplicación
                                   •    Descripción del error acontecido


9.4                Reparación
                                   Las reparaciones en el dispositivo deben realizarse únicamente por personal de
                                   SICK AG con la debida formación y autorización. Si el cliente realiza intervenciones
                                   o modificaciones en el dispositivo, quedará anulado cualquier derecho de garantía
                                   otorgado por SICK AG.

9.5                Eliminación
                                   Todos los dispositivos que ya no puedan utilizarse deben eliminarse de forma respe‐
                                   tuosa con el medio ambiente según las normativas aplicables sobre eliminación de
                                   residuos de cada país. No elimine el producto con los residuos domésticos.

                                   IMPORTANTE
                                   Peligro medioambiental debido a la eliminación indebida del dispositivo
                                   La eliminación indebida del dispositivo puede provocar daños medioambientales.
                                   Por ese motivo debe observar las siguientes indicaciones:
                                   ■    Debe respetarse siempre la normativa medioambiental vigente en su país.
                                   ■    Clasificar los materiales según el tipo y entregarlos en un punto de reciclaje.




8026228/18SG/2024-12-16 | SICK                                                   B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link   53
Sujeto a cambio sin previo aviso

10 DATOS TÉCNICOS


10             Datos técnicos
10.1           Sistema mecánico y eléctrico
                                       Tensión de ali‐               CC 18 V ... 24 V, ± 10%, incluida la ondulación residual 1)
                                       mentación Vs
                                       Consumo de                    < 1,5 W (con 24 V CC) 2)
                                       potencia
                                       Tiempo de cone‐               Máx. 300 ms
                                       xión
                                       Tiempo de preca‐ < 30 minutos 3)
                                       lentamiento
                                       Material de la                Plástico (PBT)
                                       carcasa
                                       Material de los               Plástico (PMMA)
                                       visores de ven‐
                                       tana
                                       Tipo de conexión              Cable con conector macho, M12, 5 polos, codificación A, 30 cm
                                       Par de apriete de Máx. 0,8 Nm
                                       los tornillos de
                                       fijación
                                       Indicación                    Pantalla OLED, LED de estado
                                       Elementos de                  4 teclas
                                       mando
                                       Peso                          90 g
                                       Dimensiones (An 27 mm x 60 mm x 50 mm
                                       x Al x P)
                                       Grado de protec‐              IP67
                                       ción
                                       Clase de protec‐              III (EN 50178)
                                       ción
                                       Seguridad eléc‐               IEC 61010-1 AMD 1:2016-12
                                       trica
                                      1)    Valores límite, protegido contra polarización inversa.
                                      2)    Sin carga, a +20 °C.
                                      3)    En la fase de calentamiento del dispositivo, los valores medidos están sujetos a una gran variancia
                                            (desviación de temperatura).


10.2           Rendimiento
                                       Campo de medi‐                OD2000-030xxxx: 25 mm … 35 mm
                                       ción 1)                       OD2000-050xxxx: 40 mm … 60 mm
                                                                     OD2000-130xxxx: 60 mm … 200 mm
                                                                     OD2000-245xxxx: 70 mm … 420 mm
                                                                     OD2000-350xxxx: 100 mm … 600 mm
                                                                     OD2000-700xxxx: 200 mm … 1.200 mm
                                       Objeto de medi‐               Objetos naturales
                                       ción




54     B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                                         8026228/18SG/2024-12-16 | SICK
                                                                                                                               Sujeto a cambio sin previo aviso

DATOS TÉCNICOS 10


                                    Repetibili‐           OD2000-030xxxx: 0,1 µm
                                    dad 2) 3) 4)          OD2000-050xxxx: 0,2 µm
                                                          OD2000-130xxxx: 4 µm
                                                          OD2000-245xxxx: 10 µm
                                                          OD2000-350xxxx: 20 µm
                                                          OD2000-700xxxx: 100 µm
                                    Linealidad 2) 4) 5)   OD2000-030xxxx: ± 10 µm
                                                          OD2000-050xxxx: ± 20 µm
                                                          OD2000-130xxxx: ± 140 µm
                                                          OD2000-245xxxx: ± 350 μm
                                                          OD2000-350xxxx: ± 500 μm
                                                          OD2000-700xxxx: ± 1 mm (200 mm ... 700 mm), ± 3 mm (700 mm ...
                                                          1.200 mm)
                                    Frecuencia de         ≤ 7,5 kHz
                                    medición
                                    Tiempo de salida ≥ 0,133 ms
                                    Tiempo de res‐        ≥ 0,533 ms 6)
                                    puesta
                                    Emisor de luz         Láser rojo
                                                          Luz roja visible
                                    Clase de láser        OD2000-030, OD2000-050xxxx, OD2000-130xxxx: clase de láser 1
                                                          (IEC 60825-1:2014, EN 60825-1:2014) 7)
                                                          OD2000-245xxxx, OD2000-350xxxx, OD2000-700xxxx: clase de láser 2
                                                          (IEC 60825-1:2014, EN 60825-1:2014) 8)
                                                          Se corresponde con 21 CFR 1040.10 y 1040.11 a excepción de la confor‐
                                                          midad con IEC 60825-1 ed. 3, como se describe en el documento Laser
                                                          Notice No. 56 de 8 de mayo de 2019.
                                    Tamaño típico         OD2000-030xxxx: Ø 50 µm (30 mm)
                                    del spot              OD2000-050xxxx: Ø 70 µm (50 mm)
                                                          OD2000-130xxxx: Ø 300 μm (130 mm)
                                                          OD2000-245xxxx: Ø 500 µm (245 mm)
                                                          OD2000-350xxxx: Ø 600 µm (350 mm)
                                                          OD2000-700xxxx: Ø 1 mm (700 mm)
                                    Función adicional Funciones de registro de valores medidos y funciones de evaluación, filtro
                                                      de promedios y filtro de mediana ajustables, modos de punto de conmuta‐
                                                      ción: punto único SP1 (DtO) / ventana SP1, SP2 (ventana u ObSB) / apren‐
                                                      dizaje de la salida digital, inversión de la salida digital, aprendizaje de la
                                                      salida analógica 9), inversión de la salida analógica 9), salida analógica con‐
                                                      mutable (mA/V) 9), entrada multifunción: emisor desconectado/funciones
                                                      de retención/desactivado, desconectar pantalla, bloqueo de las teclas de
                                                      mando, pantalla de indicación giratoria 180°, función de alarma, salto de
                                                      la altura del borde, modo temporizador (retardo de conexión/desconexión,
                                                      impulso)
                                   1)   6% ... 90% de reflectividad difusa con los ajustes predeterminados.
                                   2)   Medición al 60% de reflectividad difusa (cerámica, blanco).
                                   3)   Ajuste del valor promedio: 512
                                        Mediana: 31
                                        Frecuencia de medición: 5 kHz
                                        En el centro del campo de medición
                                        Para la medición estática.
                                   4)   Con T = 25 °C y condiciones generales constantes.
                                   5)   Tenga en cuenta el tiempo mínimo de precalentamiento de 30 minutos.
                                   6)   En función del cálculo de valor promedio o la sensibilidad definidos.
                                   7)   Visible, longitud de onda: 655 nm, potencia máxima: 0,39 mW, potencia máxima de impulso: 0,39 mW,
                                        duración máxima de impulso: 5 ms.
                                   8)   Visible, longitud de onda: 655 nm, potencia máxima: 1 mW, potencia máxima de impulso: 1 mW,
                                        duración máxima de impulso: 5 ms.
                                   9)   No se aplica a productos sin salida analógica.



8026228/18SG/2024-12-16 | SICK                                                          B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link   55
Sujeto a cambio sin previo aviso

10 DATOS TÉCNICOS

10.3           Interfaces
                                       IO-Link                       IO-Link V1.1
                                                                     Función: datos de proceso, parametrización, diagnóstico, almacenamiento
                                                                     de datos
                                                                     Velocidad de transmisión de datos: 230,4 kBit/s (COM3), longitud de datos
                                                                     de proceso 6 bytes, tiempo de ciclo mínimo 1 ms
                                       Entrada digital               In1 1)
                                       salida digital                Cantidad: 2 2)
                                                                     Tipo: contrafase / PNP/NPN, seleccionable
                                                                     Intensidad máxima de salida IA: 100 mA
                                       Salida analó‐                 Cantidad: 1
                                       gica 3)                       Tipo: salida de corriente / salida de tensión
                                                                     Función: seleccionable
                                                                     Corriente: 4 mA ... 20 mA, ≤ 300 W
                                                                     Tensión: 0 V ... 10 V, > 10 kW
                                                                     Resolución: 16 bits
                                      1)    Puede utilizarse como emisor desconectado, activación de funciones de retención o desactivado.
                                      2)    PNP/PP: HIGH = UV > 13,5 V / LOW = UV < 8 V.
                                            NPN: HIGH = UV < 8 V/LOW = UV > 13,5 V.
                                      3)    No se aplica a productos sin salida analógica.


10.4           Datos del entorno
                                       Temperatura      –10 °C … +50 °C 1)
                                       ambiente de ser‐
                                       vicio
                                       Temperatura de –20 °C … +60 °C
                                       almacenamiento
                                       Humedad rela‐                 35 % ... 85 %
                                       tiva del aire (sin
                                       condensación)
                                       Desviación de                 OD2000-030xxxx: ± 6 μm/K
                                       temperatura                   OD2000-050xxxx: 12 µm/K
                                                                     OD2000-130xxxx: 84 µm/K
                                                                     OD2000-245xxxx: 210 μm/K
                                                                     OD2000-350xxxx: 300 μm/K
                                                                     OD2000-700xxxx: 600 µm/K
                                       Insensibilidad                Luz artificial: ≤ 3.000 lx 2)
                                       típica a la luz               Luz solar: ≤ 10.000 lx
                                       ambiental
                                       Resistencia a                 EN 60068-2-6, EN 60068-2-64
                                       oscilaciones
                                       Resistencia a                 EN 60068-2-27
                                       choque
                                      1)    Temperatura de servicio con UV = 24 V.
                                      2)    Con desplazamiento continuo del objeto en el campo de medición.




56     B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                                     8026228/18SG/2024-12-16 | SICK
                                                                                                                           Sujeto a cambio sin previo aviso

DATOS TÉCNICOS 10


10.5               Rango de interferencia
                                   OD2000-030xxxx


                                                                                          5.5 (0.22)
                                                            4 (0.16)




                                                                                                           Dimensions in mm (inch)
                                                                       12

                                                                                                       3
                                       Q1

                                    Q2⁄QA

                                              PWR




                                                                       14.5 (0.57)
                                                            4 (0.16)
                                                                                         5.5 (0.22)
                                            40 (1.57)
                                                        0 4
                                                    Distance in mm (inch)




                                                                             12 (0.47)
                                                         2

                                                                                         10.5 (0.41)



                                                                                                           Dimensions in mm (inch)
                                                                                                       3


                                                         10 (0.39)
                                                                            1
                                            20 (0.79)
                                            40 (1.57)
                                                        0 4
                                                    Distance in mm (inch)

                                   Figura 19: Rango de interferencia Od2000-030xxxx, unida unidad de medida: mm (pulgadas),
                                   separador decimal: punto
                                   1          Eje óptico del emisor y el receptor
                                   2          Rango de interferencia
                                   3          Medidas en mm (pulg.)
                                   4          Distancia en mm (pulg.)




8026228/18SG/2024-12-16 | SICK                                                                                                       B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link   57
Sujeto a cambio sin previo aviso

10 DATOS TÉCNICOS

                                    OD2000-050xxxx


                                                                                                       6.5 (0.26)
                                                            4 (0.16)




                                                                                                                            Dimensions in mm (inch)
                                                                           1                       2
                                        Q1

                                       Q2⁄QA

                                                PWR
                                                                                                                    3


                                                                             14.5 (0.57)
                                                            4 (0.16)
                                                                                                       6.5 (0.26)
                                                                         70 (2.76)
                                                           0       4
                                                           Distance in mm (inch)




                                                                                     16.5 (0.65)




                                                                                                                        Dimensions in mm (inch)
                                                                                                       15 (0.59)

                                                                                                                    3

                                                             10 (0.39)   1                     2
                                               35 (1.38)
                                                                         70 (2.76)
                                                           0       4
                                                           Distance in mm (inch)

                                    Figura 20: Rango de interferencia Od2000-050xxxx, unida unidad de medida: mm (pulgadas),
                                    separador decimal: punto
                                    1            Eje óptico del emisor y el receptor
                                    2            Rango de interferencia
                                    3            Medidas en mm (pulg.)
                                    4            Distancia en mm (pulg.)




58   B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                                                                      8026228/18SG/2024-12-16 | SICK
                                                                                                                                                          Sujeto a cambio sin previo aviso

DATOS TÉCNICOS 10


                                   OD2000-130xxxx


                                                             12.5 (0.49)
                                                                                                                                                  13 (0.51)




                                                                                                                                                                              Dimensions in mm (inch)
                                                                                       1                   2

                                        Q1

                                       Q2⁄QA
                                                                                                                                                                          3
                                               PWR




                                                                                                   250 (9.84)
                                                                                                     4 Distance in mm (inch)                      13 (0.51)


                                                                                       26 (1.02)


                                                                                                                                                              68 (2.68)




                                                                                                                                                                              Dimensions in mm (inch)
                                                       10 (0.39)                1
                                                                                                     2                                                                    3
                                                                           50 (1.97)




                                                                                                   250 (9.84)
                                                                                                     4 Distance in mm (inch)
                                   Figura 21: Rango de interferencia Od2000-130xxxx, unida unidad de medida: mm (pulgadas),
                                   separador decimal: punto
                                   1           Eje óptico del emisor y el receptor
                                   2           Rango de interferencia
                                   3           Medidas en mm (pulg.)
                                   4           Distancia en mm (pulg.)




8026228/18SG/2024-12-16 | SICK                                                                              B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                 59
Sujeto a cambio sin previo aviso

10 DATOS TÉCNICOS

                                    OD2000-245xxxx

                                                             4 (0.16)




                                                                                                                                                                          Dimensions in mm (inch)
                                                                                                                                            20 (0.79)



                                                                                                                                                                      3
                                        Q1

                                       Q2⁄QA

                                               PWR




                                                                              14.5 (0.57)
                                                                                                                                            20 (0.79)

                                                             4 (0.16)
                                                                                                         1      2

                                                         0                                              4 Distance in mm (inch)                      460 (18.11)



                                                                                            28 (1.10)




                                                                                                                                                                          Dimensions in mm (inch)
                                                             10 (0.39)
                                                                                                                                                         108 (4.25)
                                                                                                                                                                      3
                                                                                                         1      2
                                                                         60 (2.36)


                                                         0                                              4 Distance in mm (inch)                      460 (18.11)

                                    Figura 22: Rango de interferencia Od2000-245xxxx, unida unidad de medida: mm (pulgadas),
                                    separador decimal: punto
                                    1           Eje óptico del emisor y el receptor
                                    2           Rango de interferencia
                                    3           Medidas en mm (pulg.)
                                    4           Distancia en mm (pulg.)




60   B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                                                  8026228/18SG/2024-12-16 | SICK
                                                                                                                                      Sujeto a cambio sin previo aviso

DATOS TÉCNICOS 10


                                   OD2000-350xxxx

                                                      4 (0.16)




                                                                                                                                                                                            Dimensions in mm (inch)
                                                                                                                                                           27 (1.06)



                                                                                                                                                                                        3
                                       Q1

                                    Q2⁄QA

                                            PWR




                                                                       14.5 (0.57)
                                                                                                                                                           27 (1.06)

                                                      4 (0.16)
                                                                                                  1      2

                                                  0                                              4 Distance in mm (inch)                                             660 (25.98)



                                                                                     30 (1.18)




                                                                                                                                                                                            Dimensions in mm (inch)
                                                      10 (0.39)
                                                                                                                                                                           132 (5.20)
                                                                                                                                                                                        3
                                                                                                  1      2
                                                                  90 (3.54)


                                                  0                                              4 Distance in mm (inch)                                             660 (25.98)

                                   Figura 23: Rango de interferencia Od2000-350xxxx, unidad de medida de la distancia: mm
                                   (pulgadas), separador decimal: punto
                                   1        Eje óptico del emisor y el receptor
                                   2        Rango de interferencia
                                   3        Medidas en mm (pulg.)
                                   4        Distancia en mm (pulg.)




8026228/18SG/2024-12-16 | SICK                                                                               B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                    61
Sujeto a cambio sin previo aviso

10 DATOS TÉCNICOS

                                    OD2000-700xxxx

                                                             4 (0.16)




                                                                                                                                                                      Dimensions in mm (inch)
                                                                                                                                        53 (2.09)



                                                                                                                                                                  3
                                        Q1

                                       Q2⁄QA

                                               PWR




                                                                          14.5 (0.57)
                                                                                                                                        53 (2.09)

                                                             4 (0.16)
                                                                                                     1      2

                                                         0                                          4 Distance in mm (inch)                    1400 (55.12)



                                                                                        32 (1.26)




                                                                                                                                                                      Dimensions in mm (inch)
                                                             10 (0.39)
                                                                                                                                                     172 (6.77)
                                                                                                                                                                  3
                                                                                                     1      2
                                                                    180 (7.09)


                                                         0                                          4 Distance in mm (inch)                    1400 (55.12)

                                    Figura 24: Rango de interferencia Od2000-700xxxx, unidad de medida de la distancia: mm
                                    (pulgadas), separador decimal: punto
                                    1           Eje óptico del emisor y el receptor
                                    2           Rango de interferencia
                                    3           Medidas en mm (pulg.)
                                    4           Distancia en mm (pulg.)




62   B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                                              8026228/18SG/2024-12-16 | SICK
                                                                                                                                  Sujeto a cambio sin previo aviso

DATOS TÉCNICOS 10


10.6               Dibujo acotado
                                                     50 (1.97)                                                               27 (1.06)
                                    4.5                                                                                             12.5
                                   (0.18)       25.4 (1.00)                                                                            (0.49)

                                   1                                                                                                                                           4

                                                                                                                                                                               5
                                                                            2x Ø 4.5                                                                                           6
                                                                               (0.18) 1

                                                                                                      55.3 (2.18)

                                                                                       50.8 (2.00)     60 (2.36)                                                               28.3 (1.11)


                                                                                                                                                                 25.8 (1.02)
                                                                                                                                                                                  34 (1.34)
                                                                                                                                                                                 35.3 (1.39)
                                                                                                                                                                                 36.5 (1.44)
                                                                                                                                                 10   (0.39)

                                   2                                                                                                                                    7
                                                                                       (0 4.
                                                                                   Ø     .1 5
                                                                                           8)                                                                           8
                                                                                                                                                                        9
                                                                                                                      3




                                   Figura 25: estructura y dimensiones del dispositivo, unidad de medida: mm (pulg.), separador
                                   decimal: punto
                                   1        Orificios de fijación (M4)
                                   2        Punto cero del dispositivo (distancia = 0 mm)
                                   3        Cable de dispositivo (longitud 300 mm) con conector macho M12 de 5 polos, codificación
                                            A
                                   4        Centro del eje óptico, receptor (tipo de dispositivo OD2000-350, OD2000-700)
                                   5        Centro del eje óptico, receptor (tipo de dispositivo OD2000-245)
                                   6        Centro del eje óptico, receptor (tipo de dispositivo OD2000-130)
                                   7        Centro del eje óptico, receptor (tipo de dispositivo OD2000-050)
                                   8        Centro del eje óptico, receptor (tipo de dispositivo OD2000-030)
                                   9        Centro del eje óptico, emisor


10.7               Tamaño del spot
                                   OD2000-030xxxx


                                                          Ø 120 µm                                    Ø 50 µm                                         Ø 150 µm




                                                 0      25 (0.98)                                30 (1.18)                                        35 (1.38)

                                   Figura 26: Tamaño típico del spot OD2000-030xxxx, unidad de medida de la distancia: mm
                                   (pulgadas), separador decimal: punto




8026228/18SG/2024-12-16 | SICK                                                                       B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                         63
Sujeto a cambio sin previo aviso

10 DATOS TÉCNICOS

                                    OD2000-050xxxx


                                                                     Ø 100 µm            Ø 70 µm                         Ø 250 µm




                                                        0          40 (1.57)           50 (1.97)                       60 (2.36)

                                    Figura 27: Tamaño típico del spot OD2000-050xxxx, unidad de medida de la distancia: mm
                                    (pulgadas), separador decimal: punto

                                    OD2000-130xxxx



                                                                       Ø 0.7 (0.03)            Ø 0.3 (0.01)                          Ø 0.5 (0.02)




                                                         0          60 (2.36)          130 (5.12)                        200 (7.87)

                                    Figura 28: Tamaño típico del spot OD2000-130xxxx, unidad de medida de la distancia: mm
                                    (pulgadas), separador decimal: punto

                                    OD2000-245xxxx


                                                                     Ø 600 µm            Ø 500 µm                        Ø 800 µm




                                                        0          70 (2.76)          245 (9.65)                     420 (16.54)

                                    Figura 29: Tamaño típico del spot OD2000-245xxxx, unidad de medida de la distancia: mm
                                    (pulgadas), separador decimal: punto

                                    OD2000-350xxxx


                                                                     Ø 700 µm            Ø 600 µm                        Ø 1000 µm




                                                        0          100 (3.94)         350 (13.78)                    600 (23.62)

                                    Figura 30: Tamaño típico del spot OD2000-350xxxx, unidad de medida de la distancia: mm
                                    (pulgadas), separador decimal: punto




64   B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                              8026228/18SG/2024-12-16 | SICK
                                                                                                                  Sujeto a cambio sin previo aviso

DATOS TÉCNICOS 10


                                   OD2000-700xxxx


                                                                 Ø 600 µm                                 Ø 1000 µm                                      Ø 1600 µm




                                                    0      200 (7.87)                                  700 (27.56)                                 1200 (47.24)

                                   Figura 31: Tamaño típico del spot OD2000-700xxxx, unidad de medida de la distancia: mm
                                   (pulgadas), separador decimal: punto


10.8               Diagramas de linealidad
                                   OD2000-030xxxx
                                               Typical linearity deviation in mm (inch) 1
                                        0.06
                                    (0.0023)


                                        0.04
                                    (0.0015)


                                        0.02
                                    (0.0007)
                                                                                                  4                              5
                                                                 3
                                         0.0


                                       –0.02
                                   (–0.0007)


                                       –0.04
                                   (–0.0015)


                                       –0.06
                                   (–0.0023)
                                               25        26                  27       28       29         30           31           32            33                  34       35
                                           (0.98)       (1.02)              (1.06)   (1.10)   (1.14)     (1.18)       (1.22)      (1.26)        (1.30)               (1.34)   (1.38)

                                                                                                                                            Distance in mm (inch) 2

                                   1       Desviación de la linealidad típica en mm (pulg.)
                                   2       Distancia en mm (pulg.)
                                   3       Blanco, 60% de reflectividad
                                   4       Negro 9,5% de reflectividad
                                   5       Acero inoxidable




8026228/18SG/2024-12-16 | SICK                                                                           B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link              65
Sujeto a cambio sin previo aviso

10 DATOS TÉCNICOS

                                    OD2000-050xxxx
                                                  Typical linearity deviation in mm (inch) 1
                                          0.06
                                      (0.0023)

                                          0.04
                                      (0.0015)

                                          0.02
                                      (0.0007)                                                             4
                                                                                              3
                                            0.0

                                        –0.02                                                              5
                                    (–0.0007)

                                        –0.04
                                    (–0.0015)


                                        –0.06
                                    (–0.0023)
                                                  40          42       44       46       48        50       52       54           56          58         60
                                               (1.57)        (1.65)   (1.73)   (1.81)   (1.89)    (1.97)   (2.05)   (2.13)      (2.20)      (2.28)      (2.36)
                                                                                                                             Distance in mm (inch) 2

                                    1           Desviación de la linealidad típica en mm (pulg.)
                                    2           Distancia en mm (pulg.)
                                    3           Blanco, 60% de reflectividad
                                    4           Negro 9,5% de reflectividad
                                    5           Acero inoxidable




66   B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                                             8026228/18SG/2024-12-16 | SICK
                                                                                                                                 Sujeto a cambio sin previo aviso

DATOS TÉCNICOS 10


                                   OD2000-130xxxx
                                               Typical linearity deviation in mm (inch) 1
                                      0.3
                                   (0.01)



                                      0.2
                                   (0.01)


                                                                                                                    5
                                      0.1
                                                                    3                         4

                                      0.0



                                     -0.1



                                     -0.2
                                   (-0.01)



                                     -0.3
                                   (-0.01)
                                              60           80           100           120           140                160                180               200
                                             (2.36)       (3.15)        (3.94)       (4.72)        (5.51)             (6.30)             (7.09)             (7.87)

                                                                                                                               Distance in mm (inch) 2

                                   1           Desviación de la linealidad típica en mm (pulg.)
                                   2           Distancia en mm (pulg.)
                                   3           Blanco, 60% de reflectividad
                                   4           Negro 9,5% de reflectividad
                                   5           Acero inoxidable




8026228/18SG/2024-12-16 | SICK                                                                B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link            67
Sujeto a cambio sin previo aviso

10 DATOS TÉCNICOS

                                    OD2000-245xxxx
                                                Typical linearity deviation in mm (inch) 1
                                        3.0
                                     (0.12)



                                        2.0
                                     (0.08)



                                        1.0
                                     (0.04)
                                                                                                                     4             5
                                                                                                             3
                                        0.0



                                       -1.0
                                    (-0.04)



                                       -2.0
                                    (-0.08)



                                       -3.0
                                    (-0.12)
                                               70                  120   170           220      270       320              370              420
                                              (2.76)           (4.72)    (6.69)       (8.66)   (10.63)   (12.60)         (14.57)           (16.54)

                                                                                                                Distance in mm (inch) 2

                                    1           Desviación de la linealidad típica en mm (pulg.)
                                    2           Distancia en mm (pulg.)
                                    3           Blanco, 60% de reflectividad
                                    4           Negro 9,5% de reflectividad
                                    5           Acero inoxidable




68   B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                                   8026228/18SG/2024-12-16 | SICK
                                                                                                                       Sujeto a cambio sin previo aviso

DATOS TÉCNICOS 10


                                   OD2000-350xxxx
                                               Typical linearity deviation in mm (inch) 1

                                      3.0
                                   (0.12)


                                      2.0
                                   (0.08)


                                      1.0
                                   (0.04)                                                                                                  4
                                                                                                                            3                        5
                                      0.0


                                     -1.0
                                   (-0.04)


                                     -2.0
                                   (-0.08)


                                     -3.0
                                   (-0.12)
                                             100       150      200       250      300       350         400          450           500          550          600
                                             (3.94)   (5.91)   (7.87)    (9.84)   (11.81)   (13.78)    (15.75)      (17.72)       (19.69)      (21.65)       (23.62)

                                                                                                                               Distance in mm (inch) 2

                                   1           Desviación de la linealidad típica en mm (pulg.)
                                   2           Distancia en mm (pulg.)
                                   3           Blanco, 60% de reflectividad
                                   4           Negro 9,5% de reflectividad
                                   5           Acero inoxidable




8026228/18SG/2024-12-16 | SICK                                                                 B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link             69
Sujeto a cambio sin previo aviso

10 DATOS TÉCNICOS

                                    OD2000-700xxxx
                                                Typical linearity deviation in mm (inch) 1
                                        5.0
                                     (0.20)

                                        4.0
                                     (0.16)


                                        3.0
                                     (0.12)

                                        2.0
                                                                                                                          5
                                     (0.08)
                                                                                                  4
                                        1.0
                                     (0.04)                                         3
                                        0.0


                                       -1.0
                                    (-0.04)

                                       -2.0
                                    (-0.08)


                                       -3.0
                                    (-0.12)

                                       -4.0
                                    (-0.16)

                                       -5.0
                                    (-0.20)
                                              200         300       400       500        600           700       800          900     1000       1100        1200
                                              (7.87)     (11.81)   (15.75)   (19.69)    (23.62)       (27.56)   (31.50)   (35.43)     (39.37)    (43.31)    (47.24)
                                                                                                                                    Distance in mm (inch) 2

                                    1           Desviación de la linealidad típica en mm (pulg.)
                                    2           Distancia en mm (pulg.)
                                    3           Blanco, 60% de reflectividad
                                    4           Negro 9,5% de reflectividad
                                    5           Acero inoxidable




70   B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                                                     8026228/18SG/2024-12-16 | SICK
                                                                                                                                         Sujeto a cambio sin previo aviso

ACCESORIOS 11


11                 Accesorios

                                   INDICACIÓN
                                   En la página del producto encontrará accesorios y, dado el caso, la información de
                                   montaje correspondiente para su producto.
                                   Puede acceder a la página del producto con la SICK Product ID: pid.sick.com/{P/N}/{S/N}
                                   {P/N} es la referencia del producto, véase la placa de características.
                                   {S/N} es el número de serie del producto, véase la placa de características (si se
                                   indica).




8026228/18SG/2024-12-16 | SICK                                                  B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link   71
Sujeto a cambio sin previo aviso

12 ANEXO


12                   Anexo
12.1                 Estructura del menú

12.1.1               Estructura de los menús en el menú rápido


                          3s                                               1)
                                              SET Q1 / Q2                                    SET Q1 / Q2                             SET Q1 / Q2
       Distancia
                                                Modo                                     SP1 Aprendizaje (auto)                  SP2 Aprendizaje (auto)



                                            Seleccionar opción



                          3s
     Distancia (rel.)                     SET aprendizaje punto cero



                                                Seleccionar opción



                         3s
 Distancia (bar)                               Curva de distribución de la luz



                                              Seleccionar rango




                         3s                                                       1)
                                                 SET Qa                                                 SET Qa
     Valor analógico
                                         4 mA / 0 V Aprendizaje (auto)                         20 mA / 10 V Aprendizaje (auto)




                         3s
       Modo                                   Modo SET



                                           Seleccionar opción




                                            Start                               Parada

     Arrancando            3s
                                         Valor mín.                        Valor máx.                    Valor medio                     Delta mín./máx.




                                                                                                       Desviación estándar




72           B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                                               8026228/18SG/2024-12-16 | SICK
                                                                                                                                           Sujeto a cambio sin previo aviso

ANEXO 12


1)       Opción alternativa para el ajuste del punto de conmutación o el valor analógico en el menú rápido
         1    Para registrar la distancia actual como punto de conmutación o valor analógico, pulse la tecla                                     o        .
         2    Ajustar la distancia a través de las teclas   y    en pasos de 1/10 mm.
         3    Para confirmar la entrada, pulse       .

12.1.2             Estructura del menú principal
Grupo de menús de medición

     /         Menú           Menú Fil‐         Menú         Menú        Menú         ROI cer‐  Menú     Menú                        Valor de          Tiempo de
               Tiempo         tro de            Dirección    Desvia‐     Calibra‐     cano/ROI Selección Modo de                     sustitución       supresión
               de ciclo       valores           de medi‐     ción del    ción         lejano    del pico error                       (Menú             de error
                              medidos           ción         valor                    (Menú                                          Modo de           (Menú
                                                             medido                   Region of                                      error)            Modo de
                                                                                      Interest                                                         error)
                                                                                      (ROI))

Grupo de menús Q1 Salida

     /           Q1 Modo           SP1,          Q1 Mín./ Menú Q1         Menú Q1      Menú        Menú              Q1 Ajuste Menú        Q1 Tole‐
                 (Grupo            SP2,          Máx. Salto Dirección     Desplaza‐    Q1 / Q2     Q1 / Q2           del tempo‐ Q1 / Q2 rancia
                 de                ajuste del    de altura  del salto     miento       Lógica      Modo de           rizador    Histéresis
                 menús             umbral        (Menú                    de ciclos    del punto   tempori‐
                 Q1                de señal      Q1 Mín./                              de con‐     zador
                 Salida)           (Ajuste       Máx.                                  mutación
                                   del punto     Cambio
                                   de con‐       altura )
                                   muta‐
                                   ción) 1)
1)   SP2 sólo está disponible en el modo de salida Q1 Ventana (SP1,SP2:Ventana).

Grupo de menús Q2 / Qa salida

     /         Q2 Modo        SP1,              Q2 Mín./     Menú       Menú        Menú      Menú    Q2 Valor             Menú     Q2 Tole‐                  Ajuste
               (Grupo         SP2,              Máx. Salto   Q1         Q1 Des‐     Q1 / Q2   Q1 / Q2 de                   Q1 / Q2 rancia                     del valor
               de             ajuste del        de altura    Direc‐     plaza‐      Lógica    Modo    tiempo               Histére‐                           analó‐
               menús          umbral            (Menú        ción del   miento      del       de tem‐                      sis                                gico
               Q1             de señal          Q1 Mín./     salto      de          punto     poriza‐
               Salida)        (Ajuste           Máx.                    ciclos      de con‐   dor
                              del punto         Cambio                              muta‐
                              de con‐           altura )                            ción
                              muta‐
                              ción) 1)
1)   SP2 sólo está disponible en el modo de salida Q2 Ventana (SP1,SP2:Ventana).

Grupo de menús Entrada IN

     /                              Menú Función IN               Menú Función de reten‐ Menú Supresión de                         Menú Lógica de
                                                                  ción IN                rebotes IN                                entrada IN

Grupo de menús Dispositivo

     /                 Restaurar el              Menú Restaurar Menú Guardar Menú Idioma                     Configuración               Menú Emisor                Menú Salida
                       dispositivo               calibración    ajustes del                                  de la pantalla                                         PNP/NPN/PP
                                                                cliente

Grupo de menús Información
Información de estado (Grupo de menús Info)




8026228/18SG/2024-12-16 | SICK                                                                  B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link          73
Sujeto a cambio sin previo aviso

12 ANEXO

Grupo de menús RUN
Abrir el menú RUN.

12.2            Declaraciones de conformidad y certificados
                                       En la página del producto puede descargarse declaraciones de conformidad y certifica‐
                                       dos.
                                       Puede acceder a la página del producto con la SICK Product ID: pid.sick.com/{P/N}/{S/N}
                                       {P/N} es la referencia del producto, véase la placa de características.
                                       {S/N} es el número de serie del producto, véase la placa de características (si se
                                       indica).

12.3            Licencias
                                       SICK utiliza software de código abierto publicado por los titulares de los derechos con
                                       una licencia libre. Se utilizan, entre otros, los siguientes tipos de licencia: GNU General
                                       Public License (GPL versión 2, GPL versión 3), GNU Lesser General Public License
                                       (LGPL), licencia MIT, licencia zlib y licencias derivadas de la licencia BSD.
                                       Este programa está disponible para el uso general, pero sin ningún tipo de garantía.
                                       Esta exclusión de garantía incluye también las garantías implícitas de comerciabilidad
                                       o aptitud del programa para un propósito en particular.
                                       Puede obtenerse información más detallada en GNU General Public Licence.
                                       Véanse los textos de las licencias en www.sick.com/licensetexts.
                                       Los textos de las licencias también están disponibles en forma impresa, previa solici‐
                                       tud.




74      B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link                                        8026228/18SG/2024-12-16 | SICK
                                                                                                               Sujeto a cambio sin previo aviso

ANEXO 12




8026228/18SG/2024-12-16 | SICK     B E T R I E B S A N L E I T U N G | OD2000 Analog / IO-Link   75
Sujeto a cambio sin previo aviso

8026228/18SG/2024-12-16/es
                             Australia                                 Hungary                          Slovenia
                             Phone +61 (3) 9457 0600                   Phone +36 1 371 2680             Phone +386 591 78849
                                    1800 33 48 02 – tollfree           E-Mail ertekesites@sick.hu       E-Mail office@sick.si
                             E-Mail sales@sick.com.au                  India                            South Africa
                             Austria                                   Phone +91-22-6119 8900           Phone +27 10 060 0550
                             Phone +43 (0) 2236 62288-0                E-Mail info@sick-india.com       E-Mail info@sickautomation.co.za
                             E-Mail office@sick.at                     Israel                           South Korea
                             Belgium/Luxembourg                        Phone +972 97110 11              Phone +82 2 786 6321/4
                             Phone +32 (0) 2 466 55 66                 E-Mail info@sick-sensors.com     E-Mail infokorea@sick.com
                             E-Mail info@sick.be                       Italy                            Spain
                             Brazil                                    Phone +39 02 27 43 41            Phone +34 93 480 31 00
                             Phone +55 11 3215-4900                    E-Mail info@sick.it              E-Mail info@sick.es
                             E-Mail comercial@sick.com.br              Japan                            Sweden
                             Canada                                    Phone +81 3 5309 2112            Phone +46 10 110 10 00
                             Phone +1 905.771.1444                     E-Mail support@sick.jp           E-Mail info@sick.se
                             E-Mail cs.canada@sick.com                 Malaysia                         Switzerland
                             Czech Republic                            Phone +603-8080 7425             Phone +41 41 619 29 39
                             Phone +420 234 719 500                    E-Mail enquiry.my@sick.com       E-Mail contact@sick.ch
                             E-Mail sick@sick.cz                       Mexico                           Taiwan
                             Chile                                     Phone +52 (472) 748 9451         Phone +886-2-2375-6288
                             Phone +56 (2) 2274 7430                   E-Mail mexico@sick.com           E-Mail sales@sick.com.tw
                             E-Mail chile@sick.com                     Netherlands                      Thailand
                             China                                     Phone +31 (0) 30 204 40 00       Phone +66 2 645 0009
                             Phone +86 20 2882 3600                    E-Mail info@sick.nl              E-Mail marcom.th@sick.com
                             E-Mail info.china@sick.net.cn             New Zealand                      Turkey
                             Denmark                                   Phone +64 9 415 0459             Phone +90 (216) 528 50 00
                             Phone +45 45 82 64 00                            0800 222 278 – tollfree   E-Mail info@sick.com.tr
                             E-Mail sick@sick.dk                       E-Mail sales@sick.co.nz          United Arab Emirates
                             Finland                                   Norway                           Phone +971 (0) 4 88 65 878
                             Phone +358-9-25 15 800                    Phone +47 67 81 50 00            E-Mail contact@sick.ae
                             E-Mail sick@sick.fi                       E-Mail sick@sick.no              United Kingdom
                             France                                    Poland                           Phone +44 (0)17278 31121
                             Phone +33 1 64 62 35 00                   Phone +48 22 539 41 00           E-Mail info@sick.co.uk
                             E-Mail info@sick.fr                       E-Mail info@sick.pl              USA
                             Germany                                   Romania                          Phone +1 800.325.7425
                             Phone +49 (0) 2 11 53 010                 Phone +40 356-17 11 20           E-Mail info@sick.com
                             E-Mail info@sick.de                       E-Mail office@sick.ro            Vietnam
                             Greece                                    Singapore                        Phone +65 6744 3732
                             Phone +30 210 6825100                     Phone +65 6744 3732              E-Mail sales.gsg@sick.com
                             E-Mail office@sick.com.gr                 E-Mail sales.gsg@sick.com
                             Hong Kong                                 Slovakia
                             Phone +852 2153 6300                      Phone +421 482 901 201
                             E-Mail ghk@sick.com.hk                    E-Mail mail@sick-sk.sk


                             Detailed addresses and further locations at www.sick.com




                             SICK AG | Waldkirch | Germany | www.sick.com