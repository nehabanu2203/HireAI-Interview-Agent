import os
import pandas as pd
import dashboard
import report


def test_save_interview_creates_file_and_row(tmp_path, monkeypatch):
    data_file = tmp_path / "data" / "interviews.csv"
    monkeypatch.setattr(dashboard, "DATA_FILE", str(data_file))

    dashboard.save_interview("Alice", "a@example.com", "Dev", 2, 8, "✅ Hire")

    assert data_file.exists()
    df = pd.read_csv(data_file)
    assert df.shape[0] == 1
    assert df.iloc[0]["Candidate"] == "Alice"


def test_generate_pdf_creates_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    filename = report.generate_pdf("Bob", "Dev", 7, "✅ Hire", ["Good job", "Needs improvement"]) 

    # ensure returned filename exists and is non-empty
    assert os.path.exists(filename)
    assert os.path.getsize(filename) > 0
