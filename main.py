from analyzer.static_rules import analyze_java_code
from analyzer.ai_reviewer import ai_review

def read_file(path):
    with open(path, "r") as f:
        return f.read()

if __name__ == "__main__":
    code = read_file("samples/BadCode_Test.java")

    print("=== STATIC ANALYSIS ===")
    static_issues = analyze_java_code(code)
    for issue in static_issues:
        print("-", issue)

    print("\n=== AI REVIEW ===")
    ai_feedback = ai_review(code)
    print(ai_feedback)
