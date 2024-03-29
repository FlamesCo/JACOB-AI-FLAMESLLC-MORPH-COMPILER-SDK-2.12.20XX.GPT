import openai

# Set the API key
openai.api_key =  "sk-"

import tkinter as tk
from tkinter import filedialog

class TextEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set the window title
        self.title("MORPH [UNCOL COMPILER SDK 0.X.X] - Flames LLC 0.X")
        ## disable maximize button circle dot to not worknig
        self.resizable(False, False)

        # Create a text input for the user to enter a description of the desired code
        self.description_input = tk.Entry(self, width=30)
        self.description_input.pack()
        self.description_input.insert(0, "Enter code description")

        # Create a dropdown menu to select the programming language
        self.language_var = tk.StringVar(self)
        self.language_var.set("MORPHIC LANG ")  # default value
        self.language_dropdown = tk.OptionMenu(self, self.language_var, "MORPH UNCOL Universal Compiler SCP-603 EMULATOR, RUNS ON JACOB SITE FCP-00A","LANG DATA MODIFERIER V1.0 - MORPH COMPILER TURBO MODE. GENERATES UPDATES FOR THE COMPILER AND THE JACOB PROCESSER IN ITS VRAM TO CHAT WITH THE USER AND UPDATE","Morphic Query SDK Compiles MORPH CODE in any language using daisychain V0.1 self aware and updates itself on the fly""[JACOB IDE COMPILER RESIDES IN FLAMES LLC GIHUB REPO LEARNS FROM CHATTING IT SIMULATES SCP-603 [JACOB]]"," ChatGPT3.5 Turbo API | QUERIES JACOB API ENGLISH TO ANSII MORPHIC API","Python", "HTML", "C#", "Rust", "Morph Compiler LANG","Assembly","Autotranslate","Query Google", "OpenAI CODEX (BETA)")
        self.language_dropdown.pack()

        # Create a button to generate the code
        self.generate_button = tk.Button(self, text="Generate", command=self.generate_code)
        self.generate_button.pack()

        # Create a button to save the code
        self.save_button = tk.Button(self, text="Save", command=self.save_code)
        self.save_button.pack()

        # Create a text area to display the generated code
        self.code_display = tk.Text(self)
        self.code_display.pack()

    def generate_code(self):
        # Get the user's input description and selected programming language
        description = self.description_input.get()
        language = self.language_var.get()

        # Use the ChatGPT API to generate the code
        response = openai.Completion.create(
            engine="code-davanci-002",
            prompt=f"Write a {language} program that {description}",
            temperature=0,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        code = response["choices"][0]["text"]

        # Display the generated code
        self.code_display.delete(1.0, tk.END)
        self.code_display.insert(1.0, code)

    def save_code(self):
        # Open a file dialog to choose where to save the code
        file_path = filedialog.asksaveasfilename()

        # Write the code to the file
        with open(file_path, "w") as f:
            f.write(self.code_display.get(1.0, tk.END))

text_editor = TextEditor()
text_editor.mainloop()