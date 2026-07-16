import sys
import os
import datetime
import traceback

try:
    import pdfplumber
    from pypdf import PdfReader
except ImportError:
    print("Error: Required libraries are not installed. Please install them using 'pip install pypdf pdfplumber'")
    sys.exit(1)

def extract_pdf_info(pdf_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = os.path.basename(pdf_path)
    title = os.path.splitext(filename)[0]
    output_md_path = os.path.join(output_dir, f"{title}.md")

    timestamp = datetime.datetime.now().isoformat()
    
    content = ""
    
    try:
        # Extract Text and Tables using pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            for page_idx, page in enumerate(pdf.pages):
                content += f"## Page {page_idx + 1}\n\n"
                
                # Extract Text
                text = page.extract_text()
                if text:
                    content += text + "\n\n"
                
                # Extract Tables
                tables = page.extract_tables()
                if tables:
                    for table_idx, table in enumerate(tables):
                        content += f"### Table {table_idx + 1}\n\n"
                        for row_idx, row in enumerate(table):
                            # Clean up None values and newlines
                            clean_row = [str(cell).replace('\n', ' ') if cell is not None else "" for cell in row]
                            content += "| " + " | ".join(clean_row) + " |\n"
                            
                            # Add markdown table separator after header
                            if row_idx == 0:
                                separator = ["---"] * len(clean_row)
                                content += "| " + " | ".join(separator) + " |\n"
                        content += "\n"

        # Extract Images using pypdf
        reader = PdfReader(pdf_path)
        for page_idx, page in enumerate(reader.pages):
            count = 0
            for image_file_object in page.images:
                try:
                    img_name = f"{title}_page_{page_idx + 1}_img_{count}_{image_file_object.name}"
                    img_path = os.path.join(output_dir, img_name)
                    
                    with open(img_path, "wb") as fp:
                        fp.write(image_file_object.data)
                        
                    content += f"### Image extracted from Page {page_idx + 1}\n\n"
                    # Relative path for the markdown link
                    content += f"![{image_file_object.name}]({img_name})\n\n"
                    
                    # TODO: Implement OCR here using pytesseract and Pillow
                    # e.g., text_from_img = pytesseract.image_to_string(Image.open(img_path))
                    # content += f"**OCR Text:**\n{text_from_img}\n\n"
                    
                    count += 1
                except Exception as e:
                    print(f"Warning: Failed to extract an image on page {page_idx + 1}. Error: {e}")

    except Exception as e:
        print(f"Error reading PDF {pdf_path}: {e}")
        traceback.print_exc()
        sys.exit(1)

    # Write the output markdown file with OKF YAML Frontmatter
    try:
        with open(output_md_path, 'w', encoding='utf-8') as f:
            f.write("---\n")
            f.write(f"title: \"{title}\"\n")
            f.write(f"timestamp: \"{timestamp}\"\n")
            f.write("---\n\n")
            f.write(content)
            
        print(f"Extraction complete. Results saved to {output_md_path}")
    except Exception as e:
        print(f"Error writing Markdown output: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract.py <input.pdf> <output_dir>")
        sys.exit(1)
        
    extract_pdf_info(sys.argv[1], sys.argv[2])
