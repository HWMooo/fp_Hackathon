=================== HOW TO USE ====================
1. fork and clone the repo.
2. cd in repo root directory.
3. run - pipenv shell
4. pipenv install
5. the required packages should now be installed to start server run - pipenv run dev
6. to exit ctrl+c

if errors try install required packages seperately, these can be found in pipfile.

=================== WHAT IT DOES ====================
1. type a film search query such as 'horror', 'comedy', 'Harry Potter'
2. will return a list of films related to the search query.
3. click on a film title, this will take you to a route with the imbdID of that film,
it will show the poster, release date and type - 'movie'/'series'.
4. researching in searchbar in that route will go back to index path and show new list of movies.

=================== THINGS TO ADD ====================
1. it search's by search query but not really genre, need to find another api.
2. api lacks info to display once clicked, need to find another api.
3. add css/style to the page.
4. error handling
5. testing!!!!!!!