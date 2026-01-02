-- =====================================================
-- 05_seed_photos.sql - Photos de test
-- =====================================================

-- Note: Les URLs sont des placeholders. En production, utiliser des vraies URLs
-- (Unsplash, Cloudinary, S3, etc.)

INSERT INTO photos (
    id, property_id, url, 
    url_thumbnail, url_small, url_medium, url_large, url_original,
    url_thumbnail_webp, url_small_webp, url_medium_webp, url_large_webp,
    has_webp, original_filename, original_width, original_height, size_bytes, content_type,
    is_primary, display_order, caption
) VALUES

-- ==================== Photos Property 1: Bastille ====================
(
    'a67894bc-8311-4e08-ae6a-87b8885ff420',
    '780b81ae-3ef4-4b4f-8ac0-092b3ca4c11b',
    'https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=800',
    'https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=150',
    'https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=400',
    'https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=800',
    'https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=1200',
    'https://images.unsplash.com/photo-1502672260266-1c1ef2d93688',
    NULL, NULL, NULL, NULL,
    FALSE, 'salon_bastille.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Séjour lumineux avec parquet ancien'
),
(
    'deae7c14-a4ae-4c89-bd93-bb0d4744db36',
    '780b81ae-3ef4-4b4f-8ac0-092b3ca4c11b',
    'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800',
    'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=150',
    'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=400',
    'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800',
    'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=1200',
    'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2',
    NULL, NULL, NULL, NULL,
    FALSE, 'chambre1_bastille.jpg', 1920, 1280, 412000, 'image/jpeg',
    FALSE, 1, 'Chambre principale'
),
(
    '24044683-cad0-430d-a93e-f2f45489687b',
    '780b81ae-3ef4-4b4f-8ac0-092b3ca4c11b',
    'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=800',
    'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=150',
    'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=400',
    'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=800',
    'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=1200',
    'https://images.unsplash.com/photo-1584622650111-993a426fbf0a',
    NULL, NULL, NULL, NULL,
    FALSE, 'sdb_bastille.jpg', 1920, 1280, 380000, 'image/jpeg',
    FALSE, 2, 'Salle de bains'
),

-- ==================== Photos Property 2: Passy luxe ====================
(
    '48cc2da8-cbcb-491f-8266-f00a0ef21b92',
    'd53e4ef6-5bf8-428a-9aa4-9d631b047f99',
    'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800',
    'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=150',
    'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=400',
    'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800',
    'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1200',
    'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9',
    NULL, NULL, NULL, NULL,
    FALSE, 'salon_passy.jpg', 1920, 1280, 612000, 'image/jpeg',
    TRUE, 0, 'Double séjour avec cheminée'
),
(
    '197c75ff-9e42-4f07-95a7-d802d726b258',
    'd53e4ef6-5bf8-428a-9aa4-9d631b047f99',
    'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=800',
    'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=150',
    'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=400',
    'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=800',
    'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=1200',
    'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c',
    NULL, NULL, NULL, NULL,
    FALSE, 'terrasse_passy.jpg', 1920, 1280, 580000, 'image/jpeg',
    FALSE, 1, 'Terrasse avec vue Tour Eiffel'
),
(
    'a98075fd-d988-4253-a7eb-60e0e48e688f',
    'd53e4ef6-5bf8-428a-9aa4-9d631b047f99',
    'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=800',
    'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=150',
    'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=400',
    'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=800',
    'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=1200',
    'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3',
    NULL, NULL, NULL, NULL,
    FALSE, 'cuisine_passy.jpg', 1920, 1280, 490000, 'image/jpeg',
    FALSE, 2, 'Cuisine équipée Gaggenau'
),
(
    '7e341a9f-72d7-47c1-8f6b-5c3eb62fe5e5',
    'd53e4ef6-5bf8-428a-9aa4-9d631b047f99',
    'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=800',
    'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=150',
    'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=400',
    'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=800',
    'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1200',
    'https://images.unsplash.com/photo-1600585154340-be6161a56a0c',
    NULL, NULL, NULL, NULL,
    FALSE, 'chambre_passy.jpg', 1920, 1280, 510000, 'image/jpeg',
    FALSE, 3, 'Suite parentale'
),

