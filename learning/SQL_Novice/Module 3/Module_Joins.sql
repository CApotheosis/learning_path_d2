/*Test Tables*/
CREATE TABLE T1 AS
SELECT 1 AS ID FROM dual
UNION ALL
SELECT 2 FROM dual
UNION ALL
SELECT 4 FROM dual;

CREATE TABLE T2 AS
SELECT 1 AS ID FROM dual
UNION ALL
SELECT 2 FROM dual
UNION ALL
SELECT 3 FROM dual;

/*--------------------------------
              Cross join
---------------------------------*/
--#1
SELECT *
FROM t1 CROSS JOIN t2;

--#2
SELECT e.first_name||' '||e.last_name AS fi,
       e.department_id, d.department_id 
       ,department_name
FROM employees e CROSS JOIN departments d;

--Check
SELECT COUNT(*) FROM employees;
SELECT COUNT(*) FROM departments;
SELECT 108*29 FROM dual;



SELECT first_name, department_name, departments.manager_id
      ,employees.manager_id
FROM employees CROSS JOIN departments;

SELECT e.employee_id, e.department_id, d.department_id
   --   ,departments.department_id
FROM employees e CROSS JOIN departments d;

--Cross join - implicit form
SELECT e.first_name||' '||e.last_name AS fi,
       e.department_id, d.department_id 
FROM employees e, departments d, employees e1;


SELECT EXTRACT(YEAR FROM hire_date) AS y
      ,COUNT(*) AS qty
FROM employees
GROUP BY EXTRACT(YEAR FROM hire_date)
ORDER BY y

FROM (
SELECT *
FROM employees
ORDER BY employee_id
FETCH FIRST 100 ROWS ONLY ) t1,
 
--Using cross 
join to build a report
--list of years

/*CREATE OR REPLACE VIEW V_YEARS AS
SELECT (SELECT MIN (EXTRACT(YEAR FROM hire_date)) FROM employees) + LEVEL - 1 AS YEAR
FROM dual
CONNECT BY LEVEL <= (SELECT MAX (EXTRACT(YEAR FROM hire_date))- MIN (EXTRACT(YEAR FROM hire_date)) FROM employees)+1;*/

SELECT YEAR FROM v_years;






SELECT v.YEAR --, EXTRACT(YEAR FROM hire_date) 
      ,SUM(DECODE ( v.YEAR, EXTRACT(YEAR FROM hire_date) ,1,0)) AS s1
      ,SUM(CASE
         WHEN v.YEAR = EXTRACT(YEAR FROM hire_date) THEN 1
           ELSE 0
       END )AS s2
FROM v_years v CROSS JOIN employees e
GROUP BY v.YEAR
ORDER BY v.YEAR


-- how many employees were hired in each year
SELECT v.YEAR, SUM(decode(EXTRACT(YEAR FROM hire_date),v.YEAR,1,0)) AS qty
FROM employees e CROSS JOIN v_years v  
GROUP BY v.YEAR
ORDER BY v.year

/*--------------------------------
              INNER JOIN
---------------------------------*/
--#1
SELECT *
FROM t1 INNER JOIN t2 ON t1.id = t2.id;

-- Task: for each row in T1 list records from T2, that store greater number than current T1.ID


--#2
SELECT e.first_name||' '||e.last_name AS fi,
       e.department_id, d.department_id, d.department_name 
FROM employees e 
     INNER JOIN departments d ON e.department_id = d.department_id; 

-- Implicit form
SELECT e.first_name||' '||e.last_name AS fi,
       e.department_id, d.department_id, d.department_name
FROM employees e, departments d
WHERE e.department_id = d.department_id ;



SELECT e.first_name||' '||e.last_name AS fi,
       e.department_id, d.department_id, d.department_name
FROM employees e, departments d
WHERE e.manager_id = d.manager_id;

SELECT e.first_name||' '||e.last_name AS fi,
       e.department_id, d.department_id, d.department_name
FROM employees e, departments d
WHERE e.manager_id = d.location_id;

SELECT e.first_name||' '||e.last_name AS fi,
       e.department_id, d.department_id, d.department_name
FROM employees e, departments d
WHERE e.job_id = d.location_id;



--#3
SELECT e.last_name, e.first_name,  
       j.job_title
FROM employees e
     JOIN jobs j ON e.job_id = j.job_id;
		 
		 
-- TASKS
--#1
/*Print departments that are located in region ‘Americas’. List:
  -  Department name
  - City, where the department is located*/ 
 --#1 
SELECT d.department_name, l.city
      ,r.region_name
FROM  departments d
      JOIN locations l ON l.location_id = d.location_id
      JOIN countries c ON c.country_id = l.country_id
      JOIN regions r ON (r.region_id = c.region_id AND r.region_name = 'Americas');

--#2 yes!
SELECT d.department_name, l.city
      ,r.region_name
FROM  departments d
      JOIN locations l ON l.location_id = d.location_id
      JOIN countries c ON c.country_id = l.country_id
      JOIN regions r ON r.region_id = c.region_id     
