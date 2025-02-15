import pytesseract
from PIL import Image
import re

# Path to the image
image_path = r"C:\data\credit_card.png"

# Set the path to tesseract.exe (if it's not already in PATH)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

try:
    # Open the image
    image = Image.open(image_path)

    # Extract text using Tesseract OCR
    extracted_text = pytesseract.image_to_string(image)

    # Extract only numbers and remove spaces
    extracted_numbers = re.sub(r"\D", "", extracted_text)  # Keep only digits

    # Save the extracted number to a file
    output_file = r"C:\data\credit-card.txt"
    with open(output_file, "w") as file:
        file.write(extracted_numbers)

    print(f"Extracted number saved to: {output_file}")

except FileNotFoundError:
    print("Error: File not found!")
except Exception as e:
    print(f"An error occurred: {e}")
