-- shows, and all genres linked to that show
SELECT t.title, g.name FROM tv_shows AS t
LEFT JOIN tv_show_genres AS d ON t.id=d.show_id
LEFT JOIN tv_genres AS g ON g.id=d.genre_id
ORDER BY t.title, g.name;
