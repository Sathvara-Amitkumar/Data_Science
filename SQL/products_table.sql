create table products(
	product_id serial PRIMARY KEY,
	name varchar(70) NOT NULL,
	sku_code char(8) UNIQUE NOT NULL check (char_length(sku_code)=8),
	price NUMERIC(10,2) CHECK (price > 0),
	stock_quantity int default 0 check(stock_quantity >= 0),
	is_available boolean default TRUE,
	category VARCHAR(30) NOT NULL,
	added_on DATE default CURRENT_DATE,
	last_update TIMESTAMP default now()
)

drop table products;

alter table products alter column category type varchar(50);

INSERT INTO products (name, sku_code, price , stock_quantity, is_available, category)
VALUES
('Wireless Mouse', 'WM123456', 699.99, 50, TRUE, 'Electronics'),
('Bluetooth Speaker', 'BS234567', 1499.00, 30, TRUE, 'Electronics'),
('Laptop Stand', 'LS345678', 799.50, 20, TRUE, 'Accessories'),
('USB-C Hub', 'UC456789', 1299.99, 15, TRUE, 'Accessories'),
('Notebook', 'NB567890', 99.99, 100, TRUE, 'Stationery'),
('Pen Set', 'PS678901', 199.00, 200, TRUE, 'Stationery'),
('Coffee Mug', 'CM789012', 299.00, 75, TRUE, 'Home & Kitchen'),
('LED Desk Lamp', 'DL890123', 899.00, 40, TRUE, 'Home & Kitchen'),
('Yoga Mat', 'YM901234', 499.00, 25, TRUE, 'Fitness'),
('Water Bottle', 'WB012345', 349.00, 60, TRUE, 'Fitness');


select * from products order by product_id asc;
select *from products where category='Electronics';
select category, count(*) from products group by category having count(*) > 1;
select *from products order by price desc;
select *From products limit 3 offset 1;
select name as item_name From products;
select distinct category from products;

select *from products where price between 400 and 1500;

select *from products where category in ('Fitness', 'Stationary');

select *from products where sku_code like '%5';
select *from products where sku_code like '%123%';
select *from products where sku_code like '_M%';

select count(*) from products; 
select sum(price) as Total_price from products where category in ('Accessories', 'Stationary'); 
select round(avg(price), 2) from products; 



-- Test - 2

-- Q1. Display the name and price of the cheapest product in the entire table.
select name,price from products where price = (select min(price) from products);

-- Q2.Find the average price of products that belong to the 'Home & Kitchen' or 'Fitness' category.
select avg(price) from products where category in ('Home & Kitchen', 'Fitness') group by category;

-- Q3. Show product names and stock quantity where the product is available, stock is more than 50, and price is not equal to ₹299.
select name, stock_quantity from products where is_available = true and stock_quantity > 50 and price != 299;

-- Q4. Find the most expensive product in each category (name and price).
select category, max(price) from products group by category;

-- Q5. Show all unique categories in uppercase, sorted in descending order.
select DISTINCT UPPER(category) as category_upper from products ORDER BY category_upper desc;



-- String Function

select UPPER(name) from products;
select LOWER(name) from products;
select name, length(sku_code) from products;

select substring('Hello, This is Amitkumar', 13);
select name, lower(substring(sku_code, 1,2)) from products;
select right('This is Amitkumar', 9);
select name, left(sku_code, 2) from products;

select concat(name,' -> ', right(sku_code,2)) as product_with_code from products;
select concat_ws(' : ', name,category, left(sku_code,2)) as product_category_code from products;

select trim('    svbkbsn      ');
select name, replace(sku_code, left(sku_code, 2), 'AK') from products;
select name, substring(sku_code, 1,2) from products;
select *From products;



-- Case -> conditional expression
SELECT name, price, 
	CASE
		WHEN price > 1000 THEN 'Expensive'
		WHEN price BETWEEN 600 AND 1000 THEN 'Moderate'
		ELSE 'Cheap'
	END AS price_tag
FROM products; 

-- Above created is virtual data, now creating actual data 
alter table products add column price_tag varchar(20) default 'Out of Stock';

UPDATE products 
	SET price_tag =
		CASE
			WHEN price > 1000 THEN 'Expensive'
			WHEN price BETWEEN 600 AND 1000 THEN 'Moderate'
			ELSE 'Cheap'
		END;
			

-- is available column you have boolean true and false show case a new column to with in_stock and out of stock.
select name, is_available,
	case
		when is_available then 'In Stock'
		else 'Out of Stock'
	end as availability_status
from products;

-- HIGHLIGHT STOCK STATUS
alter table products add column stock_level varchar(20);

update products set stock_level = 
	case
		when stock_quantity > 100 then 'High Stock'
		when stock_quantity between 30 and 100 then 'Medium Stock'
		else 'Low Stock'
	end;
	
select *from products;
