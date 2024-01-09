from fpdf import FPDF

#  PDF should be A4, which is 210mm wide by 297mm tall.
class PDF(FPDF):
    def __init__(self, name):
        super().__init__(orientation="portrait", unit="mm",format="A4")
        self.name = name

    def pdf_format(self):
        #set bkgd color to white
        self.set_page_background((255, 255, 255))


    def title(self):
        self.set_font("Helvetica", "B", 50)
        self.cell(0,60,"CS50 Shirtificate", border=0, align="C")


    def shirt(self):
        # image_x = (page_width-imagewidth)/2
        # (210-170)/2 = 20
        self.image("./shirtificate.png",x=20,y=70, w=170, h=150)

    def shirt_font(self, name):
        self.set_font("Times", "B", 40)
        # x = self.get_string_width(f)
        # x = (self.w - self.get_string_width(f"{self.name} took CS50")) / 2
        self.set_xy(20, 90)
        self.cell(0, 50, f"{name} took CS50", border=0, align="C")


    @staticmethod
    def get_name():
        name = input("Name: ")
        return name
    # def get_name():
    #     name = input("Name: ")
    #     return name

    def generate_pdf(self, name):
        self.add_page()
        self.pdf_format()
        self.title()
        self.shirt()
        self.shirt_font(name)
        self.output("shirtificate.pdf")

def main():

    name = PDF.get_name()
    pdf = PDF(name)
    pdf.generate_pdf(name)



if __name__ == "__main__":
    main()