-- ==================== Photos Property 3: Studio Montmartre ====================
(
    '9cd8e2e1-f6e2-4df3-8694-bc993a339633',
    '6fb71fbf-b34d-4613-8d8e-7f96d58cb084',
    'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=800',
    'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=150',
    'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=400',
    'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=800',
    'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=1200',
    'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267',
    NULL, NULL, NULL, NULL,
    FALSE, 'studio_montmartre.jpg', 1920, 1280, 420000, 'image/jpeg',
    TRUE, 0, 'Pièce principale rénovée'
),
(
    'cd693fa5-f323-49f3-9218-f2e751b6f76a',
    '6fb71fbf-b34d-4613-8d8e-7f96d58cb084',
    'https://images.unsplash.com/photo-1560185893-a55cbc8c57e8?w=800',
    'https://images.unsplash.com/photo-1560185893-a55cbc8c57e8?w=150',
    'https://images.unsplash.com/photo-1560185893-a55cbc8c57e8?w=400',
    'https://images.unsplash.com/photo-1560185893-a55cbc8c57e8?w=800',
    'https://images.unsplash.com/photo-1560185893-a55cbc8c57e8?w=1200',
    'https://images.unsplash.com/photo-1560185893-a55cbc8c57e8',
    NULL, NULL, NULL, NULL,
    FALSE, 'cuisine_montmartre.jpg', 1920, 1280, 350000, 'image/jpeg',
    FALSE, 1, 'Cuisine équipée'
),

-- ==================== Photos Property 4: Loft Montreuil ====================
(
    'fa2c50de-b514-4307-8ed4-48e19b3aa109',
    '718d7bb5-560a-406a-87ca-694ed54f5107',
    'https://images.unsplash.com/photo-1600607687644-c7171b42498b?w=800',
    'https://images.unsplash.com/photo-1600607687644-c7171b42498b?w=150',
    'https://images.unsplash.com/photo-1600607687644-c7171b42498b?w=400',
    'https://images.unsplash.com/photo-1600607687644-c7171b42498b?w=800',
    'https://images.unsplash.com/photo-1600607687644-c7171b42498b?w=1200',
    'https://images.unsplash.com/photo-1600607687644-c7171b42498b',
    NULL, NULL, NULL, NULL,
    FALSE, 'loft_montreuil.jpg', 1920, 1280, 680000, 'image/jpeg',
    TRUE, 0, 'Espace de vie avec verrière'
),
(
    '18f3ced7-2d08-481f-938c-b511a339887d',
    '718d7bb5-560a-406a-87ca-694ed54f5107',
    'https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?w=800',
    'https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?w=150',
    'https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?w=400',
    'https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?w=800',
    'https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?w=1200',
    'https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b',
    NULL, NULL, NULL, NULL,
    FALSE, 'jardin_montreuil.jpg', 1920, 1280, 520000, 'image/jpeg',
    FALSE, 1, 'Jardin privatif'
),

-- ==================== Photos Property 5: Location Passy ====================
(
    '845aec8d-c1d7-4c45-a8a2-a9e0f0dd0b53',
    'a326dae9-b9f9-428b-9e79-2acbcc078c82',
    'https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=800',
    'https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=150',
    'https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=400',
    'https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=800',
    'https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=1200',
    'https://images.unsplash.com/photo-1600210492486-724fe5c67fb0',
    NULL, NULL, NULL, NULL,
    FALSE, 'sejour_loc_passy.jpg', 1920, 1280, 450000, 'image/jpeg',
    TRUE, 0, 'Séjour meublé design'
),

