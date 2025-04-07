#!/bin/bash
set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Recolectar archivos estáticos
python manage.py collectstatic --no-input

# Ejecutar migraciones
python manage.py migrate

# Crear el superusuario automáticamente
echo "Creating superuser..."
echo "from django.contrib.auth.models import User; User.objects.create_superuser('testUser123', 'testuser@example.com', 'Test@1234')" | python manage.py shell
