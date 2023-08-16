-- import the database dump from hbtn_0d_tvshows
SELECT t.title, s.genre_id FROM tv_shows t
JOIN tv_show_genres s ON s.genre_id=t.id
ORDER BY t.title, s.genre_id;
