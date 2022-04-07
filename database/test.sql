CREATE TABLE EMPLOYEES(
    Employee_id number(6) PRIMARY KEY,
    First_Name varchar(20),
    Last_Name varchar(25) NOT NULL,
);

INSERT INTO EMPLOYESS
VALUES (123456, 'Sunil', 'kumar');

INSERT INTO EMPLOYESS
VALUES (245567, 'Hari', 'prasath');

SELECT * from EMPLOYESS;