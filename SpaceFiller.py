import os
import time
import customtkinter as ctk
import tkinter.filedialog as fdialog

UNITS = ["MB", "GB"]

TO_MB = {"MB": 1, "GB": 1024}

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")



class File:
    def __init__(self, size_mb: int, output_file: str) -> None:
        self.size_mb = int(size_mb)
        self.output_file = output_file
        self.block_1mb = b"\0" * (1024 * 1024)

    def create(self, progress=None):
        try:
            with open(self.output_file, "wb") as file:
                for i in range(self.size_mb):
                    file.write(self.block_1mb)

                    if progress:
                        progress(i + 1)

        except IOError as err:
            raise IOError({err})
        
        except Exception as err:
            raise IOError({err})


class App(ctk.CTk):
    def __init__(self) -> None:

        # --- WINDOW CREATION ---
        super().__init__()

        # --- WINDOW CONFIG ---
        self.title("Space Filler")
        self.geometry("500x350")
        self.resizable(False, False)
        self.iconbitmap("logo.ico")

        # --- CONTENT CENTER ---
        self.columnconfigure(0, weight=1)  # EMPTY
        self.columnconfigure(1, weight=3)  # CONTENT
        self.columnconfigure(2, weight=1)  # EMPTY

        # --- UI COMPONENTS ---
        self.create_title()
        self.create_size_input()
        self.create_file_input()
        self.create_launch_button()
        self.create_status_label()
        
        self.progress_bar = ctk.CTkProgressBar(
            master=self, 
            width=300, 
            height=15,
            mode="determinate",
        )
        self.progress_bar.set(0) # Empezar en 0%

        
        self.error_color = "#DA2C00"
        
        
        

    def create_title(self):
        self.title_label = ctk.CTkLabel(
            master=self, text="Space Filler", font=("Roboto", 24, "bold")
        )
        self.title_label.grid(row=0, column=1, pady=(20, 20), sticky="ew")

    def create_size_input(self):
        self.size_frame = ctk.CTkFrame(
            master=self, corner_radius=8, border_width=0, fg_color="transparent"
        )
        self.size_frame.grid(row=1, column=1, padx=20, pady=15, sticky="ew")

        self.size_frame.columnconfigure(0, weight=1)
        self.size_frame.columnconfigure(1, weight=0)

        self.size_entry = ctk.CTkEntry(
            master=self.size_frame,
            placeholder_text="Size (ex. 100)",
            corner_radius=6,
            border_width=0,
            fg_color=("gray90", "gray20"),
            height=35,
        )
        self.size_entry.grid(row=0, column=0, padx=(0, 5), sticky="ew")

        self.size_unit = ctk.CTkComboBox(
            master=self.size_frame,
            values=UNITS,
            corner_radius=8,
            border_width=0,
            justify="center",
            width=100,
            height=35,
        )
        self.size_unit.grid(row=0, column=1)

    def create_file_input(self):
        self.file_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.file_frame.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

        # self.file_frame = ctk.CTkFrame(master=self, corner_radius=0, border_width=0)

        self.file_frame.columnconfigure(0, weight=1)
        self.file_frame.columnconfigure(1, weight=0)

        self.file_path = ctk.StringVar(value="")
        self.file_label = ctk.CTkLabel(
            master=self.file_frame,
            textvariable=self.file_path,
            fg_color=("gray90", "gray20"),
            corner_radius=6,
            height=35,
            anchor="e",
        )
        self.file_label.grid(row=0, column=0, sticky="ew", padx=(0, 5))

        self.file_button = ctk.CTkButton(
            master=self.file_frame,
            text="SAVE AS",
            # command=File.Location,
            command=self.select_location,
            width=100,
            height=35,
        )
        self.file_button.grid(row=0, column=1)

    def create_launch_button(self):
        self.create_button = ctk.CTkButton(
            master=self,
            text="CREATE FILE",
            command=self.start_creation,
            height=40,
            font=("Roboto", 14, "bold"),
        )
        self.create_button.grid(row=3, column=1, padx=20, pady=(20, 10), sticky="ew")

    def create_status_label(self):
        self.status_label = ctk.CTkLabel(
            master=self,
            text="Waiting for file destination",
            text_color="gray",
            font=(
                "Roboto",
                14,
            ),
        )
        self.status_label.grid(row=4, column=1, pady=10)

    def select_location(self):
        location = fdialog.asksaveasfilename(
            defaultextension=".sf",
            filetypes=[("Space Filer", "*.sf"), ("All files", "*.*")]
        )
        if location:
            self.file_path.set(location)

    def start_creation(self):
        size_str = self.size_entry.get()
        unit = self.size_unit.get()
        path = self.file_path.get()

        if not size_str.isdigit():
            self.status_label.configure(text="Size must be a number", text_color=self.error_color)
            return
        
        if not path:
            self.status_label.configure(text="Select a location to save the file", text_color=self.error_color)
            return
        
        try:
            total_mb = int(size_str) * TO_MB[unit]
            
            self.status_label.grid_forget()
            self.progress_bar.grid(row=4, column=1, pady=15)
            self.progress_bar.set(0)
            self.update()
            
            
            def update_proges_bar(current_mb):
                percent = current_mb / total_mb
                self.progress_bar.set(percent)
                self.update()
            
            file = File(total_mb, path)
            file.create(update_proges_bar)
            
            self.progress_bar.grid_forget()
            self.status_label.grid(row=4, column=1, pady=10) # Vuelve la etiqueta
            self.status_label.configure(text=f"File created ({total_mb} MB)", text_color="green")
            
        except  Exception as e:
            self.status_label.configure(text=f"Error: {str(e)}", text_color=self.error_color)


if __name__ == "__main__":

    app = App()
    app.mainloop()
