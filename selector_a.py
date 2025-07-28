# selector_a.py - Adobe Round 1B Phase A

import os, json
from datetime import datetime
from sentence_transformers import SentenceTransformer, util

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Define persona and job
persona = "PhD Researcher in Computational Biology"
job = "Write a literature review on graph neural networks for drug discovery"
task_query = f"{persona}. Task: {job}"

# Folders
input_folder = "input"
output_folder = "output"

documents = []
sections = []

# Load section outlines from JSON (generated in Round 1A)
for file in os.listdir(input_folder):
    if file.endswith(".pdf"):
        json_name = file.replace(".pdf", ".json")
        json_path = os.path.join(output_folder, json_name)

        if not os.path.exists(json_path):
            continue

        with open(json_path) as f:
            data = json.load(f)

        for entry in data["outline"]:
            sections.append({
                "document": file,
                "text": entry["text"],
                "page": entry["page"]
            })
        documents.append(file)

# Compute semantic similarity
section_texts = [s["text"] for s in sections]
query_emb = model.encode(task_query, convert_to_tensor=True)
section_embs = model.encode(section_texts, convert_to_tensor=True)
cos_scores = util.cos_sim(query_emb, section_embs)[0]

# Rank sections
scored_sections = []
for idx, score in enumerate(cos_scores):
    scored_sections.append({
        "document": sections[idx]["document"],
        "page_number": sections[idx]["page"],
        "section_title": sections[idx]["text"],
        "importance_rank": float(score)
    })

scored_sections.sort(key=lambda x: x["importance_rank"], reverse=True)
top_sections = scored_sections[:10]

# Save result
result = {
    "input_documents": documents,
    "persona": persona,
    "job_to_be_done": job,
    "timestamp": datetime.now().isoformat(),
    "extracted_sections": top_sections
}

with open("output/round1b_phaseA.json", "w") as f:
    json.dump(result, f, indent=2)

print("\n✅ Round 1B Phase A output saved to output/round1b_phaseA.json")
