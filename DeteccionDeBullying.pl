%Hechos respuesta
respuesta(1, 1, "nunca o casi nunca").
respuesta(2, 2, "a veces").
respuesta(3, 3, "con bastante frecuencia").
respuesta(4, 4, "siempre o casi siempre").

% Hechos dinamico para las respuestas
:- dynamic respuesta_personal/2, respuesta_ansiedad/2, respuesta_depresion/2.

% Hechos dinámicos para almacenar los datos del estudiante
:- dynamic estudiante/6.

% Hechos de experiencia personal
pregunta_personal(pregunta_personal_1, 'Te molestan otros estudiantes en el colegio?').
pregunta_personal(pregunta_personal_2, 'Te han hecho sentir mal o incómodo de alguna manera en el colegio?').
pregunta_personal(pregunta_personal_3, 'Tienes situaciónes en las que te hayan tratado de manera injusta o desagradable?').
pregunta_personal(pregunta_personal_4, 'Has notado que ciertos estudiantes te tratan de forma negativa o te evitan?').
pregunta_personal(pregunta_personal_5, 'Con que frecuencia tus compañeros te han dicho cosas hirientes o te hayan hecho sentir menos?').

% Hechos de interacción personal
pregunta_personal(pregunta_personal_6, 'Alguna vez has sentido que otros estudiantes te han amenazado o tratado mal?').
pregunta_personal(pregunta_personal_7, 'Presencias situaciones en las que te hayan pedido que hagas algo que no querías hacer?').
pregunta_personal(pregunta_personal_8, 'Has experimentado situaciones en las que te hayan excluido o dejado fuera de actividades o grupos?').
pregunta_personal(pregunta_personal_9, 'Recibes comentarios o actitudes negativas de otros estudiantes?').
pregunta_personal(pregunta_personal_10, 'Has notado que algunos estudiantes intentan controlar o influir en ti de manera negativa?').

% Hechos de impacto social
pregunta_personal(pregunta_personal_11, 'Has sentido que tus relaciones con otros estudiantes han cambiado negativamente debido a situaciones desagradables?').
pregunta_personal(pregunta_personal_12, 'Has notado que te cuesta más relacionarte o hacer amigos debido a experiencias negativas en el colegio?').
pregunta_personal(pregunta_personal_13, 'Has experimentado cambios en tu participación en actividades sociales o eventos escolares debido a situaciones incómodas?').
pregunta_personal(pregunta_personal_14, 'Has notado que otros estudiantes te tratan de manera diferente después de situaciones negativas en el colegio?').

% Hechos de deterioro académico
pregunta_personal(pregunta_personal_15, 'Has experimentado una disminución en tu rendimiento académico recientemente?').
pregunta_personal(pregunta_personal_16, 'Sientes dificultad para concentrarte durante las clases?').
pregunta_personal(pregunta_personal_17, 'Pierdes el interés en los cursos?').
pregunta_personal(pregunta_personal_18, 'Sientees calificaciones más bajas de lo habitual en tus exámenes o trabajos?').
pregunta_personal(pregunta_personal_19, 'Prefieres no asistir a clases por alguna incomodidad que tengas con un compañero de colegio?').
pregunta_personal(pregunta_personal_20, 'Prefieres no asistir a clases por alguna incomodidad que tengas con un profesor?').

