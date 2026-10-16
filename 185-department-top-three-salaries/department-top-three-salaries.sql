# Write your MySQL query statement below
select
d.name As Department,
e.name As Employee,
e.salary As Salary
from Employee e
inner join Department d on e.departmentId = d.id
where 3 > (
    select count(DISTINCT t.salary)
    from Employee t
    where t.salary > e.salary
    and e.DepartmentId=t.DepartmentId
)