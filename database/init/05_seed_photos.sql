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
    'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=800',
    'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=150',
    'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=400',
    'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=800',
    'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=1200',
    'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267',
    NULL, NULL, NULL, NULL,
    FALSE, 'chambre1_bastille.jpg', 1920, 1280, 412000, 'image/jpeg',
    FALSE, 1, 'Chambre principale'
),
(
    '24044683-cad0-430d-a93e-f2f45489687b',
    '780b81ae-3ef4-4b4f-8ac0-092b3ca4c11b',
    'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800',
    'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=150',
    'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=400',
    'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800',
    'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=1200',
    'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2',
    NULL, NULL, NULL, NULL,
    FALSE, 'sdb_bastille.jpg', 1920, 1280, 380000, 'image/jpeg',
    FALSE, 2, 'Salle de bains'
),

-- ==================== Photos Property 2: Passy luxe ====================
(
    '48cc2da8-cbcb-491f-8266-f00a0ef21b92',
    'd53e4ef6-5bf8-428a-9aa4-9d631b047f99',
    'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=800',
    'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=150',
    'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=400',
    'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=800',
    'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1200',
    'https://images.unsplash.com/photo-1600585154340-be6161a56a0c',
    NULL, NULL, NULL, NULL,
    FALSE, 'salon_passy.jpg', 1920, 1280, 612000, 'image/jpeg',
    TRUE, 0, 'Double séjour avec cheminée'
),
(
    '197c75ff-9e42-4f07-95a7-d802d726b258',
    'd53e4ef6-5bf8-428a-9aa4-9d631b047f99',
    'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800',
    'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=150',
    'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=400',
    'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800',
    'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1200',
    'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9',
    NULL, NULL, NULL, NULL,
    FALSE, 'terrasse_passy.jpg', 1920, 1280, 580000, 'image/jpeg',
    FALSE, 1, 'Terrasse avec vue Tour Eiffel'
),
(
    'a98075fd-d988-4253-a7eb-60e0e48e688f',
    'd53e4ef6-5bf8-428a-9aa4-9d631b047f99',
    'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=800',
    'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=150',
    'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=400',
    'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=800',
    'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=1200',
    'https://images.unsplash.com/photo-1586023492125-27b2c045efd7',
    NULL, NULL, NULL, NULL,
    FALSE, 'cuisine_passy.jpg', 1920, 1280, 490000, 'image/jpeg',
    FALSE, 2, 'Cuisine équipée Gaggenau'
),
(
    '7e341a9f-72d7-47c1-8f6b-5c3eb62fe5e5',
    'd53e4ef6-5bf8-428a-9aa4-9d631b047f99',
    'https://images.unsplash.com/photo-1618219908412-a29a1bb7b86e?w=800',
    'https://images.unsplash.com/photo-1618219908412-a29a1bb7b86e?w=150',
    'https://images.unsplash.com/photo-1618219908412-a29a1bb7b86e?w=400',
    'https://images.unsplash.com/photo-1618219908412-a29a1bb7b86e?w=800',
    'https://images.unsplash.com/photo-1618219908412-a29a1bb7b86e?w=1200',
    'https://images.unsplash.com/photo-1618219908412-a29a1bb7b86e',
    NULL, NULL, NULL, NULL,
    FALSE, 'chambre_passy.jpg', 1920, 1280, 510000, 'image/jpeg',
    FALSE, 3, 'Suite parentale'
),

-- ==================== Photos Property 3: Studio Montmartre ====================
(
    '9cd8e2e1-f6e2-4df3-8694-bc993a339633',
    '6fb71fbf-b34d-4613-8d8e-7f96d58cb084',
    'https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?w=800',
    'https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?w=150',
    'https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?w=400',
    'https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?w=800',
    'https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?w=1200',
    'https://images.unsplash.com/photo-1616486338812-3dadae4b4ace',
    NULL, NULL, NULL, NULL,
    FALSE, 'studio_montmartre.jpg', 1920, 1280, 420000, 'image/jpeg',
    TRUE, 0, 'Pièce principale rénovée'
),
(
    'cd693fa5-f323-49f3-9218-f2e751b6f76a',
    '6fb71fbf-b34d-4613-8d8e-7f96d58cb084',
    'https://images.unsplash.com/photo-1615529328331-f8917597711f?w=800',
    'https://images.unsplash.com/photo-1615529328331-f8917597711f?w=150',
    'https://images.unsplash.com/photo-1615529328331-f8917597711f?w=400',
    'https://images.unsplash.com/photo-1615529328331-f8917597711f?w=800',
    'https://images.unsplash.com/photo-1615529328331-f8917597711f?w=1200',
    'https://images.unsplash.com/photo-1615529328331-f8917597711f',
    NULL, NULL, NULL, NULL,
    FALSE, 'cuisine_montmartre.jpg', 1920, 1280, 350000, 'image/jpeg',
    FALSE, 1, 'Cuisine équipée'
),

-- ==================== Photos Property 4: Loft Montreuil ====================
(
    'fa2c50de-b514-4307-8ed4-48e19b3aa109',
    '718d7bb5-560a-406a-87ca-694ed54f5107',
    'https://images.unsplash.com/photo-1617806118233-18e1de247200?w=800',
    'https://images.unsplash.com/photo-1617806118233-18e1de247200?w=150',
    'https://images.unsplash.com/photo-1617806118233-18e1de247200?w=400',
    'https://images.unsplash.com/photo-1617806118233-18e1de247200?w=800',
    'https://images.unsplash.com/photo-1617806118233-18e1de247200?w=1200',
    'https://images.unsplash.com/photo-1617806118233-18e1de247200',
    NULL, NULL, NULL, NULL,
    FALSE, 'loft_montreuil.jpg', 1920, 1280, 680000, 'image/jpeg',
    TRUE, 0, 'Espace de vie avec verrière'
),
(
    '18f3ced7-2d08-481f-938c-b511a339887d',
    '718d7bb5-560a-406a-87ca-694ed54f5107',
    'https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?w=800',
    'https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?w=150',
    'https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?w=400',
    'https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?w=800',
    'https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?w=1200',
    'https://images.unsplash.com/photo-1583847268964-b28dc8f51f92',
    NULL, NULL, NULL, NULL,
    FALSE, 'jardin_montreuil.jpg', 1920, 1280, 520000, 'image/jpeg',
    FALSE, 1, 'Jardin privatif'
),

-- ==================== Photos Property 5: Location Passy ====================
(
    '845aec8d-c1d7-4c45-a8a2-a9e0f0dd0b53',
    'a326dae9-b9f9-428b-9e79-2acbcc078c82',
    'https://images.unsplash.com/photo-1493809842364-78817add7ffb?w=800',
    'https://images.unsplash.com/photo-1493809842364-78817add7ffb?w=150',
    'https://images.unsplash.com/photo-1493809842364-78817add7ffb?w=400',
    'https://images.unsplash.com/photo-1493809842364-78817add7ffb?w=800',
    'https://images.unsplash.com/photo-1493809842364-78817add7ffb?w=1200',
    'https://images.unsplash.com/photo-1493809842364-78817add7ffb',
    NULL, NULL, NULL, NULL,
    FALSE, 'sejour_loc_passy.jpg', 1920, 1280, 450000, 'image/jpeg',
    TRUE, 0, 'Séjour meublé design'
),

