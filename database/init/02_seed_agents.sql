-- =====================================================
-- 02_seed_agents.sql - Agents immobiliers de test
-- =====================================================

-- Note: Le password pour tous les agents est "Password123!"
-- Hash généré avec bcrypt (sha256 + bcrypt comme dans ton code)

INSERT INTO agents (id, name, agency_name, email, phone, password_hash, rsac_number, city, is_verified, is_active) VALUES

-- Agent 1: Paris - Vérifié
(
    '1937c11c-0796-40b9-a231-ab24332e23a1',
    'Marie Dupont',
    'Immobilier Paris Centre',
    'marie.dupont@immo-paris.fr',
    '0612345678',
    '$2b$12$/eIY/wdc2IixyLWIJVlGwOVciXA04OK/CJzVwMqz4nSpIKBxyDG3O',
    'RSAC751234567',
    'Paris',
    TRUE,
    TRUE
),

-- Agent 2: Paris 16ème - Vérifié
(
    '18cb5033-07aa-431c-9c9d-2532fce5e258',
    'Jean-Pierre Martin',
    'Barnes Paris 16',
    'jp.martin@barnes-paris.fr',
    '0623456789',
    '$2b$12$/eIY/wdc2IixyLWIJVlGwOVciXA04OK/CJzVwMqz4nSpIKBxyDG3O',
    'RSAC752345678',
    'Paris',
    TRUE,
    TRUE
),

-- Agent 3: Lyon - Vérifié
(
    '9c6645fa-6a35-46f7-8b6a-b5883862ae49',
    'Sophie Bernard',
    'Lyon Prestige Immobilier',
    'sophie.bernard@lyon-prestige.fr',
    '0634567890',
    '$2b$12$/eIY/wdc2IixyLWIJVlGwOVciXA04OK/CJzVwMqz4nSpIKBxyDG3O',
    'RSAC693456789',
    'Lyon',
    TRUE,
    TRUE
),

-- Agent 4: Marseille - Vérifié
(
    '22479295-f7bd-4d9a-bc9e-3d660d18a1f8',
    'Lucas Petit',
    'Agence du Vieux Port',
    'lucas.petit@vieuxport-immo.fr',
    '0645678901',
    '$2b$12$/eIY/wdc2IixyLWIJVlGwOVciXA04OK/CJzVwMqz4nSpIKBxyDG3O',
    'RSAC134567890',
    'Marseille',
    TRUE,
    TRUE
),

-- Agent 5: Bordeaux - Vérifié
(
    'd15aaa6d-be7d-4f64-b677-f07ca75f1346',
    'Camille Roux',
    'Bordeaux Properties',
    'camille.roux@bordeaux-prop.fr',
    '0656789012',
    '$2b$12$/eIY/wdc2IixyLWIJVlGwOVciXA04OK/CJzVwMqz4nSpIKBxyDG3O',
    'RSAC335678901',
    'Bordeaux',
    TRUE,
    TRUE
),

-- Agent 6: Vitry-sur-Seine - Non vérifié (pour tester)
(
    '6deb05b1-f453-4667-8fe0-45372c20bea5',
    'Christian Leng',
    'Agence Vitry',
    'christian.leng@agence-vitry.fr',
    '0667890123',
    '$2b$12$/eIY/wdc2IixyLWIJVlGwOVciXA04OK/CJzVwMqz4nSpIKBxyDG3O',
    'RSAC946789012',
    'Vitry-sur-Seine',
    FALSE,
    TRUE
),

-- Agent 7: Nice - Vérifié
(
    '4d5b94d4-2acf-4e8a-af7c-64d26f7d9a9c',
    'Emma Leroy',
    'Côte d''Azur Immobilier',
    'emma.leroy@cote-azur-immo.fr',
    '0678901234',
    '$2b$12$/eIY/wdc2IixyLWIJVlGwOVciXA04OK/CJzVwMqz4nSpIKBxyDG3O',
    'RSAC067890123',
    'Nice',
    TRUE,
    TRUE
),

-- Agent 8: Toulouse - Vérifié
(
    '2375e3c3-60ee-4269-adfe-5899f0947449',
    'Thomas Moreau',
    'Toulouse Habitat',
    'thomas.moreau@toulouse-habitat.fr',
    '0689012345',
    '$2b$12$/eIY/wdc2IixyLWIJVlGwOVciXA04OK/CJzVwMqz4nSpIKBxyDG3O',
    'RSAC318901234',
    'Toulouse',
    TRUE,
    TRUE
),

-- Agent 9: Nantes - Non vérifié
(
    '6f167cd8-7b93-4898-b5a1-d57f6a8796bb',
    'Julie Simon',
    'Nantes Immobilier',
    'julie.simon@nantes-immo.fr',
    '0690123456',
    '$2b$12$/eIY/wdc2IixyLWIJVlGwOVciXA04OK/CJzVwMqz4nSpIKBxyDG3O',
    'RSAC449012345',
    'Nantes',
    FALSE,
    TRUE
),

-- Agent 10: Strasbourg - Vérifié
(
    'd3fa20b8-0bcb-4a32-9520-86cc238bd012',
    'Pierre Laurent',
    'Alsace Immobilier',
    'pierre.laurent@alsace-immo.fr',
    '0601234567',
    '$2b$12$/eIY/wdc2IixyLWIJVlGwOVciXA04OK/CJzVwMqz4nSpIKBxyDG3O',
    'RSAC670123456',
    'Strasbourg',
    TRUE,
    TRUE
);

SELECT 'Agents seeded successfully! Total: ' || COUNT(*) FROM agents;