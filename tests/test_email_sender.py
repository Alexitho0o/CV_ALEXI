from utils.email_sender import send_contact_email


class DummySMTP:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.logged = False
        self.sent = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def login(self, user: str, password: str) -> None:
        self.logged = True

    def sendmail(self, from_addr: str, to_addr: str, body: str) -> None:
        self.sent = True


def test_send_contact_email_missing_credentials(monkeypatch) -> None:
    monkeypatch.delenv("GMAIL_USER", raising=False)
    monkeypatch.delenv("GMAIL_PASSWORD", raising=False)

    ok, msg = send_contact_email("Alexi", "alexi@test.com", "Prueba", "Hola")

    assert not ok
    assert "Configuración de correo no disponible" in msg


def test_send_contact_email_success(monkeypatch) -> None:
    monkeypatch.setenv("GMAIL_USER", "bot@gmail.com")
    monkeypatch.setenv("GMAIL_PASSWORD", "app-pass")
    monkeypatch.setattr("utils.email_sender.smtplib.SMTP_SSL", DummySMTP)

    ok, msg = send_contact_email("Alexi", "alexi@test.com", "Prueba", "Hola")

    assert ok
    assert "Mensaje enviado exitosamente" in msg