-- ==================== Photos Property 7: Lyon Presqu''île ====================
(
    '0edc846a-5bcf-4882-8cc2-feaec8647b21',
    'bfcf9b00-007d-4203-942b-007353ac0855',
    'https://images.unsplash.com/photo-1600573472550-8090b5e0745e?w=800',
    'https://images.unsplash.com/photo-1600573472550-8090b5e0745e?w=150',
    'https://images.unsplash.com/photo-1600573472550-8090b5e0745e?w=400',
    'https://images.unsplash.com/photo-1600573472550-8090b5e0745e?w=800',
    'https://images.unsplash.com/photo-1600573472550-8090b5e0745e?w=1200',
    'https://images.unsplash.com/photo-1600573472550-8090b5e0745e',
    NULL, NULL, NULL, NULL,
    FALSE, 'salon_lyon.jpg', 1920, 1280, 510000, 'image/jpeg',
    TRUE, 0, 'Séjour avec moulures'
),
(
    'c2a8db6f-9088-4789-a3c0-230339fd5c21',
    'bfcf9b00-007d-4203-942b-007353ac0855',
    'https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?w=800',
    'https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?w=150',
    'https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?w=400',
    'https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?w=800',
    'https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?w=1200',
    'https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde',
    NULL, NULL, NULL, NULL,
    FALSE, 'cheminee_lyon.jpg', 1920, 1280, 480000, 'image/jpeg',
    FALSE, 1, 'Cheminée en marbre'
),

-- ==================== Photos Property 10: Marseille Vieux-Port ====================
(
    '6eb19549-f019-453e-b8b9-d1970c98f65b',
    '4cd19b24-3e11-439a-a8ad-d5af0b2c4b05',
    'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800',
    'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=150',
    'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=400',
    'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800',
    'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1200',
    'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9',
    NULL, NULL, NULL, NULL,
    FALSE, 'salon_marseille.jpg', 1920, 1280, 590000, 'image/jpeg',
    TRUE, 0, 'Séjour vue mer'
),
(
    'ff0c5e0f-d897-4e15-ac6d-dd51cc304566',
    '4cd19b24-3e11-439a-a8ad-d5af0b2c4b05',
    'https://images.unsplash.com/photo-1600566752355-35792bedcfea?w=800',
    'https://images.unsplash.com/photo-1600566752355-35792bedcfea?w=150',
    'https://images.unsplash.com/photo-1600566752355-35792bedcfea?w=400',
    'https://images.unsplash.com/photo-1600566752355-35792bedcfea?w=800',
    'https://images.unsplash.com/photo-1600566752355-35792bedcfea?w=1200',
    'https://images.unsplash.com/photo-1600566752355-35792bedcfea',
    NULL, NULL, NULL, NULL,
    FALSE, 'terrasse_marseille.jpg', 1920, 1280, 620000, 'image/jpeg',
    FALSE, 1, 'Terrasse panoramique'
),

-- ==================== Photos Property 11: Bordeaux Échoppe ====================
(
    '041ec46e-4057-4fa2-8ea6-27e520c02270',
    'ea771c5b-d25f-4518-91e5-8e2a9f7e7a01',
    'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=800',
    'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=150',
    'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=400',
    'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=800',
    'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1200',
    'https://images.unsplash.com/photo-1600585154340-be6161a56a0c',
    NULL, NULL, NULL, NULL,
    FALSE, 'echoppe_bordeaux.jpg', 1920, 1280, 540000, 'image/jpeg',
    TRUE, 0, 'Façade échoppe bordelaise'
),
(
    'ffaadf12-d09c-4de8-afbd-767ac6145c64',
    'ea771c5b-d25f-4518-91e5-8e2a9f7e7a01',
    'https://images.unsplash.com/photo-1600566752447-e2b9d3e4c9c0?w=800',
    'https://images.unsplash.com/photo-1600566752447-e2b9d3e4c9c0?w=150',
    'https://images.unsplash.com/photo-1600566752447-e2b9d3e4c9c0?w=400',
    'https://images.unsplash.com/photo-1600566752447-e2b9d3e4c9c0?w=800',
    'https://images.unsplash.com/photo-1600566752447-e2b9d3e4c9c0?w=1200',
    'https://images.unsplash.com/photo-1600566752447-e2b9d3e4c9c0',
    NULL, NULL, NULL, NULL,
    FALSE, 'jardin_bordeaux.jpg', 1920, 1280, 480000, 'image/jpeg',
    FALSE, 1, 'Jardin arboré'
),

