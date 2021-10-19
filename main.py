import tkinter as tk
import string
import secrets


class App(tk.Frame):
    PASSWORD_LENGTH = 12

    def __init__(self, master):
        tk.Frame.__init__(self, master)               
        
        self.tkroot = master
        self.tkroot.title("Simple Password Generator")
        self.tkroot.geometry("380x200")
        self.tkroot.eval('tk::PlaceWindow . center')

        self.title = tk.Label(text="Generate Password", font=("Helvetica", 18))
        self.title.grid(column=0, row=1, pady=20, columnspan=3)

        self.entry = tk.Entry(self, font=("Helvetica", 18),bd=0, width=18, justify='center')
        self.entry.grid(column=1, row=2, pady=20)

        self.generate_icon = tk.PhotoImage(file="images/generate.png", width=30, height=30)
        self.generate_button = tk.Button(self, text="Generate Password", image=self.generate_icon, command=self.show_password, font=("Helvetica", 14))
        self.generate_button.grid(column=2,row=2, padx=10)

        self.copy_icon = tk.PhotoImage(file="copy.png", width=30, height=30)
        self.copy_button = tk.Button(self, text="Copy", image=self.copy_icon, command=self.copy_to_clipboard, font=("Helvetica", 14), width=30)
        self.copy_button.grid(column=3,row=2)

        self.label = tk.Label(self, text="")
        self.label.grid(column=1, row=3)
        
        self.tkroot.grid_rowconfigure(0)
        self.tkroot.grid_rowconfigure(4)
        self.tkroot.grid_columnconfigure(0, weight=1)
        self.tkroot.grid_columnconfigure(4, weight=1)
            
    def show_password(self):
        password = self.generate_password()
        self.clear_text()
        self.entry.insert(0, password)
        self.hide_copy_to_clipboard()
               

    def generate_password(self):
        length = self.PASSWORD_LENGTH
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(length))    
        return password
    
    def clear_text(self):
        self.entry.delete(0, 'end')

    def copy_to_clipboard(self):
        self.tkroot.clipboard_clear()
        self.tkroot.clipboard_append(self.entry.get())
        print(self.entry.get())
        self.show_copy_to_clipboard()  

    def show_copy_to_clipboard(self):
        self.label.config(text="Password copied to clipboard!")

    def hide_copy_to_clipboard(self):
        self.label.config(text="")
            
def main():
    root = tk.Tk()
    App(root).grid()
    root.mainloop()

if __name__ == "__main__":
    main()
    

