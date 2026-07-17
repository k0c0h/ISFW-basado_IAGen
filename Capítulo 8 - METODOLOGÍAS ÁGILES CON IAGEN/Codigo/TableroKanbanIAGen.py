"""
AI Kanban Co-Pilot
==================

Simulador de tablero híbrido Scrum-Kanban potenciado por un motor de
recomendaciones tipo IAGen, presentado como una aplicación de escritorio
moderna construida con CustomTkinter.

El eje central de la aplicación es el panel "AI Co-Pilot": un motor que
analiza el tablero en tiempo real y emite directrices para optimizar el
Lead Time, respetando los límites WIP y las reglas de flujo de Kanban.

Autor: Generado y refinado con asistencia de IA a partir de un
       AgileBoardSimulator base (lógica Scrum-Kanban + pruebas unitarias).
"""

from __future__ import annotations

import io
import unittest
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Tuple

import customtkinter as ctk


# =============================================================================
# 1. CAPA DE DOMINIO / BACKEND (lógica pura, independiente de la UI)
# =============================================================================

# Orden canónico de las columnas del tablero. Las claves internas se
# mantienen SIN tilde ("En revision") para no romper compatibilidad con el
# código y las pruebas unitarias originales; la UI se encarga de mostrar
# la etiqueta con tilde ("En revisión") al usuario.
COLUMN_ORDER: List[str] = ["Backlog", "En progreso", "En revision", "Terminado"]

COLUMN_DISPLAY_NAMES: Dict[str, str] = {
    "Backlog": "Backlog",
    "En progreso": "En progreso",
    "En revision": "En revisión",
    "Terminado": "Terminado",
}

TAG_SEGURIDAD = "seguridad"
TAG_GENERAL = "general"


class Urgencia(str, Enum):
    """Nivel de urgencia de una recomendación emitida por el motor de IA."""

    CRITICO = "Crítico"
    ADVERTENCIA = "Advertencia"
    OPTIMIZACION = "Optimización de Flujo"


@dataclass
class Recomendacion:
    """Representa una tarjeta de notificación inteligente del AI Co-Pilot."""

    nivel: Urgencia
    titulo: str
    mensaje: str
    icono: str = "🤖"
    tarea_ids: List[str] = field(default_factory=list)


