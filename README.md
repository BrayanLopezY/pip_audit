# Readme add

# pip audit

# Para poder ejecutar pip audit, necesitas activar un entorno virtual con el siguiente comando

    python -m venv venv

# Y ahora para poder actvarlo se ejecuta el siguiente comando

    venv\Scripts\activate

# Una vez ya activado ejecutar el comando 
    
    pip install -r requirements.txt

# Luego ejecutar el comando audit

    pip-audit -f json

# y para arreglar ejecutar el siguiente comando

    pip-audit --fix
