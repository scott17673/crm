CREATE TABLE IF NOT EXISTS manufacturers (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  company text NOT NULL DEFAULT '',
  stage text DEFAULT 'Unqualified',
  industry text DEFAULT '',
  does_manufacture boolean DEFAULT true,
  has_so_facilities boolean DEFAULT false,
  end_product text DEFAULT '',
  machines text DEFAULT '',
  maintenance_needed text DEFAULT '',
  signals text DEFAULT '',
  tags text[] DEFAULT '{}',
  notes text DEFAULT '',
  email_domain text DEFAULT '',
  email_format text DEFAULT '{first}.{last}',
  last_contact date,
  created_at timestamptz DEFAULT now()
);

CREATE TABLE IF NOT EXISTS manufacturing_sites (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  manufacturer_id uuid REFERENCES manufacturers(id) ON DELETE CASCADE,
  address text DEFAULT '',
  phone text DEFAULT '',
  created_at timestamptz DEFAULT now()
);

CREATE TABLE IF NOT EXISTS manufacturer_contacts (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  manufacturer_id uuid REFERENCES manufacturers(id) ON DELETE CASCADE,
  name text DEFAULT '',
  title text DEFAULT '',
  linkedin text DEFAULT '',
  created_at timestamptz DEFAULT now()
);

CREATE TABLE IF NOT EXISTS vendors (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  company text DEFAULT '',
  name text DEFAULT '',
  title text DEFAULT '',
  email text DEFAULT '',
  phone text DEFAULT '',
  industry text DEFAULT '',
  region text DEFAULT '',
  stage text DEFAULT 'Lead',
  tags text[] DEFAULT '{}',
  notes text DEFAULT '',
  last_contact date,
  created_at timestamptz DEFAULT now()
);

CREATE TABLE IF NOT EXISTS lost_contacts (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  company text DEFAULT '',
  name text DEFAULT '',
  title text DEFAULT '',
  email text DEFAULT '',
  phone text DEFAULT '',
  industry text DEFAULT '',
  region text DEFAULT '',
  lost_reason text DEFAULT '',
  deal_value integer DEFAULT 0,
  tags text[] DEFAULT '{}',
  notes text DEFAULT '',
  last_contact date,
  created_at timestamptz DEFAULT now()
);

CREATE TABLE IF NOT EXISTS activities (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  contact_id uuid NOT NULL,
  contact_type text DEFAULT '',
  type text DEFAULT 'Note',
  note text DEFAULT '',
  date date DEFAULT CURRENT_DATE,
  created_by text DEFAULT 'You',
  created_at timestamptz DEFAULT now()
);
ALTER TABLE manufacturers ADD COLUMN IF NOT EXISTS notes text DEFAULT ''; ADD COLUMN IF NOT EXISTS email_domain text DEFAULT ''; ADD COLUMN IF NOT EXISTS email_format text DEFAULT '{first}.{last}';
