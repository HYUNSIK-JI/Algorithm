select 
    hre.DEPT_ID as DEPT_ID,
    hrd.DEPT_NAME_EN as DEPT_NAME_EN,
    round(sum(hre.SAL) / count(hre.DEPT_ID), 0) as AVG_SAL
from
    HR_DEPARTMENT as hrd,
    HR_EMPLOYEES as hre
where hrd.DEPT_ID = hre.DEPT_ID
group by DEPT_ID
order by AVG_SAL desc