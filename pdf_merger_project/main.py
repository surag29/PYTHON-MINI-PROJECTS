import PyPDF2

# Create a PDF merger object
merger = PyPDF2.PdfMerger()

# List of PDF files to merge
pdf_files = [
    r"pdf_merger_project\Data Analyst To De Cloud Roadmap.pdf",
    r"pdf_merger_project\data_analyst_de_roadmap.pdf"
]

# Add PDFs one by one
for pdf in pdf_files:
    merger.append(pdf)

# Save the merged PDF
merger.write("merged_output.pdf")
merger.close()

print("PDF merged successfully!")
