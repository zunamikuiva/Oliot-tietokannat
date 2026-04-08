SELECT
    city,
    COUNT(*) 
FROM Accounts
GROUP BY city
HAVING COUNT(*) >= 5
ORDER BY city ASC;