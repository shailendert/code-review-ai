import re

def analyze_java_code(code: str):
    issues = []

    # Rule 1: Long methods (>50 lines)
    methods = re.findall(r'\{([^}]*)\}', code, re.DOTALL)
    for m in methods:
        if len(m.split('\n')) > 50:
            issues.append("Method too long (>50 lines)")

    # Rule 2: Too many parameters
    params = re.findall(r'\((.*?)\)', code)
    for p in params:
        if len(p.split(',')) > 4:
            issues.append("Too many parameters in method")

    # Rule 3: System.out usage
    if "System.out.println" in code:
        issues.append("Use logging instead of System.out.println")

    return issues
