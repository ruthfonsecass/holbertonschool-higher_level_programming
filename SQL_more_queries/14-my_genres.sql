-- Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_genres.name AS name
FROM tv_genres
JOIN tv_show_genres 
        ON genres.id = tv_show_genres.genre_id
JOIN tv_shows 
        ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY gname;