% Hechos de ansiedad
pregunta_ansiedad(pregunta_ansiedad_1, 'Te sientes más intranquilo y nervioso que de costumbre?').
pregunta_ansiedad(pregunta_ansiedad_2, 'Te sientes atemorizado sin motivo?').
pregunta_ansiedad(pregunta_ansiedad_3, 'Te alteras o te angustias fácilmente?').
pregunta_ansiedad(pregunta_ansiedad_4, 'Sientes como si te estuvieras deshaciendo en pedazos?').
pregunta_ansiedad(pregunta_ansiedad_5, 'Crees que nada está bien y van a pasar muchas desgracias?').
pregunta_ansiedad(pregunta_ansiedad_6, 'Te tiemblan los brazos y las piernas?').
pregunta_ansiedad(pregunta_ansiedad_7, 'Sufres dolores de cabeza, del cuello y de la espalda?').
pregunta_ansiedad(pregunta_ansiedad_8, 'Te sientes débil y te cansas fácilmente?').
pregunta_ansiedad(pregunta_ansiedad_9, 'Te cuesta calmarte cuando estás intranquilo?').
pregunta_ansiedad(pregunta_ansiedad_10, 'Sientes que el corazón te late rápido?').
pregunta_ansiedad(pregunta_ansiedad_11, 'Sufres mareos?').
pregunta_ansiedad(pregunta_ansiedad_12, 'Te desmayas o sientes que vas a desmayarte?').
pregunta_ansiedad(pregunta_ansiedad_13, 'Te cuesta respirar?').
pregunta_ansiedad(pregunta_ansiedad_14, 'Se te duermen y hormiguean los dedos de las manos y de los pies?').
pregunta_ansiedad(pregunta_ansiedad_15, 'Sufres dolores de estómago o indigestión?').
pregunta_ansiedad(pregunta_ansiedad_16, 'Tienes que orinar con mucha frecuencia?').
pregunta_ansiedad(pregunta_ansiedad_17, 'Generalmente tienes las manos frías y mojadas?').
pregunta_ansiedad(pregunta_ansiedad_18, 'La cara se te pone caliente y roja?').
pregunta_ansiedad(pregunta_ansiedad_19, 'Te cuesta dormir por las noches?').
pregunta_ansiedad(pregunta_ansiedad_20, 'Tienes pesadillas?').

% Hechos de depresión
pregunta_depresion(pregunta_depresion_1, 'Te sientes abatido y melancólico?').
pregunta_depresion(pregunta_depresion_2, 'Al día siguiente, ¿te sigues sintiendo mal?').
pregunta_depresion(pregunta_depresion_3, 'Tienes accesos de llanto o ganas de llorar?').
pregunta_depresion(pregunta_depresion_4, 'Tienes problemas para dormir en la noche?').
pregunta_depresion(pregunta_depresion_5, 'No tienes tanto apetito como antes?').
pregunta_depresion(pregunta_depresion_6, 'Has perdido el interés por el sexo opuesto?').
pregunta_depresion(pregunta_depresion_7, 'Notas que estás perdiendo peso?').
pregunta_depresion(pregunta_depresion_8, 'Tienes trastornos intestinales y estreñimiento?').
pregunta_depresion(pregunta_depresion_9, 'Te late el corazón más rápido de lo habitual?').
pregunta_depresion(pregunta_depresion_10, 'Te cansas sin motivo?').
pregunta_depresion(pregunta_depresion_11, 'Tienes la mente más abrumada que antes?').
pregunta_depresion(pregunta_depresion_12, 'Haces las cosas con más dificultad que antes?').
pregunta_depresion(pregunta_depresion_13, 'Te sientes nervioso y no puedes estar quieto?').
pregunta_depresion(pregunta_depresion_14, 'No crees tener futuro?').
pregunta_depresion(pregunta_depresion_15, 'Te sientes más irritable que antes?').
pregunta_depresion(pregunta_depresion_16, 'Te es difícil tomar decisiones?').
pregunta_depresion(pregunta_depresion_17, 'Te sientes inútil?').
pregunta_depresion(pregunta_depresion_18, 'Te satisface tu vida actual?').
pregunta_depresion(pregunta_depresion_19, 'Crees que los demás estarían mejor si tú murieras?').
pregunta_depresion(pregunta_depresion_20, 'Ya no disfrutas de las mismas cosas que antes?').

% Regla principal para empezar el cuestionario
 inicio :- capturar_datos_estudiante, preguntas_iniciales, calcular_resultados.



