from services.contact_service import (
    MAX_MENSAJE_LEN,
    MAX_NOMBRE_LEN,
    submit_contact_form,
    validate_contact_input,
)


def test_validate_contact_input_required_fields() -> None:
    assert validate_contact_input("", "a@b.com", "hola") is not None
    assert validate_contact_input("Alexi", "", "hola") is not None
    assert validate_contact_input("Alexi", "a@b.com", "") is not None


def test_validate_contact_input_invalid_email() -> None:
    error = validate_contact_input("Alexi", "correo-invalido", "mensaje")
    assert error == "❌ Ingresa un correo electrónico válido."


def test_validate_contact_input_length_limits() -> None:
    long_name = "a" * (MAX_NOMBRE_LEN + 1)
    long_message = "m" * (MAX_MENSAJE_LEN + 1)

    assert validate_contact_input(long_name, "a@b.com", "ok") is not None
    assert validate_contact_input("Alexi", "a@b.com", long_message) is not None


def test_submit_contact_form_validation_short_circuit(monkeypatch) -> None:
    called = {"value": False}

    def fake_send(*args, **kwargs):
        called["value"] = True
        return True, "ok"

    monkeypatch.setattr("services.contact_service.send_contact_email", fake_send)
    ok, msg = submit_contact_form("Alexi", "bad-email", "Asunto", "Mensaje")

    assert not ok
    assert "correo electrónico válido" in msg
    assert called["value"] is False

