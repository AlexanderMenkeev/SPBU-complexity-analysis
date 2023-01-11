UPDATE book
SET price = 0.7 * price;

SELECT * FROM book;

UPDATE book
SET price = 0.9 * price
WHERE amount BETWEEN 5 and 10;