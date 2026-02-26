# utils/email_sender.py
# -*- coding: utf-8 -*-
"""
Módulo para envío de corrios electrónicos desde el formulario de contacto.
Utiliza SMTP de Gmail con credenciales desde variables de entorno.
"""

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from dotenv import load_dotenv

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
        # Crear mensaje
        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"[CONTACTO] {asunto_tipo}"
        msg["From"] = GMAIL_USER
        msg["To"] = DESTINATARIO
        msg["Reply-To"] = email_remitente
        
        # Cuerpo del mensaje en HTML
        fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        html_body = f"""
        <html>
            <body style="font-family: Arial, sans-serif; background-color: #f8fafc; padding: 20px;">
                <div style="max-width: 600px; margin: 0 auto; background-color: white; padding: 30px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                    <h2 style="color: #0891b2; border-bottom: 2px solid #0891b2; padding-bottom: 10px;">
                        📬 Nuevo Mensaje de Contacto
                    </h2>
                    
                    <div style="margin: 20px 0;">
                        <p><strong style="color: #0f172a;">📝 Nombre:</strong> {nombre}</p>
                        <p><strong style="color: #0f172a;">📧 Correo:</strong> <a href="mailto:{email_remitente}">{email_remitente}</a></p>
                        <p><strong style="color: #0f172a;">📌 Asunto:</strong> {asunto_tipo}</p>
                        <p><strong style="color: #0f172a;">📅 Fecha/Hora:</strong> {fecha_hora}</p>
                    </div>
                    
                    <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 20px 0;">
                    
                    <div style="margin: 20px 0; white-space: pre-wrap; line-height: 1.6; color: #334155;">
                        <strong>Mensaje:</strong>
                        <p>{mensaje}</p>
                    </div>
                    
                    <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 20px 0;">
                    
                    <p style="font-size: 0.9rem; color: #64748b; text-align: center;">
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

Nombre: {nombre}
Correo: {email_remitente}
Asunto: {asunto_tipo}
Fecha/Hora: {fecha_hora}

---

Mensaje:
{mensaje}
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
        return False, (
            "❌ Error de autenticación. Las credenciales de Gmail son incorrectas. "
            "Verifica GMAIL_USER y GMAIL_PASSWORD en variables de entorno."
        )
    except smtplib.SMTPException as e:
        return False, f"❌ Error SMTP: {str(e)}"
    except Exception as e:
        return False, f"❌ Error al enviar correo: {str(e)}"
