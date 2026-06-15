CREATE TABLE IF NOT EXISTS mood_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(50) NOT NULL,
    timestamp DATETIME NOT NULL,
    mood VARCHAR(50) NOT NULL,
    category VARCHAR(100) NOT NULL,
    adjusted_category VARCHAR(150) NOT NULL,
    interest VARCHAR(100),
    age INT,
    gender VARCHAR(50)
);