% Regla para capturar los datos del estudiante
capturar_datos_estudiante :-
    writeln("¡Bienvenido al sistema experto para el diagnostico de bullying! Porfavor ingrese sus datos"),
    write('Ingrese su nombre: '),
    read(Nombre),
    write('Ingrese su apellido paterno: '),
    read(ApellidoP),
    write('Ingrese su apellido materno: '),
    read(ApellidoM),
    write('Ingrese su edad: '),
    read(Edad), 
    write('Ingrese su genero: '),
    read(Genero),
    write('Ingrese el grado de secundaria que esta cursando: '),
    read(Grado),
    assertz(estudiante(Nombre, ApellidoP, ApellidoM, Edad, Genero, Grado)).

% Regla para mostrar los datos del estudiante
mostrar_datos_estudiante :-
    estudiante(Nombre, ApellidoP, ApellidoM, Edad, Genero, Grado),
    format('Nombre y apellidos: ~w ~w ~w~nEdad: ~w~nGenero: ~w~nGrado:~w~n', [Nombre, ApellidoP, ApellidoM, Edad, Genero, Grado]),
    fail.
mostrar_datos_estudiante.



% Reglas para preguntas iniciales
preguntas_iniciales :-
    writeln("Responde las siguientes preguntas:"),
    hacer_pregunta_personal(pregunta_personal_1, Respuesta1),
    hacer_pregunta_personal(pregunta_personal_2, Respuesta2),
    hacer_pregunta_personal(pregunta_personal_3, Respuesta3),
    hacer_pregunta_personal(pregunta_personal_4, Respuesta4),
    hacer_pregunta_personal(pregunta_personal_5, Respuesta5),
    hacer_pregunta_personal(pregunta_personal_6, Respuesta6),
    hacer_pregunta_personal(pregunta_personal_7, Respuesta7),
    hacer_pregunta_personal(pregunta_personal_8, Respuesta8),
    hacer_pregunta_personal(pregunta_personal_9, Respuesta9),
    hacer_pregunta_personal(pregunta_personal_10, Respuesta10),
    hacer_pregunta_personal(pregunta_personal_11, Respuesta11),
    hacer_pregunta_personal(pregunta_personal_12, Respuesta12),
    hacer_pregunta_personal(pregunta_personal_13, Respuesta13),
    hacer_pregunta_personal(pregunta_personal_14, Respuesta14),
    hacer_pregunta_personal(pregunta_personal_15, Respuesta15),
    hacer_pregunta_personal(pregunta_personal_16, Respuesta16),
    hacer_pregunta_personal(pregunta_personal_17, Respuesta17),
    hacer_pregunta_personal(pregunta_personal_18, Respuesta18),
    hacer_pregunta_personal(pregunta_personal_19, Respuesta19),
    hacer_pregunta_personal(pregunta_personal_20, Respuesta20),

    hacer_pregunta_ansiedad(pregunta_ansiedad_1, Respuesta21),
    hacer_pregunta_ansiedad(pregunta_ansiedad_2, Respuesta22),
    hacer_pregunta_ansiedad(pregunta_ansiedad_3, Respuesta23),
    hacer_pregunta_ansiedad(pregunta_ansiedad_4, Respuesta24),
    hacer_pregunta_ansiedad(pregunta_ansiedad_5, Respuesta25),
    hacer_pregunta_ansiedad(pregunta_ansiedad_6, Respuesta26),
    hacer_pregunta_ansiedad(pregunta_ansiedad_7, Respuesta27),
    hacer_pregunta_ansiedad(pregunta_ansiedad_8, Respuesta28),
    hacer_pregunta_ansiedad(pregunta_ansiedad_9, Respuesta29),
    hacer_pregunta_ansiedad(pregunta_ansiedad_10, Respuesta30),
    hacer_pregunta_ansiedad(pregunta_ansiedad_11, Respuesta31),
    hacer_pregunta_ansiedad(pregunta_ansiedad_12, Respuesta32),
    hacer_pregunta_ansiedad(pregunta_ansiedad_13, Respuesta33),
    hacer_pregunta_ansiedad(pregunta_ansiedad_14, Respuesta34),
    hacer_pregunta_ansiedad(pregunta_ansiedad_15, Respuesta35),
    hacer_pregunta_ansiedad(pregunta_ansiedad_16, Respuesta36),
    hacer_pregunta_ansiedad(pregunta_ansiedad_17, Respuesta37),
    hacer_pregunta_ansiedad(pregunta_ansiedad_18, Respuesta38),
    hacer_pregunta_ansiedad(pregunta_ansiedad_19, Respuesta39),
    hacer_pregunta_ansiedad(pregunta_ansiedad_20, Respuesta40),

    hacer_pregunta_depresion(pregunta_depresion_1, Respuesta41),
    hacer_pregunta_depresion(pregunta_depresion_2, Respuesta42),
    hacer_pregunta_depresion(pregunta_depresion_3, Respuesta43),
    hacer_pregunta_depresion(pregunta_depresion_4, Respuesta44),
    hacer_pregunta_depresion(pregunta_depresion_5, Respuesta45),
    hacer_pregunta_depresion(pregunta_depresion_6, Respuesta46),
    hacer_pregunta_depresion(pregunta_depresion_7, Respuesta47),
    hacer_pregunta_depresion(pregunta_depresion_8, Respuesta48),
    hacer_pregunta_depresion(pregunta_depresion_9, Respuesta49),
    hacer_pregunta_depresion(pregunta_depresion_10, Respuesta50),
    hacer_pregunta_depresion(pregunta_depresion_11, Respuesta51),
    hacer_pregunta_depresion(pregunta_depresion_12, Respuesta52),
    hacer_pregunta_depresion(pregunta_depresion_13, Respuesta53),
    hacer_pregunta_depresion(pregunta_depresion_14, Respuesta54),
    hacer_pregunta_depresion(pregunta_depresion_15, Respuesta55),
    hacer_pregunta_depresion(pregunta_depresion_16, Respuesta56),
    hacer_pregunta_depresion(pregunta_depresion_17, Respuesta57),
    hacer_pregunta_depresion(pregunta_depresion_18, Respuesta58),
    hacer_pregunta_depresion(pregunta_depresion_19, Respuesta59),
    hacer_pregunta_depresion(pregunta_depresion_20, Respuesta60).