class AgileBoardSimulator:
    """Simula un tablero híbrido Scrum-Kanban con límites WIP
    y un motor de recomendaciones tipo IAGen enfocado en optimizar
    el flujo de trabajo (Lead Time) del equipo.
    """

    def __init__(self, wip_limits: Dict[str, int]):
        self.columns: Dict[str, List[Dict[str, Any]]] = {
            "Backlog": [],
            "En progreso": [],
            "En revision": [],
            "Terminado": [],
        }
        self.wip_limits = wip_limits
        self.audit_log: List[Dict[str, Any]] = []

    # -------------------------------------------------------------------
    # Operaciones básicas del tablero
    # -------------------------------------------------------------------
    def add_to_backlog(self, task_id: str, title: str, tag: str = TAG_GENERAL) -> None:
        self.columns["Backlog"].append(
            {
                "id": task_id,
                "title": title,
                "tag": tag,
                "blocked": False,
            }
        )

    def move_task(self, task_id: str, origin: str, destino: str) -> bool:
        limite = self.wip_limits.get(destino)

        if limite is not None and len(self.columns[destino]) >= limite:
            self._log(task_id, origin, destino, aceptado=False)
            return False

        tarea = next(
            (t for t in self.columns[origin] if t["id"] == task_id),
            None,
        )

        if tarea is None:
            raise ValueError(f"Tarea {task_id} no existe en {origin}")

        self.columns[origin].remove(tarea)
        self.columns[destino].append(tarea)

        self._log(task_id, origin, destino, aceptado=True)

        return True

    def flag_blocked(self, task_id: str) -> None:
        for columna in self.columns.values():
            for tarea in columna:
                if tarea["id"] == task_id:
                    tarea["blocked"] = True

    def unflag_blocked(self, task_id: str) -> None:
        for columna in self.columns.values():
            for tarea in columna:
                if tarea["id"] == task_id:
                    tarea["blocked"] = False

    def find_task(self, task_id: str) -> Optional[Dict[str, Any]]:
        for columna in self.columns.values():
            for tarea in columna:
                if tarea["id"] == task_id:
                    return tarea
        return None

    def find_task_column(self, task_id: str) -> Optional[str]:
        for nombre_columna, tareas in self.columns.items():
            if any(t["id"] == task_id for t in tareas):
                return nombre_columna
        return None

    def _log(self, task_id: str, origin: str, destino: str, aceptado: bool) -> None:
        self.audit_log.append(
            {
                "timestamp": datetime.now().isoformat(timespec="seconds"),
                "task_id": task_id,
                "origin": origin,
                "destino": destino,
                "aceptado": aceptado,
            }
        )

    # -------------------------------------------------------------------
    # Motor de recomendaciones IAGen (versión original — se conserva
    # intacta para no romper las pruebas unitarias existentes).
    # -------------------------------------------------------------------
    def recomendaciones_ia(self) -> List[str]:
        """Motor simple que emula sugerencias de una IAGen."""

        sugerencias = []

        bloqueadas = [
            t for t in self.columns["En progreso"]
            if t["blocked"]
        ]

        if bloqueadas:
            nombres = ", ".join(t["title"] for t in bloqueadas)

            sugerencias.append(
                f"Priorizar el desbloqueo de: {nombres} antes de iniciar nuevas tareas."
            )

        for columna, limite in self.wip_limits.items():
            ocupacion = len(self.columns.get(columna, []))

            if limite is not None and ocupacion >= limite:
                sugerencias.append(
                    f"La columna '{columna}' alcanzó su límite WIP ({limite}); "
                    "evitar mover nuevas tareas hasta liberar espacio."
                )

        seguridad = [
            t for t in self.columns["En revision"]
            if t["tag"] == TAG_SEGURIDAD
        ]

        if seguridad:
            sugerencias.append(
                "Generar resumen de hallazgos de seguridad (DAST) antes del sprint review."
            )

        if not sugerencias:
            sugerencias.append(
                "El flujo del tablero es saludable; sin acciones urgentes."
            )

        return sugerencias

    # -------------------------------------------------------------------
    # Motor de recomendaciones IAGen — versión avanzada para el AI Co-Pilot
    # -------------------------------------------------------------------
    def recomendaciones_ia_avanzadas(self) -> List[Recomendacion]:
        """Analiza el estado del tablero y produce recomendaciones
        clasificadas por urgencia (Crítico / Advertencia / Optimización
        de Flujo), pensadas para reducir el Lead Time del equipo.
        """

        recomendaciones: List[Recomendacion] = []

        # 1. Regla Kanban: "Deja de empezar, empieza a terminar"
        bloqueadas = [t for t in self.columns["En progreso"] if t["blocked"]]
        if bloqueadas:
            nombres = ", ".join(t["title"] for t in bloqueadas)
            recomendaciones.append(
                Recomendacion(
                    nivel=Urgencia.CRITICO,
                    titulo="Tareas bloqueadas retienen el flujo",
                    mensaje=(
                        f"Prioriza desbloquear: {nombres}. Regla Kanban: "
                        "\"deja de empezar, empieza a terminar\" — no jales "
                        "nuevas historias del Backlog hasta resolver esto."
                    ),
                    icono="🚫",
                    tarea_ids=[t["id"] for t in bloqueadas],
                )
            )

        # 2. Semáforo de límites WIP por columna
        for columna, limite in self.wip_limits.items():
            if limite is None:
                continue

            ocupacion = len(self.columns.get(columna, []))
            nombre = COLUMN_DISPLAY_NAMES.get(columna, columna)

            if ocupacion >= limite:
                recomendaciones.append(
                    Recomendacion(
                        nivel=Urgencia.CRITICO,
                        titulo=f"Cuello de botella en '{nombre}'",
                        mensaje=(
                            f"La columna alcanzó su límite WIP ({ocupacion}/{limite}). "
                            "Evita mover nuevas tareas; enfoca al equipo en terminar "
                            "lo que ya está en curso para restaurar el flujo."
                        ),
                        icono="🛑",
                    )
                )
            elif limite > 1 and ocupacion >= limite - 1:
                recomendaciones.append(
                    Recomendacion(
                        nivel=Urgencia.ADVERTENCIA,
                        titulo=f"'{nombre}' cerca del límite WIP",
                        mensaje=(
                            f"Ocupación actual {ocupacion}/{limite}. Considera cerrar "
                            "tareas en curso antes de aceptar una nueva para evitar "
                            "saturar la columna."
                        ),
                        icono="⚠️",
                    )
                )

        # 3. Hallazgos de seguridad (DAST) retenidos en revisión
        seguridad = [
            t for t in self.columns["En revision"] if t["tag"] == TAG_SEGURIDAD
        ]
        if seguridad:
            nombres = ", ".join(t["title"] for t in seguridad)
            recomendaciones.append(
                Recomendacion(
                    nivel=Urgencia.CRITICO,
                    titulo="Hallazgos de seguridad (DAST) pendientes",
                    mensaje=(
                        f"Despacha de inmediato: {nombres}. Retener tareas de "
                        "seguridad en revisión incrementa el riesgo de desplegar "
                        "vulnerabilidades sin remediar."
                    ),
                    icono="🛡️",
                    tarea_ids=[t["id"] for t in seguridad],
                )
            )

        # 4. Optimización de flujo: hay capacidad y nada bloquea el avance
        limite_progreso = self.wip_limits.get("En progreso")
        ocupacion_progreso = len(self.columns["En progreso"])
        hay_capacidad = limite_progreso is None or ocupacion_progreso < limite_progreso

        if not bloqueadas and hay_capacidad and self.columns["Backlog"]:
            recomendaciones.append(
                Recomendacion(
                    nivel=Urgencia.OPTIMIZACION,
                    titulo="Capacidad disponible para avanzar",
                    mensaje=(
                        "No hay bloqueos activos y 'En progreso' tiene espacio. "
                        "Puedes jalar la siguiente historia priorizada del Backlog "
                        "para mantener el Lead Time bajo control."
                    ),
                    icono="✅",
                )
            )

        if not recomendaciones:
            recomendaciones.append(
                Recomendacion(
                    nivel=Urgencia.OPTIMIZACION,
                    titulo="Flujo estable",
                    mensaje="El tablero está saludable; sin acciones urgentes por el momento.",
                    icono="✨",
                )
            )

        return recomendaciones

    def puede_jalar_nueva_historia(self) -> Tuple[bool, str]:
        """Aplica la regla Kanban de priorizar el desbloqueo de tareas
        existentes antes de permitir jalar nuevas historias del Backlog.
        """
        bloqueadas = [t for t in self.columns["En progreso"] if t["blocked"]]
        if bloqueadas:
            nombres = ", ".join(t["title"] for t in bloqueadas)
            return False, (
                f"Regla Kanban activa: desbloquea primero {nombres} antes de "
                "iniciar una nueva historia."
            )
        return True, "OK"

    def wip_status(self, columna: str) -> str:
        """Devuelve el estado semafórico ('verde', 'amarillo', 'rojo',
        'neutral') de una columna en función de su ocupación vs. límite WIP.
        """
        limite = self.wip_limits.get(columna)
        if limite is None:
            return "neutral"

        ocupacion = len(self.columns.get(columna, []))
        if ocupacion >= limite:
            return "rojo"
        if limite > 1 and ocupacion >= limite - 1:
            return "amarillo"
        return "verde"

    def generate_report(self) -> Dict[str, Any]:
        return {
            "estado_tablero": {
                col: [t["id"] for t in tareas]
                for col, tareas in self.columns.items()
            },
            "recomendaciones": self.recomendaciones_ia(),
            "movimientos_registrados": len(self.audit_log),
        }


