def analyze_url(url: str):
    if not url:
        return 0, "No URL provided"

    suspicious_keywords = ["login", "verify", "bank", "update", "confirm"]
    score = 0
    reasons = []

    # Rule-based keyword matching
    for kw in suspicious_keywords:
        if kw in url.lower():
            score += 25
            reasons.append(f"Contains '{kw}'")

    # Check for insecure HTTP
    if url.startswith("http://"):
        score += 20
        reasons.append("Uses insecure HTTP")

    # Score should not exceed 100
    score = min(score, 100)

    # Prepare explanation text
    reason_text = ", ".join(reasons) if reasons else "Looks safe"
    return score, reason_text
