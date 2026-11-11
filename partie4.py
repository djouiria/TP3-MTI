# Separate Interfaces
class Printable:
    def print_document(self, document):
        pass


class Scannable:
    def scan_document(self, document):
        pass


class Faxable:
    def fax_document(self, document):
        pass


# Implementing Classes
class BasicPrinter(Printable):
    def print_document(self, document):
        print(f"Printing: {document}")


class AdvancedPrinter(Printable, Scannable, Faxable):
    def print_document(self, document):
        print(f"Printing: {document}")

    def scan_document(self, document):
        print(f"Scanning: {document}")

    def fax_document(self, document):
        print(f"Faxing: {document}")


if __name__ == '__main__':
    # الطابعة البسيطة: تطبع فقط
    basic = BasicPrinter()
    basic.print_document("Document1.pdf")

    # الطابعة المتقدمة: تطبع وتمسح وترسل فاكس
    advanced = AdvancedPrinter()
    advanced.print_document("Document2.pdf")
    advanced.scan_document("Document2.pdf")
    advanced.fax_document("Document2.pdf")