SELECT title, name_genre, price
FROM 
    genre INNER JOIN book
    ON genre.genre_id = book.genre_id
WHERE amount > 8
ORDER BY price DESC;

///

SELECT name_genre
FROM genre LEFT JOIN book
     ON genre.genre_id = book.genre_id
WHERE book_id IS NULL;

///

SELECT name_genre, title, name_author
FROM genre 
    JOIN book ON genre.genre_id = book.genre_id
    JOIN author ON author.author_id = book.author_id
WHERE name_genre LIKE '%роман%'
ORDER BY title; 

SELECT age, COUNT(age) FROM teacher GROUP BY age;

