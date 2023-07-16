
CREATE TABLE cdc_test (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    dummy VARCHAR(100),
    category VARCHAR(1) CHECK (category IN ('A', 'B', 'C', 'D', 'E', 'F'))
);

INSERT INTO cdc_test (dummy, category)
VALUES
    ('Lorem ipsum dolor sit amet', 'A'),
    ('Consectetur adipiscing elit', 'B'),
    ('Sed do eiusmod tempor incididunt', 'C'),
    ('Ut labore et dolore magna aliqua', 'D'),
    ('Ut enim ad minim veniam', 'E'),
    ('Quis nostrud exercitation ullamco', 'F'),
    ('Laboris nisi ut aliquip ex ea commodo consequat', 'A'),
    ('Duis aute irure dolor in reprehenderit', 'B'),
    ('Voluptate velit esse cillum dolore', 'C'),
    ('Eu fugiat nulla pariatur', 'D');