-- ==================== Photos Property 7: Lyon Presqu''île ====================
(
    '0edc846a-5bcf-4882-8cc2-feaec8647b21',
    'bfcf9b00-007d-4203-942b-007353ac0855',
    'https://images.unsplash.com/photo-1554995207-c18c203602cb?w=800',
    'https://images.unsplash.com/photo-1554995207-c18c203602cb?w=150',
    'https://images.unsplash.com/photo-1554995207-c18c203602cb?w=400',
    'https://images.unsplash.com/photo-1554995207-c18c203602cb?w=800',
    'https://images.unsplash.com/photo-1554995207-c18c203602cb?w=1200',
    'https://images.unsplash.com/photo-1554995207-c18c203602cb',
    NULL, NULL, NULL, NULL,
    FALSE, 'salon_lyon.jpg', 1920, 1280, 510000, 'image/jpeg',
    TRUE, 0, 'Séjour avec moulures'
),
(
    'c2a8db6f-9088-4789-a3c0-230339fd5c21',
    'bfcf9b00-007d-4203-942b-007353ac0855',
    'https://images.unsplash.com/photo-1484154218962-a197022b25ba?w=800',
    'https://images.unsplash.com/photo-1484154218962-a197022b25ba?w=150',
    'https://images.unsplash.com/photo-1484154218962-a197022b25ba?w=400',
    'https://images.unsplash.com/photo-1484154218962-a197022b25ba?w=800',
    'https://images.unsplash.com/photo-1484154218962-a197022b25ba?w=1200',
    'https://images.unsplash.com/photo-1484154218962-a197022b25ba',
    NULL, NULL, NULL, NULL,
    FALSE, 'cheminee_lyon.jpg', 1920, 1280, 480000, 'image/jpeg',
    FALSE, 1, 'Cheminée en marbre'
),

-- ==================== Photos Property 10: Marseille Vieux-Port ====================
(
    '6eb19549-f019-453e-b8b9-d1970c98f65b',
    '4cd19b24-3e11-439a-a8ad-d5af0b2c4b05',
    'https://images.unsplash.com/photo-1489171078254-c3365d6e359f?w=800',
    'https://images.unsplash.com/photo-1489171078254-c3365d6e359f?w=150',
    'https://images.unsplash.com/photo-1489171078254-c3365d6e359f?w=400',
    'https://images.unsplash.com/photo-1489171078254-c3365d6e359f?w=800',
    'https://images.unsplash.com/photo-1489171078254-c3365d6e359f?w=1200',
    'https://images.unsplash.com/photo-1489171078254-c3365d6e359f',
    NULL, NULL, NULL, NULL,
    FALSE, 'salon_marseille.jpg', 1920, 1280, 590000, 'image/jpeg',
    TRUE, 0, 'Séjour vue mer'
),
(
    'ff0c5e0f-d897-4e15-ac6d-dd51cc304566',
    '4cd19b24-3e11-439a-a8ad-d5af0b2c4b05',
    'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800',
    'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=150',
    'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400',
    'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800',
    'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200',
    'https://images.unsplash.com/photo-1558618666-fcd25c85cd64',
    NULL, NULL, NULL, NULL,
    FALSE, 'terrasse_marseille.jpg', 1920, 1280, 620000, 'image/jpeg',
    FALSE, 1, 'Terrasse panoramique'
),

-- ==================== Photos Property 11: Bordeaux Échoppe ====================
(
    '041ec46e-4057-4fa2-8ea6-27e520c02270',
    'ea771c5b-d25f-4518-91e5-8e2a9f7e7a01',
    'https://images.unsplash.com/photo-1560440021-33f9b867899d?w=800',
    'https://images.unsplash.com/photo-1560440021-33f9b867899d?w=150',
    'https://images.unsplash.com/photo-1560440021-33f9b867899d?w=400',
    'https://images.unsplash.com/photo-1560440021-33f9b867899d?w=800',
    'https://images.unsplash.com/photo-1560440021-33f9b867899d?w=1200',
    'https://images.unsplash.com/photo-1560440021-33f9b867899d',
    NULL, NULL, NULL, NULL,
    FALSE, 'echoppe_bordeaux.jpg', 1920, 1280, 540000, 'image/jpeg',
    TRUE, 0, 'Façade échoppe bordelaise'
),
(
    'ffaadf12-d09c-4de8-afbd-767ac6145c64',
    'ea771c5b-d25f-4518-91e5-8e2a9f7e7a01',
    'https://images.unsplash.com/photo-1501183638710-841dd1904471?w=800',
    'https://images.unsplash.com/photo-1501183638710-841dd1904471?w=150',
    'https://images.unsplash.com/photo-1501183638710-841dd1904471?w=400',
    'https://images.unsplash.com/photo-1501183638710-841dd1904471?w=800',
    'https://images.unsplash.com/photo-1501183638710-841dd1904471?w=1200',
    'https://images.unsplash.com/photo-1501183638710-841dd1904471',
    NULL, NULL, NULL, NULL,
    FALSE, 'jardin_bordeaux.jpg', 1920, 1280, 480000, 'image/jpeg',
    FALSE, 1, 'Jardin arboré'
),

-- ==================== Photos Property 13: Nice Promenade ====================
(
    '5ec85b7c-d9ac-4274-b4a6-920374a215a0',
    'b9a78f27-9d4d-48b9-b21e-b96f6c62e301',
    'https://images.unsplash.com/photo-1567225557594-88d73e55f2cb?w=800',
    'https://images.unsplash.com/photo-1567225557594-88d73e55f2cb?w=150',
    'https://images.unsplash.com/photo-1567225557594-88d73e55f2cb?w=400',
    'https://images.unsplash.com/photo-1567225557594-88d73e55f2cb?w=800',
    'https://images.unsplash.com/photo-1567225557594-88d73e55f2cb?w=1200',
    'https://images.unsplash.com/photo-1567225557594-88d73e55f2cb',
    NULL, NULL, NULL, NULL,
    FALSE, 'vue_nice.jpg', 1920, 1280, 650000, 'image/jpeg',
    TRUE, 0, 'Vue mer depuis le séjour'
),
(
    'f3258426-a64a-4404-ac91-f2f2871ebf40',
    'b9a78f27-9d4d-48b9-b21e-b96f6c62e301',
    'https://images.unsplash.com/photo-1558882224-dda166c4fbcf?w=800',
    'https://images.unsplash.com/photo-1558882224-dda166c4fbcf?w=150',
    'https://images.unsplash.com/photo-1558882224-dda166c4fbcf?w=400',
    'https://images.unsplash.com/photo-1558882224-dda166c4fbcf?w=800',
    'https://images.unsplash.com/photo-1558882224-dda166c4fbcf?w=1200',
    'https://images.unsplash.com/photo-1558882224-dda166c4fbcf',
    NULL, NULL, NULL, NULL,
    FALSE, 'terrasse_nice.jpg', 1920, 1280, 580000, 'image/jpeg',
    FALSE, 1, 'Terrasse vue Méditerranée'
),

