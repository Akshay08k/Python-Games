import tkinter as tk
from cryptography.fernet import Fernet
import pyperclip

class PasswordEncrypterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Encrypter and Descriptor")

        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)

        self.left_frame = tk.Frame(root, bg="#EFEFEF")  # Light gray background
        self.left_frame.pack(side=tk.LEFT, padx=20, pady=20)

        self.right_frame = tk.Frame(root, bg="#F5F5F5")  # Lighter gray background
        self.right_frame.pack(side=tk.LEFT, padx=20, pady=20)

        self.label = tk.Label(self.left_frame, text="Enter Password:", fg="#333333")  # Dark gray text
        self.label.pack()

        self.password_entry = tk.Entry(self.left_frame, show="*")
        self.password_entry.pack()

        self.encrypt_button = tk.Button(self.left_frame, text="Encrypt", command=self.encrypt_password, bg="#007ACC", fg="white")  # Blue background, white text
        self.encrypt_button.pack()

        self.encrypted_password_label = tk.Label(self.left_frame, text="", wraplength=250, fg="#333333")  # Dark gray text
        self.encrypted_password_label.pack()

        self.copy_button = tk.Button(self.left_frame, text="Copy Encrypted Password", command=self.copy_encrypted_password, bg="#007ACC", fg="white")  # Blue background, white text
        self.copy_button.pack()

        self.decrypt_label = tk.Label(self.right_frame, text="Enter Encrypted Password:", fg="#333333")  # Dark gray text
        self.decrypt_label.pack()

        self.encrypted_password_entry = tk.Entry(self.right_frame)
        self.encrypted_password_entry.pack()

        self.decrypt_button = tk.Button(self.right_frame, text="Decrypt", command=self.decrypt_password, bg="#007ACC", fg="white")  # Blue background, white text
        self.decrypt_button.pack()

        self.decrypted_password_label = tk.Label(self.right_frame, text="", wraplength=250, fg="#333333")  # Dark gray text
        self.decrypted_password_label.pack()

    def encrypt_password(self):
        password = self.password_entry.get().encode()
        encrypted_password = self.fernet.encrypt(password)
        self.encrypted_password_label.config(text=f"Encrypted Password: {encrypted_password.decode()}")

    def copy_encrypted_password(self):
        encrypted_password = self.encrypted_password_label.cget("text").split(": ")[1]
        pyperclip.copy(encrypted_password)

    def decrypt_password(self):
        encrypted_password = self.encrypted_password_entry.get()
        try:
            decrypted_password = self.fernet.decrypt(encrypted_password.encode()).decode()
            self.decrypted_password_label.config(text=f"Decrypted Password: {decrypted_password}")
        except:
            self.decrypted_password_label.config(text="Invalid encrypted password")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordEncrypterApp(root)
    root.mainloop()
