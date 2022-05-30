from PyPDF2 import PdfFileReader, PdfFileWriter

def split_pdf(infn, outfn):
    pdf_output = PdfFileWriter()
    pdf_input = PdfFileReader(open(infn, 'rb'))
    # 获取 pdf 共用多少页
    page_count = pdf_input.getNumPages()
    print(page_count)
    # 将 pdf 第五页之后的页面，输出到一个新的文件
    for i in range(5, page_count):
        pdf_output.addPage(pdf_input.getPage(i))
    pdf_output.write(open(outfn, 'wb'))

def add_bookmark(pdfmark, outfile):     # 列表参数 pdfmark（二维列表，存储着书签的名称和所在页数）当前需要编辑的已经存在的PDF文件
    """添加书签，从0开始"""
    print(pdfmark)
    pdf_output = PdfFileWriter()
    pdf_input = PdfFileReader(open(outfile, 'rb'))
    pdf_output.appendPagesFromReader(pdf_input)
    for i in pdfmark:
        pdf_output.addBookmark(i[0], i[1])
    pdf_output.write(open('bookmark.pdf', 'wb'))

def merge_pdf(infnList, outfn):
    pdf_output = PdfFileWriter()
    for infn in infnList:
        pdf_input = PdfFileReader(open(infn, 'rb'))
        page_count = pdf_input.getNumPages()
        for i in range(page_count):
            pdf_output.addPage(pdf_input.getPage(i))
    pdf_output.write(open(outfn, 'wb'))

if __name__ == '__main__':
    infn = 'E:\pdf文档\Linux命令大全完整版.pdf'
    outfn = 'E:\out.pdf'
    split_pdf(infn, outfn)