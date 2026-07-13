from src.core.parser import PDFParser
from src.core.section_detector import SectionDetector


def main():

    parser = PDFParser("data/papers/attention.pdf")

    detector = SectionDetector()

    elements = []

    # Extract elements from every page
    for page in range(parser.get_total_pages()):

        elements.extend(
            parser.extract_layout_elements(page)
        )

    headings = detector.detect_sections(elements)

    print("\nDetected Headings\n")

    for heading in headings:

        print(
            f"Page {heading['page'] + 1:02d} | "
            f"{heading['title']}"
        )


if __name__ == "__main__":
    main()