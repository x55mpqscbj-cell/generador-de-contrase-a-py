# 🔐 Generador de Contraseñas en Python

Un script sencillo en Python que genera contraseñas aleatorias de 15 caracteres combinando letras minúsculas, mayúsculas, números y símbolos.

## ¿Cómo funciona?

1. Usa el módulo `string` para obtener los conjuntos de caracteres: minúsculas, mayúsculas, dígitos y símbolos.
2. Junta todos los conjuntos en una sola cadena.
3. Con `random.choices()` escoge 15 caracteres al azar y los une en la contraseña final.

## ▶️ Cómo usarlo

```bash
python contraseñas.py
```

El script imprime los conjuntos de caracteres y, al final, la contraseña generada.

## 🛡️ ¿Cómo me ayuda en mi carrera de ciberseguridad?

Este proyecto es pequeño, pero toca ideas que se usan todo el tiempo en seguridad informática:

- **Entender qué hace fuerte a una contraseña:** la fortaleza viene de la longitud y del tamaño del conjunto de caracteres. Con 94 caracteres posibles y 15 posiciones, hay una cantidad enorme de combinaciones, lo que hace inviable un ataque de fuerza bruta.
- **Pensar como atacante y como defensor:** saber cómo se generan las contraseñas ayuda a entender cómo se rompen (fuerza bruta, diccionarios, credential stuffing) y cómo se previenen.
- **Aleatoriedad y criptografía:** me enseñó la diferencia entre `random` (pseudoaleatorio, NO apto para seguridad real) y `secrets` (diseñado para criptografía). Una mejora pendiente es migrar el script a `secrets`.
- **Buenas prácticas de higiene digital:** contraseñas únicas y largas por cada cuenta, y uso de gestores de contraseñas.
- **Práctica de Python para automatizar tareas:** en pentesting y análisis de seguridad se escriben scripts propios constantemente.
- **Portafolio y documentación:** subir proyectos a GitHub con un README claro es parte de construir un perfil profesional.

## 🚀 Mejoras futuras

- Cambiar `random` por `secrets` para generación criptográficamente segura.
- Permitir elegir la longitud y los tipos de caracteres por input o argumentos.
- Garantizar al menos un carácter de cada tipo.
- Calcular y mostrar la entropía de la contraseña.

## 👤 Autor

**Anthony Ivan Barrios**
