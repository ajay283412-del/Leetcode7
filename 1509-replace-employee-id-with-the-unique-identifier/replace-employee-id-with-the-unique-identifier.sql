# Write your MySQL query statement below
select unique_id,name 
from Employees as A
left join 
EmployeeUNI as B
on A.id = B.id;