import PyPDF2
import io


def extract_text_from_pdf(file_content: bytes) -> str:
  """
  Extract text from a PDF file given its content as bytes.

  Args:
      file_content (bytes): The content of the PDF file.

  Returns:
      str: The extracted text from the PDF.
  """
  pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_content))
  text = ""

  for page in pdf_reader.pages:
    text += page.extract_text() + "\n"

  return text.strip()