# =============================================================================
# 2. PRUEBAS UNITARIAS (backend) — se conservan y se ejecutan también
#    de forma transparente desde la interfaz gráfica (botón "Ejecutar
#    Pruebas Unitarias").
# =============================================================================
class TestAgileBoardSimulator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.board = AgileBoardSimulator(
            wip_limits={
                "En progreso": 2,
                "En revision": 2,
            }
        )

        cls.board.add_to_backlog(
            "T1",
            "Diseñar API de autenticación"
        )

        cls.board.add_to_backlog(
            "T2",
            "Configurar pipeline CI/CD"
        )

        cls.board.add_to_backlog(
            "T3",
            "Escaneo DAST del módulo de login",
            tag="seguridad"
        )

    # NOTA DE MANTENIMIENTO: los métodos se numeran (01, 02) para
    # garantizar un orden de ejecución determinista. TestLoader ordena
    # los métodos alfabéticamente por nombre; sin el prefijo numérico,
    # "test_recomendacion_por_tarea_bloqueada" se ejecutaría ANTES que
    # "test_respeta_limite_wip" (la 'c' de "recomendacion" precede a la
    # 's' de "respeta"), rompiendo la dependencia de estado que esta
    # prueba necesita (T1 debe estar ya en "En progreso").

    def test_01_respeta_limite_wip(self):

        self.assertTrue(
            self.board.move_task(
                "T1",
                "Backlog",
                "En progreso"
            )
        )

        self.assertTrue(
            self.board.move_task(
                "T2",
                "Backlog",
                "En progreso"
            )
        )

        self.assertFalse(
            self.board.move_task(
                "T3",
                "Backlog",
                "En progreso"
            )
        )

        aceptado = self.board.audit_log[-1]["aceptado"]

        self.assertFalse(aceptado)

        self.assertEqual(
            len(self.board.columns["En progreso"]),
            2
        )

    def test_02_recomendacion_por_tarea_bloqueada(self):

        self.board.flag_blocked("T1")

        recomendaciones = self.board.recomendaciones_ia()

        self.assertTrue(
            any(
                "Diseñar API de autenticación" in r
                for r in recomendaciones
            )
        )


def ejecutar_pruebas_unitarias() -> str:
    """Ejecuta la suite de pruebas y devuelve el reporte como texto,
    para mostrarlo de forma transparente en la consola de la UI.
    """
    buffer = io.StringIO()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAgileBoardSimulator)
    runner = unittest.TextTestRunner(stream=buffer, verbosity=2)
    resultado = runner.run(suite)

    resumen = (
        f"\n{'=' * 60}\n"
        f"Pruebas ejecutadas: {resultado.testsRun}  |  "
        f"Fallos: {len(resultado.failures)}  |  "
        f"Errores: {len(resultado.errors)}\n"
        f"Estado: {'✅ TODO OK' if resultado.wasSuccessful() else '❌ REVISAR FALLOS'}\n"
        f"{'=' * 60}\n"
    )
    return buffer.getvalue() + resumen


# =============================================================================
# 3. CAPA DE PRESENTACIÓN (CustomTkinter) — Aplicación de escritorio
# =============================================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Paleta de colores centralizada (tema oscuro moderno, estilo "AI Co-Pilot").
PALETTE: Dict[str, str] = {
    "bg": "#0f1220",
    "surface": "#171b2e",
    "surface_alt": "#1f2440",
    "surface_card": "#242a4a",
    "border": "#333a5c",
    "text": "#e9ebfa",
    "text_dim": "#9aa0c3",
    "accent": "#7aa2f7",
    "accent_soft": "#2b3466",
    "success": "#4ade80",
    "success_soft": "#173a2b",
    "warning": "#facc15",
    "warning_soft": "#3a3312",
    "danger": "#f87171",
    "danger_soft": "#3a1f22",
    "security": "#b48ce8",
    "security_soft": "#2b2143",
}

URGENCIA_COLOR: Dict[Urgencia, str] = {
    Urgencia.CRITICO: PALETTE["danger"],
    Urgencia.ADVERTENCIA: PALETTE["warning"],
    Urgencia.OPTIMIZACION: PALETTE["success"],
}

