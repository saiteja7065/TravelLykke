# Deployment Guide for TravelLykke

## Production Deployment Steps

### 1. Server Setup
- Ubuntu/CentOS server with Python 3.13+
- MySQL 8.0+
- Nginx
- Gunicorn

### 2. Environment Setup
```bash
# Clone repository
git clone https://github.com/saiteja7065/TravelLykke.git
cd TravelLykke

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install gunicorn
```

### 3. Database Setup
```bash
# Install MySQL
sudo apt install mysql-server

# Create database
mysql -u root -p
CREATE DATABASE travel_booking_db;
CREATE USER 'travel_user'@'localhost' IDENTIFIED BY 'secure_password';
GRANT ALL PRIVILEGES ON travel_booking_db.* TO 'travel_user'@'localhost';
FLUSH PRIVILEGES;
```

### 4. Environment Configuration
```bash
# Copy environment file
cp .env.example .env

# Edit .env with production values
nano .env
```

### 5. Django Setup
```bash
cd backend

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Test server
python manage.py runserver 0.0.0.0:8000
```

### 6. Gunicorn Configuration
Create `/etc/systemd/system/travellykke.service`:
```ini
[Unit]
Description=TravelLykke Django App
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/path/to/TravelLykke/backend
Environment="PATH=/path/to/TravelLykke/venv/bin"
ExecStart=/path/to/TravelLykke/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/path/to/TravelLykke/backend/travellykke.sock travel_booking.wsgi:application

[Install]
WantedBy=multi-user.target
```

### 7. Nginx Configuration
Create `/etc/nginx/sites-available/travellykke`:
```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /path/to/TravelLykke/backend;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/path/to/TravelLykke/backend/travellykke.sock;
    }
}
```

### 8. SSL Setup (Let's Encrypt)
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

### 9. Start Services
```bash
sudo systemctl start travellykke
sudo systemctl enable travellykke
sudo systemctl restart nginx
```

### 10. Maintenance
```bash
# Update code
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic
sudo systemctl restart travellykke
```

## Docker Deployment (Alternative)

### Dockerfile
```dockerfile
FROM python:3.13-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
WORKDIR /app/backend

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "travel_booking.wsgi:application"]
```

### docker-compose.yml
```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
    depends_on:
      - db
      
  db:
    image: mysql:8.0
    environment:
      MYSQL_DATABASE: travel_booking_db
      MYSQL_ROOT_PASSWORD: rootpassword
    volumes:
      - mysql_data:/var/lib/mysql

volumes:
  mysql_data:
```

## Security Checklist
- [ ] Set DEBUG=False
- [ ] Configure ALLOWED_HOSTS
- [ ] Use environment variables for secrets
- [ ] Set up SSL/HTTPS
- [ ] Configure firewall
- [ ] Regular backups
- [ ] Monitor logs
- [ ] Update dependencies regularly
