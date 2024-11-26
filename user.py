import pytesseract
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def ensure_tesseract_installed():
  """Checks if Tesseract OCR is installed and raises an exception if not."""
  try:
    pytesseract.pytesseract.tesseract_cmd
  except Exception as e:
    raise Exception from e

def preprocess_image(image):
  """Preprocesses the image to improve OCR accuracy.

  Args:
    image: PIL Image object.

  Returns:
    Preprocessed image (grayscale and optionally deskewed).
  """
  # Convert to grayscale
  gray_image = image.convert('L')
  # Optionally apply deskewing (implement your preferred deskewing method here)
  # ...
  return gray_image

def extract_text_from_image(image_path):
  """Extracts text from an image using Tesseract OCR with error handling.

  Args:
    image_path: Path to the image file.

  Returns:
    Extracted text from the image, or an empty string if errors occur.
  """

  ensure_tesseract_installed()

  try:
    img = Image.open(image_path)
    preprocessed_img = preprocess_image(img)
    text = pytesseract.image_to_string(preprocessed_img)
    return text
  except Exception as e:
    print(f"Error extracting text: {e}")
    return ""

if __name__ == "__main__":
  image_path = input("Enter the path to the image: ")
  extracted_text = extract_text_from_image(image_path)
  if extracted_text:
    print(f"Extracted text:\n{extracted_text}")
  else:
    print("Failed to extract text.")