% Regla para hacer preguntas personales y guardar respuestas
hacer_pregunta_personal(Pregunta, Respuesta) :-
    pregunta_personal(Pregunta, PreguntaText),
    writeln(PreguntaText),
    writeln("1. nunca o casi nunca"),
    writeln("2. a veces"),
    writeln("3. con bastante frecuencia"),
    writeln("4. siempre o casi siempre"),
    read(Respuesta),
    assertz(respuesta_personal(Pregunta, Respuesta)).

% Regla para hacer preguntas de ansiedad y guardar respuestas
hacer_pregunta_ansiedad(Pregunta, Respuesta) :-
    pregunta_ansiedad(Pregunta, PreguntaText),
    writeln(PreguntaText),
    writeln("1. nunca o casi nunca"),
    writeln("2. a veces"),
    writeln("3. con bastante frecuencia"),
    writeln("4. siempre o casi siempre"),
    read(Respuesta),
    assertz(respuesta_ansiedad(Pregunta, Respuesta)).

% Regla para hacer preguntas de depresión y guardar respuestas
hacer_pregunta_depresion(Pregunta, Respuesta) :-
    pregunta_depresion(Pregunta, PreguntaText),
    writeln(PreguntaText),
    writeln("1. nunca o casi nunca"),
    writeln("2. a veces"),
    writeln("3. con bastante frecuencia"),
    writeln("4. siempre o casi siempre"),
    read(Respuesta),
    assertz(respuesta_depresion(Pregunta, Respuesta)).



