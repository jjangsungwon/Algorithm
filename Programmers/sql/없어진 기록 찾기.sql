SELECT o.animal_id, o.name
FROM (animal_outs o left outer join animal_ins i on (o.animal_id = i.animal_id))
WHERE i.animal_id IS NULL
ORDER BY o.animal_id