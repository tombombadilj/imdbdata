# imdbdata
## 10/7/16

This code (movie_search.py) takes a list of movies store in csv files (e.g., movie_titles included in the repository), and gather information from IMDb, including director names, genres (up to four), total runtime (in minutes), primary language, and user rating into another csv file. Here are a couple things to keep in mind:

*Please see http://imdbpy.sourceforge.net/docs/README.txt for instructions on how to download and install imdbpy before using this program. 

*The list of movie names cannot contain a title, and it must be placed in the same directory as the movie_search.py code. When there are remakes or TV shows with the same names, the movieID might not be correct. I am working on improving this challenge now.

*It takes a while to extract data from IMDb for 700+ movies. My suggestion is to do them by segment (e.g., 100 at a time) just in case you encounter any errors.

*You will get couple csv files at the end of the code: 1) out.csv: movie titles + movieIDs and 2) movie_info.csv: movieIDs, user ratings, director, language, runtime, and genres.

*I am not too familiar with Python dataframe - please feel free to make changes and let me know if you have any questions. 

*I included a presentation that I built based on data extracted. 

Thank you!