URGENCIA_SOFT: Dict[Urgencia, str] = {
    Urgencia.CRITICO: PALETTE["danger_soft"],
    Urgencia.ADVERTENCIA: PALETTE["warning_soft"],
    Urgencia.OPTIMIZACION: PALETTE["success_soft"],
}

URGENCIA_ORDEN: Dict[Urgencia, int] = {
    Urgencia.CRITICO: 0,
    Urgencia.ADVERTENCIA: 1,
    Urgencia.OPTIMIZACION: 2,
}

WIP_COLOR: Dict[str, str] = {
    "rojo": PALETTE["danger"],
    "amarillo": PALETTE["warning"],
    "verde": PALETTE["success"],
    "neutral": PALETTE["text_dim"],
}


def _pill(master, text: str, color: str, soft_color: Optional[str] = None,
          font_size: int = 11) -> ctk.CTkLabel:
    """Crea una etiqueta tipo 'pill' (badge) redondeada."""
    return ctk.CTkLabel(
        master,
        text=text,
        text_color=color,
        fg_color=soft_color or PALETTE["surface_alt"],
        corner_radius=10,
        font=ctk.CTkFont(size=font_size, weight="bold"),
        padx=8,
        pady=2,
    )


class ConfirmDialog(ctk.CTkToplevel):
    """Modal ligero para advertencias del motor de IA / reglas Kanban."""

    def __init__(self, master, title: str, message: str, kind: str = "warning"):
        super().__init__(master)
        self.title(title)
        self.geometry("420x220")
        self.resizable(False, False)
        self.configure(fg_color=PALETTE["surface"])
        self.transient(master)
        self.grab_set()

        color = PALETTE["danger"] if kind == "warning" else PALETTE["accent"]
        icon = "🚫" if kind == "warning" else "ℹ️"

        ctk.CTkLabel(
            self, text=icon, font=ctk.CTkFont(size=32),
        ).pack(pady=(20, 4))

        ctk.CTkLabel(
            self, text=title, text_color=color,
            font=ctk.CTkFont(size=15, weight="bold"), wraplength=380,
        ).pack(pady=(0, 8))

        ctk.CTkLabel(
            self, text=message, text_color=PALETTE["text"],
            font=ctk.CTkFont(size=12), wraplength=380, justify="center",
        ).pack(padx=16, pady=(0, 16))

        ctk.CTkButton(
            self, text="Entendido", fg_color=color, hover_color=color,
            command=self.destroy, width=120,
        ).pack(pady=(0, 16))

        self.after(10, self.focus_force)


class TaskCard(ctk.CTkFrame):
    """Tarjeta visual de una tarea del tablero Kanban."""

    def __init__(self, master, task: Dict[str, Any], column: str, app: "KanbanAIApp"):
        is_blocked = bool(task.get("blocked"))
        is_security = task.get("tag") == TAG_SEGURIDAD

        if is_blocked:
            border_color = PALETTE["danger"]
            fg_color = PALETTE["danger_soft"]
        elif is_security:
            border_color = PALETTE["security"]
            fg_color = PALETTE["security_soft"]
        else:
            border_color = PALETTE["border"]
            fg_color = PALETTE["surface_card"]

        super().__init__(
            master, corner_radius=14, border_width=2,
            border_color=border_color, fg_color=fg_color,
        )

        self.app = app
        self.task = task
        self.column = column

        self.grid_columnconfigure(0, weight=1)

        # --- Encabezado: id + badges ---
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 2))
        header.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            header, text=task["id"], text_color=PALETTE["text_dim"],
            font=ctk.CTkFont(size=10, weight="bold"),
        ).grid(row=0, column=0, sticky="w")

        badges = ctk.CTkFrame(self, fg_color="transparent")
        badges.grid(row=1, column=0, sticky="w", padx=10)
        col_idx = 0
        if is_security:
            _pill(badges, "🛡 DAST/Seguridad", PALETTE["security"],
                  PALETTE["security_soft"]).grid(row=0, column=col_idx, padx=(0, 4))
            col_idx += 1
        if is_blocked:
            _pill(badges, "🚫 BLOQUEADO", PALETTE["danger"],
                  PALETTE["danger_soft"]).grid(row=0, column=col_idx, padx=(0, 4))

        # --- Título ---
        ctk.CTkLabel(
            self, text=task["title"], text_color=PALETTE["text"],
            font=ctk.CTkFont(size=13, weight="bold"),
            wraplength=190, justify="left", anchor="w",
        ).grid(row=2, column=0, sticky="ew", padx=10, pady=(6, 10))

        # --- Botonera de acciones ---
        actions = ctk.CTkFrame(self, fg_color="transparent")
        actions.grid(row=3, column=0, sticky="ew", padx=8, pady=(0, 10))
        actions.grid_columnconfigure((0, 1, 2), weight=1)

        prev_col = self.app.prev_column(column)
        next_col = self.app.next_column(column)

        btn_prev = ctk.CTkButton(
            actions, text="◀", width=32, height=28,
            fg_color=PALETTE["surface_alt"], hover_color=PALETTE["accent_soft"],
            state="normal" if prev_col else "disabled",
            command=lambda: self.app.handle_move(task["id"], column, prev_col),
        )
        btn_prev.grid(row=0, column=0, padx=2)

        lock_icon = "🔓" if is_blocked else "🔒"
        btn_lock = ctk.CTkButton(
            actions, text=lock_icon, width=32, height=28,
            fg_color=PALETTE["surface_alt"], hover_color=PALETTE["danger_soft"],
            command=lambda: self.app.handle_toggle_block(task["id"]),
        )
        btn_lock.grid(row=0, column=1, padx=2)

        btn_next = ctk.CTkButton(
            actions, text="▶", width=32, height=28,
            fg_color=PALETTE["accent_soft"], hover_color=PALETTE["accent"],
            state="normal" if next_col else "disabled",
            command=lambda: self.app.handle_move(task["id"], column, next_col),
        )
        btn_next.grid(row=0, column=2, padx=2)


