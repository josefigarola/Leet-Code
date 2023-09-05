# Write your MySQL query statement below
select d1.Name as Department, e1.Name as Employee, e1.Salary as Salary
from Employee e1, Department d1, 

(select d.Id as Id, e.Name as Employee, max(e.Salary) as Salary
from Employee e, Department d
where e.DepartmentId = d.Id
group by d.Id) as a

where e1.DepartmentId = d1.Id and d1.Id = a.Id and a.Salary = e1.Salary