import interview
from types import SimpleNamespace


def test_generate_questions_parsing(monkeypatch):
    fake_content = "1. What is Python?\n2) Explain OOP.\n3. Another\n4. Fourth\n5. Fifth\n6. Extra"
    fake_resp = SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=fake_content))])

    monkeypatch.setattr(interview.client.chat.completions, "create", lambda *a, **k: fake_resp)

    qs = interview.generate_questions("Developer")
    assert len(qs) == 5
    assert qs[0] == "What is Python?"
    assert qs[1] == "Explain OOP."
