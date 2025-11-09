# SpaceFiller 📦

`SpaceFiller` is a simple, interactive Python utility to create dummy files of a specified size. It's perfect for testing disk space limitations, creating large placeholders for drive testing, or reserving a specific amount of space on a device.

This script was built to be robust, with a clean progress bar, input validation, and interactive prompts to prevent common errors.

---

## 🚀 Features

* **Custom Size:** Create a file of any size you specify in Megabytes (MB).
* **Interactive Prompts:**
    * Warns you if the target file already exists and asks for permission to overwrite (`[y/N]`).
    * Asks to retry (`[Y/n]`) if the file is created with an incorrect size.
* **Progress Bar:** Uses `tqdm` to show a real-time progress bar, including creation speed (MB/s) and estimated time.
* **Input Validation:** Ensures the size is always a positive number (at least 1 MB).
* **CLI-Driven:** Uses `argparse` for easy-to-use command-line arguments.

---

## 🔧 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/v-camon/FileSize.git](https://github.com/v-camon/FileSize.git)
    cd FileSize
    ```

2.  **Install the dependency:**
    This script has one dependency, `tqdm`, for the progress bar.
    ```bash
    pip install tqdm
    ```

---

## ⚙️ Usage

The script is controlled via command-line arguments. You can see all available options by running:

```bash
python SpaceFiller.py --help
```

### Arguments

* `-s, --size <MB>`: The size of the file to create, in Megabytes (MB).
    * *Default: 3*
* `-o, --output <PATH>`: The name and path of the file to create.
    * *Default: "spaceFiller"*

### Examples

**1. Run with default settings**
(Creates a 3MB file named `spaceFiller` in the current directory)
```bash
python SpaceFiller.py
```

**2. Run only with -s flag**
(Creates a 500MB file named `spaceFiller` in the current directory)
```bash
python SpaceFiller.py -s 500
```
**2. Run with -s and -o flags**
(Creates a 2048MB file on the E:\ drive)
```bash
python SpaceFiller.py --size 2048 --output "E:\filler.dat"
```
---

## 📈 Example Output

Running the script provides interactive feedback and a clear progress bar:

```bash
$ python SpaceFiller.py -s 100 -o test.dat
Creating file test.dat (100 MB)...
Creating test.dat: 100%|██████████| 100/100 [00:01<00:00, 85.12MB/s]
File created on test.dat
```
Example of an overwrite prompt:

```bash
$ python SpaceFiller.py -s 10
File exists. Do you want to Overwrite? [y/N]: n
Operation canceled.
```
---

## 📄 License

This project is licensed under the MIT License.