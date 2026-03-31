"""Servicio de validación y envío de mensajes de contacto."""

import re
from dataclasses import dataclass

from utils.email_sender import send_contact_email

EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
MAX_NOMBRE_LEN = 80
MAX_MENSAJE_LEN = 1500


@dataclass(frozen=True)
class ContactSubmission:
    nombre: str
    email: str
    asunto: str
    mensaje: str


def validate_contact_input(nombre: str, email: str, mensaje: str) -> str | None:
    """Retorna mensaje de error si hay validaciones fallidas, o None si es válido."""
    nombre_limpio = nombre.strip()
    email_limpio = email.strip()
    mensaje_limpio = mensaje.strip()

    if not nombre_limpio or not email_limpio or not mensaje_limpio:
        return "❌ Por favor completa todos los campos."
    if len(nombre_limpio) > MAX_NOMBRE_LEN:
        return f"❌ El nombre no puede superar {MAX_NOMBRE_LEN} caracteres."
    if not EMAIL_REGEX.match(email_limpio):
        return "❌ Ingresa un correo electrónico válido."
    if len(mensaje_limpio) > MAX_MENSAJE_LEN:
        return f"❌ El mensaje no puede superar {MAX_MENSAJE_LEN} caracteres."
    return None


def submit_contact_form(nombre: str, email: str, asunto: str, mensaje: str) -> tuple[bool, str]:
    """Valida y envía un mensaje de contacto."""
    validation_error = validate_contact_input(nombre, email, mensaje)
    if validation_error:
        return False, validation_error

    submission = ContactSubmission(
        nombre=nombre.strip(),
        email=email.strip(),
        asunto=asunto.strip(),
        mensaje=mensaje.strip(),
    )
    return send_contact_email(
        submission.nombre,
        submission.email,
        submission.asunto,
        submission.mensaje,
    )

