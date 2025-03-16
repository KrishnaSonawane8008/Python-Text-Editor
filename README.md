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
<br>
<h2>The Big Problem</h2>
The problem with the project lies with the Tkinter library, specifiaclly the canvas widget renderer, the renderer is not fast enough to make constant updates(given the fact that Tkinter is a ui library and not a rendering library,i should have expected that, but, oh well....). This limitation of the library means that large amounts of elements on the widget takes a long time to render, this becomes a huge problem when you try to render an entire page of text which on the lower end will contain atleast 1-1.5 thousand letters(yes, letters), and because each letter is treated an element, this means that the tkinter renderer is given atleast hundereds of elements to render at each zoomin, zoomout, page pan/drag, or page scroll action, this makes the program really laggy and completely useless.
<h3>What I tried to Solve it</h3>
I have tried Instead of rendering every canvas element all at once, we can render the entire image containing all elements to be rendered and updated only when needed, hence making the zoomin, zoomout... actions faster, but this means that the image needs to be recreated everytime the user adds someting to the page, which took even longer after adding a few hundered elements to the image and also the quality of zoomed in letters is not good at all.
<br>
<br>
Then I tried culling/removing all the elements outside the view, this worked great when zoomed in, but still lagged as before when zoomed out, making the actions such as page pan nearly freeze the entire program.
<br>
<br>
I tried making a level of detail system, which means the elements from afar appear less detailed and the elements zoomed up close appear more detailed, the problem with this approach was that this only gave a slight increment in performance because the number of elements does not change only their quality changes, plus the constant shifting between the less and more detailed versions of the elements introduces some stress on the program.
<br>
<h2>Conclusion</h2>
When you are trying to make something like a text editor, its given that you will need to do a lot of operations regarding graphics rendering. High level libraries such as tkinter tends to be a lot slower in such cases because the core of the library is focused on making a ui not a renderer. In such cases you can use some low levl python library ment for rendering or even a library form some faster language such as C++.
<br>
<h2>Sources</h2>
For FPDF: https://www.youtube.com/watch?v=q70xzDG6nls&list=PLjNQtX45f0dR9K2sMJ5ad9wVjqslNBIC0
<br>
For Tknter: https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV