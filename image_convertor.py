from PIL import Image
from pathlib import Path
import os
import sys

# ------------------------
# Console setup
# ------------------------

os.system("title Image Convertor.py")
os.system("color 1")

print("Starting imageconvertorpy...\n")

# Get the folder where the EXE or script is located
if getattr(sys, "frozen", False):
    BASE_DIR = Path(sys.executable).parent
else:
    BASE_DIR = Path(__file__).parent

# Create Images folder if it doesn't exist
OUTPUT_FOLDER = BASE_DIR / "Images"
OUTPUT_FOLDER.mkdir(exist_ok=True)


def convert_image(input_path, output_extension):
    input_path = Path(input_path)

    if not input_path.exists():
        print("Error: File not found.")
        return

    output_extension = output_extension.lower().replace(".", "")

    output_path = OUTPUT_FOLDER / f"{input_path.stem}.{output_extension}"

    try:
        with Image.open(input_path) as img:
            if output_extension in ("jpg", "jpeg"):
                img = img.convert("RGB")

            img.save(output_path)

        print("\nSuccessfully converted!")
        print(f"Saved to: {output_path}")

    except Exception as e:
        print(f"\nError while converting image:\n{e}")


# ------------------------
# User Input
# ------------------------

file_path = input("Enter the image path: ").strip().strip('"')
extension = input("Convert to (png, jpg, jpeg, bmp, gif, webp, etc.): ").strip()

convert_image(file_path, extension)

print("\nConverted successfully, check Images folder.")
input("\nPress Enter to exit...")