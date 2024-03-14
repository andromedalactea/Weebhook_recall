import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os 
def send_emails( sender_email, sender_password,recipient_email,message ):
    """
    Envía correos electrónicos con un mensaje personalizado, un archivo adjunto y una imagen incrustada.

    Parámetros:
    :param df: DataFrame con las columnas 'name' y 'emails' para cada destinatario.
    :param sender_email: Correo electrónico del remitente.
    :param sender_password: Contraseña de aplicación del remitente.
    :param attachment_path: Ruta al archivo PDF para adjuntar en el correo.
    :param image_path: Ruta a la imagen para incrustar en el correo.

    Retorno:
    :returns: None
    """
    # Conectar con el servidor de correo
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)


    # Recorrer cada fila del DataFrame y enviar el correo
 
    # Crear el mensaje
    msg = MIMEMultipart()
    msg["From"] = f"Juan de ClickGreen <{sender_email}>"
    msg["To"] = recipient_email
    msg["Subject"] = "Eco json"

    # HTML del mensaje
    html = f"{message}"
    
    msg.attach(MIMEText(html, "html"))
   

    # Enviar el correo
    server.sendmail(sender_email, recipient_email, msg.as_string())

    # Desconectar del servidor
    server.quit()