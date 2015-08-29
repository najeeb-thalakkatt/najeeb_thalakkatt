# Movie Aggregator

## Part A: 
Create a console based application that accepts movie details like Name, Run Time, Language, Lead Actor and Genre and then export these details into one of the 2 formats, depending on user’s choice - “plain text” or “PDF”.

## Part B: 
Make the application extensible so that it is easy to “plug in” a new format and the application automatically has the capability to export to the new format without making any changes to the application code.

## Implementation Details:
This project is done in Python 2.7, with pdfkit for pdf generation.

## How to Run:
1. Clone the project https://github.com/najeebta/najeeb_thalakkatt.git
2. Install wkhtmltopdf http://wkhtmltopdf.org/downloads.html as per the OS.
3. On your virtual env install pdfkit, from command line >> pip install pdfkit 
4. Now run the app:
   * cd najeeb_thalakkatt\Movie Aggregator\movie_agg_app
   * python app.py name run_time language lead_actor genre pdf/text
   * eg: python app.py interstellar 169 English Mathew-Macc Sc-Fi pdf
   * eg: python app.py interstellar 169 English Mathew-Macc Sc-Fi text
5. Out put will be placed in the project folder itself as output
