from pprint import pprint

from src.core.parser import PDFParser


def main():

    pdf = PDFParser("data/papers/attention.pdf")

    print("=" * 80)
    print(f"Total Pages: {pdf.get_total_pages()}")
    print("=" * 80)

    elements = pdf.extract_layout_elements(0)

    print("\nFirst 10 layout elements:\n")

    for element in elements[:10]:
        pprint(element)


if __name__ == "__main__":
    main()