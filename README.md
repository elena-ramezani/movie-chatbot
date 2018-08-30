# movie-chatbot
movie bot that let you select movies base on time,genres, etc

# Show me movie webhook implementation in Python

This is a really  webhook implementation that gets movie information in  JSON and returns a fulfillment response.



# Deploy to:
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

# What does the service do?
It's a movie information fulfillment service that uses [OMDB Movie API].
The services takes the `movie name` parameter from the action, performs gathering information  for the movie


# How to do it
## generate API key from OMDB site (https://www.omdbapi.com/)
you can get information about movie using this line
http://www.omdbapi.com/?apikey=[your key]&t=[movie name]


results are like this:

    {"Title":"Friends","Year":"1994–2004","Rated":"TV-14","Released":"22 Sep 1994","Runtime":"22 min","Genre":"Comedy, Romance","Director":"N/A","Writer":"David Crane, Marta Kauffman","Actors":"Jennifer Aniston, Courteney Cox, Lisa Kudrow, Matt LeBlanc","Plot":"Follows the personal and professional lives of six 20 to 30-something-year-old friends living in Manhattan.","Language":"English, Dutch, Italian, French","Country":"USA","Awards":"Won 1 Golden Globe. Another 68 wins & 211 nominations.","Poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BMTg4NzEyNzQ5OF5BMl5BanBnXkFtZTYwNTY3NDg4._V1._CR24,0,293,443_SX89_AL_.jpg_V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"8.9/10"}],"Metascore":"N/A","imdbRating":"8.9","imdbVotes":"574,259","imdbID":"tt0108778","Type":"series","totalSeasons":"10","Response":"True"}


## how to make a webhook on Heroku
1- install Heroku CLI

    brew install heroku/brew/heroku

    heroku login ## with your user name and password

get the repository
    get show-me-movie's source code to your local machine.
    https://git.heroku.com/show-me-movie.git

    cd show-me-movie

Deploy your changes
Make some changes to the code you just cloned and deploy them to Heroku using Git.

    git add .
    git commit -am "update"
    git push heroku master

get url of webhook and add "webhook" at the end

    https://show-me-movie.herokuapp.com/webhook

insert url into fulfilement part of dialogflow


## Dialogflow
for each part generate one intent, for example:

    movie_year
    movie_award

 and correspond couple of questions that you think user may ask for each part



