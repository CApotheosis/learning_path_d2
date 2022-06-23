# Python Data Types
## Python Numbers
Integers, floating point numbers and complex numbers fall under Python numbers category. 
Integers can be of any length, it is only limited by the memory available.
A floating-point number is accurate up to 15 decimal places. 

## Immutable:
- numbers
- string
- tuple
- frozenset
- 
## Mutable:
- list
- set
- dict


"company_names": [
  "admitad",
  "itechart",
  "leverx",
  "itransition",
  "innowise",
  "altoros",
  "playtika"
  "wargaming",
  "andersen",
  "sciencesoft",
  "godel",
  "softswiss",
  "sk hynix",
  
  "exadel",
  "forte group",
  "issoft",
],
with junior as
  (SELECT 
      DISTINCT jv.primary_skill as junior_primary_skill, count(jv.primary_skill) as junior_vacancy_count
FROM 


 update tasks
 set is_valid_for_report = false
 where start_time not in (
 	1628856867509872800,
 	1633079178835473000,
 	1633597420840795000,
 	1633893400671642000,
 	1634149011926449000,
 	1634245697789702000,
 	1634856358781391000,
 	1638954851858493800,
 	1639574484994365700,
 	1639702804986125924,
 	1639789204978110553,
 	1639962005291070438,
 	1640090034831766100,
 	1640134804787643488,
 	1640267336454456800,
 	1640394004952972506,
 	1640480404766359907,
 	1640566805225849198,
 	1640653204941993178,
 	1640739606041344834,
 	1640826004712360067,
 	1640912404785301137,
 	1640998804862289930,
 	1641085205006909744,
 	1641171605027896666,
 	1641258004710613297,
 	1641409681796168843,
 	1641430804887880814
 );
-- select count(vacancies.task_id) from vacancies, (
-- select id from tasks
-- where is_valid_for_report = true
-- ) AS foo
-- where foo.id = vacancies.task_id


-- select count(*) from tasks
-- inner join vacancies on vacancies.task_id = tasks.id
-- where start_time = 1634157681493423000;

-- select tasks.is_valid_for_report, to_timestamp(tasks.start_time / POWER(10, 9))::date as start_date, tasks.start_time as time, count(vacancies.id) as counter  
-- from tasks, vacancies
-- where tasks.id = vacancies.task_id and tasks.is_valid_for_report = true
-- GROUP BY tasks.id 
-- having count(vacancies.id) > 100
-- order by start_date;
