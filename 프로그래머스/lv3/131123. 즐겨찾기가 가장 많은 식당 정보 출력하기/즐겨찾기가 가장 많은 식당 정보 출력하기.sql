SELECT A.FOOD_TYPE, A.REST_ID, A.REST_NAME, A.FAVORITES
FROM REST_INFO AS A
WHERE A.FAVORITES = (SELECT 
                     MAX(B.FAVORITES) 
                     FROM REST_INFO AS B 
                     INNER JOIN REST_INFO 
                     ON A.food_type = B.food_type)
GROUP BY A.FOOD_TYPE
ORDER BY FOOD_TYPE DESC