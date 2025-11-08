import os

import argparse


def prompt_yes_no(question: str, default_yes: bool) -> bool:
    positive_answer = ["y", "yes"]
    negative_answer = ["n", "no"]

    if default_yes:
        prompt: str = f"{question} [Y/n]: "
    else:
        prompt: str = f"{question} [y/N]: "

    user_response = input(prompt).strip().lower()

    if default_yes:
        if user_response in negative_answer:
            return False
        else:
            return True

    if not default_yes:
        if user_response in positive_answer:
            return True
        else:
            return False


class File:

    def __init__(self, size_mb, output_file):
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
            print("Deleting file")

            if os.path.exists(self.outputFile):
                os.remove(self.outputFile)
                print("File deleted")

        except Exception as err:
            print("--- Unexpected Error ---")
            print(err)


def main(size: int, output_file: str):
    file = File(size, output_file)

    if file.ifExisting():
        if not prompt_yes_no("File is existing do you want to Overwrite", False):
            print("File would not be Overwrite closing")
            return

        print("Overwriting file...")

    file.create()

    if file.isCorrect():
        print(f"File created on {output_file} ")
        return

    if prompt_yes_no(
        "File was created but size was not the expected. \nDo you want to retry",
        True,
    ):
        print("Retrying...")
        main(size, output_file)
    else:
        print(f"File created on {output_file} with WRONG size")
        return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="SpaceFiller: Creates a dummy file of a specified size.",
        epilog="Example: python SpaceFiller.py -s 100 -o D:\\kindle_spacer.dat",
    )


    parser.add_argument(
        "-s",
        "--size",
        type=int,
        default=3, 
        help="The size of the file to create, in Megabytes (MB). Default is 3.",
    )


    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="spaceFiller",
        help="The name (and path) of the file to create. Default is 'spaceFiller'.",
    )

    args = parser.parse_args()

    main(args.size, args.output)