-- ==================== Photos Property 13: Nice Promenade ====================
(
    '5ec85b7c-d9ac-4274-b4a6-920374a215a0',
    'b9a78f27-9d4d-48b9-b21e-b96f6c62e301',
    'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=800',
    'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=150',
    'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=400',
    'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=800',
    'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=1200',
    'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c',
    NULL, NULL, NULL, NULL,
    FALSE, 'vue_nice.jpg', 1920, 1280, 650000, 'image/jpeg',
    TRUE, 0, 'Vue mer depuis le séjour'
),
(
    'f3258426-a64a-4404-ac91-f2f2871ebf40',
    'b9a78f27-9d4d-48b9-b21e-b96f6c62e301',
    'https://images.unsplash.com/photo-1600566753086-00f18fb6b3ea?w=800',
    'https://images.unsplash.com/photo-1600566753086-00f18fb6b3ea?w=150',
    'https://images.unsplash.com/photo-1600566753086-00f18fb6b3ea?w=400',
    'https://images.unsplash.com/photo-1600566753086-00f18fb6b3ea?w=800',
    'https://images.unsplash.com/photo-1600566753086-00f18fb6b3ea?w=1200',
    'https://images.unsplash.com/photo-1600566753086-00f18fb6b3ea',
    NULL, NULL, NULL, NULL,
    FALSE, 'terrasse_nice.jpg', 1920, 1280, 580000, 'image/jpeg',
    FALSE, 1, 'Terrasse vue Méditerranée'
),

-- ==================== Photos Property 15: Vitry ====================
(
    'c5a44b4f-7e41-4917-aaef-305f157d1bea',
    '53fa9092-2e73-4d07-abcc-1db5da1c257b',
    'https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=800',
    'https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=150',
    'https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=400',
    'https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=800',
    'https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=1200',
    'https://images.unsplash.com/photo-1600585154526-990dced4db0d',
    NULL, NULL, NULL, NULL,
    FALSE, 'maison_vitry.jpg', 1920, 1280, 490000, 'image/jpeg',
    TRUE, 0, 'Façade maison de ville'
),
(
    '40cd7743-dd26-46b8-865f-372752e3d9c8',
    '53fa9092-2e73-4d07-abcc-1db5da1c257b',
    'https://images.unsplash.com/photo-1600566752734-2a0cd66c42c1?w=800',
    'https://images.unsplash.com/photo-1600566752734-2a0cd66c42c1?w=150',
    'https://images.unsplash.com/photo-1600566752734-2a0cd66c42c1?w=400',
    'https://images.unsplash.com/photo-1600566752734-2a0cd66c42c1?w=800',
    'https://images.unsplash.com/photo-1600566752734-2a0cd66c42c1?w=1200',
    'https://images.unsplash.com/photo-1600566752734-2a0cd66c42c1',
    NULL, NULL, NULL, NULL,
    FALSE, 'jardin_vitry.jpg', 1920, 1280, 420000, 'image/jpeg',
    FALSE, 1, 'Jardin privatif'
);

-- ==================== Ajouter des favoris pour tester ====================
INSERT INTO favorites (id, user_id, property_id) VALUES
('950f90a1-2e95-4809-8f59-2eebffc3bcf0', 'a948513d-0702-46a3-999c-af7caeebe060', '780b81ae-3ef4-4b4f-8ac0-092b3ca4c11b'),
('857b2abf-4117-488f-b8f9-c9a6106f46c7', 'a948513d-0702-46a3-999c-af7caeebe060', 'd53e4ef6-5bf8-428a-9aa4-9d631b047f99'),
('902d0448-ca22-4db8-9af9-e5bba2dc02c7', '1ade390f-f531-4224-96ea-de365c81329c', 'bfcf9b00-007d-4203-942b-007353ac0855'),
('881305da-972f-4823-a523-50f65ab0520a', '894c23a7-a078-40b4-91ca-da5d7240fb58', '2015fc04-70e8-41f8-bd56-19970d464adf'),
('257caa3f-1fbe-4adc-8fc3-2bcde559cbe4', 'f6eb9ae3-674b-4804-840a-3e302bbee554', '4cd19b24-3e11-439a-a8ad-d5af0b2c4b05'),
('81f971a4-a6ab-47b6-94d7-8174a27c0ee9', '02e8577c-c21d-43d2-ad34-222da8c72998', '53fa9092-2e73-4d07-abcc-1db5da1c257b');

SELECT 'Photos seeded successfully! Total: ' || COUNT(*) FROM photos;
SELECT 'Favorites seeded successfully! Total: ' || COUNT(*) FROM favorites;