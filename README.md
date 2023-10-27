# Overview


I am working on a Rate My Apartment website that will take user input 1  form a form and project graphs and other useful data. This latest update includes the backend developement for this project. I used sqlite and python for this.

I created a table called apartment. to focus the program and what it executes I created a cursor variable that is related to the sqlite file. As I went through the program I added, removed, changed things and then commited it (finalizing my changes) to the file. As I went I saved querys which produced a dataframe that was the df I updated as I went until in the end I took that datafram and made a graph with it using altair.

This is all for a future apartment rating website.
{Provide a link to your YouTube demonstration. It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of how created the Relational Database.}

[Software Demo Video]([http://youtube.link.goes.here](https://youtu.be/nXoaQNy3WMA))

# Relational Database


I created a database in an sql file it started out empty. So I created a table called apartment and filled it with varius row values. Then I created a graph to display the price for apartments over the years.
This is an early developement project. I only have one table so far but plan to branch out to more the more information I get in the future. Right now I just created the data but I plan to link this to a form using CSS and Html. The one table has the following tables and their value types
    prepapartment TEXT NOT NULL,
    star TEXT,
    apartment TEXT,
    housing TEXT,
    semester TEXT,
    UpcomingSchoolYear INTEGER,
    ThisSemesterCost INTEGER

# Development Environment
-Visual Studio Code 2023

- sqlite3 (most recent)
- python 3.11.5
- numpy
- altair
- pandas
  
(previous work)
- css
- html

# Useful Websites

{Make a list of websites that you found helpful in this project}

for the backend (most recent update)
- [sqlite website](https://www.sqlitetutorial.net/sqlite-rename-column/)
- [sql w3schools]([https://www.sqlitetutorial.net/sqlite-rename-column/](https://www.w3schools.com/sql/))
- [sqlite w3schools]([http://url.link.goes.here](https://www.w3schools.blog/sqlite-tutorial))

for the css and html front end
[button as a link](https://stackoverflow.com/questions/40974745/how-do-i-make-submit-button-redirect-to-another-page)
* [html accessing css](https://sebhastian.com/css-not-linking-html/)
* [W3 Schools](https://www.w3schools.com/css/default.asp)

* [html to csv file](https://stackoverflow.com/questions/22264375/how-to-export-html-form-to-csv-file)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}

- Item 1 get the back end to link with the form (front end)
- Item 2 get the graph working better.
- Item 3 unclutter code to be more readable and more convenient such as more automation.
- Item 4 accessibility
