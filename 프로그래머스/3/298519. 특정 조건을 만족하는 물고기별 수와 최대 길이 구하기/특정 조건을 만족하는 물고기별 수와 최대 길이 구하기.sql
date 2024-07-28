SELECT 
    COUNT(1) AS FISH_COUNT,
    MAX(fish.LENGTH) AS MAX_LENGTH,
    fish.FISH_TYPE AS FISH_TYPE
FROM 
    FISH_INFO AS fish
WHERE 
    fish.FISH_TYPE IN (
        SELECT 
            FISH_TYPE
        FROM 
            FISH_INFO
        GROUP BY 
            FISH_TYPE
        HAVING 
            AVG(IFNULL(LENGTH, 10)) >= 33
    )
GROUP BY 
    fish.FISH_TYPE
ORDER BY fish.FISH_TYPE