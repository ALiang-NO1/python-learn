from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger, generic

class GetPdfBookmark:
    deep_count = 0
    input = None
    bm = None
    inputname = None
    reallypagenum = {}
    tabs = ""

    def __init__(self, inputname):
        self.inputname = inputname
        try:
            self.input = PdfFileReader(open(inputname, "rb"))
        except:
            quit()

        self.bm = self.input.outlines

        self.__FixBookmarksPageNumber(self.input.getPage(0)['/Parent']['/Kids'],
                                      self.input.getPage(0)['/Parent']['/Count'])

    def __FixBookmarksPageNumber(self, data, data_len):
        for i in range(data_len):
            self.reallypagenum[str(data[i].idnum)] = str(i)

    def __writetab(self, out, count):
        for i in range(count):
            self.tabs += "\t"

    def __getpage(self, v):
        num = str(v[15:-4])
        return self.reallypagenum[num]

    def __writeData(self, out, item):
        out.write("%s%s\t%s\t%s\t%s\n" % (
        self.tabs, str(item.title), self.__getpage(str(item.page)), str(item.left), str(item.top)))
        self.tabs = ""

    def __writeBookmarks(self, out, bm):
        for item in bm:
            if not hasattr(item, "typ"):
                self.deep_count += 1
                self.__writeBookmarks(out, item)
                self.deep_count -= 1
            else:
                self.__writetab(out, self.deep_count)
                self.__writeData(out, item)

    def write(self, outputname=None):

        if outputname == None:
            out = open(self.inputname[:-4] + "_bookmarks.txt", "w", encoding="utf-8")
        else:
            out = open(outputname, "w", encoding="utf-8")

        self.__writeBookmarks(out, self.bm)
        out.close()


class SetPdfBookmark:
    # file = None
    def __init__(self, filename):
        self.filename = filename
        input = PdfFileReader(open(filename, "rb"))
        self.file = PdfFileWriter()
        self.file.appendPagesFromReader(input)

    def testset(self, data=None):

        peretns = self.file.addBookmark("test", 10, None, None, False, False, "/XYZ", 0, 728, 0)
        peretns = self.file.addBookmark("test", 100, peretns, None, False, False, "/XYZ", 0, 728, 0)

        self.file.write(open(self.filename[:-4] + "_bookmarks.pdf", "wb"))

    def getTabCount(self, str):
        count = 0
        for ch in str:
            if ch == '\t':
                count += 1
            else:
                break
        return count

    def setfromfile(self, file):
        # try:
        file = open(file, "r", encoding="utf-8")

        alllines = file.readlines()

        perents = [None]

        oldperent = None

        nowLayer = 0

        for index in range(len(alllines)):
            line = alllines[index]

            count = self.getTabCount(line)

            if count > nowLayer:
                perents.append(oldperent)
                nowLayer += 1
            elif count < nowLayer:
                perents.pop()
                nowLayer -= 1
            elif count == 0:
                perents = [None]
                nowLayer = 0

            tp = line[count:].split("\t")

            if len(tp) != 4:
                continue

            oldperent = self.file.addBookmark(tp[0], int(tp[1]), perents[-1], None, False, False, "/XYZ", int(tp[2]),
                                              int(tp[3]), 0)

        self.file.write(open(self.filename[:-4] + "_bookmarks.pdf", "wb"))

        print("ok")

        file.close()


bm = GetPdfBookmark("test.pdf")
bm.write()

# bm = SetPdfBookmark("nobookmarks.pdf")
# bm.setfromfile("bookmarks.txt")