% Regla para calcular los resultados y comparar las respuestas
    calcular_resultados :-
        findall(Respuesta, respuesta_personal(_, Respuesta), RespuestasPersonales),
        findall(Respuesta, respuesta_ansiedad(_, Respuesta), RespuestasAnsiedad),
        findall(Respuesta, respuesta_depresion(_, Respuesta), RespuestasDepresion),
        sum_list(RespuestasPersonales, SumaPersonal),
        sum_list(RespuestasAnsiedad, SumaAnsiedad),
        sum_list(RespuestasDepresion, SumaDepresion),

        nivel_personal(SumaPersonal, EstadoP),
        nivel_ansiedad(SumaAnsiedad, EstadoA),
        nivel_depresion(SumaDepresion, EstadoD),

        mostrar_datos_estudiante,

        writeln("Resultados:"),
        writeln("Preguntas del estado del estudiante:"),
        writeln("Suma Personal: " + SumaPersonal),
        writeln("Diagnostico de la situacion del estudiante segun su entorno personal, social y academico:" + EstadoP),

        writeln("Preguntas de Ansiedad:"),
        writeln("Suma Ansiedad: " + SumaAnsiedad),
        writeln("Diagnostico:" + EstadoA),
        
        writeln("Preguntas de Depresion:"),
        writeln("Suma Depresion: " + SumaDepresion),
        writeln("Diagnostico:" + EstadoD),

        diagnostico_bullying(EstadoP,EstadoA,EstadoD,DiagnosticoB),
        writeln("Diagnostico de Bullying:" + DiagnosticoB).

        % Reglas de comparaciones personal
        nivel_personal(SumaPersonal,"intensa") :- SumaPersonal >= 70.
        nivel_personal(SumaPersonal, "moderada") :- SumaPersonal =< 69, SumaPersonal >= 60.
        nivel_personal(SumaPersonal, "leve") :- SumaPersonal =< 59, SumaPersonal >= 50.  
        nivel_personal(SumaPersonal, "normal") :- SumaPersonal < 50.

        % Reglas de comparaciones ansiedad
        nivel_ansiedad(SumaAnsiedad,"intensa") :- SumaAnsiedad >= 70.
        nivel_ansiedad(SumaAnsiedad, "moderada") :- SumaAnsiedad =< 69, SumaAnsiedad >= 60.
        nivel_ansiedad(SumaAnsiedad, "leve") :- SumaAnsiedad =< 59, SumaAnsiedad >= 50.  
        nivel_ansiedad(SumaAnsiedad, "normal") :- SumaAnsiedad < 50.

        % Reglas de comparaciones depresion
        nivel_depresion(SumaDepresion,"intensa") :- SumaDepresion >= 70.
        nivel_depresion(SumaDepresion, "moderada") :- SumaDepresion =< 69, SumaDepresion >= 60.
        nivel_depresion(SumaDepresion, "leve") :- SumaDepresion =< 59, SumaDepresion >= 50.  
        nivel_depresion(SumaDepresion, "normal") :- SumaDepresion < 50.


        %Reglas de Diagnostico de bullying
        diagnostico_bullying(EstadoP,EstadoA,EstadoD,'Es una victima de bullying'):- 
            EstadoP="intensa",
            EstadoA="intensa",
            EstadoD="intensa".

        diagnostico_bullying(EstadoP,EstadoA,EstadoD,'Posible victima de bullying'):- 
            (EstadoA="moderada"; EstadoA="intensa"), 
            (EstadoD="moderada"; EstadoD="intensa"),
            (EstadoP="moderada"; EstadoP="intensa").
        
        diagnostico_bullying(EstadoP,EstadoA,EstadoD,'Propenso a ser victima de bullying'):- 
                (EstadoA="leve"; EstadoA="moderada"; EstadoA="intensa"), 
                (EstadoD="leve"; EstadoD="moderada"; EstadoD="intensa"),
                (EstadoP="leve"; EstadoP="moderada"; EstadoP="intensa").

 
        diagnostico_bullying(EstadoP,EstadoA,EstadoD,'No es victima de bullying'):- 
            EstadoP="normal",
            EstadoA="normal",
            EstadoD="normal".