class KanbanColumnWidget(ctk.CTkFrame):
    """Columna del tablero Kanban con encabezado semafórico y tarjetas."""

    def __init__(self, master, column_key: str, app: "KanbanAIApp"):
        super().__init__(master, corner_radius=18, fg_color=PALETTE["surface"],
                          border_width=1, border_color=PALETTE["border"])
        self.column_key = column_key
        self.app = app

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # --- Encabezado ---
        self.header = ctk.CTkFrame(self, fg_color="transparent")
        self.header.grid(row=0, column=0, sticky="ew", padx=14, pady=(14, 6))
        self.header.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(
            self.header, text=COLUMN_DISPLAY_NAMES.get(column_key, column_key),
            text_color=PALETTE["text"], font=ctk.CTkFont(size=15, weight="bold"),
        )
        self.title_label.grid(row=0, column=0, sticky="w")

        self.wip_badge = ctk.CTkLabel(
            self.header, text="", corner_radius=10, padx=8, pady=2,
            font=ctk.CTkFont(size=11, weight="bold"),
        )
        self.wip_badge.grid(row=0, column=1, sticky="e")

        self.semaphore_bar = ctk.CTkFrame(self, height=4, corner_radius=2)
        self.semaphore_bar.grid(row=1, column=0, sticky="new", padx=14)
        self.semaphore_bar.grid_propagate(False)
        self.semaphore_bar.configure(height=4)

        # --- Contenedor scrollable de tarjetas ---
        self.cards_container = ctk.CTkScrollableFrame(
            self, fg_color="transparent",
        )
        self.cards_container.grid(row=2, column=0, sticky="nsew", padx=8, pady=(8, 14))
        self.grid_rowconfigure(2, weight=1)

    def refresh(self):
        for widget in self.cards_container.winfo_children():
            widget.destroy()

        tasks = self.app.board.columns[self.column_key]
        for task in tasks:
            card = TaskCard(self.cards_container, task, self.column_key, self.app)
            card.pack(fill="x", padx=4, pady=6)

        if not tasks:
            ctk.CTkLabel(
                self.cards_container, text="— sin tareas —",
                text_color=PALETTE["text_dim"], font=ctk.CTkFont(size=11, slant="italic"),
            ).pack(pady=20)

        limite = self.app.board.wip_limits.get(self.column_key)
        estado = self.app.board.wip_status(self.column_key)
        color = WIP_COLOR[estado]

        if limite is None:
            self.wip_badge.configure(text=f"{len(tasks)} / ∞",
                                      text_color=PALETTE["text_dim"],
                                      fg_color=PALETTE["surface_alt"])
        else:
            self.wip_badge.configure(text=f"WIP {len(tasks)}/{limite}",
                                      text_color=color,
                                      fg_color=PALETTE["surface_alt"])

        self.semaphore_bar.configure(fg_color=color if limite else PALETTE["border"])


class RecommendationCard(ctk.CTkFrame):
    """Tarjeta de notificación inteligente del AI Co-Pilot."""

    def __init__(self, master, rec: Recomendacion):
        color = URGENCIA_COLOR[rec.nivel]
        soft = URGENCIA_SOFT[rec.nivel]

        super().__init__(master, corner_radius=12, fg_color=soft,
                          border_width=1, border_color=color)

        self.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(self, text=rec.icono, font=ctk.CTkFont(size=20),
                      fg_color="transparent").grid(row=0, column=0, rowspan=2,
                                                    padx=(12, 6), pady=12)

        _pill(self, rec.nivel.value, color, PALETTE["surface"], font_size=10).grid(
            row=0, column=1, sticky="w", pady=(10, 0)
        )

        ctk.CTkLabel(
            self, text=rec.titulo, text_color=PALETTE["text"],
            font=ctk.CTkFont(size=13, weight="bold"),
            wraplength=260, justify="left", anchor="w",
        ).grid(row=1, column=1, sticky="ew", padx=(0, 10), pady=(4, 0))

        ctk.CTkLabel(
            self, text=rec.mensaje, text_color=PALETTE["text_dim"],
            font=ctk.CTkFont(size=11), wraplength=260, justify="left", anchor="w",
        ).grid(row=2, column=1, sticky="ew", padx=(0, 10), pady=(2, 12))


