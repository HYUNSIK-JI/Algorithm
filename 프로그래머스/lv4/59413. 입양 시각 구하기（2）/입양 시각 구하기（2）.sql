WITH RECURSIVE AllHours AS (
    SELECT 0 AS HOUR 
    UNION ALL 
    SELECT HOUR + 1 FROM AllHours WHERE HOUR < 23
)

SELECT 
    h.HOUR,
    COALESCE(COUNT(a.DATETIME), 0) AS COUNT
FROM 
    AllHours h
LEFT JOIN 
    ANIMAL_OUTS a ON h.HOUR = HOUR(a.DATETIME)
GROUP BY 
    h.HOUR
ORDER BY 
    h.HOUR;
