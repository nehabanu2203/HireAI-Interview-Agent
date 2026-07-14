import statistics

def calculate_recommendation(score):

    if score >= 9:
        return "🌟 Strong Hire"

    elif score >= 7:
        return "✅ Hire"

    elif score >= 5:
        return "🟡 Consider"

    return "❌ Reject"


def calculate_average(results):

    scores = [item["score"] for item in results]

    return round(statistics.mean(scores),2)


def skill_breakdown(results):

    avg = calculate_average(results)

    technical = min(10, round(avg+0.5,1))
    communication = min(10, round(avg,1))
    confidence = max(1, round(avg-0.5,1))
    problem_solving = min(10, round(avg+0.2,1))

    return {

        "Technical":technical,

        "Communication":communication,

        "Confidence":confidence,

        "Problem Solving":problem_solving

    }