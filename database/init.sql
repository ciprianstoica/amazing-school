CREATE TABLE public."class" (
	id serial4 NOT NULL,
	class_number int4 NULL,
	class_letter varchar(2) NULL,
	CONSTRAINT class_pkey PRIMARY KEY (id)
);

CREATE TABLE public.student (
	id serial4 NOT NULL,
	first_name varchar(20) NOT NULL,
	last_name varchar(20) NOT NULL,
	class_id int4 NOT NULL,
	CONSTRAINT student_pkey PRIMARY KEY (id),
	CONSTRAINT student_class_id_fkey FOREIGN KEY (class_id) REFERENCES public."class"(id)
);

INSERT INTO "PUBLIC"."class" (CLASS_NUMBER,CLASS_LETTER) VALUES
	 (10,'a'),
	 (8,'b'),
	 (5,'c');

INSERT INTO "PUBLIC"."STUDENT" (FIRST_NAME,LAST_NAME,CLASS_ID) VALUES
	 ('Ionel','Pop',1),
	 ('Ionela','Popa',2),
	 ('Ionut','Popescu',2),
	 ('Ionica','Popinciuc',3),
	 ('Iulia','Ionescu',1),
	 ('Gigel','Pop',2);