-- ==================== Photos Property 15: Vitry ====================
(
    'c5a44b4f-7e41-4917-aaef-305f157d1bea',
    '53fa9092-2e73-4d07-abcc-1db5da1c257b',
    'https://images.unsplash.com/photo-1505691938895-1758d7feb511?w=800',
    'https://images.unsplash.com/photo-1505691938895-1758d7feb511?w=150',
    'https://images.unsplash.com/photo-1505691938895-1758d7feb511?w=400',
    'https://images.unsplash.com/photo-1505691938895-1758d7feb511?w=800',
    'https://images.unsplash.com/photo-1505691938895-1758d7feb511?w=1200',
    'https://images.unsplash.com/photo-1505691938895-1758d7feb511',
    NULL, NULL, NULL, NULL,
    FALSE, 'maison_vitry.jpg', 1920, 1280, 490000, 'image/jpeg',
    TRUE, 0, 'Façade maison de ville'
),
(
    '40cd7743-dd26-46b8-865f-372752e3d9c8',
    '53fa9092-2e73-4d07-abcc-1db5da1c257b',
    'https://images.unsplash.com/photo-1540518614846-7eded433c457?w=800',
    'https://images.unsplash.com/photo-1540518614846-7eded433c457?w=150',
    'https://images.unsplash.com/photo-1540518614846-7eded433c457?w=400',
    'https://images.unsplash.com/photo-1540518614846-7eded433c457?w=800',
    'https://images.unsplash.com/photo-1540518614846-7eded433c457?w=1200',
    'https://images.unsplash.com/photo-1540518614846-7eded433c457',
    NULL, NULL, NULL, NULL,
    FALSE, 'jardin_vitry.jpg', 1920, 1280, 420000, 'image/jpeg',
    FALSE, 1, 'Jardin privatif'
),
-- ==================== Property: Lyon Brotteaux - 4 photos ====================
-- 7557b9a8-e2f1-4263-8b30-ac828304eb63 - Appartement familial 5 pièces - Brotteaux
(
    'dcc35e23-144e-43f7-9cea-492267bfdd50',
    '7557b9a8-e2f1-4263-8b30-ac828304eb63',
    'https://images.unsplash.com/photo-1595526114035-0d45ed16cfbf?w=800',
    'https://images.unsplash.com/photo-1595526114035-0d45ed16cfbf?w=150',
    'https://images.unsplash.com/photo-1595526114035-0d45ed16cfbf?w=400',
    'https://images.unsplash.com/photo-1595526114035-0d45ed16cfbf?w=800',
    'https://images.unsplash.com/photo-1595526114035-0d45ed16cfbf?w=1200',
    'https://images.unsplash.com/photo-1595526114035-0d45ed16cfbf',
    NULL, NULL, NULL, NULL,
    FALSE, 'salon_brotteaux.jpg', 1920, 1280, 520000, 'image/jpeg',
    TRUE, 0, 'Séjour lumineux avec parquet'
),
(
    '6b1b4d95-f197-4961-8a49-c4c8d2a00217',
    '7557b9a8-e2f1-4263-8b30-ac828304eb63',
    'https://images.unsplash.com/photo-1631679706909-1844bbd07221?w=800',
    'https://images.unsplash.com/photo-1631679706909-1844bbd07221?w=150',
    'https://images.unsplash.com/photo-1631679706909-1844bbd07221?w=400',
    'https://images.unsplash.com/photo-1631679706909-1844bbd07221?w=800',
    'https://images.unsplash.com/photo-1631679706909-1844bbd07221?w=1200',
    'https://images.unsplash.com/photo-1631679706909-1844bbd07221',
    NULL, NULL, NULL, NULL,
    FALSE, 'chambre1_brotteaux.jpg', 1920, 1280, 410000, 'image/jpeg',
    FALSE, 1, 'Chambre parentale'
),
(
    'c2dfa525-88f3-4c57-87a9-1aa9cca06229',
    '7557b9a8-e2f1-4263-8b30-ac828304eb63',
    'https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=800',
    'https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=150',
    'https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=400',
    'https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=800',
    'https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=1200',
    'https://images.unsplash.com/photo-1618221195710-dd6b41faaea6',
    NULL, NULL, NULL, NULL,
    FALSE, 'sdb_brotteaux.jpg', 1920, 1280, 380000, 'image/jpeg',
    FALSE, 2, 'Salle de bains moderne'
),
(
    'e08de743-7bb0-466e-b267-7a7a1905e4f5',
    '7557b9a8-e2f1-4263-8b30-ac828304eb63',
    'https://images.unsplash.com/photo-1600210491369-e753d80a41f3?w=800',
    'https://images.unsplash.com/photo-1600210491369-e753d80a41f3?w=150',
    'https://images.unsplash.com/photo-1600210491369-e753d80a41f3?w=400',
    'https://images.unsplash.com/photo-1600210491369-e753d80a41f3?w=800',
    'https://images.unsplash.com/photo-1600210491369-e753d80a41f3?w=1200',
    'https://images.unsplash.com/photo-1600210491369-e753d80a41f3',
    NULL, NULL, NULL, NULL,
    FALSE, 'cuisine_brotteaux.jpg', 1920, 1280, 450000, 'image/jpeg',
    FALSE, 3, 'Cuisine équipée'
),

-- ==================== Property: Lyon Croix-Rousse Canut - 3 photos ====================
-- d755c78e-8d4e-42b7-9d92-d92f3ac7a914 - Canut 5 pièces rénové - Croix-Rousse
(
    '360acced-ed8c-4221-82b6-2a33aad9982d',
    'd755c78e-8d4e-42b7-9d92-d92f3ac7a914',
    'https://images.unsplash.com/photo-1613545325278-f24b0cae1224?w=800',
    'https://images.unsplash.com/photo-1613545325278-f24b0cae1224?w=150',
    'https://images.unsplash.com/photo-1613545325278-f24b0cae1224?w=400',
    'https://images.unsplash.com/photo-1613545325278-f24b0cae1224?w=800',
    'https://images.unsplash.com/photo-1613545325278-f24b0cae1224?w=1200',
    'https://images.unsplash.com/photo-1613545325278-f24b0cae1224',
    NULL, NULL, NULL, NULL,
    FALSE, 'salon_canut.jpg', 1920, 1280, 550000, 'image/jpeg',
    TRUE, 0, 'Séjour avec poutres apparentes'
),
(
    '04954b6c-6e0d-4305-8882-4cae315a61f0',
    'd755c78e-8d4e-42b7-9d92-d92f3ac7a914',
    'https://images.unsplash.com/photo-1615876234886-fd9a39fda97f?w=800',
    'https://images.unsplash.com/photo-1615876234886-fd9a39fda97f?w=150',
    'https://images.unsplash.com/photo-1615876234886-fd9a39fda97f?w=400',
    'https://images.unsplash.com/photo-1615876234886-fd9a39fda97f?w=800',
    'https://images.unsplash.com/photo-1615876234886-fd9a39fda97f?w=1200',
    'https://images.unsplash.com/photo-1615876234886-fd9a39fda97f',
    NULL, NULL, NULL, NULL,
    FALSE, 'chambre_canut.jpg', 1920, 1280, 420000, 'image/jpeg',
    FALSE, 1, 'Chambre avec cachet'
),
(
    '0f85c7dd-cc81-48b1-a49f-40d82f31ac37',
    'd755c78e-8d4e-42b7-9d92-d92f3ac7a914',
    'https://images.unsplash.com/photo-1616137466211-f939a16a6d8a?w=800',
    'https://images.unsplash.com/photo-1616137466211-f939a16a6d8a?w=150',
    'https://images.unsplash.com/photo-1616137466211-f939a16a6d8a?w=400',
    'https://images.unsplash.com/photo-1616137466211-f939a16a6d8a?w=800',
    'https://images.unsplash.com/photo-1616137466211-f939a16a6d8a?w=1200',
    'https://images.unsplash.com/photo-1616137466211-f939a16a6d8a',
    NULL, NULL, NULL, NULL,
    FALSE, 'cuisine_canut.jpg', 1920, 1280, 390000, 'image/jpeg',
    FALSE, 2, 'Cuisine aménagée'
),

-- ==================== Property: Lyon Monplaisir Studio - 1 photo ====================
-- a1b86df1-4d9d-4216-bd8c-ca935bad0e66 - Studio étudiant - Monplaisir
(
    '2930ed87-6a16-431b-b88f-cd6747d86be1',
    'a1b86df1-4d9d-4216-bd8c-ca935bad0e66',
    'https://images.unsplash.com/photo-1615874959474-d609969a20ed?w=800',
    'https://images.unsplash.com/photo-1615874959474-d609969a20ed?w=150',
    'https://images.unsplash.com/photo-1615874959474-d609969a20ed?w=400',
    'https://images.unsplash.com/photo-1615874959474-d609969a20ed?w=800',
    'https://images.unsplash.com/photo-1615874959474-d609969a20ed?w=1200',
    'https://images.unsplash.com/photo-1615874959474-d609969a20ed',
    NULL, NULL, NULL, NULL,
    FALSE, 'studio_monplaisir.jpg', 1920, 1280, 320000, 'image/jpeg',
    TRUE, 0, 'Studio étudiant fonctionnel'
),

