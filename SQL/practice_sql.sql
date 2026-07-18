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
select *from students;

ALTER TABLE student_profile ADD CONSTRAINT fk_stduent_id FOREIGN KEY(st_id) REFERENCES students(st_id);

SELECT 
	s.st_id,
	s.name,
	sp.address,
	sp.age,
	sp.phone
FROM students s
JOIN student_profile sp
ON s.st_id = sp.st_id;

-- 1 to Many Relationship
create table marks (
	 mark_id serial PRIMARY KEY,
	 st_id INT,
	 subject varchar(50),
	 marks INT,
	 FOREIGN KEY(st_id) REFERENCES students(st_id)
);

INSERT INTO marks (st_id, subject, marks)
VALUES
(1, 'English', 85), (1, 'Math', 89), (1, 'Science', 92),
(2, 'English', 80), (2, 'Math', 75), (2, 'Science', 78),
(3, 'English', 72), (3, 'Math', 70), (3, 'Science', 74);

select *from students;
drop table students;
delete from students where st_id=5;

INSERT INTO marks (st_id, subject, marks)
VALUES (4, 'English', 90), (4, 'Math', 89);

INSERT INTO students (name) VALUES ('Amitkumar');

-- JOINS

-- Show each student's name along with their subject and marks.
select s.name, m.subject, m.marks 
from students s join marks m 
ON s.st_id = m.st_id;

select s.name, m.subject, m.marks 
from students s left join marks m 
ON s.st_id = m.st_id;

-- Show marks for only "Simran Mehta" in all subjects.
select s.name, m.subject, m.marks 
from students s join marks m 
ON s.st_id = m.st_id where name='Simran Mehta';

-- Show only those subjects where marks are above 75.
select s.name, m.subject, m.marks 
from students s join marks m 
ON s.st_id = m.st_id where marks > 75;

-- Sort all students’ subject marks in descending order of marks.
select s.name, m.subject, m.marks 
from students s JOIN marks m
ON s.st_id = m.st_id ORDER BY marks DESC;

-- Show each student's average marks.
select s.name, round(avg(marks), 2) as AVG_marks 
from students s JOIN marks m
ON s.st_id = m.st_id GROUP BY name ORDER BY AVG_marks DESC;

-- Cross Join
select s.name, m.subject, m.marks from students s CROSS JOIN marks m; 