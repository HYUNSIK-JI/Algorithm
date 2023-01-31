SELECT
    A.CATEGORY, A.price AS MAX_PRICE, A.PRODUCT_NAME
FROM
    FOOD_PRODUCT AS A,
    (
        SELECT CATEGORY, MAX(price) AS price
        FROM FOOD_PRODUCT
        GROUP BY CATEGORY
    ) as B
WHERE A.CATEGORY in ('과자', '국', '김치', '식용유') 
and A.price = B.price 
and A.CATEGORY = B.CATEGORY
GROUP BY A.category
ORDER BY A.price DESC