-- ==================== Property: Lyon Point du Jour Maison - 4 photos ====================
-- ccaa2b0f-bd78-4b83-b7b9-4f022e1c2849 - Maison 5 pièces avec jardin - Point du Jour
(
    'ddb69334-9ba9-4006-b695-4b907a07d98b',
    'ccaa2b0f-bd78-4b83-b7b9-4f022e1c2849',
    'https://images.unsplash.com/photo-1617325247661-675ab4b64ae2?w=800',
    'https://images.unsplash.com/photo-1617325247661-675ab4b64ae2?w=150',
    'https://images.unsplash.com/photo-1617325247661-675ab4b64ae2?w=400',
    'https://images.unsplash.com/photo-1617325247661-675ab4b64ae2?w=800',
    'https://images.unsplash.com/photo-1617325247661-675ab4b64ae2?w=1200',
    'https://images.unsplash.com/photo-1617325247661-675ab4b64ae2',
    NULL, NULL, NULL, NULL,
    FALSE, 'facade_pointdujour.jpg', 1920, 1280, 580000, 'image/jpeg',
    TRUE, 0, 'Façade de la maison'
),
(
    '530eea3c-175a-4775-a0ed-44a2e2de199f',
    'ccaa2b0f-bd78-4b83-b7b9-4f022e1c2849',
    'https://images.unsplash.com/photo-1616594039964-ae9021a400a0?w=800',
    'https://images.unsplash.com/photo-1616594039964-ae9021a400a0?w=150',
    'https://images.unsplash.com/photo-1616594039964-ae9021a400a0?w=400',
    'https://images.unsplash.com/photo-1616594039964-ae9021a400a0?w=800',
    'https://images.unsplash.com/photo-1616594039964-ae9021a400a0?w=1200',
    'https://images.unsplash.com/photo-1616594039964-ae9021a400a0',
    NULL, NULL, NULL, NULL,
    FALSE, 'salon_pointdujour.jpg', 1920, 1280, 520000, 'image/jpeg',
    FALSE, 1, 'Séjour spacieux'
),
(
    '2a9ec19e-cb4e-47f6-9b98-c1eebede414d',
    'ccaa2b0f-bd78-4b83-b7b9-4f022e1c2849',
    'https://images.unsplash.com/photo-1560185127-6ed189bf02f4?w=800',
    'https://images.unsplash.com/photo-1560185127-6ed189bf02f4?w=150',
    'https://images.unsplash.com/photo-1560185127-6ed189bf02f4?w=400',
    'https://images.unsplash.com/photo-1560185127-6ed189bf02f4?w=800',
    'https://images.unsplash.com/photo-1560185127-6ed189bf02f4?w=1200',
    'https://images.unsplash.com/photo-1560185127-6ed189bf02f4',
    NULL, NULL, NULL, NULL,
    FALSE, 'jardin_pointdujour.jpg', 1920, 1280, 480000, 'image/jpeg',
    FALSE, 2, 'Jardin arboré'
),
(
    '55dda56a-ac99-4378-9357-20f3711ad8ea',
    'ccaa2b0f-bd78-4b83-b7b9-4f022e1c2849',
    'https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=800',
    'https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=150',
    'https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=400',
    'https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=800',
    'https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=1200',
    'https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af',
    NULL, NULL, NULL, NULL,
    FALSE, 'chambre_pointdujour.jpg', 1920, 1280, 410000, 'image/jpeg',
    FALSE, 3, 'Chambre principale'
),

-- ==================== Property: Bordeaux Triangle d'Or - 3 photos ====================
-- 3806bc56-212a-403d-b654-51665b34ab08 - Appartement 5 pièces - Triangle d'Or
(
    '3002bb50-db4f-4116-ba88-740235704c17',
    '3806bc56-212a-403d-b654-51665b34ab08',
    'https://images.unsplash.com/photo-1560185007-c5ca9d2c014d?w=800',
    'https://images.unsplash.com/photo-1560185007-c5ca9d2c014d?w=150',
    'https://images.unsplash.com/photo-1560185007-c5ca9d2c014d?w=400',
    'https://images.unsplash.com/photo-1560185007-c5ca9d2c014d?w=800',
    'https://images.unsplash.com/photo-1560185007-c5ca9d2c014d?w=1200',
    'https://images.unsplash.com/photo-1560185007-c5ca9d2c014d',
    NULL, NULL, NULL, NULL,
    FALSE, 'salon_triangledor.jpg', 1920, 1280, 560000, 'image/jpeg',
    TRUE, 0, 'Séjour bourgeois avec moulures'
),
(
    '070e0861-8f2b-40d0-b7bf-f4ad86d87c3e',
    '3806bc56-212a-403d-b654-51665b34ab08',
    'https://images.unsplash.com/photo-1616046229478-9901c5536a45?w=800',
    'https://images.unsplash.com/photo-1616046229478-9901c5536a45?w=150',
    'https://images.unsplash.com/photo-1616046229478-9901c5536a45?w=400',
    'https://images.unsplash.com/photo-1616046229478-9901c5536a45?w=800',
    'https://images.unsplash.com/photo-1616046229478-9901c5536a45?w=1200',
    'https://images.unsplash.com/photo-1616046229478-9901c5536a45',
    NULL, NULL, NULL, NULL,
    FALSE, 'cheminee_triangledor.jpg', 1920, 1280, 490000, 'image/jpeg',
    FALSE, 1, 'Cheminée d''époque'
),
(
    '852df5e7-5aaa-421b-9168-b22c696f5a41',
    '3806bc56-212a-403d-b654-51665b34ab08',
    'https://images.unsplash.com/photo-1618220179428-22790b461013?w=800',
    'https://images.unsplash.com/photo-1618220179428-22790b461013?w=150',
    'https://images.unsplash.com/photo-1618220179428-22790b461013?w=400',
    'https://images.unsplash.com/photo-1618220179428-22790b461013?w=800',
    'https://images.unsplash.com/photo-1618220179428-22790b461013?w=1200',
    'https://images.unsplash.com/photo-1618220179428-22790b461013',
    NULL, NULL, NULL, NULL,
    FALSE, 'cuisine_triangledor.jpg', 1920, 1280, 420000, 'image/jpeg',
    FALSE, 2, 'Cuisine aménagée'
),

-- ==================== Property: Bordeaux Caudéran Maison - 5 photos ====================
-- 5cd00260-955e-4418-99b9-fc13fa16f451 - Maison familiale 5 pièces - Caudéran
(
    '9abea6df-4647-4306-a320-41342ec16f95',
    '5cd00260-955e-4418-99b9-fc13fa16f451',
    'https://images.unsplash.com/photo-1615873968403-89e068629265?w=800',
    'https://images.unsplash.com/photo-1615873968403-89e068629265?w=150',
    'https://images.unsplash.com/photo-1615873968403-89e068629265?w=400',
    'https://images.unsplash.com/photo-1615873968403-89e068629265?w=800',
    'https://images.unsplash.com/photo-1615873968403-89e068629265?w=1200',
    'https://images.unsplash.com/photo-1615873968403-89e068629265',
    NULL, NULL, NULL, NULL,
    FALSE, 'facade_cauderan.jpg', 1920, 1280, 620000, 'image/jpeg',
    TRUE, 0, 'Façade maison contemporaine'
),
(
    '8c51ef1c-7294-470f-83b0-2233d2b5c8c8',
    '5cd00260-955e-4418-99b9-fc13fa16f451',
    'https://images.unsplash.com/photo-1609766857326-18c83d7c5a76?w=800',
    'https://images.unsplash.com/photo-1609766857326-18c83d7c5a76?w=150',
    'https://images.unsplash.com/photo-1609766857326-18c83d7c5a76?w=400',
    'https://images.unsplash.com/photo-1609766857326-18c83d7c5a76?w=800',
    'https://images.unsplash.com/photo-1609766857326-18c83d7c5a76?w=1200',
    'https://images.unsplash.com/photo-1609766857326-18c83d7c5a76',
    NULL, NULL, NULL, NULL,
    FALSE, 'salon_cauderan.jpg', 1920, 1280, 580000, 'image/jpeg',
    FALSE, 1, 'Séjour lumineux'
),
(
    '5f5125ad-6984-4b35-b91f-6026324c920e',
    '5cd00260-955e-4418-99b9-fc13fa16f451',
    'https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=800',
    'https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=150',
    'https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=400',
    'https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=800',
    'https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=1200',
    'https://images.unsplash.com/photo-1505693416388-ac5ce068fe85',
    NULL, NULL, NULL, NULL,
    FALSE, 'jardin_cauderan.jpg', 1920, 1280, 510000, 'image/jpeg',
    FALSE, 2, 'Jardin avec piscine'
),
(
    'f6f834cb-2e25-42af-9f02-f96a46101157',
    '5cd00260-955e-4418-99b9-fc13fa16f451',
    'https://images.unsplash.com/photo-1588046130717-0eb0c9a3ba15?w=800',
    'https://images.unsplash.com/photo-1588046130717-0eb0c9a3ba15?w=150',
    'https://images.unsplash.com/photo-1588046130717-0eb0c9a3ba15?w=400',
    'https://images.unsplash.com/photo-1588046130717-0eb0c9a3ba15?w=800',
    'https://images.unsplash.com/photo-1588046130717-0eb0c9a3ba15?w=1200',
    'https://images.unsplash.com/photo-1588046130717-0eb0c9a3ba15',
    NULL, NULL, NULL, NULL,
    FALSE, 'chambre_cauderan.jpg', 1920, 1280, 440000, 'image/jpeg',
    FALSE, 3, 'Suite parentale'
),
(
    '072d7eff-9c2d-4a7a-b5e0-769afb984a95',
    '5cd00260-955e-4418-99b9-fc13fa16f451',
    'https://images.unsplash.com/photo-1595514535116-8cf8d43b3316?w=800',
    'https://images.unsplash.com/photo-1595514535116-8cf8d43b3316?w=150',
    'https://images.unsplash.com/photo-1595514535116-8cf8d43b3316?w=400',
    'https://images.unsplash.com/photo-1595514535116-8cf8d43b3316?w=800',
    'https://images.unsplash.com/photo-1595514535116-8cf8d43b3316?w=1200',
    'https://images.unsplash.com/photo-1595514535116-8cf8d43b3316',
    NULL, NULL, NULL, NULL,
    FALSE, 'sdb_cauderan.jpg', 1920, 1280, 400000, 'image/jpeg',
    FALSE, 4, 'Salle de bains design'
),

