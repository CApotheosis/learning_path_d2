select current_date as Now_Date

/*String routines*/
SELECT first_name||' '||last_name AS Full_Name
        ,LENGTH(phone_number) AS PhoneLength 
        ,CHR(LENGTH(first_name)) AS RandomSymbol 
	     ,REVERSE(first_name) AS ReverseString  
        ,LOWER(first_name) AS LowerString
	     ,UPPER(last_name) AS UpperString
FROM employees;

/**Working with interval*/
SELECT current_date
       ,current_date + 1 AS next_day
	   ,current_date + INTERVAL '1' MONTH AS next_month
	   ,current_date + INTERVAL '1' YEAR AS next_year;

/*Extract*/	   
SELECT current_date,
       EXTRACT (month from current_date) as mnth,
       EXTRACT (day from current_date) as day;

SELECT TO_DATE('01.01', 'DD.MM');

SELECT TO_DATE('01.JAN.2021', 'DD.MON.YYYY');

SELECT TO_DATE('15-01', 'DD-MM');


SELECT  5 + NULL AS s1
       ,5 - NULL AS s2
       ,5 * NULL AS s3
			 ,5 / NULL AS s4
       ,5


SELECT salary,salary + salary*coalesce(commission_pct,0) AS total_sal
FROM employees;



SELECT e.first_name, e.last_name, e.salary,
       CASE 
	       WHEN e.salary > 15000 THEN 'Cool'
    	    WHEN e.salary < 1000 THEN 'Not cool'
	       ELSE 'Simply worker'
      END AS salary_status
FROM employees e;


SELECT job_id,
       decode(job_id, 
			    'IT_PROG', 'SuperHero',
				 'AD_VP', 'Boss',
				 'Worker' ) as description
FROM employees;



select e.employee_id, 
       e.first_name, 
       e.last_name
from employees e
order by e.last_name DESC;


select e.employee_id, 
       e.first_name, 
       e.last_name
from employees e
order by e.last_name using <; --asc
