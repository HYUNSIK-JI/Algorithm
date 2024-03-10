select info.ID, info.EMAIL, info.FIRST_NAME, info.LAST_NAME
from DEVELOPER_INFOS as info
where info.SKILL_1 = 'Python' or info.SKILL_2 = 'Python' or info.SKILL_3 = 'Python'
order by info.ID