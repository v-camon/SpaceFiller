import os
import customtkinter as ctk
import tkinter.filedialog as fdialog

units = ["MB", "GB", "TB"]

fromMB = {"MB": 1, "GB": 1024, "TB": 1024**2}

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self) -> None:

        # WINDOW
        super().__init__()

        self.title("Space Filler")
        self.geometry("600x300")

        # COMPONENT
        self.size_frame = ctk.CTkFrame(
            master=self, corner_radius=0, border_width=2, fg_color="transparent"
        )
        self.size_entry = ctk.CTkEntry(
            master=self.size_frame,
            placeholder_text="test",
            corner_radius=0,
            border_width=0,
            fg_color="transparent",
        )
        self.size_unit = ctk.CTkComboBox(
            master=self.size_frame,
            values=units,
            corner_radius=0,
            border_width=0,
            justify="center",
            width=70,
        )

        self.save_frame = ctk.CTkFrame(
            master=self, corner_radius=0, border_width=2, width=215, height=28
        )
        self.save_frame.grid_propagate(False)
        self.save_frame.columnconfigure(1, weight=0)
        self.save_frame.columnconfigure(0, weight=1)
        self.save_label = ctk.CTkLabel(
            master=self.save_frame,
            text="",
            corner_radius=0,
            width=135,
            anchor="e",
        )
        self.save_button = ctk.CTkButton(
            master=self.save_frame,
            text="Destination",
            command=File.Location,
            corner_radius=0,
            border_width=0,
            width=80,
        )

        # POSITION
        self.size_frame.grid(row=0, column=0, padx=20, pady=10)
        self.size_entry.grid(row=0, column=0, padx=(2, 0), pady=2)
        self.size_unit.grid(row=0, column=1, padx=(0, 2), pady=2)

        self.save_frame.grid(row=1, column=0, padx=20, pady=10)
        self.save_label.grid(row=1, column=0)
        self.save_button.grid(row=1, column=1)


class File:
    def __init__(self, size_mb, output_file) -> None:
        self.block_1mb = b"\0" * (1024 * 1024)
        self.size_mb = size_mb
        self.size_bytes = self.size_mb * (1024 * 1024)
        self.outputFile = output_file

    def isCorrect(self) -> bool:
        if not os.path.exists(self.outputFile):
            return False

        if os.path.getsize(self.outputFile) != self.size_bytes:
            return False

        return True

    def ifExisting(self) -> bool:
        return os.path.exists(self.outputFile)

    def Location():
        location = fdialog.asksaveasfile()
        app.save_label.configure(text=location.name)

    def create(self):
        try:
            with open(self.outputFile, "wb") as file:
                for i in range(self.size_mb):
                    file.write(self.block_1mb)

        except IOError as err:
            print("--- ERROR ---")
            print(err)

        except KeyboardInterrupt:
            print("Process canceled by User")
            print("Deleting file...")
            exit()

            if os.path.exists(self.outputFile):
                os.remove(self.outputFile)
                print("File deleted")

        except Exception as err:
            print("--- Unexpected Error ---")
            print(err)


def main(size: int, output_file: str) -> None:
    file = File(size, output_file)
    file.create()
    print(f"File created on {output_file} with WRONG size")


if __name__ == "__main__":

    app = App()
    app.mainloop()
    # main(size, output)
