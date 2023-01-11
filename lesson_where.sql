SELECT author, title, price 
FROM book
WHERE amount < 10;

SELECT title, author, price, amount 
FROM book
WHERE (price < 500 OR price > 600) 
    AND (price * amount >= 5000);


SELECT title, author
FROM book
WHERE price BETWEEN 540.50 AND 800 
    AND amount IN(2, 3, 5, 7);

SELECT author, title
FROM book
WHERE amount BETWEEN 2 and 14
ORDER BY author DESC, title;

SELECT title, author
FROM book
WHERE author LIKE "% %С.%" AND  title LIKE "%_% %_%"
ORDER BY title;

SELECT DISTINCT amount
FROM book; 
