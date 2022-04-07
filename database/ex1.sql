CREATE TABLE Employee(
    Employee_id NUMBER(6) PRIMARY KEY,
    First_Name VARCHAR(20),
    Last_Name VARCHAR(25) NOT NULL,
    Email VARCHAR(25) NOT NULL,
    Phone_number VARCHAR(10),
    Hire_date Date NOT NULL,
    Job_id VARCHAR(10) NOT NULL,
    Salary NUMBER(8,2),
    Commission_pct NUMBER(2,2),
    Manager_id NUMBER(6),
    Department_id NUMBER(4)
);

CREATE TABLE Department (
    Dept_id 