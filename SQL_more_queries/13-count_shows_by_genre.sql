-- Script Description: Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each

-- Query to select genres and count the number of shows linked to each genre
SELECT tv_show_genres.genre_id AS genre, COUNT(tv_shows.id) AS number_of_shows
FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
