#  Generador de contraseñas seguras
1. Generar contraseñas seguras:
- Solicitar al usuario la longitud de la contraseña y los tipos de caracteres a incluir (mayúsculas, minúsculas, números y caracteres especiales).
- Validar que el usuario haya seleccionado al menos un tipo de carácter. Si no, mostrar un mensaje de error y volver a solicitar las preferencias.
- Generar la contraseña de manera aleatoria según las preferencias del usuario.
- Mostrar la contraseña generada.
  
2. Comprobar la fuerza de una contraseña ingresada por el usuario:
- Evaluar la fortaleza de la contraseña basándose en criterios como longitud, uso de mayúsculas, minúsculas, números, caracteres especiales y diversidad de caracteres.
- Mostrar un mensaje indicando si la contraseña es débil, media o fuerte.
  
3. Guardar la contraseña en una base de datos (opcional):
- Preguntar al usuario si desea guardar la contraseña generada.
- Si el usuario acepta, almacenar la contraseña en una base de datos junto con un identificador único (por ejemplo, un nombre de usuario o servicio asociado).
- Mostrar un mensaje de confirmación si la contraseña se guardó correctamente.

4. Flujo general:
- Permitir al usuario generar una contraseña, comprobar la fuerza de una contraseña o salir del programa.
- Preguntar al usuario si desea realizar otra acción después de completar una operación. Si la respuesta es afirmativa, volver al menú principal; de lo contrario, finalizar el programa.

<img src="https://github.com/easalazarp/secure-password-genetator/blob/5660dd92ad1b1ee1a2240be7cf37e7f3158805eb/Diagrama%20de%20flujo.jpg" alt="Diagrama de flujo" />
