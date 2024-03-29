SELECT A.USER_ID, A.NICKNAME, 
CONCAT(A.CITY," ", A.STREET_ADDRESS1, " ", A.STREET_ADDRESS2) AS 전체주소,
CONCAT(SUBSTRING(A.TLNO FROM 1 FOR 3), "-", SUBSTRING(A.TLNO FROM 4 FOR 4), "-", SUBSTRING(A.TLNO FROM 8 FOR 4)) AS 전화번호
FROM USED_GOODS_USER AS A
INNER JOIN USED_GOODS_BOARD AS B
ON A.USER_ID = B.WRITER_ID
GROUP BY B.WRITER_ID
HAVING COUNT(B.WRITER_ID) >= 3
ORDER BY A.USER_ID DESC