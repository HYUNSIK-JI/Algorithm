SELECT MEMBER_ID, MEMBER_NAME, GENDER, 
DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE MONTH(DATE_OF_BIRTH) = "03" and TLNO is not null and GENDER ="W"
order by MEMBER_ID