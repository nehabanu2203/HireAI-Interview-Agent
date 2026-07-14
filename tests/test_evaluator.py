import evaluator
from types import SimpleNamespace
import groq


def test_evaluate_answer_success(monkeypatch):
    fake_resp = SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content="Score: 8/10\n\nStrengths\nGood\n\nWeaknesses\nNone\n\nSuggestions\nKeep it up\n\nOverall Feedback\nNice."))])

    def fake_create(*args, **kwargs):
        return fake_resp

    monkeypatch.setattr(evaluator.client.chat.completions, "create", fake_create)

    res = evaluator.evaluate_answer("Q", "A")
    assert res["score"] == 8
    assert "Strengths" in res["feedback"]


def test_evaluate_answer_api_error(monkeypatch):
    def fake_create(*args, **kwargs):
        raise groq.APIConnectionError("down")

    monkeypatch.setattr(evaluator.client.chat.completions, "create", fake_create)

    res = evaluator.evaluate_answer("Q", "A")
    assert res["score"] == 5
    fb = res["feedback"].lower()
    assert ("evaluation service is unavailable" in fb) or ("the candidate provided a response" in fb)
