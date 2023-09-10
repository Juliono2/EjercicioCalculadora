# Calculadora en Python

Esta es una calculadora simple implementada en Python utilizando la biblioteca Tkinter para la interfaz gráfica. 
La calculadora puede realizar operaciones haciendo uso de una clase que intenta simular una interfaz quien provee las operaciones.

## Funcionalidades

- Suma
- Resta
- Multiplicación
- División
- Potenciación
- Borrado de caracteres
- Borrado de todo el contenido
- Calcular expresion

## Cómo usar la calculadora

1. Ejecute el programa `calculadora.py`.
2. Aparecerá una ventana con la interfaz de la calculadora.
3. Haga clic en los botones numéricos (0-9) para ingresar números.
4. Utilice los botones de operadores (+, -, *, /, ^) para seleccionar la operación deseada.
5. Puede utilizar el botón "C" para borrar todo el contenido o el botón "←" para borrar un carácter a la vez.
6. Haga clic en el botón "=" para calcular el resultado.
7. El resultado se mostrará en la parte inferior de la calculadora.

## Consideraciones

A pesar de ser una calculadora funcional, esta implementación tiene algunas limitaciones y consideraciones importantes:

1. **Manejo de Excepciones:** Esta calculadora no maneja excepciones, lo que significa que no realiza comprobaciones exhaustivas de errores. Por lo tanto, puede arrojar resultados inesperados o errores en situaciones como la división por cero o la entrada de caracteres no válidos. Los usuarios deben ser conscientes de las limitaciones y evitar operaciones no válidas.

2. **Operaciones Simples:** La calculadora está diseñada para realizar operaciones simples de un solo operador a la vez. No admite expresiones matemáticas complejas ni la combinación de múltiples operadores en una sola entrada. Cada operación debe completarse antes de ingresar una nueva.

3. **Borrado de Números:** Al ingresar un nuevo operador, la calculadora borra por completo el número anterior y considera el nuevo operador como el inicio de una nueva operación. Esto puede ser confuso si el usuario comete un error en la entrada y desea corregirlo.

4. **División por Cero:** La calculadora no incluye comprobaciones para la división por cero. Si el usuario intenta dividir un número por cero, la calculadora mostrará un resultado indefinido o un error.

5. **Características Adicionales:** Esta implementación se centra en las operaciones básicas y la interfaz de usuario. No incluye características adicionales como el manejo de paréntesis, funciones trigonométricas u otras funciones avanzadas de una calculadora científica estándar.

A pesar de estas limitaciones, la calculadora proporciona una funcionalidad básica para realizar cálculos rápidos y simples. Los usuarios deben utilizarla con precaución y comprender sus restricciones.


## Requisitos
- Python 3.x
- Biblioteca Tkinter
