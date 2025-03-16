<h1>Python PDF Editor</h1>
<br>
The goal of this project was to provide a method to make custom pdfs. The project uses python as its only language, two main python libraries are used to make the pdf editor, namely FPDF(pdf editing library) and Tkinter(ui library). The project is divided in two parts, the pdf editor program which will produce a pdf when given some input and the second part is the UI for the pdf editor which uses the Tkinter library as the UI framework and also to render text and other elements on the pdf page.
<br>
<h2>PDF Editor</h2>
The pdf editor program uses the FPDF python library to create pdfs, the idea is to create some intermediate file to serve as the input to the pdf editor program, which will then use the FPDF framework to create a pdf. The main reason why i chose to create this program was to use custom font in the pdf, the FPDF library allowed me to do so if i provide it a font file. The required format of custom font file is called true-type(.ttf), some online websites allow you to make your own ttf files for free. The ttf file can then be further customized using a program such as "fontforge".
<h3>PDF Editor Output</h3>
You can see that the pdf contains custom text font here <a href="/PdfCreator/helloworld.pdf">helloworld.pdf</a>.
<img src="/PdfCreator/pdfeditor_output.png" >
<br>
<h2>PDF Editor UI</h2>
The program uses the Tkinter python library as its UI framework, I chose this library because how popular it was(also top search result on google plus its also written in python so...). The idea was to take input from the UI to create a text file which will be given to the PDF editor program to generate the final output. The UI was to display each page of the pdf as it is being edited, the Tkinter library allows you to display drawings using its canvas widget. This means the tkinter renderer will also be used to show text editing in the UI(this becomes a problem in the future).
<br>
<br>
The UI looks like this
<br>
<video src="https://github.com/user-attachments/assets/25074d23-83f6-489d-96f2-471fd50cc263" controls="controls" muted="muted" style="max-width: 730px;" ></video>