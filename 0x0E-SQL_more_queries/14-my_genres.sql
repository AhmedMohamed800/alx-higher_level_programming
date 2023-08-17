-- script that uses the hbtn_0d_tvshows
SELECT t.name FROM tv_genres AS t
JOIN tv_show_genres AS g ON t.id=g.genre_id
JOIN tv_shows AS d ON d.id=g.show_id
WHERE d.title = 'Dexter'
ORDER BY name;