-- ==================== Property: Bordeaux Bastide - 3 photos ====================
-- 6e2257e7-fbd4-4d06-9c8d-997ea3d52566 - Appartement 5 pièces - Bastide
(
    '00edc449-b6af-40c1-8051-ded7152642e0',
    '6e2257e7-fbd4-4d06-9c8d-997ea3d52566',
    'https://images.unsplash.com/photo-1564078516393-cf04bd966897?w=800',
    'https://images.unsplash.com/photo-1564078516393-cf04bd966897?w=150',
    'https://images.unsplash.com/photo-1564078516393-cf04bd966897?w=400',
    'https://images.unsplash.com/photo-1564078516393-cf04bd966897?w=800',
    'https://images.unsplash.com/photo-1564078516393-cf04bd966897?w=1200',
    'https://images.unsplash.com/photo-1564078516393-cf04bd966897',
    NULL, NULL, NULL, NULL,
    FALSE, 'salon_bastide.jpg', 1920, 1280, 540000, 'image/jpeg',
    TRUE, 0, 'Séjour avec vue dégagée'
),
(
    '2124db7c-364c-4a7a-a7a1-e344eacaf79f',
    '6e2257e7-fbd4-4d06-9c8d-997ea3d52566',
    'https://images.unsplash.com/photo-1611892440504-42a792e24d32?w=800',
    'https://images.unsplash.com/photo-1611892440504-42a792e24d32?w=150',
    'https://images.unsplash.com/photo-1611892440504-42a792e24d32?w=400',
    'https://images.unsplash.com/photo-1611892440504-42a792e24d32?w=800',
    'https://images.unsplash.com/photo-1611892440504-42a792e24d32?w=1200',
    'https://images.unsplash.com/photo-1611892440504-42a792e24d32',
    NULL, NULL, NULL, NULL,
    FALSE, 'cuisine_bastide.jpg', 1920, 1280, 460000, 'image/jpeg',
    FALSE, 1, 'Cuisine moderne équipée'
),
(
    'f60d6aa7-38cb-4f73-830f-669e2adfc11b',
    '6e2257e7-fbd4-4d06-9c8d-997ea3d52566',
    'https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?w=800',
    'https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?w=150',
    'https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?w=400',
    'https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?w=800',
    'https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?w=1200',
    'https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd',
    NULL, NULL, NULL, NULL,
    FALSE, 'balcon_bastide.jpg', 1920, 1280, 420000, 'image/jpeg',
    FALSE, 2, 'Balcon avec vue'
),

-- ==================== Property: Bordeaux Bassins à flot Studio - 1 photo ====================
-- e5ea388d-6392-47d7-b1ca-c77cabb20647 - Studio moderne - Bassins à flot
(
    '35d7a2a4-ad18-4275-b7d1-6aa0a3c5a641',
    'e5ea388d-6392-47d7-b1ca-c77cabb20647',
    'https://images.unsplash.com/photo-1505693314120-0d443867891c?w=800',
    'https://images.unsplash.com/photo-1505693314120-0d443867891c?w=150',
    'https://images.unsplash.com/photo-1505693314120-0d443867891c?w=400',
    'https://images.unsplash.com/photo-1505693314120-0d443867891c?w=800',
    'https://images.unsplash.com/photo-1505693314120-0d443867891c?w=1200',
    'https://images.unsplash.com/photo-1505693314120-0d443867891c',
    NULL, NULL, NULL, NULL,
    FALSE, 'studio_bassins.jpg', 1920, 1280, 340000, 'image/jpeg',
    TRUE, 0, 'Studio moderne et lumineux'
),

-- ==================== Property: Lyon Presqu'île - 3 photos ====================
-- 9a1c6a2a-9d9e-4f9f-9b4e-0a8e8f3d4f01 - Appartement 5 pièces - Presqu'île
(
    'fc20afbb-8012-40ef-84d1-2bb3363a90f2',
    '9a1c6a2a-9d9e-4f9f-9b4e-0a8e8f3d4f01',
    'https://images.unsplash.com/photo-1566665797739-1674de7a421a?w=800',
    'https://images.unsplash.com/photo-1566665797739-1674de7a421a?w=150',
    'https://images.unsplash.com/photo-1566665797739-1674de7a421a?w=400',
    'https://images.unsplash.com/photo-1566665797739-1674de7a421a?w=800',
    'https://images.unsplash.com/photo-1566665797739-1674de7a421a?w=1200',
    'https://images.unsplash.com/photo-1566665797739-1674de7a421a',
    NULL, NULL, NULL, NULL,
    FALSE, 'salon_presquile.jpg', 1920, 1280, 580000, 'image/jpeg',
    TRUE, 0, 'Séjour avec prestations soignées'
),
(
    '52b5ecef-d358-4a28-9315-ee51e37b044e',
    '9a1c6a2a-9d9e-4f9f-9b4e-0a8e8f3d4f01',
    'https://images.unsplash.com/photo-1586105251261-72a756497a11?w=800',
    'https://images.unsplash.com/photo-1586105251261-72a756497a11?w=150',
    'https://images.unsplash.com/photo-1586105251261-72a756497a11?w=400',
    'https://images.unsplash.com/photo-1586105251261-72a756497a11?w=800',
    'https://images.unsplash.com/photo-1586105251261-72a756497a11?w=1200',
    'https://images.unsplash.com/photo-1586105251261-72a756497a11',
    NULL, NULL, NULL, NULL,
    FALSE, 'cheminee_presquile.jpg', 1920, 1280, 510000, 'image/jpeg',
    FALSE, 1, 'Salon avec cheminée'
),
(
    'd78dcb8b-9686-4cdb-8ed0-d669f865c0d9',
    '9a1c6a2a-9d9e-4f9f-9b4e-0a8e8f3d4f01',
    'https://images.unsplash.com/photo-1614849286521-4c58b2f0ff15?w=800',
    'https://images.unsplash.com/photo-1614849286521-4c58b2f0ff15?w=150',
    'https://images.unsplash.com/photo-1614849286521-4c58b2f0ff15?w=400',
    'https://images.unsplash.com/photo-1614849286521-4c58b2f0ff15?w=800',
    'https://images.unsplash.com/photo-1614849286521-4c58b2f0ff15?w=1200',
    'https://images.unsplash.com/photo-1614849286521-4c58b2f0ff15',
    NULL, NULL, NULL, NULL,
    FALSE, 'chambre_presquile.jpg', 1920, 1280, 430000, 'image/jpeg',
    FALSE, 2, 'Chambre parentale'
),

