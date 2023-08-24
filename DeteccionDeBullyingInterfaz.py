import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import ttkthemes


class BullyingQuestionnaireApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Experto de Detección de Bullying")
        self.root.configure(bg="#0d1b2a")  # Cambiar el color de fondo
        self.root.iconbitmap("C:/Users/yanlu/Downloads/fi/ic.ico")
        
         # Cargar y redimensionar la imagen
        self.image = Image.open("C:/Users/yanlu/Downloads/fi/2.png")
        self.image = self.image.resize((100, 100))# Ajusta el tamaño según lo deseado
        self.photo = ImageTk.PhotoImage(self.image)
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Bahnschrift", 12))  # Personalizar la fuente de los botones


        # Estilo de la etiqueta de bienvenida
        welcome_label_style = ttk.Style()
        welcome_label_style.configure("Welcome.TLabel", font=("Courier New", 20), background="#0d1b2a", foreground="white", attrs=['bold'])

        # Mostrar la imagen junto al mensaje de bienvenida con fondo transparente
        self.welcome_label = ttk.Label(root, text="         ¡Bienvenido! \nSistema Experto de Detección de Bullying",
                                       compound="left", image=self.photo, style="Welcome.TLabel")
        self.welcome_label.pack(padx=20, pady=10)        
        self.enter_button = ttk.Button(root, text="Ingresar", command=self.close_welcome_and_open_instructions)
        self.enter_button.pack(padx=20, pady=10)
        self.questions_completed = False
        self.show_results_button = None  # Inicializa la variable
        self.data_entry_window = None  # Inicializa la ventana de ingresar datos
        self.name = ""  # Almacenar el nombre
        self.age = ""   # Almacenar la edad

    def close_welcome_and_open_instructions(self):
        self.root.withdraw()  # Oculta la ventana de bienvenida
        self.open_instructions_window()  # Abre la ventana de instrucciones

    def open_instructions_window(self):
        self.instructions_window = tk.Toplevel(self.root)
        self.instructions_window.title("Instrucciones")
        self.instructions_window.iconbitmap("C:/Users/yanlu/Downloads/fi/ic.ico")
        self.instructions_window.configure(bg="#343a40")
        self.instructions_window.geometry("400x550")  # Establecer el tamaño de la ventana
        
        # Centrar la ventana en la pantalla
        screen_width = self.instructions_window.winfo_screenwidth()
        screen_height = self.instructions_window.winfo_screenheight()
        window_width = 400
        window_height = 550
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        self.instructions_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        
        instructions_text = (
            "Antes de dar inicio a la evaluación, te solicitaremos que registres algunos datos con el fin de analizar tus respuestas de manera apropiada.\n\n"
            "El cuestionario consta de un total de 60 preguntas, distribuidas en tres secciones: ansiedad, depresión y aspectos personales. Cada una de estas categorías contiene 20 preguntas. Por favor, te pedimos que leas con atención cada interrogante y elijas la opción que mejor refleje tu experiencia.\n\n"
            "Una vez hayas completado todas las secciones del cuestionario, estaremos en capacidad de analizar tus respuestas y proporcionarte una evaluación. Queremos asegurarte que tus respuestas serán tratadas con absoluta confidencialidad. Si en algún momento decides interrumpir el proceso, tienes la opción de hacerlo y tus respuestas serán descartadas.\n\n"
            "¡Agradecemos tu participación en esta evaluación!"
        )
        
        instructions_text_widget = tk.Text(self.instructions_window, wrap="word", font=("Candara Light", 12), bg="#343a40", fg="white", padx=20, pady=20)
        instructions_text_widget.insert("0.85", instructions_text)
        instructions_text_widget.config(state="disabled")
        instructions_text_widget.pack(fill="both", expand=True)
        
        accept_button = ttk.Button(self.instructions_window, text="Aceptar", command=self.close_instructions_and_open_data_entry)
        accept_button.pack(padx=20, pady=10)

        
    def close_instructions_and_open_data_entry(self):
        self.instructions_window.destroy()  # Cierra la ventana de instrucciones
        self.open_data_entry_window()  # Abre la ventana de registrar datos
        
    def create_entry(self, parent, label_text):
        entry_frame = tk.Frame(parent)
        entry_frame.pack(padx=20, pady=5, fill=tk.BOTH)

        label = ttk.Label(entry_frame, text=label_text)
        label.pack(side=tk.LEFT, padx=5)

        entry = ttk.Entry(entry_frame)
        entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        return entry
    
    def open_data_entry_window(self):
        self.root.withdraw()  
        self.root.iconbitmap("C:/Users/yanlu/Downloads/fi/ic.ico")
    
        # Utiliza el tema "arc" o "equilux" en lugar de "clam"
        self.data_entry_window = ttkthemes.ThemedTk(theme="arc")
        self.data_entry_window.title("Ingresar Datos")
        self.data_entry_window.geometry("300x410")
        # Cambiar el icono de la ventana de ingreso de datos
        self.data_entry_window.iconbitmap("C:/Users/yanlu/Downloads/fi/ic.ico") 
        # Personalizar colores de los botones de opción en la ventana de registro de datos
        data_entry_style = ttk.Style(self.data_entry_window)

        # Personalizar colores de los botones de opción en la ventana de registro de datos
        data_entry_style = ttk.Style(self.data_entry_window)
        data_entry_style.configure("TRadiobutton", background="#343a40")
        data_entry_style.configure("TRadiobutton", foreground="black")

        # Cambios en colores y estilo
        self.data_entry_window.configure(bg="#343a40")

        self.register_label = ttk.Label(self.data_entry_window, text="INGRESE DATOS", font=("Arial Black", 15), background="#343a40", foreground="white")
        self.register_label.pack(padx=20, pady=20)

        # Estilo de las entradas
        entry_style = ttk.Style(self.data_entry_window)
        entry_style.configure("TEntry", fieldbackground="white", foreground="black")  # Cambiar colores
        self.name_entry = self.create_entry(self.data_entry_window, "Nombre")
        self.last_name_entry = self.create_entry(self.data_entry_window, "Apellido Paterno")
        self.mother_last_name_entry = self.create_entry(self.data_entry_window, "Apellido Materno")
        self.age_entry = self.create_entry(self.data_entry_window, "Edad")

        # Género
        self.gender_label = ttk.Label(self.data_entry_window, text="Género", font=("Arial", 10), background="#e8e8e8", foreground="gray")
        self.gender_label.pack(padx=20, pady=5)

        gender_options = ["Masculino", "Femenino"]
        self.gender_var = tk.StringVar()
        self.gender_var.set(gender_options[0])
        self.gender_menu = ttk.Combobox(self.data_entry_window, textvariable=self.gender_var, values=gender_options, state="readonly")
        self.gender_menu.pack(padx=20, pady=5)

        # Grado
        self.grade_label = ttk.Label(self.data_entry_window, text="Grado", font=("Arial", 10), background="#e8e8e8", foreground="gray")
        self.grade_label.pack(padx=20, pady=5)

        grades = ["1ro", "2do", "3ro", "4to", "5to"]
        self.grade_var = tk.StringVar()
        self.grade_var.set(grades[0])
        self.grade_menu = ttk.Combobox(self.data_entry_window, textvariable=self.grade_var, values=grades, state="readonly")
        self.grade_menu.pack(padx=20, pady=5)

        self.register_button = ttk.Button(self.data_entry_window, text="Registrar Datos", command=self.register_and_start_questionnaire)
        self.register_button.pack(pady=10)
        # Centrar la ventana en la pantalla
        screen_width = self.data_entry_window.winfo_screenwidth()
        screen_height = self.data_entry_window.winfo_screenheight()
        window_width = 300
        window_height = 410
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        self.data_entry_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    
    def register_and_start_questionnaire(self):
        self.name = self.name_entry.get()  # Almacenar el nombre ingresado
        self.last_name = self.last_name_entry.get()  # Almacenar el apellido paterno ingresado
        self.mother_last_name = self.mother_last_name_entry.get()  # Almacenar el apellido materno ingresado
        self.age = self.age_entry.get()  # Almacenar la edad ingresada
        self.grade = self.grade_var.get()  # Almacenar el grado de secundaria seleccionado

        if self.name and self.last_name and self.mother_last_name and self.age and self.grade:
            self.data_entry_window.destroy()  # Cierra la ventana de ingresar datos
            self.close_main_and_start_questionnaire()
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa todos los datos.")


    def close_main_and_start_questionnaire(self):
        self.root.withdraw()  # Oculta la ventana principal
        self.start_ansiedad_questionnaire()  # Abre la ventana de preguntas

    def start_ansiedad_questionnaire(self):
        self.questionnaire_window = tk.Toplevel(self.root)
        self.questionnaire_window.title("Cuestionario de Bullying - Ansiedad")
        self.questionnaire_window.iconbitmap("C:/Users/yanlu/Downloads/fi/ic.ico")
        self.current_section = "ansiedad"
        self.current_question_index = 0
        self.answers = []
        self.questions = [
            '1. Te sientes más intranquilo y nervioso que de costumbre?',
            '2. Te sientes atemorizado sin motivo?',
            '3. Te alteras o te angustias fácilmente?',
            '4. Sientes como si te estuvieras deshaciendo en pedazos?',
            '5. Crees que nada está bien y van a pasar muchas desgracias?',
            '6. Te tiemblan los brazos y las piernas?',
            '7. Sufres dolores de cabeza, del cuello y de la espalda?',
            '8. Te sientes débil y te cansas fácilmente?',
            '9. Te cuesta calmarte cuando estás intranquilo?',
            '10. Sientes que el corazón te late rápido?',
            '11. Sufres mareos?',
            '12. Te desmayas o sientes que vas a desmayarte?',
            '13. Te cuesta respirar?',
            '14. Se te duermen y hormiguean los dedos de las manos y de los pies?',
            '15. Sufres dolores de estómago o indigestión?',
            '16. Tienes que orinar con mucha frecuencia?',
            '17. Generalmente tienes las manos frías y mojadas?',
            '18. La cara se te pone caliente y roja?',
            '19. Te cuesta dormir por las noches?',
            '20. Tienes pesadillas?'
        ]
        self.create_question_ui()

    def ansiedad_callback(self):
        self.questionnaire_window.destroy()
        self.start_depresion_questionnaire()

    def start_depresion_questionnaire(self):
        self.questionnaire_window.destroy()
        self.questionnaire_window = tk.Toplevel(self.root)
        self.questionnaire_window.title("Cuestionario de Bullying - Depresión")
        self.questionnaire_window.iconbitmap("C:/Users/yanlu/Downloads/fi/ic.ico")
        self.current_section = "depresion"
        self.current_question_index = 0
        self.questions = [
            '21. Te sientes abatido y melancólico?',
            '22. Al día siguiente, ¿te sigues sintiendo mal?',
            '23. Tienes accesos de llanto o ganas de llorar?',
            '24. Tienes problemas para dormir en la noche?',
            '25. No tienes tanto apetito como antes?',
            '26. Has perdido el interés por el sexo opuesto?',
            '27. Notas que estás perdiendo peso?',
            '28. Tienes trastornos intestinales y estreñimiento?',
            '29. Te late el corazón más rápido de lo habitual?',
            '30. Te cansas sin motivo?',
            '31. Tienes la mente más abrumada que antes?',
            '32. Haces las cosas con más dificultad que antes?',
            '33. Te sientes nervioso y no puedes estar quieto?',
            '34. No crees tener futuro?',
            '35. Te sientes más irritable que antes?',
            '36. Te es difícil tomar decisiones?',
            '37. Te sientes inútil?',
            '38. Te satisface tu vida actual?',
            '39. Crees que los demás estarían mejor si tú murieras?',
            '40. Ya no disfrutas de las mismas cosas que antes?'
        ]
        self.create_question_ui()

    def depresion_callback(self):
        self.questionnaire_window.destroy()
        self.start_personal_questionnaire()

    def start_personal_questionnaire(self):
        self.questionnaire_window.destroy()
        self.questionnaire_window = tk.Toplevel(self.root)
        self.questionnaire_window.title("Cuestionario de Bullying - Personal")
        self.questionnaire_window.iconbitmap("C:/Users/yanlu/Downloads/fi/ic.ico")
        self.current_section = "personal"
        self.current_question_index = 0
        self.questions = [
            '41. Te molestan otros estudiantes en el colegio?',
            '42. Te han hecho sentir mal o incómodo de alguna manera en el colegio?',
            '43. Tienes situaciones en las que te hayan tratado de manera injusta o desagradable?',
            '44. Has notado que ciertos estudiantes te tratan de forma negativa o te evitan?',
            '45. Con qué frecuencia tus compañeros te han dicho cosas hirientes o te hayan hecho sentir menos?',
            '46. Alguna vez has sentido que otros estudiantes te han amenazado o tratado mal?',
            '47. Presencias situaciones en las que te hayan pedido que hagas algo que no querías hacer?',
            '48. Has experimentado situaciones en las que te hayan excluido o dejado fuera de actividades o grupos?',
            '49. Recibes comentarios o actitudes negativas de otros estudiantes?',
            '50. Has notado que algunos estudiantes intentan controlar o influir en ti de manera negativa?',
            '51. Has sentido que tus relaciones con otros estudiantes han cambiado negativamente debido a situaciones desagradables?',
            '52. Has notado que te cuesta más relacionarte o hacer amigos debido a experiencias negativas en el colegio?',
            '53. Has experimentado cambios en tu participación en actividades sociales o eventos escolares debido a situaciones incómodas?',
            '54. Has notado que otros estudiantes te tratan de manera diferente después de situaciones negativas en el colegio?',
            '55. Has experimentado una disminución en tu rendimiento académico recientemente?',
            '56. Sientes dificultad para concentrarte durante las clases?',
            '57. Pierdes el interés en los cursos?',
            '58. Sientes calificaciones más bajas de lo habitual en tus exámenes o trabajos?',
            '59. Prefieres no asistir a clases por alguna incomodidad que tengas con un compañero de colegio?',
            '60. Prefieres no asistir a clases por alguna incomodidad que tengas con un profesor?'
        ]
        self.create_question_ui()


    def create_question_ui(self):
        self.questionnaire_window.geometry("800x350")
        self.questionnaire_window.configure(bg="#212529")  # Cambiar color de fondo

        self.current_question = tk.Label(
            self.questionnaire_window,
            text=self.questions[self.current_question_index],
            background="#212529",
            foreground="#e63946",
            font=("Bahnschrift", 14, "bold")
        )
        self.current_question.pack(padx=20, pady=20, anchor="center")

        self.answer_var = tk.StringVar()
        self.answer_var.set("")

        answer_options = [
            "1. nunca o casi nunca",
            "2. a veces",
            "3. con bastante frecuencia",
            "4. siempre o casi siempre"
        ]

        self.answer_radios = []
        for i, option in enumerate(answer_options):
            radio_button = tk.Radiobutton(
                self.questionnaire_window,
                text=option,
                variable=self.answer_var,
                value=i + 1,
                background="#212529",
                foreground="#edede9",
                font=("Bahnschrift", 12),
                selectcolor="#343a40"  # Cambiar el color de fondo al seleccionar una opción
            )
            self.answer_radios.append(radio_button)
            radio_button.pack(padx=20, pady=5, anchor="w")

        self.next_button = ttk.Button(self.questionnaire_window, text="Siguiente", command=self.next_question)
        self.next_button.pack(pady=10)

        self.show_results_button = ttk.Button(self.questionnaire_window, text="Mostrar Resultados", command=self.calculate_results)
        self.show_results_button.pack(pady=10)
        self.show_results_button.config(state=tk.DISABLED)  # Deshabilitar el botón inicialmente

        # Deseleccionar los botones de radio al abrir la ventana
        for radio_button in self.answer_radios:
            radio_button.deselect()



    def start_questionnaire(self, questions, callback):
        self.question_index = 0
        self.answers = []

        self.current_question = tk.Label(self.questionnaire_window, text=questions[self.question_index])
        self.current_question.pack(pady=10)

        self.answer_var = tk.StringVar()
        self.answer_var.set("")

        self.answer_radios = []
        for i in range(4):
            radio_button = tk.Radiobutton(self.questionnaire_window, text=f"Opción {i+1}", variable=self.answer_var, value=i+1)
            self.answer_radios.append(radio_button)
            radio_button.pack()

        self.show_results_button = tk.Button(self.questionnaire_window, text="Mostrar Resultados", command=self.calculate_results)
        self.show_results_button.pack(pady=10)
        self.show_results_button.config(state=tk.DISABLED)  # Deshabilitar el botón inicialmente

        self.next_button = tk.Button(self.questionnaire_window, text="Siguiente", command=lambda: self.next_question(callback))
        self.next_button.pack(pady=10)

    def next_question(self):
        if self.answer_var.get():
            self.answers.append(int(self.answer_var.get()))
            self.answer_var.set("")
            self.current_question_index += 1

            if self.current_question_index < len(self.questions):
                self.current_question.config(text=self.questions[self.current_question_index])
                for radio_button in self.answer_radios:
                    radio_button.deselect()
                if self.current_question_index == len(self.questions) - 1:
                    self.show_results_button.config(state=tk.DISABLED)  # Deshabilitar el botón de "Mostrar Resultados"
            else:
                self.show_results_button.config(state=tk.NORMAL)  # Habilitar el botón de "Mostrar Resultados"
                self.next_button.config(state=tk.DISABLED)  # Deshabilitar el botón "Siguiente"
                if self.current_section == "ansiedad":
                    self.start_depresion_questionnaire()
                elif self.current_section == "depresion":
                    self.start_personal_questionnaire()
                else:
                    self.calculate_results()
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una respuesta.")


    def calculate_results(self):

        suma_ansiedad = sum(self.answers[:20])
        suma_depresion = sum(self.answers[20:40])
        suma_personal = sum(self.answers[40:])
        
        estado_personal = self.compare_score(suma_personal)
        estado_ansiedad = self.compare_score(suma_ansiedad)
        estado_depresion = self.compare_score(suma_depresion)
        
        diagnostic_bullying = self.diagnose_bullying(estado_personal, estado_ansiedad, estado_depresion)
        
         # Crear la ventana de resultados sin barra de título
        results_window = tk.Toplevel(self.root)
        results_window.overrideredirect(True)  # Ocultar la barra de título
        results_window.geometry("500x470")
        results_window.configure(bg="#adb5bd")  # Cambiar color de fondo de la ventana de resultados

        # Calcular las dimensiones de la pantalla
        screen_width = results_window.winfo_screenwidth()
        screen_height = results_window.winfo_screenheight()

        # Calcular las dimensiones de la ventana
        window_width = 500
        window_height = 470

        # Calcular las coordenadas para centrar la ventana
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        # Establecer la geometría de la ventana y su posición
        results_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        results_window.configure(bg="#adb5bd")  # Cambiar color de fondo de la ventana de resultados

        # Cargar la imagen y convertirla en un icono
        icon_image = Image.open("C:/Users/yanlu/Downloads/fi/ic.ico")  
        icon_image = icon_image.resize((32, 32))  # Ajusta el tamaño según lo deseado
        icon_photo = ImageTk.PhotoImage(icon_image)

        # Establecer el icono en la ventana de resultados
        results_window.tk.call("wm", "iconphoto", results_window._w, icon_photo)

        results_label = tk.Label(results_window, text="Resultados del Cuestionario", font=("Arial Black", 15), bg="#adb5bd", fg="white")  # Cambiar colores de la etiqueta de resultados
        results_label.pack(pady=10)

        results_text = f"Resultados para {self.name} {self.last_name} {self.mother_last_name},de {self.age} años:\n\n"
        results_text += f"Preguntas de Aspectos Personales:\nPuntaje Total: {suma_personal}\nDiagnóstico: {estado_personal}\n\n"
        results_text += f"Preguntas de Ansiedad:\nPuntaje Total: {suma_ansiedad}\nDiagnóstico: {estado_ansiedad}\n\n"
        results_text += f"Preguntas de Depresión:\nPuntaje Total: {suma_depresion}\nDiagnóstico: {estado_depresion}\n\n"
        results_text += f"Diagnóstico de Bullying\n {diagnostic_bullying}"

        results_display = tk.Label(
        results_window,
        text=results_text,
        bg="#adb5bd",
        fg="#1f2833",  # Cambiar el color del texto
        font=("Bahnschrift", 12),  # Cambiar la fuente y el tamaño del texto
        wraplength=350  # Agregar un ajuste de línea
        )  # Cambiar colores del texto de resultados
        results_display.pack()

        close_button = tk.Button(results_window, text="Cerrar", command=results_window.destroy, bg="#adb5bd", fg="white")  # Cambiar colores del botón de cierre
        close_button.pack(pady=10)

    def compare_score(self, score):
        if score >= 70:
            return "intensa"
        elif score >= 60:
            return "moderada"
        elif score >= 50:
            return "leve"
        else:
            return "normal"

    def diagnose_bullying(self, estado_personal, estado_ansiedad, estado_depresion):
        if (estado_personal == "intensa" and estado_ansiedad == "intensa" and estado_depresion == "intensa") or (estado_personal == "moderada" and estado_ansiedad == "intensa" and estado_depresion == "intensa") :
            return "Los resultados confirman que es víctima de bullying"
        elif ("moderada" in [estado_personal, estado_ansiedad, estado_depresion]) or (estado_personal == "leve" and estado_ansiedad == "moderada" and estado_depresion == "moderada") or (estado_personal == "intensa" and estado_ansiedad == "moderada" and estado_depresion == "moderada"):
            return "Los resultados indican que está experimentando síntomas significativos de bullying en este momento."
        elif ("leve" in [estado_personal, estado_ansiedad, estado_depresion]) or (estado_personal == "normal" and estado_ansiedad == "leve" and estado_depresion == "leve")or (estado_personal == "normal" and estado_ansiedad == "leve" or estado_depresion == "leve"):
            return "Los resultados muestran indica que es propenso a ser víctima de bullying"
        else:
            return "Los resultados muestran que no es víctima de bullying"
        
    
if __name__ == "__main__":
    root = tk.Tk()
    app = BullyingQuestionnaireApp(root)
    root.mainloop()
