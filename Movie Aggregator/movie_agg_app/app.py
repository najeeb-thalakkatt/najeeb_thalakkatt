import sys
import movie
from report_gen import get_report

__author__ = 'NajeebT'

if __name__ == '__main__':

    #Getting the movie details and output format
    movie_name = sys.argv[1]
    run_time = sys.argv[2]
    language = sys.argv[3]
    lead_actor = sys.argv[4]
    genre = sys.argv[5]
    export_method = sys.argv[6]
    #Using Reflection in Python
    movie = movie.Movie(movie_name,run_time,language,lead_actor, genre)
    get_report(movie,export_method)

