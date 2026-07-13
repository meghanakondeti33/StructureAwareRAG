from src.parser import PDFParser

pdf = PDFParser("data/papers/attention.pdf")

print(f"Total Pages: {pdf.get_total_pages()}")