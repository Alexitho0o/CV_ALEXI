# Orden de lectura y alcance ATS — 2026-10-12

Control adicional sobre los PDF producidos por el código de la revisión 07203d8, con el comando `python generate_pdf.py --preview --with-ats --no-open`.

- Visual: SHA-256 `94ebcf11d2853bd824f19da1a033fa9f44564fcfa4074b8fc09bf8d5b5d33a46`, 1 página A4, 1.059.839 bytes.
- Lectura ATS: SHA-256 `5152bfebb20af5f58f43fe94b48f29b669354d9e72ca43b370b5e37dde12e566`, 3 páginas A4, 99.831 bytes.

La propiedad `experiencias_in_order` del generador se evalúa con PyMuPDF. No debe interpretarse como una certificación de orden en todos los lectores.

| PDF | PyMuPDF | pypdf | Poppler (pdftotext predeterminado) |
|---|---|---|---|
| Visual A4 | 9 experiencias en orden | 9 experiencias en orden | Recupera todo el contenido, pero reordena algunos bloques |
| LECTURA_ATS | 9 experiencias en orden | 9 experiencias en orden | 9 experiencias en orden |

Las 174 frases de control y las 40 herramientas se recuperaron en ambos documentos mediante los tres motores. Texto recuperable y orden de lectura uniforme son controles diferentes.

Para un portal que analiza el CV automáticamente, se recomienda la copia LECTURA_ATS: una columna, texto visible, sin fotografía ni logos, sin eliminar descripciones ni herramientas, cuerpo de 10 pt. El CV visual conserva una página A4 y su identidad gráfica. No se han probado filtros de una vacante ni un ATS comercial. No se garantiza aceptación universal ni selección.

El QR se decodificó desde la imagen y desde un recorte del PDF a 300 dpi. LinkedIn, teléfono y correo coinciden con data.js; la prueba física con teléfono sobre papel queda pendiente.
