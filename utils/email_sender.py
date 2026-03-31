# utils/email_sender.py
# -*- coding: utf-8 -*-
"""
Módulo para envío de corrios electrónicos desde el formulario de contacto.
Utiliza SMTP de Gmail con credenciales desde variables de entorno.
"""

import html
import logging
import os
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

logger = logging.getLogger(__name__)

# Cargar variables de entorno
load_dotenv()

def send_contact_email(nombre: str, email_remitente: str, asunto_tipo: str, mensaje: str) -> tuple[bool, str]:
    """
    Envía un correo electrónico desde el formulario de contacto.
    
    Args:
        nombre: Nombre del remitente
        email_remitente: Correo electrónico del remitente
        asunto_tipo: Tipo de asunto (categoría)
        mensaje: Cuerpo del mensaje
        
    Returns:
        tuple: (éxito: bool, mensaje_respuesta: str)
    """
    
    # Variables de entorno requeridas
    GMAIL_USER = os.getenv("GMAIL_USER", "")
    GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD", "")
    DESTINATARIO = "alexi.fs341@gmail.com"
    
    # Si no hay credenciales configuradas, retornar error
    if not GMAIL_USER or not GMAIL_PASSWORD:
        return False, (
            "⚠️ Configuración de correo no disponible en este momento. "
            "Por favor, contacta directamente a: alexi.fs341@gmail.com"
        )
    
    try:
        # Sanitizar entradas para evitar inyección HTML en el cuerpo del correo
        safe_nombre = html.escape(nombre.strip())
        safe_email = html.escape(email_remitente.strip())
        safe_asunto = html.escape(asunto_tipo.strip())
        safe_mensaje = html.escape(mensaje.strip())

        # Crear mensaje
        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"[CONTACTO] {safe_asunto}"
        msg["From"] = GMAIL_USER
        msg["To"] = DESTINATARIO
        msg["Reply-To"] = safe_email
        
        # Cuerpo del mensaje en HTML
        fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        html_body = f"""
        <html>
            <body style="font-family: Inter, Segoe UI, Roboto, Arial, sans-serif; background-color: #F8FAFC; padding: 20px;">
                <div style="max-width: 600px; margin: 0 auto; background-color: #FFFFFF; padding: 30px; border-radius: 12px; border: 1px solid #CBD5E1; box-shadow: 0 8px 20px rgba(15,23,42,0.08);">
                    <h2 style="color: #0E7490; border-bottom: 2px solid #0E7490; padding-bottom: 10px;">
                        📬 Nuevo Mensaje de Contacto
                    </h2>
                    
                    <div style="margin: 20px 0;">
                        <p><strong style="color: #0F172A;">📝 Nombre:</strong> {safe_nombre}</p>
                        <p><strong style="color: #0F172A;">📧 Correo:</strong> <a href="mailto:{safe_email}">{safe_email}</a></p>
                        <p><strong style="color: #0F172A;">📌 Asunto:</strong> {safe_asunto}</p>
                        <p><strong style="color: #0F172A;">📅 Fecha/Hora:</strong> {fecha_hora}</p>
                    </div>
                    
                    <hr style="border: none; border-top: 1px solid #CBD5E1; margin: 20px 0;">
                    
                    <div style="margin: 20px 0; white-space: pre-wrap; line-height: 1.6; color: #475569;">
                        <strong>Mensaje:</strong>
                        <p>{safe_mensaje}</p>
                    </div>
                    
                    <hr style="border: none; border-top: 1px solid #CBD5E1; margin: 20px 0;">
                    
                    <p style="font-size: 0.9rem; color: #475569; text-align: center;">
                        Este correo fue enviado desde el formulario de contacto del CV digital.
                    </p>
                </div>
            </body>
        </html>
        """
        
        # Versión texto plano
        text_body = f"""
Nuevo Mensaje de Contacto
========================

Nombre: {safe_nombre}
Correo: {safe_email}
Asunto: {safe_asunto}
Fecha/Hora: {fecha_hora}

---

Mensaje:
{safe_mensaje}
        """
        
        # Adjuntar ambas versiones
        msg.attach(MIMEText(text_body, "plain"))
        msg.attach(MIMEText(html_body, "html"))
        
        # Conectar a Gmail SMTP y enviar
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(GMAIL_USER, GMAIL_PASSWORD)
            server.sendmail(GMAIL_USER, DESTINATARIO, msg.as_string())
        
        return True, f"✅ Mensaje enviado exitosamente a {DESTINATARIO}"
        
    except smtplib.SMTPAuthenticationError:
        logger.exception("Error de autenticación SMTP al enviar correo de contacto")
        return False, (
            "❌ Error de autenticación. Las credenciales de Gmail son incorrectas. "
            "Verifica GMAIL_USER y GMAIL_PASSWORD en variables de entorno."
        )
    except smtplib.SMTPException as e:
        logger.exception("Error SMTP al enviar correo de contacto")
        return False, f"❌ Error SMTP: {str(e)}"
    except Exception:
        logger.exception("Error inesperado al enviar correo de contacto")
        return False, "❌ No fue posible enviar el mensaje en este momento. Intenta nuevamente más tarde."
