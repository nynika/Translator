import tkinter as tk                       #Tkinter is a standard Python library
from googletrans import Translator, LANGUAGES

def translate_text():
    input_lang = input_language_var.get().lower()
    output_lang = output_language_var.get().lower()
    text_to_translate = text_to_translate_var.get()

    if input_lang in LANGUAGES and output_lang in LANGUAGES:
        input_lang = LANGUAGES[input_lang]
        output_lang = LANGUAGES[output_lang]

        translation = Translator().translate(text_to_translate, src=input_lang, dest=output_lang)
        translated_text_var.set(translation.text)
    else:
        translated_text_var.set("Invalid languages")

# Create the main window
root = tk.Tk()
root.title("Simple Translator")

# Language selection
input_language_var = tk.StringVar()
output_language_var = tk.StringVar()

input_language_label = tk.Label(root, text="Input Language:")
input_language_label.grid(row=0, column=0, padx=5, pady=5)
input_language_entry = tk.Entry(root, textvariable=input_language_var)
input_language_entry.grid(row=0, column=1, padx=5, pady=5)

output_language_label = tk.Label(root, text="Output Language:")
output_language_label.grid(row=1, column=0, padx=5, pady=5)
output_language_entry = tk.Entry(root, textvariable=output_language_var)
output_language_entry.grid(row=1, column=1, padx=5, pady=5)

# Text to translate
text_to_translate_var = tk.StringVar()

text_entry_label = tk.Label(root, text="Text to Translate:")
text_entry_label.grid(row=2, column=0, padx=5, pady=5)
text_entry = tk.Entry(root, textvariable=text_to_translate_var, width=40)
text_entry.grid(row=2, column=1, padx=5, pady=5)

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate_text, bg="#4CAF50", fg="white")
translate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Translated text
translated_text_var = tk.StringVar()

result_label = tk.Label(root, text="Translated Text:")
result_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
result_entry = tk.Entry(root, textvariable=translated_text_var, state='readonly', width=40, bg="#f0f0f0")
result_entry.grid(row=4, column=1, padx=5, pady=5)

# Start the main loop
root.mainloop()
