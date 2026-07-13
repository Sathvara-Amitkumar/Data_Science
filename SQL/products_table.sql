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

INSERT INTO products (name, sku_code, price, stock_quantity, category) values 
('Wireless Mouse', 'avf6hg4h', 699.5, 50, 'Electronics'),
('Water Bottle', 'njknk679', 210.00, 100, 'Fitness'),
('Notebook', 'jk2d4g5g', 60.60, 70, 'Stationary'),
('Pen Set', 'jlkj4g5g', 130.60, 60, 'Stationary'),
('Laptop Stand', 'ls123ghq', 1399.60, 120, 'Accessories'),
('USB-C Hub', 'mn54mnb3', 640.60, 100, 'Accessories');

INSERT INTO products (name, sku_code, price, stock_quantity, category) values 
('Samsung S26 Ultra', 'jhg45as6', 189000.5, 50, 'Electronics');

select * from products order by product_id asc;
select *from products where category='Electronics';
select category, count(*) from products group by category having count(*) > 1;
select *from products order by price desc;
select *From products limit 3 offset 1;
select name as item_name From products;
select distinct category from products;

select *from products where price between 400 and 1500;

select *from products where category in ('Fitness', 'Stationary');

select *from products where sku_code like '%g';
select *from products where sku_code like '%123%';
select *from products where sku_code like '_k%';

select count(*) from products; 
select sum(price) as Total_price from products where category in ('Accessories', 'Stationary'); 
select round(avg(price), 2) from products; 