--getting all columns
SELECT *
FROM employees;

SELECT employee_id,
       last_name,
       first_name,      
       email,
       phone_number,
       hire_date,
       job_id,
       salary,
       commission_pct,
       manager_id,
       department_id     
FROM employees;

SELECT employee_id, 
          first_name, last_name, 
          email, phone_number, 
          hire_date, job_id, 
          salary, commission_pct, 
          manager_id, department_id , department_id 
          , 8
FROM employees;

--duplicate records
select  job_id
from employees;


--only unique records
select distinct job_id
from employees;


--Practice
--#1 List only unique departments from the table
select distinct department_id
from employees;



--#2 List unique jobs in each department

SELECT DISTINCT job_id, department_id
from employees;


SELECT DISTINCT job_id, department_id, manager_id
from employees;


SELECT employee_id
FROM employees;

SELECT DISTINCT employee_id
FROM employees;

--what is selected?
SELECT ROUND((SYSDATE - hire_date)/365),
       last_name ||'  ' ||first_name,
			 salary*(1+NVL(commission_pct,0))   
FROM employees;


SELECT sysdate  Now
FROM dual;

SELECT *
FROM dual


select hire_date, sysdate  Now
from employees;

SELECT (SYSDATE - hire_date)/365.25 AS "Ñòàæ"
       ,ROUND((SYSDATE - hire_date)/365.25,2) AS exp1
       ,TRUNC((SYSDATE - hire_date)/365.25,2) AS exp2
FROM employees



select hire_date, sysdate as Now
           ,round((sysdate-hire_date)/365) as experience_years
from employees;

SELECT first_name||' '||last_name AS Full_Name         
        ,LENGTH(phone_number) AS PhoneLength 
        ,CHR(ROWNUM*10) AS RandomSymbol 
	     ,REVERSE(first_name) AS ReverseString  
        ,LOWER(first_name) AS LowerString
	     ,UPPER(last_name) AS UpperString
FROM employees;

SELECT ROWNUM
FROM employees


SELECT CHR(97) ,'a'
FROM dual
--routines with date
SELECT SYSDATE
      ,SYSDATE + 1 AS next_day
	    ,SYSDATE + INTERVAL '1' MONTH AS next_month
	    ,SYSDATE + INTERVAL '10' YEAR AS next_year
			,SYSDATE + 1/24 
      ,SYSDATE - 1/24 
      ,SYSDATE + SYSDATE
FROM dual;

--using extract
SELECT sysdate,
       EXTRACT (month from sysdate) as mnth,
       EXTRACT (DAY from sysdate) as day
FROM dual;

--using to_char
--changing language parameters
ALTER SESSION SET NLS_DATE_LANGUAGE = 'ENGLISH';

SELECT TO_CHAR(SYSDATE, 'D-Month-YY') FROM DUAL; 

SELECT TO_CHAR(SYSDATE, 'Day d dd ddd Month ww year ') 
FROM DUAL; 

ALTER SESSION SET NLS_DATE_LANGUAGE = 'RUSSIAN';
--Practice
--Calculate the number of days till the end of the year


--from String to Date

SELECT '04/03/2016'  + INTERVAL '2' YEAR
FROM dual;


SELECT to_char(TO_DATE('04/03/2016', 'DD/MM/YYYY') , 'dd month year')
       ,to_char(TO_DATE('04/03/2016', 'mm/dd/YYYY') , 'dd month year')
FROM DUAL ;

SELECT TO_DATE('01.Jan.2010', 'DD.MON.YYYY') 
FROM DUAL ;

SELECT TO_DATE('15-01-10', 'DD-MM-YY')
FROM DUAL ;

SELECT * 
FROM dual; --#1 

/*
Comment type 2 

*/

--dealing with NULLS
SELECT  5 + NULL AS s1
       ,5 - NULL AS s2
       ,5 * NULL AS s3
			 ,5 / NULL AS s4
       ,5
FROM dual;

SELECT salary
       , commission_pct
       ,salary + salary*commission_pct AS total_sal
FROM employees;

--For each employee calculate total salary (take into account bonuses)
--#1
SELECT salary + salary*commission_pct AS total_sal
       ,salary, commission_pct
FROM employees;
--#2
SELECT salary + salary*nvl(commission_pct,0) AS total_sal
       ,salary, commission_pct
FROM employees;