-- ==================== Property: Lyon Part-Dieu Studio - 1 photo ====================
-- b2f1e6cb-7c23-4a9d-9b6a-3e9c9c0a7a02 - Studio récent - Part-Dieu
(
    'bb29c48c-2107-4403-9feb-d2cc9590de13',
    'b2f1e6cb-7c23-4a9d-9b6a-3e9c9c0a7a02',
    'https://images.unsplash.com/photo-1629140727571-9b5c6f6267b4?w=800',
    'https://images.unsplash.com/photo-1629140727571-9b5c6f6267b4?w=150',
    'https://images.unsplash.com/photo-1629140727571-9b5c6f6267b4?w=400',
    'https://images.unsplash.com/photo-1629140727571-9b5c6f6267b4?w=800',
    'https://images.unsplash.com/photo-1629140727571-9b5c6f6267b4?w=1200',
    'https://images.unsplash.com/photo-1629140727571-9b5c6f6267b4',
    NULL, NULL, NULL, NULL,
    FALSE, 'studio_partdieu.jpg', 1920, 1280, 310000, 'image/jpeg',
    TRUE, 0, 'Studio moderne Part-Dieu'
),

-- ==================== Property: Lyon Croix-Rousse 5 pièces - 2 photos ====================
-- c3a44c9e-7f4b-4e28-bd47-1a3f45c5b103 - Appartement 5 pièces - Croix-Rousse
(
    'dfb90229-239e-4db9-8938-2ac28b508684',
    'c3a44c9e-7f4b-4e28-bd47-1a3f45c5b103',
    'https://images.unsplash.com/photo-1560184897-ae75f418493e?w=800',
    'https://images.unsplash.com/photo-1560184897-ae75f418493e?w=150',
    'https://images.unsplash.com/photo-1560184897-ae75f418493e?w=400',
    'https://images.unsplash.com/photo-1560184897-ae75f418493e?w=800',
    'https://images.unsplash.com/photo-1560184897-ae75f418493e?w=1200',
    'https://images.unsplash.com/photo-1560184897-ae75f418493e',
    NULL, NULL, NULL, NULL,
    FALSE, 'salon_croixrousse.jpg', 1920, 1280, 530000, 'image/jpeg',
    TRUE, 0, 'Séjour familial lumineux'
),
(
    'f1756968-9113-49ad-97da-6c5b9b3dff9e',
    'c3a44c9e-7f4b-4e28-bd47-1a3f45c5b103',
    'https://images.unsplash.com/photo-1560185008-b8e5d7a36e4a?w=800',
    'https://images.unsplash.com/photo-1560185008-b8e5d7a36e4a?w=150',
    'https://images.unsplash.com/photo-1560185008-b8e5d7a36e4a?w=400',
    'https://images.unsplash.com/photo-1560185008-b8e5d7a36e4a?w=800',
    'https://images.unsplash.com/photo-1560185008-b8e5d7a36e4a?w=1200',
    'https://images.unsplash.com/photo-1560185008-b8e5d7a36e4a',
    NULL, NULL, NULL, NULL,
    FALSE, 'chambre_croixrousse.jpg', 1920, 1280, 410000, 'image/jpeg',
    FALSE, 1, 'Chambre avec vue'
),
(
    'f9aaa4ad-936b-4441-99ad-83288a4e8444',
    '0c2e7932-ea4e-4336-a337-01b51dc73417',
    'https://images.unsplash.com/photo-1560185007-5f0bb1866cab?w=800',
    'https://images.unsplash.com/photo-1560185007-5f0bb1866cab?w=150',
    'https://images.unsplash.com/photo-1560185007-5f0bb1866cab?w=400',
    'https://images.unsplash.com/photo-1560185007-5f0bb1866cab?w=800',
    'https://images.unsplash.com/photo-1560185007-5f0bb1866cab?w=1200',
    'https://images.unsplash.com/photo-1560185007-5f0bb1866cab',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_1.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Vue principale'
),

(
    '10b4bafe-dcfa-4313-ae58-0b9cb52edb72',
    '2015fc04-70e8-41f8-bd56-19970d464adf',
    'https://images.unsplash.com/photo-1578683010236-d716f9a3f461?w=800',
    'https://images.unsplash.com/photo-1578683010236-d716f9a3f461?w=150',
    'https://images.unsplash.com/photo-1578683010236-d716f9a3f461?w=400',
    'https://images.unsplash.com/photo-1578683010236-d716f9a3f461?w=800',
    'https://images.unsplash.com/photo-1578683010236-d716f9a3f461?w=1200',
    'https://images.unsplash.com/photo-1578683010236-d716f9a3f461',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_2.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Vue principale'
),

(
    'f2923881-0dab-40ad-a7a4-245b74304e7d',
    '4596e983-6f89-4c47-9717-20d1deeb6022',
    'https://images.unsplash.com/photo-1560448075-cbc16bb4af8e?w=800',
    'https://images.unsplash.com/photo-1560448075-cbc16bb4af8e?w=150',
    'https://images.unsplash.com/photo-1560448075-cbc16bb4af8e?w=400',
    'https://images.unsplash.com/photo-1560448075-cbc16bb4af8e?w=800',
    'https://images.unsplash.com/photo-1560448075-cbc16bb4af8e?w=1200',
    'https://images.unsplash.com/photo-1560448075-cbc16bb4af8e',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_3.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Vue principale'
),

(
    '21373602-5c2c-49a1-8a2a-4c1dd8c377ec',
    '7f42616f-2923-44c3-9950-37e3bbbc15af',
    'https://images.unsplash.com/photo-1560184897-502a475f7a0d?w=800',
    'https://images.unsplash.com/photo-1560184897-502a475f7a0d?w=150',
    'https://images.unsplash.com/photo-1560184897-502a475f7a0d?w=400',
    'https://images.unsplash.com/photo-1560184897-502a475f7a0d?w=800',
    'https://images.unsplash.com/photo-1560184897-502a475f7a0d?w=1200',
    'https://images.unsplash.com/photo-1560184897-502a475f7a0d',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_4.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Vue principale'
),

(
    '0887292d-1667-4ad5-a962-131bb9bf0c07',
    '8ad2150b-e022-47e0-b570-8e9883df44ec',
    'https://images.unsplash.com/photo-1560184897-67f4a3f9a7fa?w=800',
    'https://images.unsplash.com/photo-1560184897-67f4a3f9a7fa?w=150',
    'https://images.unsplash.com/photo-1560184897-67f4a3f9a7fa?w=400',
    'https://images.unsplash.com/photo-1560184897-67f4a3f9a7fa?w=800',
    'https://images.unsplash.com/photo-1560184897-67f4a3f9a7fa?w=1200',
    'https://images.unsplash.com/photo-1560184897-67f4a3f9a7fa',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_5.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Vue principale'
),

(
    'e19fadca-5174-4817-8bc1-96672f0e4271',
    'a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5e',
    'https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?w=800',
    'https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?w=150',
    'https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?w=400',
    'https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?w=800',
    'https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?w=1200',
    'https://images.unsplash.com/photo-1600607687920-4e2a09cf159d',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_6.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Séjour lumineux avec parquet'
),

(
    '19af62f7-549d-48eb-a26c-2752d58aef65',
    'a5b4c3d2-e1f0-4a9b-8c7d-6e5f4a3b2c1d',
    'https://images.unsplash.com/photo-1560448075-bb485b067938?w=800',
    'https://images.unsplash.com/photo-1560448075-bb485b067938?w=150',
    'https://images.unsplash.com/photo-1560448075-bb485b067938?w=400',
    'https://images.unsplash.com/photo-1560448075-bb485b067938?w=800',
    'https://images.unsplash.com/photo-1560448075-bb485b067938?w=1200',
    'https://images.unsplash.com/photo-1560448075-bb485b067938',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_7.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Chambre principale spacieuse'
),

(
    'b8c00e5c-42b7-40ef-ad06-4b1e248d7155',
    'a7d4e12c-5b8a-4c2d-9f1e-3b2a1c0d9e8f',
    'https://images.unsplash.com/photo-1560185127-bdf2e3e0e41b?w=800',
    'https://images.unsplash.com/photo-1560185127-bdf2e3e0e41b?w=150',
    'https://images.unsplash.com/photo-1560185127-bdf2e3e0e41b?w=400',
    'https://images.unsplash.com/photo-1560185127-bdf2e3e0e41b?w=800',
    'https://images.unsplash.com/photo-1560185127-bdf2e3e0e41b?w=1200',
    'https://images.unsplash.com/photo-1560185127-bdf2e3e0e41b',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_8.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Cuisine équipée moderne'
),

