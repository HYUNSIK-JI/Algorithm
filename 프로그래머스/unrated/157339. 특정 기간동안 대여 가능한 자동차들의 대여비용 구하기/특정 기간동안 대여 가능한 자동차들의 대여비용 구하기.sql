SELECT A.CAR_ID, A.CAR_TYPE, ROUND(A.DAILY_FEE * 30 * (100 - B.DISCOUNT_RATE) / 100) AS FEE
FROM CAR_RENTAL_COMPANY_CAR AS A

JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS B
ON A.CAR_TYPE = B.CAR_TYPE AND B.DURATION_TYPE = '30일 이상'

WHERE A.CAR_TYPE IN ("세단", "SUV") AND 
    A.CAR_ID NOT IN (
        SELECT CAR_ID
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE END_DATE >= '2022-11-01' AND START_DATE <= '2022-11-30'
    ) AND
    A.DAILY_FEE * 30 * (100 - B.DISCOUNT_RATE) / 100 BETWEEN 500000 AND 1999999
ORDER BY FEE DESC, A.CAR_TYPE, A.CAR_ID DESC;