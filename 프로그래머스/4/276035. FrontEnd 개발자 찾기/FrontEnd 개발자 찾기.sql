select
    devel.id as id,
    devel.email as email,
    devel.FIRST_NAME as FIRST_NAME,
    devel.LAST_NAME as LAST_NAME
from DEVELOPERS as devel
where devel.skill_code & (
    select sum(skill.code)
    from SKILLCODES as skill
    where skill.CATEGORY = 'Front End'
) != 0
order by id