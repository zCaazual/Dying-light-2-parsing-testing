from tkinter import ttk
import customtkinter
from ui import MainEditor

if __name__ == "__main__":
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    root = customtkinter.CTk()

    # testing transparency
    root.attributes("-alpha", 0.9)

    dark_bg_color = "#2b2b2b"
    dark_fg_color = "white"
    dark_highlight_color = "#4f4f4f"
    dark_entry_bg_color = "#383838"

    root.configure(bg=dark_bg_color)
    root.option_add("*Background", dark_bg_color)
    root.option_add("*Foreground", dark_fg_color)
    root.option_add("*HighlightColor", dark_highlight_color)
    root.option_add("*EntryField.Background", dark_entry_bg_color)

    style = ttk.Style()
    style.configure("TLabel", background=dark_bg_color, foreground=dark_fg_color)
    style.configure("TFrame", background=dark_bg_color)
    style.configure("TButton", background=dark_highlight_color, foreground=dark_fg_color)
    style.configure("TEntry", fieldbackground=dark_entry_bg_color)
    root.geometry("800x510")
    root.resizable(True, True)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    custom_label_style = ttk.Style()
    custom_label_style.configure("CustomLabel.TLabel", foreground="black")

    app = MainEditor(root, style)
    root.mainloop()
