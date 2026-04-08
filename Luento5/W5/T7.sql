SELECT
    name,
    vitamin,
    value
FROM fruit
WHERE name NOT IN (
    SELECT name
    FROM fruit
    WHERE vitamin = 'Folate (folic acid)'
)
ORDER BY name DESC, vitamin ASC;