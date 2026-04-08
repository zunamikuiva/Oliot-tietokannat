SELECT
    Employee.FirstName,
    Employee.LastName
FROM Employee
JOIN Employee manager ON Employee.ReportsTo = manager.EmployeeId
WHERE manager.FirstName = 'Nancy'
AND manager.LastName = 'Edwards'
ORDER BY Employee.FirstName ASC, Employee.LastName ASC;