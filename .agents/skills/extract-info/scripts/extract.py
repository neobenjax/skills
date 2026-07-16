import sys
import json
import re

try:
    from pypdf import PdfReader
except ImportError:
    print("Error: pypdf library is not installed. Please install it using 'pip install pypdf'")
    sys.exit(1)

def extract_resume_info(file_path, output_json_path):
    text = ""
    if file_path.lower().endswith('.pdf'):
        try:
            reader = PdfReader(file_path)
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
        except Exception as e:
            print(f"Error reading PDF: {e}")
            sys.exit(1)
    else:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
        except Exception as e:
            print(f"Error reading text file: {e}")
            sys.exit(1)
            
    lines = text.split('\n')
    
    # Common resume headers
    common_headers = [
        "experience", "work experience", "professional experience", "employment history", "career history",
        "education", "academic background",
        "skills", "technical skills", "core competencies",
        "projects", "personal projects",
        "certifications", "licenses",
        "languages",
        "summary", "profile", "professional summary", "about me",
        "awards", "honors",
        "volunteer", "community service"
    ]
    
    def is_header(line):
        cleaned = line.strip().lower()
        if not cleaned:
            return False
        # Remove non-alphanumeric chars to check against common headers
        cleaned = re.sub(r'[^a-z0-9\s]', '', cleaned).strip()
        
        if cleaned in common_headers:
            return True
            
        # Check if line is all caps and reasonably short
        # This helps catch custom headers not in our common list
        stripped_line = line.strip()
        if stripped_line.isupper() and 3 <= len(stripped_line) <= 35:
            # Additional check to ensure it's not just a location or date (dates usually have numbers)
            if not any(char.isdigit() for char in stripped_line):
                return True
                
        return False

    sections = {"uncategorized": []}
    current_section = "uncategorized"
    
    for line in lines:
        stripped_line = line.strip()
        if not stripped_line:
            continue
            
        # We might encounter lines that are just dividers like "___" or "---"
        if re.match(r'^[-_=\*]{3,}$', stripped_line):
            continue
            
        if is_header(line):
            # Capitalize properly or just use the exact case
            current_section = stripped_line
            if current_section not in sections:
                sections[current_section] = []
        else:
            sections[current_section].append(stripped_line)
            
    # Clean up and join lines, trying to maintain readable formatting
    result = {}
    for section, content in sections.items():
        if content: # Only include non-empty sections
            result[section] = "\n".join(content)
            
    try:
        with open(output_json_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=4, ensure_ascii=False)
        print(f"Extraction complete. Results saved to {output_json_path}")
    except Exception as e:
        print(f"Error writing JSON output: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract.py <input.pdf> <output.json>")
        sys.exit(1)
        
    extract_resume_info(sys.argv[1], sys.argv[2])