WHERE   r.region_name = 'Americas';


--Oracle 
SELECT d.department_name, l.city
      ,r.region_name
FROM  departments d, locations l,countries c, regions r    
WHERE l.location_id = d.location_id
      AND  c.country_id = l.country_id
      AND r.region_id = c.region_id 
      AND r.region_name = 'Americas';
      
      
--#2
/*Find out the amount of employees in each department. Print:
 - department name,
 - the amount of employees
*/	

--#3
/*List all employees having the same manager as Sarah Bell (do not list Sarah Bell).*/
SELECT e.manager_id, e1.first_name || ' '||e1.last_name AS full_name
FROM employees e /*IT'S for Sarah*/, employees e1 /*that's Sarah's rM mates*/
WHERE e.first_name = 'Sarah'
      AND e.last_name = 'Bell'
      AND e.manager_id = e1.manager_id
    /*  AND e1.first_name != 'Sarah'
      AND e1.last_name != 'Bell'*/
  --   AND NOT (e1.first_name = 'Sarah' AND e1.last_name = 'Bell')
    AND e.employee_id !=e1.employee_id

--#4
/*Find out the amount of employees in each department on each job. Print:
- department name,
- job title,
- the amount of employees.
*/





/*--------------------------------
              LEFT OUTER JOIN
---------------------------------*/
	 
SELECT d.department_id, d.department_name, 
       e.employee_id, e.first_name||' '||e.last_name AS fi
FROM departments d
     LEFT JOIN employees e  ON e.department_id = d.department_id; 
     
     
SELECT d.department_id, d.department_name, 
       e.employee_id, e.first_name||' '||e.last_name AS fi
FROM employees e 
     LEFT JOIN  departments d ON e.department_id = d.department_id; 

--Oracle-style
SELECT d.department_id, d.department_name, 
       e.employee_id, e.first_name||' '||e.last_name AS fi
FROM employees e, departments d 
WHERE e.department_id = d.department_id(+); 


/*Find out the amount of employees in each department. Print:
 - department name,
 - the amount of employees (zero, if department hasn't employees)
*/	

SELECT d.department_name,employee_id
FROM departments d
     LEFT JOIN employees e ON d.department_id = e.department_id




SELECT d.department_name, COUNT(e.employee_id) AS qty,COUNT(*) AS qty2
       ,COUNT(d.department_id) qty3, COUNT(e.department_id) qty4
FROM departments d
     FULL JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name
ORDER BY qty;


--The same task with implicit left join

SELECT d.department_name, COUNT(e.employee_id) AS qty,COUNT(*) AS qty2
FROM departments d, employees e
WHERE d.department_id  = e.department_id (+)
GROUP BY d.department_id, d.department_name
ORDER BY qty;

--
SELECT d.department_id, d.department_name
FROM departments d
     LEFT JOIN employees e  ON e.department_id = d.department_id
WHERE e.employee_id IS NULL 
ORDER BY d.department_name ;


/*--------------------------------
              RIGHT OUTER JOIN
---------------------------------*/

/*For each employee print out:
- his/her full name,
- according department.*/
SELECT d.department_name, 
       first_name||' '||last_name AS Full_name
FROM departments d
     RIGHT JOIN employees e  ON e.department_id = d.department_id;
		 
--Difference ?

SELECT d.department_name, 
       first_name||' '||last_name AS Full_name
FROM departments d
     RIGHT JOIN employees e  ON  d.department_id = e.department_id ;
		 
SELECT d.department_name, 
       first_name||' '||last_name AS Full_name
FROM employees e 
     LEFT JOIN departments d  ON e.department_id = d.department_id;
     
     
SELECT d.department_name, l.city
      ,r.region_name
FROM  departments d
      LEFT JOIN locations l ON l.location_id = d.location_id
      LEFT JOIN countries c ON c.country_id = l.country_id
      JOIN regions r ON r.region_id = c.region_id     
     
		 
--TASKS
--#1
--Print out jobs, that nobody obtains

--#2
--For each employee list their full name and full name of their manager.


/*--------------------------------
      FULL OUTER JOIN
---------------------------------*/

SELECT t1.id AS id1, t2.id AS id2
FROM t1 FULL OUTER JOIN t2 ON t1.id = t2.id;

--TASK
/*Find out the amount of employees in each department on each job. Print:
- department name,
- job title,
- the amount of employees (or zero).*/


--Find out departments with no employees and employees without a department:
SELECT d.department_name, e.first_name||' '|| e.last_name AS Full_Name
FROM departments d
     FULL JOIN employees e ON d.department_id = e.department_id
WHERE d.department_id IS NULL
      OR e.employee_id IS NULL; 
			
		
--with coalesce
SELECT COALESCE(d.department_name, e.first_name||' '|| e.last_name) AS FULL
FROM departments d
     FULL JOIN employees e ON d.department_id = e.department_id
WHERE d.department_id IS NULL
      OR e.employee_id IS NULL; 

--with decode

--with case 
			
