create table "class" (
	id serial4 not null,
	class_number int4 null,
	class_letter varchar(2) null,
	constraint class_pkey primary key (id)
);

create table student (
	id serial4 not null,
	first_name varchar(20) not null,
	last_name varchar(20) not null,
	class_id int4 not null,
	constraint student_pkey primary key (id),
	constraint student_class_id_fkey foreign key (class_id) references "class"(id)
);

insert into "class" (class_number,class_letter) values
	 (10,'a'),
	 (8,'b'),
	 (5,'c');

insert into student (first_name,last_name,class_id) values
	 ('Ionel','Pop',1),
	 ('Ionela','Popa',2),
	 ('Ionut','Popescu',2),
	 ('Ionica','Popinciuc',3),
	 ('Iulia','Ionescu',1),
	 ('Gigel','Pop',2);

