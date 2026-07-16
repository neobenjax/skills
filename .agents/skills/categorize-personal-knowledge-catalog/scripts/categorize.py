import sys
import json
import re

def categorize_markdown_content(file_path, output_json_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception as e:
        print(f"Error reading Markdown file: {e}")
        sys.exit(1)
        
    # Strip OKF YAML frontmatter if present
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            # part[0] is empty string, part[1] is frontmatter, part[2] is content
            text = parts[2].strip()
            
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
        # We also want to treat markdown headers (## Header) as headers, 
        # but the original logic stripped symbols, so it's somewhat compatible.
        # Let's cleanly handle markdown headers first.
        header_match = re.match(r'^(#{1,6})\s+(.*)$', line.strip())
        if header_match:
            cleaned = header_match.group(2).strip().lower()
        else:
            cleaned = line.strip().lower()
            
        if not cleaned:
            return False
            
        # Remove non-alphanumeric chars to check against common headers
        cleaned = re.sub(r'[^a-z0-9\s]', '', cleaned).strip()
        
        if cleaned in common_headers:
            return True
            
        # Check if line is all caps and reasonably short
        stripped_line = line.strip()
        if stripped_line.isupper() and 3 <= len(stripped_line) <= 35:
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
            # Extract header text if it's a markdown header
            header_match = re.match(r'^(#{1,6})\s+(.*)$', stripped_line)
            if header_match:
                section_name = header_match.group(2).strip()
            else:
                section_name = stripped_line
                
            current_section = section_name
            if current_section not in sections:
                sections[current_section] = []
        else:
            sections[current_section].append(stripped_line)
            
    # Clean up and join lines
    result = {}
    for section, content in sections.items():
        if content: # Only include non-empty sections
            result[section] = "\n".join(content)
            
    try:
        with open(output_json_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=4, ensure_ascii=False)
        print(f"Categorization complete. Results saved to {output_json_path}")
    except Exception as e:
        print(f"Error writing JSON output: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python categorize.py <input.md> <output.json>")
        sys.exit(1)
        
    categorize_markdown_content(sys.argv[1], sys.argv[2])
