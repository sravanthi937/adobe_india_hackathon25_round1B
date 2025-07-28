# selector_b.py - Adobe Round 1B Phase B

import os, json
import fitz  # PyMuPDF

# Folders
input_folder = "input"
output_folder = "output"

# Load Phase A result
with open(os.path.join(output_folder, "round1b_phaseA.json")) as f:
    result = json.load(f)

subsection_analysis = []

# For each top section, extract text from the relevant page
for section in result["extracted_sections"]:
    pdf_path = os.path.join(input_folder, section["document"])
    page_num = section["page_number"]

    try:
        doc = fitz.open(pdf_path)
        page = doc.load_page(page_num - 1)
        text = page.get_text().strip()
        refined = text[:500].replace("\n", " ") + "..." if len(text) > 500 else text
    except Exception as e:
        refined = f"Error reading page: {e}"

    subsection_analysis.append({
        "document": section["document"],
        "page_number": page_num,
        "refined_text": refined
    })

# Add refined snippets to result
result["subsection_analysis"] = subsection_analysis

# Save Phase B output
with open(os.path.join(output_folder, "round1b_phaseB.json"), "w") as f:
    json.dump(result, f, indent=2)

print("\n✅ Round 1B Phase B output saved to output/round1b_phaseB.json")
