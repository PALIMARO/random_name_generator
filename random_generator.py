import tkinter as tk
from tkinter import ttk
import random

# Listas de sílabas
vocal_to_vocal_syllables = ["ala", "eli", "iri", "ulo", "ovo", "ema", "osha", "uvu", "ana", "athi", "oru", "ini", "usu", "itho"]
vocal_to_consonant_syllables = ["al", "el", "ir", "ul", "ov", "em", "osh", "uv", "an"]
consonant_to_vocal_syllables = ["dra", "gla", "tha", "syla", "kra", "bra", "vyna", "nala", "grya", "zara"]
consonant_to_consonant_syllables = ["dri", "glo", "tho", "sylu", "kri", "bre", "vyno", "nalu", "grye", "zaro"]
vocal_ending_syllables = ["a", "e", "i", "o", "u"]

# Función para generar un nombre de fantasía
def generate_fantasy_name():
    num_syllables = int(num_syllables_var.get())
    name = ""
    
    for _ in range(num_syllables):
        if name and name[-1] in 'aeiou':
            # La última sílaba terminó en vocal, así que elige entre vocal-to-vocal y vocal-to-consonant
            if random.choice([True, False]):
                syllable = random.choice(vocal_to_vocal_syllables)
            else:
                syllable = random.choice(vocal_to_consonant_syllables)
        else:
            # La última sílaba terminó en consonante, elige entre consonant-to-vocal y consonant-to-consonant
            if random.choice([True, False]):
                syllable = random.choice(consonant_to_vocal_syllables)
            else:
                syllable = random.choice(consonant_to_consonant_syllables)
        
        name += syllable

    # Añadir una sílaba vocal al final para suavizar el nombre
    name += random.choice(vocal_ending_syllables)
    
    output_name_var.set(name)

# Función para copiar el nombre generado al portapapeles
def copy_to_clipboard():
    generated_name = output_name_var.get()
    root.clipboard_clear()
    root.clipboard_append(generated_name)
    root.update()

# Crear la ventana principal
root = tk.Tk()
root.title("Generador de Nombres de Fantasía")

# Crear etiquetas y campos de entrada
num_syllables_label = ttk.Label(root, text="syllables number:")
num_syllables_var = tk.StringVar(value="2")
num_syllables_entry = ttk.Entry(root, textvariable=num_syllables_var)

output_name_var = tk.StringVar()
output_name_label = ttk.Label(root, text="generated number::")
output_name_entry = ttk.Entry(root, textvariable=output_name_var)

# Crear botones
generate_button = ttk.Button(root, text="generate number", command=generate_fantasy_name)
copy_button = ttk.Button(root, text="copy to clipboard", command=copy_to_clipboard)

# Colocar elementos en la ventana
num_syllables_label.grid(row=0, column=0, sticky="w")
num_syllables_entry.grid(row=0, column=1)

generate_button.grid(row=1, column=0, columnspan=2)
output_name_label.grid(row=2, column=0, sticky="w")
output_name_entry.grid(row=2, column=1)

copy_button.grid(row=3, column=0, columnspan=2)

# Iniciar la interfaz gráfica
root.mainloop()
