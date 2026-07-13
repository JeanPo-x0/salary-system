# Sistema de Salarios

Programa en Python que calcula el salario quincenal de trabajadores, 
con una interfaz de consola personalizada con colores (usando la 
librería `rich`).

## ¿Qué hace?
- Pide los datos de cada día trabajado durante 2 semanas (quincena).
- O tambien puedes calcular una sola semana o la quincena completa (2 semanas) eligiendo al inicio.
- Registra: día, lugar de trabajo, labor realizada, horas trabajadas 
  (con minutos), horas extra y horas de almuerzo.
- Permite elegir entre 2 tarifas por hora o bien ingresar una tarifa personalizada entre ₡500 y ₡2.200.
- Calcula el pago normal y el pago con recargo del 50% en horas extra.
- Descuenta automáticamente la hora de almuerzo.
- Muestra un resumen detallado por día, subtotal por semana, y el 
  total final de la quincena.
- Formatea los montos en colones con separador de miles (₡130.000).
- Valida todas las entradas del usuario (rechaza texto donde va 
  número, rangos fuera de lo permitido, respuestas distintas a 
  "si"/"no").
- Permite calcular varios trabajadores seguidos sin tener que reiniciar el 
  programa.

## Librerías usadas
- `rich` — para dar color y formato a la consola adaptandola al cliente.

## Qué aprendí
- Funciones con `return` en vez de variables globales.
- Loops anidados y validación con `while True` + `try/except`.
- Listas de diccionarios para guardar registros día por día.
- Formateo de strings con f-strings y personalización con `rich`.
- Separar acumuladores por semana para totales independientes.
- Estructurar un programa completo en un loop principal reutilizable.

## Cómo correrlo
- Instala la dependencia:
```
pip install rich
```
- Luego ejecuta:
```
python "SistemaS - Codigo fuente.py"
```