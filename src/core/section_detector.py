"""
section_detector.py

Detects section headings in research papers using
simple layout heuristics.

Author: Meghana
Project: Structure-Aware Multimodal Research Paper Assistant
"""

import re
from typing import List, Dict


class SectionDetector:

    def __init__(self):
        pass

    def is_section_heading(self, element: Dict, body_font: float) -> bool:
        """
        Returns True if the given text span is likely to be
        a section heading.
        """

        text = element["text"].strip()

        if not text:
            return False

        # Ignore arXiv metadata
        if text.lower().startswith("arxiv:"):
            return False

        # Ignore pure numbers
        if text.isdigit():
            return False

        # Ignore decimal numbers like 28.4, 91.3
        try:
            float(text)
            return False
        except ValueError:
            pass

        # Ignore long paragraphs
        if len(text) > 80:
            return False

        size = element["font_size"]
        font = element["font"].lower()

        # -----------------------------
        # Paper Title
        # -----------------------------
        if size >= body_font + 5 and len(text) < 120:
            return True

        # -----------------------------
        # Common research paper headings
        # -----------------------------
        heading_keywords = {
            "abstract",
            "introduction",
            "background",
            "related work",
            "method",
            "methodology",
            "model",
            "model architecture",
            "experiments",
            "results",
            "evaluation",
            "training",
            "discussion",
            "conclusion",
            "references",
            "acknowledgements",
            "acknowledgments"
        }

        if text.lower() in heading_keywords:
            return True

        # Appendix
        if text.lower().startswith("appendix"):
            return True

        # -----------------------------
        # Numbered headings
        # Examples:
        # 1 Introduction
        # 3.2 Decoder
        # 4.1.3 Attention
        # -----------------------------
        if re.match(r"^\d+(\.\d+)*\.?\s+[A-Za-z]", text):
            return True

        # -----------------------------
        # Bold headings
        # -----------------------------
        if (
            size > body_font
            and ("bold" in font or "medi" in font)
            and len(text) < 60
        ):
            return True

        return False

    def detect_sections(self, elements: List[Dict]) -> List[Dict]:
        """
        Detect all section headings from parser output.
        """

        # Estimate body font size
        font_counter = {}

        for element in elements:

            text = element["text"].strip()

            if not text:
                continue

            size = round(element["font_size"])

            font_counter[size] = font_counter.get(size, 0) + 1

        body_font = max(font_counter, key=font_counter.get)

        headings = []

        for element in elements:

            if self.is_section_heading(element, body_font):

                headings.append({

                    "title": element["text"].strip(),

                    "page": element["page"],

                    "font_size": element["font_size"],

                    "font": element["font"],

                    "bbox": element["bbox"]

                })

        return headings