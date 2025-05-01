# Write your MySQL query statement below
SELECT Product.product_name , Sales.year, Sales.price FROM Product , Sales
WHERE Product.product_id=Sales.product_id ;