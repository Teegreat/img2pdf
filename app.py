import os
import img2pdf

input_dir = "C:/Users/user/Desktop/ENUGU_POL"
output_dir = "C:/Users/user/Desktop/ENUGU_POL_CONVERTED"


for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
        try:
            # Open the image file and convert it to PDF
            with open(os.path.join(input_dir, filename), "rb") as f:
                pdf_bytes = img2pdf.convert(f.read())

            # Save the PDF to the output directory with the same filename as the image file
            output_filename = os.path.splitext(filename)[0] + ".pdf"
            with open(os.path.join(output_dir, output_filename), "wb") as f:
                f.write(pdf_bytes)
        except Exception as e:
            print(f"Error converting file {filename}: {e}")
