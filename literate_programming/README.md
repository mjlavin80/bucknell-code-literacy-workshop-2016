# Literate Programming Activity

This folder houses materials on the literate programming activity for the workshop.

## Instructions
#### For this activity, we will break into teams of five or six people. Once gathered at a computer, create a Jupyter Notebook for your team by following these steps:

* Go to [https://notebook.thedatahumanist.website](https://notebook.thedatahumanist.website) and enter the Notebook Server password
* In the upper right hand corner, click "New" and select "Python" at the bottom of the dropdown menu
* A new tab will open. At the very top, next to the word "jupyter," you'll see the word <em>Untitled</em>. Click it.
* Now just type to rename your notebook. Fun team names are encouraged.  

#### Now that you have a notebook, try playing around with Jupyter a little. You might want to start with the guided tour.

* To activate the tour, click "Help > User Interface Tour"

#### Click the link below for some other things to try:

[Jupyter Notebook Sandbox](sandbox.md)

#### Now it's time to Work with the Zotero API!

* Go back to [https://notebook.thedatahumanist.website](https://notebook.thedatahumanist.website) and click on the file named "zotero_snippet.py"
* The script is divided into 17 lines of code. Select the first line, copy it to the clipboard, and go back to the your Notebook.
* Paste the first line of code into a Notebook code cell and press <em>Play</em>
* Next, locate the "Insert" Menu item and click "Insert > Cell above"
* Click on the cell, locate the "Cell" Menu item, and click "Cell > Cell Type > Markdown"
* Confer with your team to write some text about what you think the line of code below the Markdown cell is doing, and why. Narrate what you don't understand as readily as what you do. If you know any Markdown, feel free to style the cell. When you are finished, press <em>Play</em> to see how it looks.
* Once you are comfortable with this process, do the same for each line of code in "zotero_snippet.py"

#### Other things to try

* For each line of code, I would encourage you to paste key words into Google to see if you can get a better idea of the concept at play. For example, paste "from pyzotero import zotero" into a Google search and see what you get.
* Any time you notice a variable being declared (e.g. ```a = 5```), try calling the ``type()`` function on that variable in en empty cell below it. (e.g. ```type(a)```). See what it does.
* Try breaking a line of code. Is there anything you can do to make it return with an error when you press <em>Play</em>?

## An example of literate coding applied to Jupyter
[Python Programming for the Humanities Chapter 1: Getting Started] (http://nbviewer.jupyter.org/github/fbkarsdorp/python-course/blob/master/Chapter%201%20-%20Getting%20started.ipynb)
