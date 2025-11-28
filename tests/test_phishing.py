import pytest
from src.phishing_detection import analyze_url

def test_empty_url():
    score, reason = analyze_url("")
    assert score == 0
    assert "No URL" in reason or reason == "No URL provided"

def test_safe_url():
    score, reason = analyze_url("https://example.com")
    assert score == 0 or score < 10
    assert "Looks safe" in reason or "safe" in reason.lower()

def test_phishing_keywords():
    score, reason = analyze_url("http://verify-your-bank-login.com")
    assert score > 0
    assert "contains" in reason.lower() or "uses insecure http" in reason.lower()
