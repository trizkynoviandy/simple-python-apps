import tkinter as tk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.display = tk.Entry(self.master, width=18, justify="right", font=("Arial", 40), bg="#424242", fg="white")
        self.display.insert(0, "0")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            "%", "CE", "C", "DEL",
            "\u00b9/\u2093", "√", "\u0078\u00b2", "/",
            "7", "8", "9", "x",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "+/-", "0", ".", "=",
        ]
        row = 1
        col = 0
        for button in buttons:
            def callback(value=button):
                if self.display.get() == "0":
                    self.display.delete(0, tk.END)
                if value == "=":
                    result = eval(self.display.get())
                    self.display.delete(0, tk.END)
                    self.display.insert(0, str(result))
                elif value == "C":
                    self.display.delete(0, tk.END)
                    self.display.insert(0, "0")
                elif value == "DEL":
                    current_text = self.display.get()
                    self.display.delete(len(current_text)-1, tk.END)
                    if len(current_text) == 1:
                        self.display.insert(0, "0")
                elif value == "%":
                    current_text = self.display.get()
                    if current_text:
                        result = float(current_text) / 100
                        self.display.delete(0, tk.END)
                        self.display.insert(0, str(result))
                elif value == "√":
                    current_text = self.display.get()
                    if current_text:
                        result = math.sqrt(float(current_text))
                        self.display.delete(0, tk.END)
                        self.display.insert(0, str(result))
                elif value == "CE":
                    self.display.delete(0, tk.END)
                    self.display.insert(0, "0")
                elif value == "1/X":
                    current_text = self.display.get()
                    if current_text:
                        result = 1 / float(current_text)
                        self.display.delete(0, tk.END)
                        self.display.insert(0, str(result))
                elif value == "+/-":
                    current_text = self.display.get()
                    if current_text:
                        if current_text[0] == "-":
                            self.display.delete(0)
                        else:
                            self.display.insert(0, "-")
                elif value == "X\u00b2":
                    current_text = self.display.get()
                    if current_text:
                        result = float(current_text) ** 2
                        self.display.delete(0, tk.END)
                        self.display.insert(0, str(result))
                else:
                    self.display.insert(tk.END, value)
                    
            if button == "=":
                tk.Button(self.master, text=button, width=10, height=3, 
                          command=callback, bg="#3949ab", fg="white", highlightbackground="#64C755", 
                          font=("Arial", 15)).grid(row=row, column=col, padx=5, pady=5)
            elif button == "C" or button == "DEL":
                tk.Button(self.master, text=button, width=10, height=3,
                          command=callback, bg="#e53935", fg="white", highlightbackground="#64C755", 
                          font=("Arial", 15)).grid(row=row, column=col, padx=5, pady=5)
            else:
                tk.Button(self.master, text=button, width=10, height=3, 
                          command=callback, bg="#353535", fg="white", 
                          font=("Arial", 15)).grid(row=row, column=col, padx=5, pady=5)
            
            for x in range(10):
                z = str(x)
                if button == z:
                    tk.Button(self.master, text=button, width=10, height=3, 
                              command=callback, bg="#686868", fg="white", highlightbackground="#64C755", 
                              font=("Arial", 15)).grid(row=row, column=col, padx=5, pady=5)
 
            col += 1
            if col > 3:
                col = 0
                row += 1
                
root = tk.Tk()
app = Calculator(root)

root.configure(bg="#222222")
root.mainloop()