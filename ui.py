import json
import tkinter as tk
from tkinter import filedialog, colorchooser, font, messagebox, ttk
import customtkinter
import functions
from functions import create_custom_ui
from functions import process_inventory


class MainEditor:
    def __init__(self, root, style):

        self.root = root
        self.root.title("Dying Light 2 Editor")
        self.style = style
        self.button_font_size_var = tk.StringVar()
        self.label_font_size_var = tk.StringVar()
        self.tab_font_size_var = tk.StringVar()
        self.all_font_size_var = tk.StringVar()
        self.settings_menu = None

        self.frame = customtkinter.CTkScrollableFrame(root)
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Create tabs !
        self.tabs = customtkinter.CTkTabview(self.frame)
        self.tabs.grid(row=0, column=0, sticky="nsew")
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.skills_tab = customtkinter.CTkScrollableFrame(self.tabs)
        self.skills_frame = self.tabs.add("Skills")

        self.skills_subtabs = customtkinter.CTkTabview(self.skills_frame)
        self.skills_subtabs.grid(row=0, column=0, sticky="nsew")
        self.skills_frame.grid_rowconfigure(0, weight=1)
        self.skills_frame.grid_columnconfigure(0, weight=1)

        self.skills_subtab1 = customtkinter.CTkScrollableFrame(self.skills_subtabs)
        self.skills_subtab1_frame = self.skills_subtabs.add("Base Skills")

        self.skills_subtab2 = customtkinter.CTkScrollableFrame(self.skills_subtabs)
        self.skills_subtab2_frame = self.skills_subtabs.add("Legend skills")

        self.skills_subtab3 = customtkinter.CTkScrollableFrame(self.skills_subtabs)
        self.skills_subtab3_frame = self.skills_subtabs.add("Skill Points")

        self.frame_skills = customtkinter.CTkFrame(self.skills_tab)  # Use self.skills_tab
        self.frame_skills.grid(row=0, column=0, sticky="nsew")
        self.frame_skills.grid_rowconfigure(0, weight=1)
        self.frame_skills.grid_columnconfigure(0, weight=1)

        self.tab1_tab = customtkinter.CTkScrollableFrame(self.tabs)
        self.tab1_frame = self.tabs.add("Experience")

        self.tab1_subtabs = customtkinter.CTkTabview(self.tab1_frame)
        self.tab1_subtabs.grid(row=0, column=0, sticky="nsew")
        self.tab1_frame.grid_rowconfigure(0, weight=1)
        self.tab1_frame.grid_columnconfigure(0, weight=1)

        self.tab1_subtab1 = customtkinter.CTkScrollableFrame(self.tab1_subtabs)
        self.tab1_subtab1_frame = self.tab1_subtabs.add("Player XP")

        self.inventory_tab = customtkinter.CTkScrollableFrame(self.tabs)
        self.inventory_frame = self.tabs.add("Inventory")

        self.inventory_subtabs = customtkinter.CTkTabview(self.inventory_frame)
        self.inventory_subtabs.grid(row=0, column=0, sticky="nsew")
        self.inventory_frame.grid_rowconfigure(0, weight=1)
        self.inventory_frame.grid_columnconfigure(0, weight=1)

        self.inventory_subtab1 = customtkinter.CTkScrollableFrame(self.inventory_subtabs)
        self.inventory_frame1 = self.inventory_subtabs.add("Weapons")

        self.inventory_subtab2 = customtkinter.CTkScrollableFrame(self.inventory_subtabs)
        self.inventory_frame2 = self.inventory_subtabs.add("Accessories")

        self.inventory_subtab3 = customtkinter.CTkScrollableFrame(self.inventory_subtabs)
        self.inventory_frame3 = self.inventory_subtabs.add("Consumables")

        self.inventory_subtab4 = customtkinter.CTkScrollableFrame(self.inventory_subtabs)
        self.inventory_frame4 = self.inventory_subtabs.add("Outfits")

        self.inventory_subtab5 = customtkinter.CTkScrollableFrame(self.inventory_subtabs)
        self.inventory_frame5 = self.inventory_subtabs.add("Materials")

        self.inventory_subtab6 = customtkinter.CTkScrollableFrame(self.inventory_subtabs)
        self.inventory_frame6 = self.inventory_subtabs.add("Valuables")

        self.inventory_subtab7 = customtkinter.CTkScrollableFrame(self.inventory_subtabs)
        self.inventory_frame7 = self.inventory_subtabs.add("Ammo")

        self.inventory_subtab8 = customtkinter.CTkScrollableFrame(self.inventory_subtabs)
        self.inventory_frame8 = self.inventory_subtabs.add("Bundles")

        self.tab3_tab = customtkinter.CTkScrollableFrame(self.tabs)
        self.tab3_frame = self.tabs.add("Backpack")

        self.backpack_subtabs = customtkinter.CTkTabview(self.tab3_frame)
        self.backpack_subtabs.grid(row=0, column=0, sticky="nsew")
        self.tab3_frame.grid_rowconfigure(0, weight=1)
        self.tab3_frame.grid_columnconfigure(0, weight=1)

        self.backpack_subtab1 = customtkinter.CTkScrollableFrame(self.backpack_subtabs)
        self.backpack_frame1 = self.backpack_subtabs.add("Weapons")

        self.backpack_subtab2 = customtkinter.CTkScrollableFrame(self.backpack_subtabs)
        self.backpack_frame2 = self.backpack_subtabs.add("Accessories")

        self.backpack_subtab3 = customtkinter.CTkScrollableFrame(self.backpack_subtabs)
        self.backpack_frame3 = self.backpack_subtabs.add("Consumables")

        self.backpack_subtab4 = customtkinter.CTkScrollableFrame(self.backpack_subtabs)
        self.backpack_frame4 = self.backpack_subtabs.add("Outfits")

        self.backpack_subtab5 = customtkinter.CTkScrollableFrame(self.backpack_subtabs)
        self.backpack_frame5 = self.backpack_subtabs.add("Materials")

        self.backpack_subtab6 = customtkinter.CTkScrollableFrame(self.backpack_subtabs)
        self.backpack_frame6 = self.backpack_subtabs.add("Valuables")

        self.backpack_subtab7 = customtkinter.CTkScrollableFrame(self.backpack_subtabs)
        self.backpack_frame7 = self.backpack_subtabs.add("Ammo")

        self.backpack_subtab8 = customtkinter.CTkScrollableFrame(self.backpack_subtabs)
        self.backpack_frame8 = self.backpack_subtabs.add("Bundles")

        self.campaign_tab = customtkinter.CTkScrollableFrame(self.tabs)
        self.campaign_frame = self.tabs.add("Campaign")

        self.campaign_subtabs = customtkinter.CTkTabview(self.campaign_frame)
        self.campaign_subtabs.grid(row=0, column=0, sticky="nsew")
        self.campaign_frame.grid_rowconfigure(0, weight=1)
        self.campaign_frame.grid_columnconfigure(0, weight=1)

        self.campaign_subtab1 = customtkinter.CTkScrollableFrame(self.campaign_subtabs)
        self.campaign_frame1 = self.campaign_subtabs.add("Campaign Data")

        self.player_tab = customtkinter.CTkScrollableFrame(self.tabs)
        self.player_frame = self.tabs.add("Player")

        self.player_subtabs = customtkinter.CTkTabview(self.player_frame)
        self.player_subtabs.grid(row=0, column=0, sticky="nsew")
        self.player_frame.grid_rowconfigure(0, weight=1)
        self.player_frame.grid_columnconfigure(0, weight=1)

        self.player_subtab1 = customtkinter.CTkScrollableFrame(self.player_subtabs)
        self.player_frame1 = self.player_subtabs.add("1")

        self.player_subtab2 = customtkinter.CTkScrollableFrame(self.player_subtabs)
        self.player_frame2 = self.player_subtabs.add("2")

        self.create_menu_bar()

        self.file_status_label = customtkinter.CTkLabel(root, text="No Save Opened", anchor="w")
        self.file_status_label.grid(row=1, column=0, columnspan=2, sticky="we", padx=10, pady=5)

    def load_translations(self):
        selected_language = self.selected_language.get()
        try:
            json_file_path = f'assets/localization/translations_{selected_language}.json'
            print(f"Loading translations from: {json_file_path}")
            with open(json_file_path, 'r', encoding='utf-8') as json_file:
                translations = json.load(json_file)
            print(f"Loaded translations: {translations}")
            return translations
        except FileNotFoundError:
            print(f"Translation file not found for language: {selected_language}")
            return {}

    def change_language(self):
        self.translations = self.load_translations()
        self.update_ui_texts()

    def update_ui_texts(self):
        translated_text = self.translations.get("file_status_label", "No Save Opened")
        self.file_status_label.configure(text=translated_text)

    def create_menu_bar(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.open_and_read_file)

        self.settings_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Settings", menu=self.settings_menu)

        self.tools_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Tools", menu=self.tools_menu)

        self.tools_menu.add_command(label="Open IDs", command=lambda: create_custom_ui())
        self.tools_menu.add_command(label="Parse Inventory IDs", command=lambda: process_inventory())

        self.language_menu = tk.Menu(self.settings_menu, tearoff=0)
        self.settings_menu.add_cascade(label="Change Language", menu=self.language_menu)

        self.selected_language = tk.StringVar()
        self.selected_language.set("English")

        self.language_menu.add_radiobutton(label="English", variable=self.selected_language, value="English")
        self.language_menu.add_radiobutton(label="Spanish", variable=self.selected_language, value="Spanish")

        # remove this and add command directly to option
        self.language_menu.add_command(label="Apply", command=self.change_language)

        font_menu_color = tk.Menu(self.settings_menu, tearoff=0)
        font_menu_color.add_command(label="Change Button Font Color", command=self.change_button_font_color)
        font_menu_color.add_command(label="Change Label Font Color", command=self.change_label_font_color)
        font_menu_color.add_command(label="Change Tab Font Color", command=self.change_tab_font_color)
        font_menu_color.add_command(label="Change All Font Colors", command=self.change_font_color)
        self.settings_menu.add_cascade(label="Font Color", menu=font_menu_color)

        font_size_menu = tk.Menu(self.settings_menu, tearoff=0)
        font_size_menu.add_command(label="Change Button Font Size", command=self.change_button_font_size)
        font_size_menu.add_command(label="Change Label Font Size", command=self.change_label_font_size)
        font_size_menu.add_command(label="Change Tab Font Size", command=self.change_tab_font_size)
        font_size_menu.add_command(label="Change All Font Sizes", command=self.change_all_font_size)

        font_size_menu = tk.Menu(self.settings_menu, tearoff=0)

        button_font_size_submenu = tk.Menu(font_size_menu, tearoff=0)
        label_font_size_submenu = tk.Menu(font_size_menu, tearoff=0)
        tab_font_size_submenu = tk.Menu(font_size_menu, tearoff=0)
        all_font_size_submenu = tk.Menu(font_size_menu, tearoff=0)

        for size in ["8", "10", "12", "14", "16", "18", "20", "22"]:
            button_font_size_submenu.add_radiobutton(
                label=size, variable=self.button_font_size_var, value=size,
                command=self.change_button_font_size)
            label_font_size_submenu.add_radiobutton(
                label=size, variable=self.label_font_size_var, value=size,
                command=self.change_label_font_size)
            tab_font_size_submenu.add_radiobutton(
                label=size, variable=self.tab_font_size_var, value=size,
                command=self.change_tab_font_size)
            all_font_size_submenu.add_radiobutton(
                label=size, variable=self.all_font_size_var, value=size,
                command=self.change_all_font_size)

        font_size_menu.add_cascade(label="Change Button Font Size", menu=button_font_size_submenu)
        font_size_menu.add_cascade(label="Change Label Font Size", menu=label_font_size_submenu)
        font_size_menu.add_cascade(label="Change Tab Font Size", menu=tab_font_size_submenu)
        font_size_menu.add_cascade(label="Change All Font Size", menu=all_font_size_submenu)
        self.settings_menu.add_cascade(label="Font Size", menu=font_size_menu)

        font_menu = tk.Menu(self.settings_menu, tearoff=0)

        change_button_font_menu = self.change_font(self.change_button_font)
        change_label_font_menu = self.change_font(self.change_label_font)
        change_tab_font_menu = self.change_font(self.change_tab_font)
        change_all_fonts_menu = self.change_font(self.change_all_fonts)

        font_menu.add_cascade(label="Change Button Font", menu=change_button_font_menu)
        font_menu.add_cascade(label="Change Label Font", menu=change_label_font_menu)
        font_menu.add_cascade(label="Change Tab Font", menu=change_tab_font_menu)
        font_menu.add_cascade(label="Change All Fonts", menu=change_all_fonts_menu)

        self.settings_menu.add_cascade(label="Change Font", menu=font_menu)

        about_menu = tk.Menu(menubar, tearoff=0)

        about_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "This is a work in progress "
                                                                                           "save editor for dying "
                                                                                           "light 2."
                                                                                           "\nIts super early in "
                                                                                           "development and only "
                                                                                           "contains"
                                                                                           "basic"
                                                                                           "\nfunctionality for now."
                                                                                           "\nIt may contain some "
                                                                                           "bugs but"
                                                                                           "it should go without saying"
                                                                                           "\nalways keep a backup "
                                                                                           "copy of"
                                                                                           "your gamesave before "
                                                                                           "modifying"
                                                                                           "it !"
                                                                                           "\nIf you have any questions"
                                                                                           "you can reach me at my "
                                                                                           "email"
                                                                                           "below."
                                                                                           "\nzCaazual123@gmail.com"))

        menubar.add_cascade(label="About", menu=about_menu)

        credits_menu = tk.Menu(menubar, tearoff=0)

        credits_menu.add_command(label="Credits",
                                 command=lambda: messagebox.showinfo("Credits", "- BETA Testing : Batang & "
                                                                                "Thxnder7"
                                                                                "\n- Help sorting IDs : Batang, Bub, "
                                                                                "Username0001 JcB\n  Skiller and the "
                                                                                "Save Wizard community"
                                                                                "\n- Help and "
                                                                                "support : Batang, Bub, Skiller & "
                                                                                "Method"
                                                                                "\n- And a special thanks to "
                                                                                "ZERO & RIA for their "
                                                                                "inspiration <3"))

        menubar.add_cascade(label="Credits", menu=credits_menu)

    def change_font_color(self):
        color = colorchooser.askcolor(parent=self.root, title="Select Font Color")
        if color[1]:
            self.style.configure("TButton", foreground=color[1])
            self.style.configure("TLabel", foreground=color[1])
            self.style.configure("TText", foreground=color[1])
            self.style.configure("TNotebook.Tab", foreground=color[1])

    def change_button_font_color(self):
        color = colorchooser.askcolor(parent=self.root, title="Select Button Font Color")
        if color[1]:
            self.style.configure("TButton", foreground=color[1])

    def change_label_font_color(self):
        color = colorchooser.askcolor(parent=self.root, title="Select Label Font Color")
        if color[1]:
            self.style.configure("TLabel", foreground=color[1])

    def change_tab_font_color(self):
        color = colorchooser.askcolor(parent=self.root, title="Select Tab Font Color")
        if color[1]:
            self.style.configure("TNotebook.Tab", foreground=color[1])

    def change_text_font_color(self):
        color = colorchooser.askcolor(parent=self.root, title="Select Text Font Color")
        if color[1]:
            self.style.configure("TText", foreground=color[1])

    def change_font_size(self, size):
        font = ("Courier New", size)
        self.style.configure(".", font=font)
        self.style.configure("TButton", font=font)
        self.style.configure("TLabel", font=font)
        self.style.configure("TText", font=font)
        self.style.configure("TNotebook.Tab", font=font)

    def change_all_font_size(self):
        selected_size = self.all_font_size_var.get()
        if selected_size:
            self.change_font_size(int(selected_size))

    def change_button_font_size(self):
        selected_size = self.button_font_size_var.get()
        if selected_size:
            self.change_button_font(("Courier New", int(selected_size)))

    def change_label_font_size(self):
        selected_size = self.label_font_size_var.get()
        if selected_size:
            self.change_label_font(("Courier New", int(selected_size)))

    def change_tab_font_size(self):
        selected_size = self.tab_font_size_var.get()
        if selected_size:
            self.change_tab_font(("Courier New", int(selected_size)))

    def change_button_font(self, font):
        self.style.configure("TButton", font=font)

    def change_label_font(self, font):
        self.style.configure("TLabel", font=font)

    def change_tab_font(self, font):
        self.style.configure("TNotebook.Tab", font=font)

    def change_all_fonts(self, font):
        self.style.configure("TButton", font=font)
        self.style.configure("TLabel", font=font)
        self.style.configure("TNotebook.Tab", font=font)

    def change_font(self, change_func):
        available_fonts = font.families()
        font_menu = tk.Menu(self.settings_menu, tearoff=0)
        for font_name in available_fonts:
            font_menu.add_command(label=font_name, command=lambda f=font_name: change_func((f, 8)))

        return font_menu

    def open_and_read_file(self):
        file_path = filedialog.askopenfilename()
        if not file_path:
            return

        functions.open_and_read_file(self.root, self.file_status_label, file_path, self)

        self.update_status_label(file_path)

    def update_status_label(self, text):
        self.file_status_label.configure(text=f"Save Opened: {text}")
        self.file_status_label.update()

    def update_ui_with_skills(self, parsed_data):
        row_counter = 1

        for skill_name, decimal_value in parsed_data:
            row_position = row_counter * 5 + 0
            string_label = ttk.Label(self.skills_subtab1_frame, text=skill_name)
            string_label.grid(row=row_position, column=0, padx=5, pady=5, sticky="w")

            byte_var = tk.StringVar(value=str(decimal_value))
            byte_entry = customtkinter.CTkEntry(self.skills_subtab1_frame, textvariable=byte_var)
            byte_entry.grid(row=row_position, column=1, padx=10, pady=5, sticky="w")

            row_counter += 1


if __name__ == "__main__":
    root = customtkinter.CTk()
    custom_label_style = ttk.Style()
    app = MainEditor(root, ttk.Style())
    root.mainloop()