(
    '9daa86bc-e5fa-4d07-980e-35dd4163f8e6',
    'a8e9f2d3-4a1b-4b23-9c8f-2b4a5d7e3202',
    'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=800',
    'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=150',
    'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=400',
    'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=800',
    'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=1200',
    'https://images.unsplash.com/photo-1584622650111-993a426fbf0a',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_9.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Salle de bain rénovée'
),

(
    'fb569aff-72e8-40e8-9e13-169e1c6053dc',
    'b2c3d4e5-f6a7-4b8c-9d0e-1f2a3b4c5d6f',
    'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=800',
    'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=150',
    'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=400',
    'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=800',
    'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=1200',
    'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_10.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Balcon avec vue dégagée'
),

(
    'a60fa791-d038-4bd3-9586-ca285a0098b6',
    'b2c5d3e4-6f7a-4b8c-9d0e-1f2a3b4c5d6e',
    'https://images.unsplash.com/photo-1600047509782-20d39509f26d?w=800',
    'https://images.unsplash.com/photo-1600047509782-20d39509f26d?w=150',
    'https://images.unsplash.com/photo-1600047509782-20d39509f26d?w=400',
    'https://images.unsplash.com/photo-1600047509782-20d39509f26d?w=800',
    'https://images.unsplash.com/photo-1600047509782-20d39509f26d?w=1200',
    'https://images.unsplash.com/photo-1600047509782-20d39509f26d',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_11.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Escalier en marbre'
),

(
    'b43f0d0d-dca8-40eb-9f3d-f200d75b1f0c',
    'b7c8d9e0-f1a2-4b3c-4d5e-6f7a8b9c0d1e',
    'https://images.unsplash.com/photo-1556909212-d5b604d0c90d?w=800',
    'https://images.unsplash.com/photo-1556909212-d5b604d0c90d?w=150',
    'https://images.unsplash.com/photo-1556909212-d5b604d0c90d?w=400',
    'https://images.unsplash.com/photo-1556909212-d5b604d0c90d?w=800',
    'https://images.unsplash.com/photo-1556909212-d5b604d0c90d?w=1200',
    'https://images.unsplash.com/photo-1556909212-d5b604d0c90d',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_12.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Parking souterrain'
),

(
    'c2a092a6-7186-4a87-bc0f-0fa312f92035',
    'c1d2e3f4-a5b6-4c7d-8e9f-0a1b2c3d4e5f',
    'https://images.unsplash.com/photo-1565538810643-b5bdb714032a?w=800',
    'https://images.unsplash.com/photo-1565538810643-b5bdb714032a?w=150',
    'https://images.unsplash.com/photo-1565538810643-b5bdb714032a?w=400',
    'https://images.unsplash.com/photo-1565538810643-b5bdb714032a?w=800',
    'https://images.unsplash.com/photo-1565538810643-b5bdb714032a?w=1200',
    'https://images.unsplash.com/photo-1565538810643-b5bdb714032a',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_13.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Jardin aménagé avec terrasse'
),

(
    '2093e909-14e3-4089-b8e9-55d553b05372',
    'c3d4e5f6-a7b8-4c9d-0e1f-2a3b4c5d6e7f',
    'https://images.unsplash.com/photo-1570739513881-0c36c4b1027b?w=800',
    'https://images.unsplash.com/photo-1570739513881-0c36c4b1027b?w=150',
    'https://images.unsplash.com/photo-1570739513881-0c36c4b1027b?w=400',
    'https://images.unsplash.com/photo-1570739513881-0c36c4b1027b?w=800',
    'https://images.unsplash.com/photo-1570739513881-0c36c4b1027b?w=1200',
    'https://images.unsplash.com/photo-1570739513881-0c36c4b1027b',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_14.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Bureau avec fenêtres'
),

(
    '80ab840b-801f-413c-abd5-5a0577b998b2',
    'c46dd03f-1c46-4558-a5e8-cc21ba492e1f',
    'https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=800',
    'https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=150',
    'https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=400',
    'https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=800',
    'https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=1200',
    'https://images.unsplash.com/photo-1600210492486-724fe5c67fb0',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_15.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Garage indépendant'
),

(
    '060a69f6-439a-4767-a8d7-d1eee3ff7002',
    'c9b3a1d4-7e3a-4a9b-9a8c-3d4f5e6a4303',
    'https://images.unsplash.com/photo-1600585152220-90363fe7e115?w=800',
    'https://images.unsplash.com/photo-1600585152220-90363fe7e115?w=150',
    'https://images.unsplash.com/photo-1600585152220-90363fe7e115?w=400',
    'https://images.unsplash.com/photo-1600585152220-90363fe7e115?w=800',
    'https://images.unsplash.com/photo-1600585152220-90363fe7e115?w=1200',
    'https://images.unsplash.com/photo-1600585152220-90363fe7e115',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_16.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Couloir spacieux'
),

(
    '0a46f79d-88ef-4978-bbf0-c191e87282fb',
    'c9e8d7f6-5a4b-3c2d-1e0f-9a8b7c6d5e4f',
    'https://images.unsplash.com/photo-1604709177225-055f99402ea3?w=800',
    'https://images.unsplash.com/photo-1604709177225-055f99402ea3?w=150',
    'https://images.unsplash.com/photo-1604709177225-055f99402ea3?w=400',
    'https://images.unsplash.com/photo-1604709177225-055f99402ea3?w=800',
    'https://images.unsplash.com/photo-1604709177225-055f99402ea3?w=1200',
    'https://images.unsplash.com/photo-1604709177225-055f99402ea3',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_17.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Fenêtres double vitrage'
),

(
    '1201cb9c-4aec-4716-9b92-29e69686e1c0',
    'd0e2f3a4-9b7a-4c2e-8d9a-4b5c6e7f5404',
    'https://images.unsplash.com/photo-1556909211-36987daf7b4d?w=800',
    'https://images.unsplash.com/photo-1556909211-36987daf7b4d?w=150',
    'https://images.unsplash.com/photo-1556909211-36987daf7b4d?w=400',
    'https://images.unsplash.com/photo-1556909211-36987daf7b4d?w=800',
    'https://images.unsplash.com/photo-1556909211-36987daf7b4d?w=1200',
    'https://images.unsplash.com/photo-1556909211-36987daf7b4d',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_18.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Rangements intégrés'
),

(
    'd87f0216-1738-4901-93b6-21eceb1d75eb',
    'd1e2f3a4-b5c6-7d8e-9f0a-1b2c3d4e5f6a',
    'https://images.unsplash.com/photo-1588854337236-6889d631faa8?w=800',
    'https://images.unsplash.com/photo-1588854337236-6889d631faa8?w=150',
    'https://images.unsplash.com/photo-1588854337236-6889d631faa8?w=400',
    'https://images.unsplash.com/photo-1588854337236-6889d631faa8?w=800',
    'https://images.unsplash.com/photo-1588854337236-6889d631faa8?w=1200',
    'https://images.unsplash.com/photo-1588854337236-6889d631faa8',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_19.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Entrée lumineuse'
),

(
    'f52bd31f-0178-4c20-bbdb-ec1a14243b32',
    'd4c7e53d-1a2e-4b61-9e23-7b8e1d4c4104',
    'https://images.unsplash.com/photo-1600210491892-03d54c0aaf87?w=800',
    'https://images.unsplash.com/photo-1600210491892-03d54c0aaf87?w=150',
    'https://images.unsplash.com/photo-1600210491892-03d54c0aaf87?w=400',
    'https://images.unsplash.com/photo-1600210491892-03d54c0aaf87?w=800',
    'https://images.unsplash.com/photo-1600210491892-03d54c0aaf87?w=1200',
    'https://images.unsplash.com/photo-1600210491892-03d54c0aaf87',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_20.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Cuisine ouverte'
),

