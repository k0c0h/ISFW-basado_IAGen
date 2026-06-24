## **PLAN DE PRUEBAS: QA AUTOMATIZADO E INTELIGENTE** 

**Proyecto:** Prototipo de Sistema Software 

**Fecha:** 15 de junio de 2026 

**Versión:** 1.0 

## **1. Introducción y Alcance** 

Este plan define la estrategia de aseguramiento de calidad (QA) para el prototipo. El objetivo es validar la integridad del sistema mediante el rastreo de requisitos y la validación formal de los flujos del sistema, superando las limitaciones de los métodos manuales tradicionales. El alcance incluye la validación de la lógica de negocio, interfaces de usuario y procesos de datos, excluyendo pruebas de carga masiva o seguridad avanzada. 

## **2. Estrategia de Pruebas (Teoría aplicada)** 

- **Generación Automatizada (IAGen):** Uso de modelos de lenguaje para analizar el código fuente y generar escenarios de prueba, optimizando la cobertura de código frente a métodos manuales. 

- **Pruebas Basadas en Modelos (MBT):** Los diagramas de actividades UML se traducen a Máquinas de Estados Finitos Extendidas (EFSM), proporcionando una semántica formal necesaria para la automatización de pruebas y la medición precisa de cobertura de estados y transiciones. 

- **QA Predictivo:** Aplicación de algoritmos de Machine Learning (ej. Random Forest) basados en métricas de complejidad, permitiendo identificar y priorizar los módulos del sistema con mayor probabilidad de defectos antes de la ejecución dinámica. 

## **3. Matriz de Trazabilidad (RTM)** 

La trazabilidad conecta el análisis, diseño e implementación con las pruebas. La matriz debe estructurarse bajo los siguientes campos obligatorios: 

- **ID Requerimiento:** Código único del requisito ligado a la fase de análisis. 

- **Casos de Prueba Asociados:** Vinculación directa entre el requisito y su validación técnica. 

- **Prioridad:** Clasificación (Alta, Media, Baja) para gestión de riesgos. 

- **Estado:** (Activo, Inactivo, Cancelado) para seguimiento del ciclo de vida. 

- **Situación del Requerimiento:** (En espera, Entregado, Aceptado) para control de avance. 

## **4. Criterios de Aceptación** 

Para declarar el prototipo como apto para producción, se deben cumplir los siguientes hitos de calidad: 

1. **Cobertura de Modelo:** 100% de los estados y transiciones del modelo EFSM visitados durante la ejecución de las pruebas. 

2. **Integridad de Trazabilidad:** Matriz de trazabilidad (RTM) completa sin requisitos huérfanos. 

3. **Certificación Humana:** Validación técnica de los casos generados por IA para descartar repeticiones innecesarias o inconsistencias lógicas. 

