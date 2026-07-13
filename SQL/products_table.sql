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