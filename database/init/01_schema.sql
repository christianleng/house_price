-- =====================================================
-- 01_schema.sql - Création des tables et enums
-- =====================================================

-- ============== ENUMS ==============

DO $$ BEGIN
    CREATE TYPE transactiontype AS ENUM ('sale', 'rent');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE TYPE propertytype AS ENUM ('house', 'apartment', 'studio', 'loft', 'duplex', 'triplex', 'penthouse', 'villa', 'land', 'commercial', 'parking');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE TYPE heatingtype AS ENUM ('individual', 'collective', 'electric', 'gas', 'fuel', 'heat_pump', 'wood', 'solar', 'none');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE TYPE energyrating AS ENUM ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'N/A');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE TYPE orientation AS ENUM ('north', 'south', 'east', 'west', 'north_east', 'north_west', 'south_east', 'south_west');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE TYPE propertycondition AS ENUM ('new', 'excellent', 'good', 'to_refresh', 'to_renovate');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;


-- ============== TABLES ==============

-- Table agents
CREATE TABLE IF NOT EXISTS agents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL,
    agency_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    rsac_number VARCHAR(50) UNIQUE NOT NULL,
    city VARCHAR(100) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_verified BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE
);

-- Table users
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Table properties
CREATE TABLE IF NOT EXISTS properties (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    agent_id UUID NOT NULL REFERENCES agents(id) ON DELETE CASCADE,
    reference VARCHAR(50) UNIQUE NOT NULL,
    
    -- Informations de base
    title VARCHAR(200) NOT NULL,
    description TEXT,
    transaction_type transactiontype NOT NULL,
    
    -- Localisation
    address VARCHAR(300) NOT NULL,
    neighborhood VARCHAR(100),
    city VARCHAR(100) NOT NULL,
    district VARCHAR(100),
    postal_code VARCHAR(10) NOT NULL,
    latitude FLOAT,
    longitude FLOAT,
    
    -- Prix vente
    price INTEGER,
    price_per_sqm INTEGER,
    
    -- Prix location
    rent_price_monthly INTEGER,
    rent_charges INTEGER,
    charges_included BOOLEAN DEFAULT FALSE,
    deposit INTEGER,
    
    -- Caractéristiques
    property_type propertytype NOT NULL,
    surface_area INTEGER NOT NULL,
    rooms INTEGER NOT NULL,
    bedrooms INTEGER DEFAULT 0,
    bathrooms INTEGER DEFAULT 0,
    toilets INTEGER DEFAULT 0,
    
    -- Étages
    floor_number INTEGER,
    floors INTEGER,
    
    -- Équipements
    has_cave BOOLEAN DEFAULT FALSE,
    has_elevator BOOLEAN DEFAULT FALSE,
    has_balcony BOOLEAN DEFAULT FALSE,
    has_terrace BOOLEAN DEFAULT FALSE,
    has_garden BOOLEAN DEFAULT FALSE,
    has_parking BOOLEAN DEFAULT FALSE,
    parking_spaces INTEGER DEFAULT 0,
    has_garage BOOLEAN DEFAULT FALSE,
    has_cellar BOOLEAN DEFAULT FALSE,
    has_pool BOOLEAN DEFAULT FALSE,
    has_alarm BOOLEAN DEFAULT FALSE,
    has_intercom BOOLEAN DEFAULT FALSE,
    has_digicode BOOLEAN DEFAULT FALSE,
    has_caretaker BOOLEAN DEFAULT FALSE,
    
    -- État et caractéristiques
    condition propertycondition,
    orientation orientation,
    is_furnished BOOLEAN DEFAULT FALSE,
    is_quiet BOOLEAN DEFAULT FALSE,
    has_view BOOLEAN DEFAULT FALSE,
    
    -- Énergie
    heating_type heatingtype,
    energy_rating energyrating,
    ges_rating energyrating,
    
    -- Construction
    construction_year INTEGER,
    
    -- Disponibilité
    available_from TIMESTAMP WITH TIME ZONE,
    
    -- Visite virtuelle
    virtual_tour_url VARCHAR(500),

    photos_count INTEGER NOT NULL DEFAULT 0,
    views_count INTEGER NOT NULL DEFAULT 0,
    
    -- Métadonnées
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Table photos
CREATE TABLE IF NOT EXISTS photos (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    property_id UUID NOT NULL REFERENCES properties(id) ON DELETE CASCADE,
    
    -- URL Legacy
    url VARCHAR(500),
    
    -- URLs JPEG par taille
    url_thumbnail VARCHAR(500),
    url_small VARCHAR(500),
    url_medium VARCHAR(500),
    url_large VARCHAR(500),
    url_original VARCHAR(500),
    
    -- URLs WebP par taille
    url_thumbnail_webp VARCHAR(500),
    url_small_webp VARCHAR(500),
    url_medium_webp VARCHAR(500),
    url_large_webp VARCHAR(500),
    has_webp BOOLEAN DEFAULT TRUE,
    
    -- Métadonnées
    original_filename VARCHAR(255),
    original_width INTEGER,
    original_height INTEGER,
    size_bytes INTEGER,
    content_type VARCHAR(50),
    
    -- Organisation
    is_primary BOOLEAN DEFAULT FALSE,
    display_order INTEGER DEFAULT 0,
    caption VARCHAR(255),
    
    -- Timestamp
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table favorites
CREATE TABLE IF NOT EXISTS favorites (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    property_id UUID NOT NULL REFERENCES properties(id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, property_id)
);

-- Table features (caractéristiques additionnelles)
CREATE TABLE IF NOT EXISTS features (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    property_id UUID NOT NULL REFERENCES properties(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    value VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);


-- ============== INDEXES ==============

CREATE INDEX IF NOT EXISTS idx_agents_email ON agents(email);
CREATE INDEX IF NOT EXISTS idx_agents_rsac ON agents(rsac_number);

CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);

CREATE INDEX IF NOT EXISTS idx_properties_agent_id ON properties(agent_id);
CREATE INDEX IF NOT EXISTS idx_properties_transaction_type ON properties(transaction_type);
CREATE INDEX IF NOT EXISTS idx_properties_city ON properties(city);
CREATE INDEX IF NOT EXISTS idx_properties_postal_code ON properties(postal_code);
CREATE INDEX IF NOT EXISTS idx_properties_property_type ON properties(property_type);
CREATE INDEX IF NOT EXISTS idx_properties_price ON properties(price);
CREATE INDEX IF NOT EXISTS idx_properties_rent_price_monthly ON properties(rent_price_monthly);
CREATE INDEX IF NOT EXISTS idx_properties_created_at ON properties(created_at);

CREATE INDEX IF NOT EXISTS idx_photos_property_id ON photos(property_id);
CREATE INDEX IF NOT EXISTS idx_photos_is_primary ON photos(is_primary);

CREATE INDEX IF NOT EXISTS idx_favorites_user_id ON favorites(user_id);
CREATE INDEX IF NOT EXISTS idx_favorites_property_id ON favorites(property_id);


-- ============== VERIFICATION ==============

SELECT '✅ === Schema created successfully!' AS status;