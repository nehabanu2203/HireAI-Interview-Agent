import utils


def test_calculate_recommendation_boundaries():
    assert utils.calculate_recommendation(9) == "🌟 Strong Hire"
    assert utils.calculate_recommendation(7) == "✅ Hire"
    assert utils.calculate_recommendation(5) == "🟡 Consider"
    assert utils.calculate_recommendation(0) == "❌ Reject"


def test_calculate_average_and_skill_breakdown():
    results = [{"score": 8}, {"score": 6}, {"score": 7}]
    assert utils.calculate_average(results) == round((8 + 6 + 7) / 3, 2)
    breakdown = utils.skill_breakdown(results)
    assert set(breakdown.keys()) == {"Technical", "Communication", "Confidence", "Problem Solving"}
    assert 1 <= breakdown["Confidence"] <= 10
