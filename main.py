import customtkinter as ctk
import secrets
import string
import pyperclip

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class PasswordApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("SecurePassword")
        self.geometry("450x400")
        self.resizable(False, False)

        self.label_title = ctk.CTkLabel(self, text="Password Generator", font=("Roboto", 24, "bold"))
        self.label_title.pack(pady=20)

        self.result_frame = ctk.CTkFrame(self, fg_color="#2b2b2b", corner_radius=10)
        self.result_frame.pack(pady=10, padx=20, fill="x")
        
        self.label_pass = ctk.CTkLabel(self.result_frame, text="Press the button...", font=("Consolas", 18), text_color="#1fbcff")
        self.label_pass.pack(pady=15)

        self.slider_label = ctk.CTkLabel(self, text="Length: 16", font=("Roboto", 14))
        self.slider_label.pack()
        
        self.slider = ctk.CTkSlider(self, from_=8, to=32, number_of_steps=24, command=self.update_slider)
        self.slider.set(16)
        self.slider.pack(pady=10, padx=40, fill="x")

        self.btn_generate = ctk.CTkButton(self, text="GENERATE", font=("Roboto", 14, "bold"), 
                                         height=45, corner_radius=8, command=self.generate)
        self.btn_generate.pack(pady=20, padx=40, fill="x")

        self.btn_copy = ctk.CTkButton(self, text="Copy to Clipboard", fg_color="transparent", 
                                     border_width=2, text_color="white", command=self.copy)
        self.btn_copy.pack(pady=5)

    def update_slider(self, value):
        self.slider_label.configure(text=f"Length: {int(value)}")

    def generate(self):
        length = int(self.slider.get())
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password = "".join(secrets.choice(chars) for _ in range(length))
        self.label_pass.configure(text=password)

    def copy(self):
        password = self.label_pass.cget("text")
        if password != "Press the button...":
            pyperclip.copy(password)
            self.btn_copy.configure(text="COPIED!", text_color="#4CAF50")
            self.after(2000, lambda: self.btn_copy.configure(text="Copy to Clipboard", text_color="white"))

if __name__ == "__main__":
    app = PasswordApp()
    app.mainloop()
