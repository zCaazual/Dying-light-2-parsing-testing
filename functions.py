import logging
import re
import tkinter as tk
from tkinter import messagebox, filedialog
import customtkinter
import os

BACKUP_FOLDER_NAME = 'Backup'

# will change these names in the future
start_sequence = bytes.fromhex("416E74697A696E4361706163697479557067726164655374616D696E615F736B696C6C")
end_sequence = bytes.fromhex("50726F6772657373696F6E53746174653A3A45456C656D656E7456657273696F6E")


def open_and_read_file(root, file_status_label, file_path, ui_instance):
    try:

        if not file_path:
            raise ValueError("File not selected")

        file_directory = os.path.dirname(file_path)

        backup_folder_path = os.path.join(file_directory, BACKUP_FOLDER_NAME)

        if not os.path.exists(backup_folder_path):
            os.makedirs(backup_folder_path)

        backup_file_path = os.path.join(backup_folder_path, os.path.basename(file_path))
        if os.path.exists(backup_file_path):
            response = messagebox.askyesno("File Already Backed Up",
                                           f"A backup of the file '{os.path.basename(file_path)}' already exists. Do "
                                           f"you want to replace it?")
            if not response:
                return

        with open(file_path, 'rb') as file:
            file_contents = bytearray(file.read())

        parsed_data = parse_and_print_data(file_contents, start_sequence, end_sequence)

        ui_instance.update_ui_with_skills(parsed_data)

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: Permission denied to open file: {e}")
    except IOError as e:
        print(f"Error: Input/output error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def read_file_with_timeout(file_path):
    try:
        with open(file_path, 'r') as input_file:
            return input_file.read()
    except Exception as e:
        print(f"Error while processing file: {file_path}\nError message: {str(e)}")
        return None


def process_inventory():
    input_folder = filedialog.askdirectory(title="Select the folder for parsing keywords")
    if not input_folder:
        print("No folder selected. Exiting.")
        return

    output_file_path = filedialog.asksaveasfilename(defaultextension=".txt", title="Save Output File")
    if not output_file_path:
        print("No output file selected. Exiting.")
        return

    if not os.path.exists(input_folder):
        raise ValueError(f"The '{input_folder}' folder does not exist.")

    with open(output_file_path, 'w') as output_file:
        for dirpath, dirnames, filenames in os.walk(input_folder):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                print("Processing file:", file_path)

                print("Reading file content:", file_path)
                file_content = read_file_with_timeout(file_path)
                if file_content is None:
                    print(f"Error reading file: {file_path}")
                    continue

                print("Searching for lines:", file_path)
                try:
                    for line in file_content.splitlines():
                        if 'Item("' in line and 'RequiredItem("' not in line:
                            output_file.write(line[line.index('Item("'):])
                            output_file.write('\n')
                except Exception as extraction_error:
                    print("Error extracting lines:", extraction_error)

    print("Processing complete.")


def display_text(text_widget, file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        text_widget.delete("1.0", "end")
        text_widget.insert("1.0", text)


def search_text(event, search_entry, text_widget):
    logging.debug(f"Searching for {search_entry.get().lower()}")
    search_term = search_entry.get()
    text_widget.tag_remove("search", "1.0", "end")
    if search_term:  # only perform search if search term is not empty
        # find the first instance of search term in text widget, ignoring case
        start_index = text_widget.search(search_term, "1.0", nocase=1, stopindex="end")
        if start_index:
            end_index = f"{start_index}+{len(search_term)}c"
            text_widget.tag_add("search", start_index, end_index)
            text_widget.tag_config("search", background="yellow", foreground="black")
            text_widget.tag_remove("sel", "1.0", "end")
            text_widget.tag_add("sel", start_index, end_index)
            text_widget.see(start_index)
        else:
            messagebox.showinfo("Keyword not found", f"The keyword '{search_term}' was not found.")
    else:
        text_widget.tag_remove("sel", "1.0", "end")
        text_widget.yview_moveto(0)


def next_match(search_entry, text_widget):
    search_term = search_entry.get()
    text_widget.tag_remove("sel", "1.0", "end")
    start_index = text_widget.index("search.last")
    next_index = text_widget.search(search_term, f"{start_index}+1c", stopindex="end", nocase=1)
    if next_index:
        text_widget.tag_remove("search", "1.0", "end")
        text_widget.tag_add("search", next_index, f"{next_index}+{len(search_term)}c")
        text_widget.tag_config("search", background="yellow", foreground="black")
        text_widget.tag_add("sel", next_index, f"{next_index}+{len(search_term)}c")
        text_widget.see(next_index)
        text_widget.mark_set("search.last", next_index)
    else:
        all_matches = text_widget.search(search_term, "1.0", stopindex="end", nocase=1)
        if not all_matches:
            messagebox.showinfo("No Matches", "The search term was not found.")
        else:
            messagebox.showinfo("End of Document", "Reached end of document")
            text_widget.mark_set("search.last", "1.0")


def prev_match(search_entry, text_widget):
    search_term = search_entry.get()
    text_widget.tag_remove("sel", "1.0", "end")
    start_index = text_widget.index("search.first")
    prev_index = text_widget.search(search_term, f"{start_index}-1c", stopindex="1.0", nocase=1, backwards=True)
    if prev_index:
        text_widget.tag_remove("search", "1.0", "end")
        text_widget.tag_add("search", prev_index, f"{prev_index}+{len(search_term)}c")
        text_widget.tag_config("search", background="yellow", foreground="black")
        text_widget.tag_add("sel", prev_index, f"{prev_index}+{len(search_term)}c")
        text_widget.see(prev_index)
        text_widget.mark_set("search.first", prev_index)
    else:
        messagebox.showinfo("Start of Document", "Reached start of document")


def create_custom_ui():
    top = customtkinter.CTkToplevel()
    top.title("Dying light 2 All Item IDs")
    top.geometry("800x450")

    main_frame = customtkinter.CTkScrollableFrame(top, width=800, height=500)
    main_frame.grid(row=0, column=0, sticky="nsew")

    text_frame = tk.Frame(main_frame)
    text_frame.grid(row=0, column=0, sticky="nsew")

    text_widget = tk.Text(text_frame, wrap="none", borderwidth=0)
    text_widget.pack(fill="both", expand=True)

    text_widget.insert("end", "Please Click a button to display the IDs.\n" * 1)

    buttons_frame = tk.Frame(main_frame)
    buttons_frame.grid(row=1, column=0, sticky="nsew")

    button_commands = {}

    text_files_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "IDs")
    text_file_names = [f for f in os.listdir(text_files_dir) if f.endswith(".txt")]

    for i, file_name in enumerate(text_file_names):
        text_file_path = os.path.join(text_files_dir, file_name)
        command = lambda file=text_file_path: display_text(text_widget, file)
        button_commands[file_name] = command

    buttons_per_row = 6
    max_buttons = 12

    for i, (text, command) in enumerate(button_commands.items()):
        if i >= max_buttons:
            break

        row = i // buttons_per_row
        column = i % buttons_per_row

        button = customtkinter.CTkButton(buttons_frame, text=text, width=10, height=25, border_width=0, corner_radius=8,
                                         hover_color="green", hover=True, command=command)
        button.grid(row=row, column=column, padx=10, pady=5, sticky="sw")

    navigation_frame = tk.Frame(main_frame)
    navigation_frame.grid(row=2, column=0, sticky="nsew")

    search_label = tk.Label(navigation_frame, text="Search Keyword:")
    search_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    search_entry = customtkinter.CTkEntry(navigation_frame)
    search_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

    search_entry.bind("<KeyRelease>", lambda event: search_text(event, search_entry, text_widget))

    next_button = customtkinter.CTkButton(navigation_frame, text="Next", width=10, height=25, border_width=0,
                                          corner_radius=8, hover_color="green", hover=True,
                                          command=lambda: next_match(search_entry, text_widget))
    next_button.grid(row=0, column=2, padx=10, pady=5, sticky="e")

    previous_button = customtkinter.CTkButton(navigation_frame, text="Previous", width=10, height=25, border_width=0,
                                              corner_radius=8, hover_color="green", hover=True,
                                              command=lambda: prev_match(search_entry, text_widget))
    previous_button.grid(row=0, column=3, padx=10, pady=5, sticky="w")

    top.mainloop()


def parse_and_print_data(file_contents, start_sequence, end_sequence):
    start_index = file_contents.find(start_sequence)
    end_index = file_contents.find(end_sequence)

    if start_index != -1 and end_index != -1:
        data_between_sequences = file_contents[start_index:end_index + len(end_sequence)]

        pattern = b'([A-Za-z0-9_]+_skill)(..)'
        matches = re.findall(pattern, data_between_sequences)

        skip_data = False

        parsed_data = []

        for match in matches:
            full_string_bytes = match[0]
            two_bytes_after = match[1]

            if b'SGDs' in full_string_bytes:
                skip_data = True
            elif not skip_data:
                value = int.from_bytes(two_bytes_after, byteorder='little')

                parsed_data.append((full_string_bytes.decode('utf-8'), value))

                print(f"{full_string_bytes.decode('utf-8')}: {value}")

        return parsed_data

    else:
        print("Start and/or end sequence not found in the file.")