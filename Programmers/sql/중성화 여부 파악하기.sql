SELECT animal_id, name,
    (
        CASE WHEN sex_upon_intake like "%Neutered%" or sex_upon_intake like "%Spayed%" 
        THEN 'O'
        ELSE 'X'
        END
    ) as 'Áß¼ºÈ­'
FROM animal_ins
ORDER BY ANIMAL_ID