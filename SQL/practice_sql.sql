create table student (
	st_id serial primary key,
	name varchar(50),
	age bigint
);

insert into student(name, age) values('Amit', 21), ('Ayush', 25);

select *from student; 

Alter table student ADD column email varchar(50);
Alter table student DROP column email;
Alter table student ADD column email varchar(50) default 'Not Provided';
Alter table student RENAME column email to emailid;
Alter table student alter column age type smallint; 
Alter table student alter column age set default 18;
Alter table student alter column age drop default;
Alter table student ADD CONSTRAINT age_check check(age >= 5);
Alter table student DROP CONSTRAINT age_check;

-- rename table
Alter table student RENAME TO student_info;
Alter table student RENAME TO student;
Alter table student_info RENAME TO student;


-- Relationships

-- 1 - 1 Relationship
create table students (
	st_id serial PRIMARY KEY,
	name varchar(100) NOT NULL
);

create table student_profile (
	st_id INT PRIMARY KEY,
	address TEXT,
	age INT,
	phone varchar(15)
);

INSERT INTO students (name)
VALUES
('Akarsh Vyas'), ('Simran Mehta'), ('Rohan Gupta');

INSERT INTO student_profile (st_id, address, age, phone)
VALUES
(1, 'Delhi, India', 22, '9999999999'),
(2, 'Mumbai, India', 21, '8888888888'),
(3, 'Bangalore, India', 23, '7777777777');

select *from student_profile;



