-- script that uses the hbtn_0d_tvshows
SELECT t.title FROM tv_shows AS t
JOIN tv_show_genres AS d ON d.show_id = t.id
JOIN tv_genres AS g ON d.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY t.title;
