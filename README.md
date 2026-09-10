# 📚 Structure-Aware Research Paper Assistant

> An AI-powered full-stack RAG application that allows users to upload research papers, ask questions about them, and receive grounded answers based only on the content of the selected paper.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![React](https://img.shields.io/badge/React-18-61DAFB?logo=react)](https://react.dev/)
[![Node.js](https://img.shields.io/badge/Node.js-Express-green?logo=node.js)](https://nodejs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Database-47A248?logo=mongodb)](https://www.mongodb.com/)
[![FAISS](https://img.shields.io/badge/FAISS-Vector_Search-orange)](https://github.com/facebookresearch/faiss)
[![Gemini](https://img.shields.io/badge/Gemini-LLM-4285F4)](https://ai.google.dev/)

---

## 🎥 Demo

> **Demo video:** Add your screen-recorded demo here.

<!-- Replace the placeholder below with your uploaded demo GIF/video link -->

![Project Demo](docs/demo.gif)

---

## 📌 Overview

Research papers are often long, highly structured documents containing sections such as:

- Abstract
- Introduction
- Related Work
- Methodology
- Experiments
- Results
- Conclusion

Traditional RAG systems often split documents into fixed-size chunks without considering this structure.

This project uses a **structure-aware retrieval pipeline** that preserves research-paper sections during document processing.

Users can:

1. Create an account and log in securely.
2. Upload a research paper in PDF format.
3. Automatically process the paper.
4. Ask natural-language questions about the paper.
5. Retrieve the most relevant sections.
6. Receive an AI-generated answer grounded in the retrieved content.
7. Inspect the source sections, page numbers, snippets, and relevance scores.

The system also includes a **relevance gate** that prevents unrelated questions from being sent to the LLM.

---

# 🎯 Problem Statement

Generic PDF chatbots often suffer from:

- Poor chunk boundaries
- Loss of document structure
- Retrieval of semantically related but irrelevant content
- Hallucinated answers when information is not present
- Lack of source transparency

For research papers, document structure is particularly important because the same concept can have very different meanings depending on whether it appears in the methodology, results, or conclusion.

### Goal

Build a RAG system that combines:

**Document structure + semantic retrieval + relevance scoring + LLM generation**

to produce more reliable research-paper question answering.

---

# ✨ Key Features

## 📄 Research Paper Upload

Upload research papers in PDF format through the web interface.

The backend stores the document and sends it to the Python AI service for processing.

---

## 🧠 Structure-Aware PDF Processing

The PDF is processed using PyMuPDF.

The system extracts:

- Text
- Font information
- Font size
- Text flags
- Page numbers
- Layout coordinates

These elements are then used to identify document sections.

---

## 🧩 Structure-Aware Chunking

Instead of blindly splitting the entire PDF into fixed-size pieces, the system first identifies logical sections.

Example:

```text
Research Paper
│
├── Abstract
├── Introduction
├── Related Work
├── Methodology
├── Experiments
├── Results
└── Conclusion
