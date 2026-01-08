-- =====================================================
-- 03_seed_users.sql - Utilisateurs de test
-- =====================================================

-- Note: Le password pour tous les users est "Password123!"
-- Hash généré avec bcrypt (sha256 + bcrypt comme dans ton code)

INSERT INTO users (id, email, first_name, last_name, password_hash, phone, is_active) VALUES

-- User 1: Recherche appartement Paris
(
    'a948513d-0702-46a3-999c-af7caeebe060',
    'alice.martin@gmail.com',
    'Alice',
    'Martin',
    '$2b$12$/eIY/wdc2IixyLWIJVlGwOVciXA04OK/CJzVwMqz4nSpIKBxyDG3O',
    '0612345678',
    TRUE
),

-- User 2: Recherche maison Lyon
(
    '1ade390f-f531-4224-96ea-de365c81329c',
    'bob.durand@gmail.com',
    'Bob',
    'Durand',
    '$2b$12$/eIY/wdc2IixyLWIJVlGwOVciXA04OK/CJzVwMqz4nSpIKBxyDG3O',
    '0623456789',
    TRUE
),

-- User 3: Étudiant recherche studio
(
    '894c23a7-a078-40b4-91ca-da5d7240fb58',
    'claire.petit@student.fr',
    'Claire',
    'Petit',
    '$2b$12$/eIY/wdc2IixyLWIJVlGwOVciXA04OK/CJzVwMqz4nSpIKBxyDG3O',
    '0634567890',
    TRUE
),

-- User 4: Investisseur
(
    'f6eb9ae3-674b-4804-840a-3e302bbee554',
    'david.invest@outlook.com',
    'David',
    'Lemaire',
    '$2b$12$/eIY/wdc2IixyLWIJVlGwOVciXA04OK/CJzVwMqz4nSpIKBxyDG3O',
    '0645678901',
    TRUE
),

-- User 5: Famille recherche maison
(
    '02e8577c-c21d-43d2-ad34-222da8c72998',
    'famille.dubois@orange.fr',
    'Émilie',
    'Dubois',
    '$2b$12$/eIY/wdc2IixyLWIJVlGwOVciXA04OK/CJzVwMqz4nSpIKBxyDG3O',
    '0656789012',
    TRUE
),

-- User 6: Jeune couple
(
    'fcce7f51-7aa1-4b01-960a-d84771430cb0',
    'marc.sophie@gmail.com',
    'Marc',
    'Rousseau',
    '$2b$12$/eIY/wdc2IixyLWIJVlGwOVciXA04OK/CJzVwMqz4nSpIKBxyDG3O',
    '0667890123',
    TRUE
),

-- User 7: Expatrié
(
    '2aa9852f-0189-40fa-b6eb-4ba52426aa81',
    'john.smith@expat.com',
    'John',
    'Smith',
    '$2b$12$/eIY/wdc2IixyLWIJVlGwOVciXA04OK/CJzVwMqz4nSpIKBxyDG3O',
    '0678901234',
    TRUE
),

-- User 8: Retraité
(
    'f50f4d61-6f7e-47e6-a860-817443cdcff9',
    'jean.marie@free.fr',
    'Jean',
    'Moreau',
    '$2b$12$/eIY/wdc2IixyLWIJVlGwOVciXA04OK/CJzVwMqz4nSpIKBxyDG3O',
    '0689012345',
    TRUE
),

-- User 9: Compte inactif (pour tester)
(
    '79699f7f-05ea-4dfa-b18a-c7ed74fe6e35',
    'inactive.user@test.com',
    'Inactive',
    'User',
    '$2b$12$/eIY/wdc2IixyLWIJVlGwOVciXA04OK/CJzVwMqz4nSpIKBxyDG3O',
    '0690123456',
    FALSE
),

-- User 10: Test user
(
    '561dd685-2ec7-4d8b-8dde-93caef22c4be',
    'test@test.com',
    'Test',
    'User',
    '$2b$12$/eIY/wdc2IixyLWIJVlGwOVciXA04OK/CJzVwMqz4nSpIKBxyDG3O',
    '0601234567',
    TRUE
);

SELECT '✅ === Users seeded successfully! Total: ' || COUNT(*) FROM users;