"""
Proyecto Python y Mysql:
- Abrir asistente
- Login o registro
- Si elegimos registro, creará un usuario en la bbdd
- Si elegimos login, identifica el usuario y hara unas preguntas
- Crear, mostrar y borrar notas
"""

from usuarios import acciones #Importamos el modulo 

print("""
Acciones disponibles:
    - Registro
    - Login
""")

hazEl = acciones.Acciones() #Instancia de clase

accion = input("¿Que quieres hacer?: ")
m_accion = accion.lower()

if m_accion == "registro":
    hazEl.Registro()

elif m_accion == "login":
    hazEl.Login()
    