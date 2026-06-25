# ISFW-basado_IAGen - Capítulo 5


# Capítulo 5: Desarrollo de Software, Productividad y Calidad en la Era de la Inteligencia Artificial Generativa (IAGen)

Esta carpeta contiene las fuentes bibliográficas, artículos científicos, documentos de apoyo, códigos fuente de práctica, activos gráficos y resúmenes correspondientes al Capítulo 5 de la investigación, enfocado en el desarrollo de software asistido por IA.

## Contenido


Contiene libros, artículos científicos y reportes de investigación recortados por capítulos y páginas exactas utilizados como base teórica y empírica del capítulo.

Las fuentes principales incluyen:

* Advait Sarkar e Ian Drosos (2025) – *Vibe coding: programming through conversation with artificial intelligence* (Microsoft Research).
* Vincent Gurgul, Robin Gubela y Stefan Lessmann (2026) – *The State of Generative AI in Software Development: Insights from Literature and a Developer Survey* (Humboldt-Universität zu Berlin).
* Tom Taulli (2024) – *AI-Assisted Programming: Better Planning, Coding, Testing, and Deployment* (O'Reilly Media).
* Anjali Jain et al. (2024) – *AI-Assisted Programming for Web and Machine Learning* (Packt Publishing).
* Sergio Pereira (2024) – *Generative AI for Software Development: Building Software Faster and More Effectively* (O'Reilly Media).
* Mark Winteringham (2024) – *Software Testing with Generative AI: Enhancing testing with LLMs* (Manning Publications).



Incluye las transcripciones estructuradas y limpias de los capítulos pertinentes en formato Markdown (.md) para facilitar su indexación y procesamiento analítico en NotebookLM, manteniendo la numeración de páginas original para una trazabilidad exacta.



Contiene los diagramas conceptuales, esquemas arquitectónicos y representaciones gráficas educativas desarrolladas en español y a color para ilustrar los conceptos de cada sección.

---

# Subtemas del capítulo

## 5.1 El nuevo paradigma de la codificación asistida conectado al diseño del caso faro

* Evolución de la comunicación humano-computadora en programación.
* Fenómeno del "Vibe Coding" y desacoplamiento material (material disengagement).
* Metodología de diseño descendente (Top-Down Design) y funciones hoja (leaf functions).
* Gestión de riesgos del código sintáctico: "context momentum" y dependencias de ruta.
* El rol del programador como auditor lógico y supervisor de contexto.

## 5.2 Productividad y calidad del código: revisión, explicación y mejora incremental

* Calidad de código asistido y mantenibilidad a largo plazo.
* Técnicas de refactorización y depuración incremental mediante asistentes de código chat (Copilot Chat, Cursor).
* Reducción de la complejidad ciclomática en el software generado por IA.
* Aplicación del patrón de cláusulas de guarda (guard clauses) frente a condicionales profundamente anidados ("código ninja").

## 5.3 Programación multilenguaje y migración de código con validación humana

* Interoperabilidad y comunicación en ecosistemas distribuidos y políglotas.
* Construcción de servicios backend en Python Flask con serialización JSON.
* Portabilidad de modelos predictivos de Machine Learning mediante el formato universal ONNX (Open Neural Network Exchange).
* Consumo y ejecución de inferencia en el cliente mediante JavaScript y `onnxruntime` en el navegador.

## 5.4 Flujos de trabajo en equipos aumentados por IA: roles, revisión y bitácora

* Reorganización de flujos de valor y transición a células de desarrollo aumentadas (augmented teams).
* Herramientas de revisión automática en Pull Requests (Codacy, CodeRabbit) como primer filtro de seguridad y estilo.
* Reconfiguración de roles técnicos (arquitecto de contexto, auditor de prompts, validador de lógica).
* Implementación de bitácoras de auditoría (audit logs) para registrar prompts, respuestas de la IA y aprobaciones humanas.
* Mitigación de riesgos éticos, alucinaciones lógicas, seguridad (SQL injection, XSS) y propiedad intelectual.

## 5.5 Resumen, preguntas de reflexión y práctica de implementación parcial del caso faro

* Aseguramiento de calidad tradicional frente a agentes lógicos de pruebas autónomos en ciclos TDD.
* Intercepción automática de excepciones en tiempo de ejecución.
* Análisis y parseo semántico de pilas de llamadas (stack trace).
* Generación automática de reportes de bugs estructurados en JSON y sugerencias de remediación basadas en reglas.

---

# Objetivo del capítulo

Analizar el impacto y las metodologías del desarrollo de software asistido por Inteligencia Artificial Generativa, examinando la evolución hacia la codificación conversacional (Vibe Coding), las técnicas para asegurar la productividad y la calidad del código mediante refactorización lineal, la interoperabilidad políglota basada en APIs REST y ONNX, y la gobernanza de flujos de trabajo aumentados en equipos mediante bitácoras de auditoría y agentes de prueba autónomos.

---

# Preguntas de investigación

1. ¿De qué manera la transición al "Vibe Coding" y la delegación sintáctica a la IA redefinen las competencias fundamentales del ingeniero de software contemporáneo?

2. ¿Cómo impactan las técnicas de refactorización lineal (cláusulas de guarda) en la reducción de complejidad ciclomática y en la prevención de alucinaciones lógicas de los LLMs?

3. ¿Cuáles son las ventajas operacionales y de latencia al compilar modelos predictivos a ONNX para realizar inferencia local en cliente frente a servicios en la nube?

4. ¿Cómo pueden las células de desarrollo aumentadas gestionar los riesgos de cumplimiento, seguridad y propiedad intelectual utilizando pipelines de revisión por capas y bitácoras de auditoría?

5. ¿De qué forma la suite de pruebas unitarias y los agentes autónomos de QA disminuyen el tiempo promedio de resolución de incidentes (MTTR) mediante la intercepción semántica de fallos?

---

# Metodología de trabajo

1. Seleccionar y recopilar fuentes científicas, libros y reportes empíricos actualizados (2023–2026) sobre desarrollo de software asistido por IA, Vibe Coding y aseguramiento de calidad.

2. Clasificar las fuentes bibliográficas asignándolas a los subtemas 5.1 al 5.5 para garantizar una trazabilidad teórica completa.

3. Convertir y consolidar los capítulos fuente en formato Markdown (.md) en la carpeta `Fuentes/md/`, conservando marcas de página física para trazabilidad exacta.

4. Estructurar resúmenes continuos y cohesionados bajo un formato de prosa formal académica, eliminando viñetas informales de resumen.

5. Diseñar e implementar diagramas y mapas conceptuales educativos a color en español, programados en Python para evitar deformidades de texto o estéticas de IA sobrecargadas.

6. Escribir un script de compilación programática utilizando `python-docx` para ensamblar el documento final en Word, garantizando que todo el texto aparezca en negro puro.

7. Integrar la tabla formal de métricas de calidad y eficiencia comparativas dentro de la sección 5.5 del documento.

8. Codificar el Agente QA Autónomo en Python (`QAUnitTestAgent`) y documentarlo formalmente en la Actividad Práctica de la sección 5.6 dentro de una tabla de celda única estilizada con fuente Consolas.

9. Compilar la bibliografía consolidada ordenada alfabéticamente en la sección de REFERENCIAS al final del documento.

10. Validar la integridad física del archivo de Word final y de la carpeta de activos para asegurar el correcto renderizado y legibilidad del entregable.
