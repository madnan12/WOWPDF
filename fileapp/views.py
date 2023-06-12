from django.shortcuts import render
from pdf2docx import Converter
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
# from pdf2image import convеrt_from_path
import aspose.words as aw
from matplotlib.backends.backend_pdf import PdfPages
import pdfkit
# from numbering2pdf import add_numbering_to_pdf
from fileapp.models import *
# Create your views here.

def home(request):
    return render(request, 'home.html')

def pdf_to_word(request):
    if request.method == 'POST':
        pdf_file = request.FILES['pdf_file']
        docx_file = 'muscles.docx'
        print('**********',pdf_file)
        
        try:
            cv_obj = Converter(pdf_file)
            cv_obj.convert(docx_file)
            cv_obj.close()
        except Exception as e:
            print('Conversion Failed', e)
    return render(request, 'test.html')

def split_pdf(request):
    # input_pdf = PdfFileReader("file1.pdf")
    # output = PdfFileWriter()
    # output.addPage(input_pdf.getPage(0))
    # with open("first_page.pdf", "wb") as output_stream:
    #     output.write(output_stream)

    return render(request, 'split-pdf.html')
        
        
def merge_pdf(request):
    merger = PdfFileMerger()
    path_to_files = r'pdf_files/'
    for root, dirs, file_names in os.walk(path_to_files):
        for file_name in file_names:
            merger.append(path_to_files + file_name)
    merger.write("merged_all_pages.pdf")
    merger.close()
    
# def word_to_pdf(request):

def pdf_to_jpg(request):
    pages = convert_from_path('example.pdf')
    for i in range(len(pages)):
        pages[i].save('page'+ str(i) +'.jpg', 'JPEG')


def pdf_to_png(request):
    pages = convert_from_path('example.pdf')
    for i in range(len(pages)):
        pages[i].save('page'+ str(i) +'.png', 'PNG')
    
def rotate_pdf(request):
    pdf_in = open('original.pdf', 'rb')
    pdf_reader = PdfFileReader(pdf_in)
    pdf_writer = PdfFileWriter()

    for pagenum in range(pdf_reader.numPages):
        page = pdf_reader.getPage(pagenum)
        page.rotateClockwise(180)
        pdf_writer.addPage(page)

    pdf_out = open('rotated.pdf', 'wb')
    pdf_writer.write(pdf_out)
    pdf_out.close()
    pdf_in.close()

def add_watermark(request):

    pdf_file = "doc.pdf"

    watermark = "watermark.pdf"

    merged_file = "merged.pdf"

    input_file = open(pdf_file,'rb')
    input_pdf = PdfFileReader(input_file)

    watermark_file = open(watermark,'rb')
    watermark_pdf = PdfFileReader(watermark_file)

    pdf_page = input_pdf.getPage(0)

    watermark_page = watermark_pdf.getPage(0)

    pdf_page.mergePage(watermark_page)

    output = PdfFileWriter()

    output.addPage(pdf_page)

    merged_file = open(merged_file,'wb')
    output.write(merged_file)

    merged_file.close()
    watermark_file.close()
    input_file.close()

def edit_pdf(request):
    doc = aw.Document("Input.pdf")
    builder = aw.DocumentBuilder(doc)

    # Insert text at the beginning of the document.
    builder.move_to_document_start()
    builder.writeln("Morbi enim nunc faucibus a.")
    doc.update_page_layout()

    doc.save("Output.pdf")
    
    # Insert table at the beginning of the document.
    builder.move_to_document_start()
    builder.start_table()
    builder.insert_cell()
    builder.write("Row 1, cell 1.")
    builder.insert_cell()
    builder.write("Row 1, cell 2.")
    builder.end_table()
    doc.update_page_layout()

    doc.save("Output.pdf")
    
    # Insert image at the beginning of the document.
    builder.move_to_document_start()
    builder.insert_image("Image.png")
    doc.update_page_layout()

    doc.save("Output.pdf")

# def add_pdf_page_number(request):
#     pp = PdfPages('output.pdf')
#     add_numbering_to_pdf("old_file.pdf", "new_file.pdf")


def html_to_pdf(request):
    
    path_to_file = 'sample.html'
    
    pdfkit.from_file('test.html', 'out.pdf')