class AICoPilotPanel(ctk.CTkFrame):
    """Panel central de la aplicación: el 'AI Co-Pilot' para optimización
    del flujo Kanban. Se actualiza automáticamente ante cualquier cambio
    en el tablero.
    """

    def __init__(self, master, app: "KanbanAIApp"):
        super().__init__(master, corner_radius=18, fg_color=PALETTE["surface"],
                          border_width=2, border_color=PALETTE["accent"])
        self.app = app

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", padx=16, pady=(16, 4))
        header.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            header, text="🤖 AI CO-PILOT", text_color=PALETTE["accent"],
            font=ctk.CTkFont(size=17, weight="bold"),
        ).grid(row=0, column=0, sticky="w")

        self.pulse_dot = ctk.CTkLabel(
            header, text="● EN VIVO", text_color=PALETTE["success"],
            font=ctk.CTkFont(size=10, weight="bold"),
        )
        self.pulse_dot.grid(row=0, column=1, sticky="e")

        ctk.CTkLabel(
            self, text="Optimización de flujo Kanban en tiempo real",
            text_color=PALETTE["text_dim"], font=ctk.CTkFont(size=11),
        ).grid(row=1, column=0, sticky="w", padx=16, pady=(0, 10))

        self.list_container = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.list_container.grid(row=2, column=0, sticky="nsew", padx=10, pady=(0, 10))

        self.footer_label = ctk.CTkLabel(
            self, text="", text_color=PALETTE["text_dim"], font=ctk.CTkFont(size=10),
        )
        self.footer_label.grid(row=3, column=0, sticky="w", padx=16, pady=(0, 12))

    def refresh(self):
        for widget in self.list_container.winfo_children():
            widget.destroy()

        recomendaciones = self.app.board.recomendaciones_ia_avanzadas()
        recomendaciones.sort(key=lambda r: URGENCIA_ORDEN[r.nivel])

        n_criticas = sum(1 for r in recomendaciones if r.nivel == Urgencia.CRITICO)

        for rec in recomendaciones:
            card = RecommendationCard(self.list_container, rec)
            card.pack(fill="x", padx=4, pady=6)

        self.pulse_dot.configure(
            text=f"● {n_criticas} CRÍTICAS" if n_criticas else "● FLUJO SALUDABLE",
            text_color=PALETTE["danger"] if n_criticas else PALETTE["success"],
        )
        self.footer_label.configure(
            text=f"Última actualización: {datetime.now().strftime('%H:%M:%S')}"
        )


class Sidebar(ctk.CTkFrame):
    """Barra lateral: alta de tareas y configuración de límites WIP."""

    def __init__(self, master, app: "KanbanAIApp"):
        super().__init__(master, corner_radius=18, fg_color=PALETTE["surface"],
                          border_width=1, border_color=PALETTE["border"], width=260)
        self.app = app
        self.grid_columnconfigure(0, weight=1)
        self.grid_propagate(False)

        # --- Sección: Nueva tarea ---
        ctk.CTkLabel(
            self, text="➕ Nueva tarea", text_color=PALETTE["text"],
            font=ctk.CTkFont(size=14, weight="bold"),
        ).grid(row=0, column=0, sticky="w", padx=16, pady=(18, 6))

        self.title_entry = ctk.CTkEntry(
            self, placeholder_text="Título de la historia...",
            fg_color=PALETTE["surface_alt"], border_color=PALETTE["border"],
        )
        self.title_entry.grid(row=1, column=0, sticky="ew", padx=16, pady=4)

        self.tag_menu = ctk.CTkOptionMenu(
            self, values=[TAG_GENERAL, TAG_SEGURIDAD],
            fg_color=PALETTE["surface_alt"], button_color=PALETTE["accent_soft"],
            button_hover_color=PALETTE["accent"],
        )
        self.tag_menu.grid(row=2, column=0, sticky="ew", padx=16, pady=4)

        ctk.CTkButton(
            self, text="Agregar al Backlog", fg_color=PALETTE["accent"],
            hover_color=PALETTE["accent_soft"], command=self._on_add_task,
        ).grid(row=3, column=0, sticky="ew", padx=16, pady=(4, 18))

        ctk.CTkFrame(self, height=1, fg_color=PALETTE["border"]).grid(
            row=4, column=0, sticky="ew", padx=16, pady=4
        )

        # --- Sección: Configuración WIP ---
        ctk.CTkLabel(
            self, text="⚙️ Límites WIP", text_color=PALETTE["text"],
            font=ctk.CTkFont(size=14, weight="bold"),
        ).grid(row=5, column=0, sticky="w", padx=16, pady=(14, 6))

        row_progreso = ctk.CTkFrame(self, fg_color="transparent")
        row_progreso.grid(row=6, column=0, sticky="ew", padx=16, pady=4)
        row_progreso.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(row_progreso, text="En progreso", text_color=PALETTE["text_dim"],
                      font=ctk.CTkFont(size=11)).grid(row=0, column=0, sticky="w")
        self.wip_progreso_entry = ctk.CTkEntry(row_progreso, width=50,
                                                fg_color=PALETTE["surface_alt"])
        self.wip_progreso_entry.grid(row=0, column=1, sticky="e")

        row_revision = ctk.CTkFrame(self, fg_color="transparent")
        row_revision.grid(row=7, column=0, sticky="ew", padx=16, pady=4)
        row_revision.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(row_revision, text="En revisión", text_color=PALETTE["text_dim"],
                      font=ctk.CTkFont(size=11)).grid(row=0, column=0, sticky="w")
        self.wip_revision_entry = ctk.CTkEntry(row_revision, width=50,
                                                fg_color=PALETTE["surface_alt"])
        self.wip_revision_entry.grid(row=0, column=1, sticky="e")

        ctk.CTkButton(
            self, text="Aplicar límites", fg_color=PALETTE["surface_alt"],
            hover_color=PALETTE["accent_soft"], command=self._on_apply_wip,
        ).grid(row=8, column=0, sticky="ew", padx=16, pady=(6, 18))

        ctk.CTkFrame(self, height=1, fg_color=PALETTE["border"]).grid(
            row=9, column=0, sticky="ew", padx=16, pady=4
        )

        # --- Sección: Pruebas ---
        ctk.CTkLabel(
            self, text="🧪 Calidad", text_color=PALETTE["text"],
            font=ctk.CTkFont(size=14, weight="bold"),
        ).grid(row=10, column=0, sticky="w", padx=16, pady=(14, 6))

        ctk.CTkButton(
            self, text="Ejecutar pruebas unitarias", fg_color=PALETTE["success_soft"],
            text_color=PALETTE["success"], hover_color=PALETTE["success"],
            command=self.app.handle_run_tests,
        ).grid(row=11, column=0, sticky="ew", padx=16, pady=(4, 18))

        self.load_wip_values()

    def load_wip_values(self):
        self.wip_progreso_entry.delete(0, "end")
        self.wip_progreso_entry.insert(0, str(self.app.board.wip_limits.get("En progreso", "")))
        self.wip_revision_entry.delete(0, "end")
        self.wip_revision_entry.insert(0, str(self.app.board.wip_limits.get("En revision", "")))

    def _on_add_task(self):
        title = self.title_entry.get().strip()
        tag = self.tag_menu.get()
        if not title:
            ConfirmDialog(self.app, "Título requerido",
                          "Escribe un título para la nueva historia antes de agregarla.",
                          kind="warning")
            return
        self.app.handle_add_task(title, tag)
        self.title_entry.delete(0, "end")

    def _on_apply_wip(self):
        try:
            nuevo_progreso = int(self.wip_progreso_entry.get())
            nuevo_revision = int(self.wip_revision_entry.get())
            if nuevo_progreso < 1 or nuevo_revision < 1:
                raise ValueError
        except ValueError:
            ConfirmDialog(self.app, "Valor inválido",
                          "Los límites WIP deben ser números enteros positivos.",
                          kind="warning")
            return
        self.app.handle_apply_wip(nuevo_progreso, nuevo_revision)


