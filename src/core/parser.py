"""
parser.py

Reads a research paper and extracts its structure.

Author: Meghana
Project: Structure-Aware Multimodal Research Paper Assistant
"""

import fitz
from pathlib import Path
from typing import List, Dict


class PDFParser:

    def __init__(self, pdf_path: str):

        self.pdf_path = Path(pdf_path)

        if not self.pdf_path.exists():
            raise FileNotFoundError(
                f"{pdf_path} not found."
            )

        self.document = fitz.open(pdf_path)

    def get_total_pages(self) -> int:

        return len(self.document)

    def extract_text(self, page_number: int) -> str:

        page = self.document.load_page(page_number)

        return page.get_text()

    def extract_layout(self, page_number: int) -> Dict:

        page = self.document.load_page(page_number)

        return page.get_text("dict")

    def extract_layout_elements(
        self,
        page_number: int
    ) -> List[Dict]:

        layout = self.extract_layout(page_number)

        elements = []

        for block in layout["blocks"]:

            if "lines" not in block:
                continue

            for line in block["lines"]:

                for span in line["spans"]:

                    elements.append({

                        "page": page_number,

                        "text": span["text"],

                        "font": span["font"],

                        "font_size": span["size"],

                        "bbox": span["bbox"]

                    })

        return elements