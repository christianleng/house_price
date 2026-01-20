ALTER TABLE properties 
ADD COLUMN IF NOT EXISTS photos_count INTEGER NOT NULL DEFAULT 0;

UPDATE properties 
SET photos_count = (
    SELECT COUNT(*) 
    FROM photos 
    WHERE photos.property_id = properties.id
);

SELECT 
    p.id,
    p.title,
    p.photos_count,
    COUNT(ph.id) as actual_photos_count
FROM properties p
LEFT JOIN photos ph ON ph.property_id = p.id
GROUP BY p.id, p.title, p.photos_count
HAVING p.photos_count != COUNT(ph.id);