--case
SELECT e.first_name, e.last_name, e.salary,
       CASE 
	      WHEN e.salary > 15000 THEN 'Cool'
				WHEN e.salary < 1000 THEN 'Not cool'
	      ELSE 'Simply worker'
      END AS salary_status
FROM employees e;

SELECT e.first_name, e.last_name, e.salary,job_id,
       CASE 
	      WHEN job_id = 'IT_PROG' THEN 'MegaCool'
        WHEN e.salary > 15000 THEN 'Cool'
        
				WHEN e.salary < 1000 THEN 'Not cool'
	      ELSE 'Simply worker'
      END AS salary_status
FROM employees e;

--decode
SELECT job_id,
       decode(job_id, 
			        'IT_PROG', 'SuperHero',
						  'AD_VP', 'Boss',
							'Worker' ) as description
FROM employees;

--SORTING

SELECT commission_pct
FROM employees
ORDER BY commission_pct ASC NULLS FIRST

--sorting in ascending mode
select e.employee_id, 
       e.first_name, 
       e.last_name
from employees e
order by e.last_name;

--sorting in descending mode
select e.employee_id, 
       e.first_name, 
       e.last_name
from employees e
order by UPPER(e.last_name) DESC;

--SORTING WITH OFFSET 
select First_Name,Last_Name, salary
from employees
order by salary desc
FETCH next 5 ROWS ONLY;

-- top with ties
select First_Name,Last_Name, salary
from employees
order by salary desc
FETCH next 5 ROWS WITH ties;

select First_Name,Last_Name, salary
from employees
order by salary desc
FETCH next 10 PERCENT ROWS ONLY;

--Practice
--List out experience for each employee, sort from old- to newcomers. 
--If experience is the same, sort by salary. 


--list information about employees with last name 'King'
select employee_id, first_name, last_name,
       hire_date,job_id, salary          
from employees e
where e.last_name = 'King';

select employee_id, first_name, last_name,
       hire_date,job_id, salary          
from employees e
where e.last_name <> 'King';


select employee_id, first_name, last_name,
       hire_date,job_id, salary          
from employees e
where NVL(e.first_name,'ZZZZZ') <> 'Alexander';

--list information about employees hired in 2003
select employee_id, first_name, last_name,
       hire_date,job_id, salary
from employees e
where extract(year from e.hire_date) = 2003;

--what's wrong? 
select employee_id, first_name, last_name,
       hire_date,job_id, salary, extract(year from e.hire_date) AS hire_year
from hr.employees e
where hire_year > 2003 ;

select employee_id, first_name, last_name,
       hire_date,job_id, salary, extract(year from e.hire_date) AS hire_year
from hr.employees e
where extract(year from e.hire_date) > 2003 ;

/*List all employees with 
 - experience not less than 7 years ,
 - salary is greater than 5000 
 - salary is less than 7000*/

SELECT first_name, last_name,salary,hire_date
FROM employees 
WHERE (SYSDATE-hire_date)/365 >=7 
       AND  salary <7000
	     AND salary >5000;


-- list all employees on ST_CLERK or IT_PROG jobs
SELECT first_name, last_name,salary,job_id
FROM employees
WHERE job_id = 'ST_CLERK' 
      OR  job_id = 'IT_PROG'
ORDER BY job_id, salary DESC;

-- ?#1
SELECT first_name, last_name,salary,job_id
FROM employees
WHERE job_id = 'ST_CLERK' 
      OR ( job_id = 'IT_PROG' AND salary > 5000) 
ORDER BY job_id, salary DESC;

--?#2
SELECT first_name, last_name,salary,job_id
FROM employees
WHERE (job_id = 'ST_CLERK' OR  job_id = 'IT_PROG' )
       AND salary > 5000
ORDER BY job_id, salary DESC;

--#3 ==> 1
SELECT first_name, last_name,salary,job_id
FROM employees
WHERE job_id = 'ST_CLERK' 
      OR  job_id = 'IT_PROG' 
      AND salary > 5000
      OR job_id = 'SH_CLERK' 
ORDER BY job_id, salary DESC;

SELECT first_name, last_name,salary,job_id,department_id
FROM employees
--WHERE NOT (department_id = 10)
WHERE department_id != 10

--List all employees who hasn’t bonuses
--won't work
select employee_id, first_name, last_name,
           hire_date, job_id, salary, 
           commission_pct
