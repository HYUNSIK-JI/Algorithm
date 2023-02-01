SELECT A.AUTHOR_ID, B.AUTHOR_NAME, A.CATEGORY, SUM(A.price * C.sales) AS TOTAL_SALES
FROM BOOK AS A 
    INNER JOIN AUTHOR AS B ON A.AUTHOR_ID = B.AUTHOR_ID
    INNER JOIN BOOK_SALES AS C ON A.BOOK_ID = C.BOOK_ID
WHERE DATE_FORMAT(C.SALES_DATE, "%Y-%m") = "2022-01"
GROUP BY A.AUTHOR_ID, A.CATEGORY
ORDER BY A.AUTHOR_ID, A.CATEGORY DESC