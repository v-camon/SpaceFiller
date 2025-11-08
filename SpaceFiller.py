import os

import argparse


class File:

    def __init__(self, size_mb, output_file):
        self.block_1mb = b"\0" * (1024 * 1024)
        self.size_mb = size_mb
        self.size_bytes = self.size_mb * (1024 * 1024)
        self.outputFile = output_file

    def getSize(self):
        pass
        print(f"File size {fileSizeMB}MB")

    def isCorrect(self):
        if os.path.getsize(self.outputFile) == self.size_bytes:
            return True
        else:
            return False

    def ifExisting(self):
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
        print("File is existing. Closing")
        exit()

    file.create()

    if not file.isCorrect():
        print("File created but size is not correct")
        exit()

    print(f"File successfully created on {output_file} ")


if __name__ == "__main__":
    outputFile: str = "spaceFiller"
    fileSizeMB: int = 3
    main(fileSizeMB, outputFile)
