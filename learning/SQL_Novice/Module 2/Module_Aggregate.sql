SELECT job_id,department_id,hire_date,salary
FROM employees
WHERE job_id = 'IT_PROG'


--Count 
SELECT COUNT(*) as total_qty
       ,COUNT(ALL e.Manager_Id) as not_null_qty_a
       ,COUNT( e.Manager_Id) as not_null_qty
       ,COUNT(DISTINCT e.Manager_Id) as unique_qty
			 ,COUNT(*) - COUNT(Manager_Id) AS bosses_qty
FROM employees e;

--PRACTICE
--#1 Find out how many employees haven’t bonuses
SELECT COUNT(*)
FROM employees
WHERE commission_pct IS NULL

SELECT COUNT(*) - COUNT(commission_pct) 
FROM employees;

SELECT COUNT( DECODE(commission_pct,NULL,1,NULL) )
FROM employees;

SELECT commission_pct
      ,DECODE(commission_pct,NULL,1,NULL)
FROM employees  

SELECT COUNT(DECODE(commission_pct, NULL,1,NULL))
FROM employees

SELECT COUNT(CASE
             WHEN commission_pct IS NULL THEN 1
              ELSE NULL
             END)
FROM employees

-- Find out total salary of all employees
SELECT SUM(e.salary) AS total_sum
FROM employees e;

--Practice
--Calculate the total salary of employees taking into account bonuses



--Find out average salary and bonuses percentage for all employees
SELECT AVG(e.salary) AS avg_salary
       ,AVG(e.commission_pct) AS  avg_bonus
       ,SUM(commission_pct) / COUNT(*) AS avg_bonus1
       ,AVG(NVL(commission_pct,0))
FROM employees e;

SELECT COUNT(*), COUNT(commission_pct),COUNT(first_name)
FROM employees e




-- using max and min
SELECT MAX(salary) AS max_s
       ,MIN(salary) AS min_s
FROM employees e;

SELECT MAX(hire_date) AS max_s
       ,MIN(hire_date) AS min_s
FROM employees e;

SELECT MAX(first_name) AS max_s
       ,MIN(first_name) AS min_s
FROM employees e;


SELECT MAX(commission_pct) AS max_s
       ,MIN(commission_pct) AS min_s
FROM employees e;

SELECT MAX(commission_pct) AS max_s
       ,MIN(commission_pct) AS min_s
FROM employees e
WHERE commission_pct IS NULL; 


SELECT SUM(salary)
FROM employees e
WHERE department_id=80
		
/*Print out the last names of employees in the 30th department and the date of hiring 
the first employee to the department*/
SELECT LISTAGG(last_name||'->'||hire_date, '; ') 
          WITHIN GROUP (ORDER BY hire_date, last_name) "Emp_list",
       MIN(hire_date) "Earliest"
FROM employees
WHERE department_id = 30;

--Task: print out the number of employees and their total salary for each department
SELECT COUNT(*) AS qty, SUM(salary) AS total_sal
FROM employees
WHERE department_id = 10;



SELECT COUNT(*) AS qty, SUM(salary) AS total_sal
FROM employees
WHERE department_id = 20;

SELECT COUNT(*) AS qty, SUM(salary) AS total_sal
FROM employees
WHERE department_id IN (10,20);


SELECT department_id,COUNT(*) AS qty, SUM(salary) AS total_sal
FROM employees
WHERE department_id IN (10,20);



--won't work
SELECT department_id,COUNT(*) AS qty, SUM(salary) AS total_sal
FROM employees;

SELECT job_id, salary
FROM employees;


--Print out the average salary and the amount of employees in each department
SELECT e.job_id
       ,AVG(e.salary) AS avg_sal
	     ,COUNT(e.employee_id) AS qty
FROM employees e	 
GROUP BY e.job_id;

--PRACTICE
--Print out the amount of employees in each department on each job.
SELECT e.job_id
       ,COUNT(e.employee_id) AS qty
       ,department_id
FROM employees e	 
GROUP BY e.job_id,department_id
--ORDER BY e.job_id,department_id

--List out all departments, where the amount of employees is more than 5. 
SELECT COUNT(e.employee_id) AS qty
       ,department_id
FROM employees e	 
GROUP BY department_id
ORDER BY qty DESC;

SELECT COUNT(e.employee_id) AS qty
       ,department_id
FROM employees e	
WHERE  COUNT(e.employee_id) >5
GROUP BY department_id
ORDER BY qty DESC;




SELECT department_id,COUNT(employee_id) AS qty
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 5;

--#1
SELECT department_id,COUNT(employee_id) AS qty
FROM employees
WHERE department_id >90
GROUP BY department_id
HAVING COUNT(*) > 5;

--#2 - fooooo

SELECT department_id,COUNT(employee_id) AS qty
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 5
       AND department_id >90;
       
       
--PRACTICE
--Print out the average salary for the jobs having more than 5 people.  


--Print out departments, where all employees are on the same job.

--Print out departments, where all employees are on the different jobs.
