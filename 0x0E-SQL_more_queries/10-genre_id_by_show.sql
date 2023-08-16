-- import the database dump from hbtn_0d_tvshows
SELECT t.`title`, g.`genre_id` FROM `tv_shows` AS t
INNER JOIN `tv_show_genres` AS g ON g.`show_id`=t.`id`
ORDER BY t.`title`, g.`genre_id`;
