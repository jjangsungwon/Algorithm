SELECT i.name, i.datetime
FROM (animal_ins i left outer join animal_outs o on (i.animal_id = o.animal_id))
WHERE o.animal_id IS NULL
ORDER BY i.datetime
LIMIT 3