from employees e
where commission_pct = null
order by e.Last_Name;

--correct
select employee_id, first_name, last_name,
           hire_date, job_id, salary, 
           commission_pct
from employees e
where commission_pct  IS NOT null
order by e.Last_Name;

--PRACTICE
--#1 List full name of employees with work experience more then 5 years or salary more than 15000.  

/*#2 List last name of employees who:
- works in the 10th department
- has more then 2000 as a salary
- was hired not later then in 2001  
*/

select employee_id, first_name, last_name,
           hire_date, job_id, salary, 
           commission_pct
from employees e
WHERE last_name >'A'
      AND last_name < 'B'


--List all phone numbers, starting from 590:
select employee_id, first_name, last_name,
       hire_date,job_id, salary,phone_number
from employees e
where phone_number like '590%';

--List all phone numbers except of starting from 590:
select employee_id, first_name, last_name,
       hire_date,job_id, salary,phone_number
from employees e
where phone_number not like '590%'; 

select employee_id, first_name, last_name,
       hire_date,job_id, salary,phone_number
from employees e
where phone_number not like '590%'
      OR phone_number IS NULL;
      
select employee_id, first_name, last_name,
       hire_date,job_id, salary,phone_number
from employees e
where NVL(phone_number,'1') not like '590%'      


--compare
select employee_id, first_name, last_name
from employees e
where first_name like 'Sara%'
order by first_name;
--vs
select employee_id, first_name, last_name
from employees e
where first_name like 'Sara_'
order by first_name;

--#1
select employee_id, first_name, last_name
from employees e
where first_name like 'Sara__'
order by first_name;

--#2
select employee_id, first_name, last_name
from employees e
where first_name like 'Sara%'
     AND LENGTH(first_name) = 6;


select employee_id, first_name, last_name
from employees e
where first_name like 'Sara_%'
order by first_name;


select employee_id, first_name, last_name
from employees e
where first_name like 'sara%'
order by first_name;

select employee_id, first_name, last_name
from employees e
where first_name LIKE '%a'


--List all employees with underscore in a email:
--WRONG
select employee_id, first_name, last_name, email
from employees e
where  email like '%_%';


--RIGHT
select employee_id, first_name, last_name, email
from employees e
where  email like '%Z_Z%%' escape 'Z';


select employee_id, first_name, last_name, email, salary
from employees e
WHERE salary LIKE '%500'

select employee_id, first_name, last_name, email, hire_date
from employees e
WHERE to_char(hire_date,'mm') LIKE '%06%'

--using between
--all employees with salary in range
select employee_id, first_name, last_name, salary
from employees e
where salary  between 4000 and 5000;


select employee_id, first_name, last_name, salary
from employees e
where salary  >= 4000 and 
      salary <= 5000;
      
select employee_id, first_name, last_name, salary
from employees e
where salary  >= 4000 and 
      salary < 5000;      
      
select employee_id, first_name, last_name, salary
from employees e
where salary  between 4000 and 5000
      AND salary < 5000;
      
select employee_id, first_name, last_name, salary
from employees e
where salary  between 6000 and 5000;


select employee_id, first_name, last_name, salary
from employees e
where first_name  BETWEEN 'A' AND 'C';

select employee_id, first_name, last_name, salary,current_timestamp
from employees e
where hire_date  BETWEEN to_date('01.01.2010','dd.mm.yyyy') AND current_timestamp;
      
--using in
-- via OR
select first_name, last_name, salary, job_id
from employees e
WHERE e.job_id = 'PU_CLERK' 
      OR e.job_id = 'SH_CLERK' 
      OR e.job_id = 'PU_MAN';

--via IN
select first_name, last_name, salary, job_id
from employees e
WHERE e.job_id in ('PU_CLERK', 'SH_CLERK', 'PU_MAN','IT_PROG');


SELECT first_name
from employees e
WHERE first_name NOT IN ('David','Steven');


SELECT first_name
from employees e
WHERE first_name IN ('David','Steven',NULL);

SELECT first_name
from employees e
WHERE first_name = 'David'
      OR first_name = 'Steven'
      OR first_name = NULL
      
      
      
 SELECT first_name
from employees e
WHERE first_name NOT IN ('David','Steven');


SELECT first_name
from employees e
WHERE first_name != 'David'
      AND first_name != 'Steven'
      AND first_name != NULL