(
    '4e8dc8bf-8f3d-4b5b-97f7-84022e94f2bd',
    'd4e5f6a7-b8c9-4d0e-1f2a-3b4c5d6e7f8a',
    'https://images.unsplash.com/photo-1595526051245-4506e0005bd0?w=800',
    'https://images.unsplash.com/photo-1595526051245-4506e0005bd0?w=150',
    'https://images.unsplash.com/photo-1595526051245-4506e0005bd0?w=400',
    'https://images.unsplash.com/photo-1595526051245-4506e0005bd0?w=800',
    'https://images.unsplash.com/photo-1595526051245-4506e0005bd0?w=1200',
    'https://images.unsplash.com/photo-1595526051245-4506e0005bd0',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_21.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Dressing chambre'
),

(
    'eb346d61-63c4-4e56-8612-4ba663ccb4c7',
    'e1f2a3b4-5c6d-4e7f-8a9b-5d6e7f8a6505',
    'https://images.unsplash.com/photo-1574739782594-db4ead022697?w=800',
    'https://images.unsplash.com/photo-1574739782594-db4ead022697?w=150',
    'https://images.unsplash.com/photo-1574739782594-db4ead022697?w=400',
    'https://images.unsplash.com/photo-1574739782594-db4ead022697?w=800',
    'https://images.unsplash.com/photo-1574739782594-db4ead022697?w=1200',
    'https://images.unsplash.com/photo-1574739782594-db4ead022697',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_22.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Salle d''eau moderne'
),

(
    'be9d0c66-ae54-40a0-8f1a-02c1d5d49181',
    'e5a3b8a4-8a91-47ef-9bb2-0b47cfa1b105',
    'https://images.unsplash.com/photo-1600573472592-401b489a3cdc?w=800',
    'https://images.unsplash.com/photo-1600573472592-401b489a3cdc?w=150',
    'https://images.unsplash.com/photo-1600573472592-401b489a3cdc?w=400',
    'https://images.unsplash.com/photo-1600573472592-401b489a3cdc?w=800',
    'https://images.unsplash.com/photo-1600573472592-401b489a3cdc?w=1200',
    'https://images.unsplash.com/photo-1600573472592-401b489a3cdc',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_23.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Cellier'
),

(
    'f26d1e07-7a1b-451a-b6ed-5cf834281c9d',
    'e5f6a7b8-c9d0-1e2f-3a4b-5c6d7e8f9a0b',
    'https://images.unsplash.com/photo-1600489000022-c2086d79f9d4?w=800',
    'https://images.unsplash.com/photo-1600489000022-c2086d79f9d4?w=150',
    'https://images.unsplash.com/photo-1600489000022-c2086d79f9d4?w=400',
    'https://images.unsplash.com/photo-1600489000022-c2086d79f9d4?w=800',
    'https://images.unsplash.com/photo-1600489000022-c2086d79f9d4?w=1200',
    'https://images.unsplash.com/photo-1600489000022-c2086d79f9d4',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_24.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Chambre enfant'
),

(
    '114379ac-1867-44d1-88f5-0665702f138c',
    'e8d2c1b4-a5f6-4d9e-8c7b-1a2b3c4d5e6f',
    'https://images.unsplash.com/photo-1609081144289-eacc3108cd8b?w=800',
    'https://images.unsplash.com/photo-1609081144289-eacc3108cd8b?w=150',
    'https://images.unsplash.com/photo-1609081144289-eacc3108cd8b?w=400',
    'https://images.unsplash.com/photo-1609081144289-eacc3108cd8b?w=800',
    'https://images.unsplash.com/photo-1609081144289-eacc3108cd8b?w=1200',
    'https://images.unsplash.com/photo-1609081144289-eacc3108cd8b',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_25.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Véranda vitrée'
),

(
    '11b162f5-89fd-4889-9707-19eb029ec454',
    'f1a2b3c4-d5e6-4a7b-8c9d-0e1f2a3b4c5d',
    'https://images.unsplash.com/photo-1600121848594-d8644e57abab?w=800',
    'https://images.unsplash.com/photo-1600121848594-d8644e57abab?w=150',
    'https://images.unsplash.com/photo-1600121848594-d8644e57abab?w=400',
    'https://images.unsplash.com/photo-1600121848594-d8644e57abab?w=800',
    'https://images.unsplash.com/photo-1600121848594-d8644e57abab?w=1200',
    'https://images.unsplash.com/photo-1600121848594-d8644e57abab',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_26.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Cave climatisée'
),

(
    'd7383be5-55ab-4df5-aa23-e2b7c5fd63d0',
    'f6b7b7a2-5c1e-4c8f-9e93-0e2c6a7c2101',
    'https://images.unsplash.com/photo-1556912167-f556f1f39fdf?w=800',
    'https://images.unsplash.com/photo-1556912167-f556f1f39fdf?w=150',
    'https://images.unsplash.com/photo-1556912167-f556f1f39fdf?w=400',
    'https://images.unsplash.com/photo-1556912167-f556f1f39fdf?w=800',
    'https://images.unsplash.com/photo-1556912167-f556f1f39fdf?w=1200',
    'https://images.unsplash.com/photo-1556912167-f556f1f39fdf',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_27.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Toiture récente'
),

(
    '20682840-d4ff-4de4-9702-0d2b6426dae6',
    'f9a3b2c1-d4e5-4a6b-7c8d-9e0f1a2b3c4d',
    'https://images.unsplash.com/photo-1556911261-6bd341186b2f?w=800',
    'https://images.unsplash.com/photo-1556911261-6bd341186b2f?w=150',
    'https://images.unsplash.com/photo-1556911261-6bd341186b2f?w=400',
    'https://images.unsplash.com/photo-1556911261-6bd341186b2f?w=800',
    'https://images.unsplash.com/photo-1556911261-6bd341186b2f?w=1200',
    'https://images.unsplash.com/photo-1556911261-6bd341186b2f',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_28.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Chauffage centralisé'
),

(
    'c9b4fa9d-a45f-4ce1-b9c5-bc1d54d25965',
    'ff178215-8680-423d-b4bb-4d36105ab28e',
    'https://images.unsplash.com/photo-1606744888344-493238951221?w=800',
    'https://images.unsplash.com/photo-1606744888344-493238951221?w=150',
    'https://images.unsplash.com/photo-1606744888344-493238951221?w=400',
    'https://images.unsplash.com/photo-1606744888344-493238951221?w=800',
    'https://images.unsplash.com/photo-1606744888344-493238951221?w=1200',
    'https://images.unsplash.com/photo-1606744888344-493238951221',
    NULL, NULL, NULL, NULL,
    FALSE, 'property_photo_29.jpg', 1920, 1280, 524288, 'image/jpeg',
    TRUE, 0, 'Accès aisé aux transports'
);

-- ==================== Ajouter des favoris pour tester ====================
INSERT INTO favorites (id, user_id, property_id) VALUES
('950f90a1-2e95-4809-8f59-2eebffc3bcf0', 'a948513d-0702-46a3-999c-af7caeebe060', '780b81ae-3ef4-4b4f-8ac0-092b3ca4c11b'),
('857b2abf-4117-488f-b8f9-c9a6106f46c7', 'a948513d-0702-46a3-999c-af7caeebe060', 'd53e4ef6-5bf8-428a-9aa4-9d631b047f99'),
('902d0448-ca22-4db8-9af9-e5bba2dc02c7', '1ade390f-f531-4224-96ea-de365c81329c', 'bfcf9b00-007d-4203-942b-007353ac0855'),
('881305da-972f-4823-a523-50f65ab0520a', '894c23a7-a078-40b4-91ca-da5d7240fb58', '2015fc04-70e8-41f8-bd56-19970d464adf'),
('257caa3f-1fbe-4adc-8fc3-2bcde559cbe4', 'f6eb9ae3-674b-4804-840a-3e302bbee554', '4cd19b24-3e11-439a-a8ad-d5af0b2c4b05'),
('81f971a4-a6ab-47b6-94d7-8174a27c0ee9', '02e8577c-c21d-43d2-ad34-222da8c72998', '53fa9092-2e73-4d07-abcc-1db5da1c257b');

SELECT '✅ === Photos seeded successfully! Total: ' || COUNT(*) FROM photos;
SELECT '✅ === Favorites seeded successfully! Total: ' || COUNT(*) FROM favorites;