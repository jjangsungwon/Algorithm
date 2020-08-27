SELECT i.animal_id, i.name
FROM animal_ins i left outer join animal_outs o on (i.animal_id = o.animal_id)
WHERE i.datetime > o.datetime
ORDER BY i.datetime