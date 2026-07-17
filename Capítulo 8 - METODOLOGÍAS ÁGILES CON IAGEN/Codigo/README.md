# 🤖 AI Kanban Co-Pilot

**Simulador de tablero híbrido Scrum–Kanban potenciado por un motor de IA para la optimización del flujo de trabajo.**

Aplicación de escritorio construida con **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)**, evolución de un simulador de backend en Python (`AgileBoardSimulator`) hacia una herramienta visual moderna cuyo eje central es un **AI Co-Pilot**: un panel que analiza el tablero en tiempo real y emite recomendaciones para reducir el *Lead Time* del equipo, respetando los límites de trabajo en progreso (WIP) y las reglas de flujo de Kanban.

---

## 📋 Tabla de contenido

1. [Características principales](#-características-principales)
2. [Requisitos previos](#-requisitos-previos)
3. [Instalación paso a paso](#-instalación-paso-a-paso)
4. [Ejecución de la aplicación](#-ejecución-de-la-aplicación)
5. [Guía de uso rápido](#-guía-de-uso-rápido)
6. [Cómo el AI Co-Pilot optimiza el flujo](#-cómo-el-ai-co-pilot-optimiza-el-flujo)
7. [Pruebas unitarias](#-pruebas-unitarias)
8. [Estructura del código](#-estructura-del-código)
9. [Solución de problemas](#-solución-de-problemas)

---

## ✨ Características principales

- **Tablero Kanban visual** con 4 columnas (`Backlog`, `En progreso`, `En revisión`, `Terminado`), tarjetas redondeadas y semáforo de límites WIP (🟢 saludable / 🟡 cerca del límite / 🔴 saturado).
- **AI Co-Pilot en tiempo real**: panel dedicado que se recalcula automáticamente ante cualquier cambio en el tablero y presenta tarjetas de notificación clasificadas por urgencia: **Crítico**, **Advertencia** y **Optimización de Flujo**.
- **Reglas Kanban aplicadas por la IA**:
  - Bloquea el intento de jalar nuevas historias del *Backlog* mientras existan tareas bloqueadas en curso ("deja de empezar, empieza a terminar").
  - Detecta cuellos de botella al alcanzar el límite WIP de una columna.
  - Identifica tareas de seguridad (`DAST`) retenidas en "En revisión" y exige su despacho prioritario.
- **Tarjetas de tarea dinámicas**: rojas si están bloqueadas, moradas/azules si son de seguridad (DAST), con botones para moverlas o bloquearlas.
- **Configuración de límites WIP** en vivo desde la barra lateral.
- **Consola de auditoría y pruebas**: ejecuta la suite de `unittest` del backend directamente desde la interfaz, de forma transparente.

---

## 🧰 Requisitos previos

- **Python 3.9 o superior** (recomendado 3.10+).
- Acceso a una interfaz gráfica (Windows, macOS o un entorno Linux de escritorio con servidor X / Wayland).
- Conexión a internet solo para la instalación de dependencias (`pip`).

Verifica tu versión de Python:

```bash
python3 --version
```

---

## ⚙️ Instalación paso a paso

### 1. Descarga el proyecto

Coloca `agile_kanban_ai_copilot.py` y este `README.md` en una misma carpeta, por ejemplo `ai-kanban-copilot/`.

```bash
mkdir ai-kanban-copilot
cd ai-kanban-copilot
# copia aquí agile_kanban_ai_copilot.py y README.md
```

### 2. Crea el entorno virtual (`venv`)

**Windows (PowerShell o CMD):**

```powershell
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

> Sabrás que el entorno está activo porque tu terminal mostrará el prefijo `(venv)` antes del prompt.

### 3. Instala las dependencias

Con el entorno virtual activado:

```bash
pip install --upgrade pip
pip install customtkinter
```

> 💡 En algunas distribuciones de Linux, Tkinter (dependencia base de CustomTkinter) no viene incluido con Python y debe instalarse aparte a nivel de sistema operativo:
> - **Ubuntu / Debian:** `sudo apt-get install python3-tk`
> - **Fedora:** `sudo dnf install python3-tkinter`
> - **Arch:** `sudo pacman -S tk`
>
> En Windows y macOS, Tkinter ya viene incluido con el instalador oficial de Python.

### 4. (Opcional) Congela las dependencias

Si quieres versionar el entorno para el equipo:

```bash
pip freeze > requirements.txt
```

Y para que otro integrante del equipo replique el entorno:

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecución de la aplicación

Con el entorno virtual activado y las dependencias instaladas:

**Windows:**

```powershell
python agile_kanban_ai_copilot.py
```

**macOS / Linux:**

```bash
python3 agile_kanban_ai_copilot.py
```

Esto abrirá la ventana principal de **AI Kanban Co-Pilot**, con un tablero de demostración precargado (historias de ejemplo, incluyendo una tarea de seguridad DAST).

### Modo CLI (solo pruebas, sin abrir la GUI)

Útil para integrarlo en un pipeline de CI/CD o para validar rápidamente el backend:

```bash
python3 agile_kanban_ai_copilot.py --test
```

Para desactivar el entorno virtual cuando termines:

```bash
deactivate
```

---

## 🚀 Guía de uso rápido

### 1. El tablero Kanban (centro)

- Cada columna muestra su nombre y una insignia de ocupación WIP, por ejemplo `WIP 2/3`.
- La barra bajo el encabezado de cada columna cambia de color: 🟢 verde (flujo saludable), 🟡 amarillo (cerca del límite), 🔴 rojo (límite alcanzado).
- Cada tarjeta de tarea tiene tres botones:
  - `◀` mueve la tarea a la columna anterior.
  - `🔒 / 🔓` marca o desmarca la tarea como bloqueada.
  - `▶` mueve la tarea a la siguiente columna.
- Las tarjetas con el tag `seguridad` (DAST) se distinguen con borde/etiqueta morada 🛡️. Las tareas bloqueadas se pintan de rojo con la etiqueta `🚫 BLOQUEADO`.

### 2. El panel AI Co-Pilot (derecha)

Se actualiza automáticamente después de cada acción sobre el tablero (mover, bloquear, agregar tarea, cambiar límites WIP) y muestra tarjetas de notificación ordenadas por urgencia:

| Nivel | Significado | Ejemplo |
|---|---|---|
| 🔴 **Crítico** | Requiere acción inmediata | Cuello de botella por límite WIP saturado, o hallazgo DAST retenido en revisión |
| 🟡 **Advertencia** | Riesgo próximo | Una columna está a una tarea de saturarse |
| 🟢 **Optimización de Flujo** | Sugerencia de mejora | Hay capacidad disponible para jalar la siguiente historia del Backlog |

El indicador `● EN VIVO` / `● N CRÍTICAS` en la esquina del panel resume el estado general del tablero de un vistazo.

### 3. La barra lateral (izquierda)

- **➕ Nueva tarea**: escribe un título, elige el tag (`general` o `seguridad`) y agrégala al Backlog.
- **⚙️ Límites WIP**: ajusta los límites de "En progreso" y "En revisión" y presiona *Aplicar límites*; el tablero y el AI Co-Pilot se recalculan al instante.
- **🧪 Calidad**: ejecuta la suite de pruebas unitarias del backend y observa el resultado en la consola inferior.

### 4. La consola de auditoría (abajo)

Registra cronológicamente cada movimiento, bloqueo, alta de tarea, cambio de configuración y resultado de pruebas, sirviendo como bitácora de trazabilidad del equipo.

---

## 🧠 Cómo el AI Co-Pilot optimiza el flujo

El motor de recomendaciones (`recomendaciones_ia_avanzadas`) implementa cuatro reglas de análisis sobre el estado del tablero, inspiradas en prácticas de gestión de flujo Kanban:

1. **Priorizar el desbloqueo antes que lo nuevo.** Si existen tareas bloqueadas en "En progreso", el motor las señala como crítico y —a nivel de interfaz— impide jalar nuevas historias del Backlog hasta resolverlas. Esto materializa la máxima Kanban *"deja de empezar, empieza a terminar"*.
2. **Semáforo de límites WIP.** Cada columna con límite configurado se evalúa contra su ocupación actual: al llegar al límite se marca como cuello de botella crítico; al estar a una tarea de distancia, como advertencia temprana.
3. **Seguridad primero.** Las tareas con tag `seguridad` (por ejemplo, escaneos DAST) que permanecen en "En revisión" generan una alerta crítica, ya que retenerlas incrementa el riesgo de desplegar vulnerabilidades sin remediar.
4. **Sugerencias de optimización.** Cuando no hay bloqueos ni saturación, el motor identifica capacidad disponible y sugiere activamente avanzar la siguiente historia priorizada, manteniendo el flujo continuo y el Lead Time bajo control.

Esto convierte al AI Co-Pilot en un facilitador constante de las ceremonias de flujo: el equipo no necesita interpretar manualmente el tablero, ya que la IA traduce su estado en directrices accionables y priorizadas.

---

## ✅ Pruebas unitarias

El backend conserva y amplía las pruebas originales del `AgileBoardSimulator`, verificando:

- `test_01_respeta_limite_wip`: el tablero rechaza mover una tarea a una columna que ya alcanzó su límite WIP.
- `test_02_recomendacion_por_tarea_bloqueada`: el motor de recomendaciones detecta y reporta tareas bloqueadas en "En progreso".

Ejecutarlas es posible de dos formas:

- **Desde la interfaz gráfica:** botón *"Ejecutar pruebas unitarias"* en la barra lateral (sección 🧪 Calidad); el resultado se imprime en la consola inferior.
- **Desde la terminal:**

  ```bash
  python3 agile_kanban_ai_copilot.py --test
  ```

> 📝 **Nota de mantenimiento:** los métodos de prueba se nombran con prefijos numéricos (`test_01_...`, `test_02_...`) para garantizar un orden de ejecución determinista, ya que `unittest` ordena los métodos alfabéticamente y la segunda prueba depende del estado que deja la primera.

---

## 🗂️ Estructura del código

Todo vive en un único archivo, `agile_kanban_ai_copilot.py`, organizado en capas:

```
1. Capa de dominio / backend      → AgileBoardSimulator, Recomendacion, Urgencia
2. Pruebas unitarias               → TestAgileBoardSimulator, ejecutar_pruebas_unitarias()
3. Capa de presentación (UI)       → TaskCard, KanbanColumnWidget, AICoPilotPanel,
                                      RecommendationCard, Sidebar, LogConsole, KanbanAIApp
4. Punto de entrada                → bloque `if __name__ == "__main__":`
```

La lógica de negocio (backend) no importa nada de CustomTkinter, por lo que puede reutilizarse o probarse de forma completamente independiente de la interfaz gráfica.

---

## 🛠️ Solución de problemas

| Problema | Causa probable | Solución |
|---|---|---|
| `ModuleNotFoundError: No module named 'customtkinter'` | No instalaste la dependencia o el entorno virtual no está activo | Verifica `(venv)` en tu prompt y reinstala con `pip install customtkinter` |
| `ModuleNotFoundError: No module named 'tkinter'` (Linux) | Tkinter no viene con tu Python de sistema | Instala el paquete de tu distro, p. ej. `sudo apt-get install python3-tk` |
| La ventana no abre o falla con `TclError: no display` | Estás en un entorno sin interfaz gráfica (servidor remoto, contenedor sin X) | Ejecuta en una máquina con escritorio, o usa el modo `--test` para validar solo el backend |
| Los botones se ven muy pequeños/grandes | Escalado de pantalla del sistema operativo | Ajusta el escalado de tu SO o modifica `app.geometry(...)` en el código |

---

**Hecho con Python + CustomTkinter.** Contribuciones y mejoras al motor de recomendaciones son bienvenidas.
