#!/usr/bin/env python3
"""Regenera CONTACTO.png y CONTACTO.vcf sin alterar el JPG original de respaldo."""
from pathlib import Path
import json, subprocess
import qrcode
ROOT=Path(__file__).resolve().parents[1]
code="import {profile} from './src/data.js';console.log(JSON.stringify(profile));"
profile=json.loads(subprocess.check_output(['node','--input-type=module','-e',code],cwd=ROOT,text=True))
url='https://'+profile['linkedin'].replace('linkedin.com','www.linkedin.com',1)
if not url.startswith('https://www.linkedin.com/in/') or '%' in url:
    raise SystemExit('URL LinkedIn no válida: revisar src/data.js.')
# Nombre conservado de la tarjeta CONTACTO.jpg original; teléfono y correo gobernados por data.js.
lines=['BEGIN:VCARD','VERSION:3.0','N:Burgos Flores;Alexi;;;','FN:Alexi Burgos Flores',
       'EMAIL;TYPE=INTERNET:'+profile['email'],'TEL;TYPE=CELL:'+profile['phone'],'URL:'+url,'END:VCARD','']
card='\r\n'.join(lines)
qr=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M,box_size=10,border=4)
qr.add_data(card);qr.make(fit=True)
folder=ROOT/'public/img'
qr.make_image(fill_color='black',back_color='white').save(folder/'CONTACTO.png')
(folder/'CONTACTO.vcf').write_bytes(card.encode('utf-8'))
print(f'QR actualizado: {folder / "CONTACTO.png"}. Borde de seguridad: 4 módulos. URL: {url}')
