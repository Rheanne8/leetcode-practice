# Write your MySQL query statement below
WITH a AS (SELECT employee.name as Employee, department.name as Department, departmentID, salary
FROM employee
INNER JOIN department
WHERE employee.departmentID = department.id),

b AS (SELECT MAX(Salary) AS salary, departmentID
FROM employee
GROUP BY departmentID)

SELECT Employee, Department, a.salary
FROM a
JOIN b
ON a.salary = b.salary AND a.departmentID = b.departmentID