class LogConsole(ctk.CTkFrame):
    """Consola inferior: historial de auditoría y salida de pruebas unitarias."""

    def __init__(self, master):
        super().__init__(master, corner_radius=14, fg_color=PALETTE["surface"],
                          border_width=1, border_color=PALETTE["border"], height=140)
        self.grid_columnconfigure(0, weight=1)
        self.grid_propagate(False)

        ctk.CTkLabel(
            self, text="📜 Consola de auditoría y pruebas", text_color=PALETTE["text_dim"],
            font=ctk.CTkFont(size=11, weight="bold"),
        ).grid(row=0, column=0, sticky="w", padx=14, pady=(8, 2))

        self.textbox = ctk.CTkTextbox(
            self, fg_color=PALETTE["bg"], text_color=PALETTE["text"],
            font=ctk.CTkFont(size=11, family="Consolas"), wrap="word",
        )
        self.textbox.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))
        self.grid_rowconfigure(1, weight=1)
        self.textbox.configure(state="disabled")

    def log(self, message: str, level: str = "info"):
        prefix = {
            "info": "ℹ️",
            "success": "✅",
            "warning": "⚠️",
            "error": "🚫",
        }.get(level, "ℹ️")

        timestamp = datetime.now().strftime("%H:%M:%S")
        self.textbox.configure(state="normal")
        self.textbox.insert("end", f"[{timestamp}] {prefix} {message}\n")
        self.textbox.configure(state="disabled")
        self.textbox.see("end")

    def log_block(self, text: str):
        self.textbox.configure(state="normal")
        self.textbox.insert("end", text + "\n")
        self.textbox.configure(state="disabled")
        self.textbox.see("end")


