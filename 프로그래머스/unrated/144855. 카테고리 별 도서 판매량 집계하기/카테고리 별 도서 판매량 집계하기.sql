SELECT CATEGORY, SUM(B.SALES) AS TOTAL_SALES
FROM BOOK AS A INNER JOIN BOOK_SALES AS B ON A.BOOK_ID = B.BOOK_ID
WHERE DATE_FORMAT(B.SALES_DATE, "%Y-%m") = "2022-01"
GROUP BY CATEGORY
ORDER BY CATEGORY