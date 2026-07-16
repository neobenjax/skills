---
name: "extract-info"
description: "Extract information from a master resume PDF and update the knowledge-catalog. Triggers on 'Extract my information from this resume' or '/extract-info' and expects an attached resume."
---

# Extract Info Skill

This skill automates the process of extracting text from a master resume PDF, categorizing the data using a Python script, and then intelligently merging this data into the user's OKF YAML Frontmatter markdown catalog.

## Step 1: Ensure Prerequisites
First, verify that the `pypdf` library is installed by running:
`python -c "import pypdf"`

If it fails, install it via the terminal:
`pip install pypdf`

## Step 2: Extract PDF Information
Determine the path to the PDF the user wants to process. The user should have provided it in their prompt or as an attachment.
If you don't have the PDF file or path, ask the user to provide it.

Run the Python script to extract information from the PDF into a JSON file:
`python D:\AI\SKILLS\.agents\skills\extract-info\scripts\extract.py <input_pdf_path> D:\AI\SKILLS\.agents\skills\extract-info\extracted_resume.json`

## Step 3: Analyze the Output
Read the generated `extracted_resume.json` file. The top section of the resume (like personal info) will typically be found under the `"uncategorized"` key.
Next, review the existing markdown files in `D:\AI\SKILLS\knowledge-catalog`. These files use OKF YAML Frontmatter.

## Step 4: Map Information and Preview
Use your LLM capabilities to parse the JSON sections and map the details into the corresponding catalog markdown files (e.g. `experience.md`, `education.md`, `personal_info.md`).
- Present to the user a **summary** of where the extracted information should fit.
- Present a **preview** of every file's intended output (showing exactly how the file will look after changes). 
- **CRITICAL**: Do NOT modify the extracted JSON text, and do NOT modify the actual markdown files yet.

## Step 5: Ask for Approval
Stop executing tools and explicitly ask the user for approval. Wait for them to agree with the proposed changes.

## Step 6: Apply Changes
After the user approves, apply the changes to the markdown files in `D:\AI\SKILLS\knowledge-catalog`. Make sure to maintain the existing OKF YAML Frontmatter structure and append/merge the data correctly. Once done, inform the user that the operation is complete.