class KanbanAIApp(ctk.CTk):
    """Aplicación principal: orquesta el tablero, el AI Co-Pilot,
    la barra lateral y la consola de auditoría.
    """

    def __init__(self):
        super().__init__()

        self.title("AI Kanban Co-Pilot — Simulador Ágil Híbrido Scrum-Kanban")
        self.geometry("1540x880")
        self.minsize(1180, 700)
        self.configure(fg_color=PALETTE["bg"])

        self.board = AgileBoardSimulator(
            wip_limits={"En progreso": 3, "En revision": 2}
        )
        self._task_seq = 0
        self._seed_demo_data()

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self._build_header()

        self.sidebar = Sidebar(self, self)
        self.sidebar.grid(row=1, column=0, sticky="ns", padx=(16, 8), pady=8)

        self.board_area = ctk.CTkFrame(self, fg_color="transparent")
        self.board_area.grid(row=1, column=1, sticky="nsew", padx=8, pady=8)
        self.board_area.grid_rowconfigure(0, weight=1)
        self.board_area.grid_columnconfigure(tuple(range(len(COLUMN_ORDER))), weight=1)

        self.column_widgets: Dict[str, KanbanColumnWidget] = {}
        for idx, column_key in enumerate(COLUMN_ORDER):
            widget = KanbanColumnWidget(self.board_area, column_key, self)
            widget.grid(row=0, column=idx, sticky="nsew", padx=6)
            self.column_widgets[column_key] = widget

        self.ai_panel = AICoPilotPanel(self, self)
        self.ai_panel.grid(row=1, column=2, sticky="nsew", padx=(8, 16), pady=8)

        self.log_console = LogConsole(self)
        self.log_console.grid(row=2, column=0, columnspan=3, sticky="ew", padx=16, pady=(0, 16))

        self.refresh_all()
        self.log_console.log("Aplicación iniciada. Tablero cargado con datos de demostración.", "info")

    # -------------------------------------------------------------------
    # Construcción de UI
    # -------------------------------------------------------------------
    def _build_header(self):
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, columnspan=3, sticky="ew", padx=16, pady=(16, 4))
        header.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            header, text="Tablero Ágil Híbrido Scrum–Kanban",
            text_color=PALETTE["text"], font=ctk.CTkFont(size=22, weight="bold"),
        ).grid(row=0, column=0, sticky="w")

        ctk.CTkLabel(
            header,
            text="El motor de IA analiza el flujo en tiempo real para reducir el Lead Time del equipo.",
            text_color=PALETTE["text_dim"], font=ctk.CTkFont(size=12),
        ).grid(row=1, column=0, sticky="w")

    def _seed_demo_data(self):
        self.board.add_to_backlog(self._new_task_id(), "Diseñar API de autenticación")
        self.board.add_to_backlog(self._new_task_id(), "Configurar pipeline CI/CD")
        self.board.add_to_backlog(self._new_task_id(), "Escaneo DAST del módulo de login",
                                   tag=TAG_SEGURIDAD)
        self.board.add_to_backlog(self._new_task_id(), "Documentar endpoints públicos")

    def _new_task_id(self) -> str:
        self._task_seq += 1
        return f"T{self._task_seq}"

    # -------------------------------------------------------------------
    # Navegación entre columnas
    # -------------------------------------------------------------------
    @staticmethod
    def prev_column(column: str) -> Optional[str]:
        idx = COLUMN_ORDER.index(column)
        return COLUMN_ORDER[idx - 1] if idx > 0 else None

    @staticmethod
    def next_column(column: str) -> Optional[str]:
        idx = COLUMN_ORDER.index(column)
        return COLUMN_ORDER[idx + 1] if idx < len(COLUMN_ORDER) - 1 else None

    # -------------------------------------------------------------------
    # Refresco global de la UI
    # -------------------------------------------------------------------
    def refresh_all(self):
        for widget in self.column_widgets.values():
            widget.refresh()
        self.ai_panel.refresh()

    # -------------------------------------------------------------------
    # Manejadores de eventos (mutan el backend y refrescan la UI)
    # -------------------------------------------------------------------
    def handle_add_task(self, title: str, tag: str):
        task_id = self._new_task_id()
        self.board.add_to_backlog(task_id, title, tag=tag)
        self.log_console.log(f"Tarea {task_id} '{title}' añadida al Backlog (tag={tag}).",
                              "success")
        self.refresh_all()

    def handle_move(self, task_id: str, origin: Optional[str], destino: Optional[str]):
        if origin is None or destino is None:
            return

        # Regla Kanban: priorizar el desbloqueo de tareas existentes antes
        # de permitir jalar nuevas historias del Backlog.
        if origin == "Backlog" and destino == "En progreso":
            permitido, motivo = self.board.puede_jalar_nueva_historia()
            if not permitido:
                self.log_console.log(motivo, "warning")
                ConfirmDialog(self, "Regla Kanban: termina antes de empezar", motivo,
                              kind="warning")
                return

        tarea = self.board.find_task(task_id)
        nombre = tarea["title"] if tarea else task_id

        exito = self.board.move_task(task_id, origin, destino)
        if not exito:
            limite = self.board.wip_limits.get(destino)
            mensaje = (
                f"No se puede mover '{nombre}' a '{COLUMN_DISPLAY_NAMES.get(destino, destino)}': "
                f"límite WIP alcanzado ({limite})."
            )
            self.log_console.log(mensaje, "error")
            ConfirmDialog(self, "Límite WIP alcanzado", mensaje, kind="warning")
            return

        self.log_console.log(
            f"'{nombre}' movida de '{COLUMN_DISPLAY_NAMES.get(origin, origin)}' a "
            f"'{COLUMN_DISPLAY_NAMES.get(destino, destino)}'.", "success"
        )
        self.refresh_all()

    def handle_toggle_block(self, task_id: str):
        tarea = self.board.find_task(task_id)
        if tarea is None:
            return
        if tarea["blocked"]:
            self.board.unflag_blocked(task_id)
            self.log_console.log(f"'{tarea['title']}' fue desbloqueada.", "success")
        else:
            self.board.flag_blocked(task_id)
            self.log_console.log(f"'{tarea['title']}' fue marcada como BLOQUEADA.", "warning")
        self.refresh_all()

    def handle_apply_wip(self, wip_progreso: int, wip_revision: int):
        self.board.wip_limits["En progreso"] = wip_progreso
        self.board.wip_limits["En revision"] = wip_revision
        self.log_console.log(
            f"Límites WIP actualizados → En progreso: {wip_progreso}, En revisión: {wip_revision}.",
            "info",
        )
        self.refresh_all()

    def handle_run_tests(self):
        self.log_console.log("Ejecutando suite de pruebas unitarias (backend)...", "info")
        salida = ejecutar_pruebas_unitarias()
        self.log_console.log_block(salida)


# =============================================================================
# 4. PUNTO DE ENTRADA
# =============================================================================
if __name__ == "__main__":
    import sys

    if "--test" in sys.argv:
        # Modo CLI: ejecuta únicamente las pruebas unitarias del backend,
        # útil para integrarlo en un pipeline de CI sin abrir la GUI.
        print(ejecutar_pruebas_unitarias())
    else:
        app = KanbanAIApp()
        app.mainloop()
