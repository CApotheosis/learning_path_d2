select *
from [Person].[Person];

select 'abrakadabra'
from Person.Person


select distinct title
from Person.Person

select [BusinessEntityID],[PersonType],[NameStyle],[Title],
[FirstName], [FirstName], 1
from [Person].[Person];

select getdate() as HereAndNow; 

--string routines
SELECT FirstName + ' ' + LastName AS FullName         
        ,LEN(LastName) AS LastNameLength 
        ,NCHAR(BusinessEntityID) AS RandomSymbol 
	     ,REVERSE(FirstName) AS ReverseString  
         ,LOWER(FirstName) AS LowerString
	     ,UPPER(FirstName) AS UpperString
FROM Person.Person;


select NCHAR(97) 
--current date
select getdate();
--next date
select getdate() + 1;

select DATEADD(hh,1,getdate());
select DATEADD(yy,1,getdate());

--extracting parts from date
select getdate() as ddd
      ,year(getdate()) as y
      ,month(getdate()) as m
	  ,day(getdate()) as d;

--addding intervals to the date
select dateadd(month,2, getdate() ) as In2Month
       , dateadd(year,2, getdate() );

SELECT '06.03.2020' + 1

select dateadd(dd,1,datefromparts(2020,3,6))

	  

--Experience in year for each employee
select HireDate
       ,DATEDIFF(year, HireDate,getdate() ) as experience
from HumanResources.Employee;




select getdate(), '01.01.'+ year(dateadd(year,1, getdate() ))
 


-- converting string to date
select  dateadd(month,2, '04.03.2001');

select  dateadd(month,2, convert(date, '04.03.01', 2));

--NULLS
SELECT  5 + NULL AS s1
       ,5 - NULL AS s2
       ,5 * NULL AS s3
	   ,5 / NULL AS s4;

select [MiddleName] , isnull(MiddleName, 'NO')
from [Person].[Person];

--first not null
SELECT Name, Class, Color, ProductNumber,
       COALESCE(Class, Color,'Ops') AS FirstNotNull
FROM Production.Product;


SELECT COALESCE(Class, Color,ProductNumber) AS FirstNotNull
       ,COALESCE(Color,Class,ProductNumber) AS FirstNotNull1
      , Name, Class, Color, ProductNumber
FROM Production.Product;

select color,
       case 
	     when color = 'BLACK' then 'ops'
		 else color
		end
from Production.Product

SELECT COALESCE( Color,Class, ProductNumber) AS FirstNotNull
      , Name, Class, Color, ProductNumber
FROM Production.Product;

select p.Class
FROM Production.Product p;





SELECT Name, Class, Color, ProductNumber,
       COALESCE(Color, Class, ProductNumber) AS FirstNotNull
	   , COALESCE(Class, Color, ProductNumber) AS FirstNotNull1
	   , COALESCE(ProductNumber, Class, Color)
FROM Production.Product;

select [MiddleName] , isnull(isnull([Title],MiddleName), 'NO'),
       coalesce(MiddleName, 'NO')
from [Person].[Person];

select distinct [Gender],
       case
	      when [Gender] = 'F' then 'Female'
		  when [Gender] ='M' then 'Male'
		  else 'Ops'
	   end as n
from [HumanResources].[Employee]


select datediff(dd
               ,getdate()
		       , datefromparts(year(getdate()),12,31)) +1 


select FirstName,MiddleName,LastName
from [Person].[Person]
--where MiddleName = 'A'
order by  [BusinessEntityID],MiddleName 

select FirstName,MiddleName,LastName
from [Person].[Person]
order by  MiddleName desc

--- ordering
select FirstName,MiddleName,LastName, [BusinessEntityID]
from [Person].[Person]
order by LastName, MiddleName desc
offset 0 rows
     FETCH next 4 ROWS with ties;

select top 4 with ties FirstName,MiddleName,LastName, [BusinessEntityID]
from [Person].[Person]
order by LastName, MiddleName desc

--list the first largest rates: 
select top 10 Rate
from HumanResources.EmployeePayHistory
order by rate desc;

--vs

select  top 10 with ties Rate
from HumanResources.EmployeePayHistory
order by rate desc

--List 5% of the largest rates:
select top 5 percent Rate
from HumanResources.EmployeePayHistory
order by rate desc;

select 316*5/100

select * 
from HumanResources.EmployeePayHistory
select Rate
from HumanResources.EmployeePayHistory

select 316*0.05

SELECT distinct  FirstName 
FROM Person.Person 
where FirstName like 'a%'

--comparing
SELECT distinct  FirstName 
FROM Person.Person 
where FirstName like 'Andre[aw]'
order by FirstName;

SELECT distinct  FirstName 
FROM Person.Person 
where FirstName like 'Andre_'
order by FirstName;

SELECT distinct  FirstName 
FROM Person.Person 
where FirstName like 'Andre%'
order by FirstName;

select LoginID
from HumanResources.Employee
where LoginID like '%[1-9]%'



--List all employees with underscore in a login:
select LoginID
from HumanResources.Employee
where LoginID like '%[_]%';

--PRACTICE

/*List all countries with complex names 
(more then 2 words with space or ‘-’ delimiter). */


/*List all persons without middle name or with a middle name 
with the only one letter (‘J’ or ‘J.’)*/ 


/*List logins of all single males who are older 
then 25 but younger then 45  and obtains any manager position.*/