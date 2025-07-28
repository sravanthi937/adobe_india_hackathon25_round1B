

````markdown
# 🧠 Adobe India Hackathon 2025 – Round 1B

This project is submitted for **Round 1B** of the Adobe India Hackathon 2025. It builds upon structural PDF section extraction (Round 1A) and implements a **semantic section selector and content snippet generator** using `MiniLM` and modern NLP tools.

---

## 🚀 Problem Statement

Given academic PDFs and their outlines (from Round 1A), the task is to:

1. **Phase A**: Select the most relevant sections to a given query.
2. **Phase B**: Extract concise, relevant text snippets from the selected sections.

The goal is to help users **quickly locate meaningful content** in large research documents.

---

## 🧰 Tools & Libraries

- `PyMuPDF` (`fitz`) for PDF parsing
- `sentence-transformers` (MiniLM) for semantic similarity
- `scikit-learn` for scoring logic
- `Docker` for environment reproducibility

---

## 📁 Folder Structure

```bash
.
├── selector_a.py              # Phase A: Semantic section selection
├── selector_b.py              # Phase B: Snippet extraction
├── Dockerfile                 # Docker config for reproducibility
├── input/                     # Input PDFs and outline JSONs
│   ├── sample1.pdf
│   └── sample1.json           # Output from Round 1A
├── output/
│   ├── round1b_phaseA.json    # Selected sections
│   └── round1b_phaseB.json    # Extracted text snippets
└── README.md                  # This file
````

---

## 🔄 Pipeline Overview

### 🔹 Phase A: `selector_a.py`

* Loads section headings (from Round 1A `.json`)
* Uses `MiniLM` to embed:

  * Each section heading
  * A predefined or user-supplied **query**
* Calculates cosine similarity
* Selects top-k relevant sections

✅ Output → `round1b_phaseA.json`

---

### 🔹 Phase B: `selector_b.py`

* Reads selected sections from Phase A
* Loads corresponding PDF
* Extracts clean, readable text snippets from those pages
* (Optional) Summarization or filtering

✅ Output → `round1b_phaseB.json`

---

## 🐳 Dockerized Usage

### 1. Build the Docker image

```bash
docker build -t adobe-selector .
```

### 2. Run Phase A

```bash
docker run --rm ^
  -v "%cd%/input:/app/input" ^
  -v "%cd%/output:/app/output" ^
  adobe-selector python selector_a.py
```

### 3. Run Phase B

```bash
docker run --rm ^
  -v "%cd%/input:/app/input" ^
  -v "%cd%/output:/app/output" ^
  adobe-selector python selector_b.py
```

---

## 🧪 Sample Output Format

### 📄 `round1b_phaseA.json`

```json
{
  "top_sections": [
    { "text": "Methodology", "page": 3, "score": 0.91 },
    { "text": "Results", "page": 5, "score": 0.87 }
  ]
}
```

### 📄 `round1b_phaseB.json`

```json
{
  "snippets": [
    {
      "section": "Methodology",
      "page": 3,
      "text": "We conducted a longitudinal study with 50 participants..."
    },
    ...
  ]
}
```

---

## 👨‍💻 Author

**SRAVANTHI**
GitHub: [@sravanthi937](https://github.com/sravanthi937)
Submission for Adobe India Hackathon 2025 – Round 1B

---

## 📎 Related Repositories

🔗 [Round 1A – PDF Outline Extractor](https://github.com/sravanthi937/adobe_india_hackathon25_round1A)

---

## 🏁 Notes

* No internet is required during inference (except first-time model download).
* For offline use, pre-download `all-MiniLM-L6-v2` from HuggingFace.
* Tested with Python 3.9 in Docker


