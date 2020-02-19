// задание 1
CREATE DATABASE IF NOT EXISTS Employee;
USE Employee;


CREATE TABLE IF NOT EXISTS Personal_date (id_employee INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
                                         first_name VARCHAR(30) NOT NULL,
                                         last_name VARCHAR(30) NOT NULL,
                                         position VARCHAR(40) NOT NULL,
                                         salary INT NOT NULL
                                        );


// условие для того, чтобы один человек имел только одну должность, определяется путем создания уникального ключа из нескольких полей(имени, фамилии)
CREATE UNIQUE INDEX new_index ON Personal_date(first_name, last_name);


INSERT INTO Personal_date (id_employee, first_name, last_name, position, salary) VALUES (null, 'Roman', 'Petrov','director', 80000 );
INSERT INTO Personal_date (id_employee, first_name, last_name, position, salary) VALUES (null, 'Olga', 'Belova','administrator', 17000 );
INSERT INTO Personal_date (id_employee, first_name, last_name, position, salary) VALUES (null, 'Inna', 'Sedova','accountant', 20000 );
INSERT INTO Personal_date (id_employee, first_name, last_name, position, salary) VALUES (null, 'Petr', 'Smitnov','designer', 28000 );
INSERT INTO Personal_date (id_employee, first_name, last_name, position, salary) VALUES (null, 'Ivan', 'Reshetov','architect', 50000 );
INSERT INTO Personal_date (id_employee, first_name, last_name, position, salary) VALUES (null, 'Maria', 'Kalina','courier', 10000 );
INSERT INTO Personal_date (id_employee, first_name, last_name, position, salary) VALUES (null, 'Elena', 'Vinnik','designer', 25000 );


// запросы по заданию 2
SELECT * from Personal_date where salary < 30000;
SELECT * from Personal_date where salary < 30000 and position = 'designer';


// задание 3 : создание дополнительной таблицы с ключами для отношений Many-to-Many
// (чтобы создать связь внутри таблицы Many-to-Many, требуется дополнительная таблица)
CREATE TABLE IF NOT EXISTS Relationship ( id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
                                          id_first INT UNSIGNED NOT NULL ,
                                          id_second INT UNSIGNED NOT NULL
);


// добавление внешних ключей для связи с таблицей Personal_date
ALTER TABLE Relationship ADD FOREIGN KEY (id_first) REFERENCES Personal_date(id_employee);
ALTER TABLE Relationship ADD FOREIGN KEY (id_second) REFERENCES Personal_date(id_employee);


// заполнение таблицы для связей
INSERT INTO Relationship (id, id_first, id_second) VALUES (null, 1, 3 );
INSERT INTO Relationship (id, id_first, id_second) VALUES (null, 1, 2 );
INSERT INTO Relationship (id, id_first, id_second) VALUES (null, 1, 5 );
INSERT INTO Relationship (id, id_first, id_second) VALUES (null, 5, 4 );
INSERT INTO Relationship (id, id_first, id_second) VALUES (null, 5, 7 );


// запрос на выборку всех подчиненных сотрудника по имени Roman
SELECT first_name, last_name FROM Personal_date p INNER JOIN Relationship r ON p.id_employee = r.id_second
WHERE r.id_first = (SELECT id_employee FROM Personal_date WHERE first_name = 'Roman');