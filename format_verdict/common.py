def format_testing(verdict: dict):
    if "current_test" not in verdict:
        return """<span class="text-primary">Testing</span>"""
    return f"""<span class="text-primary">Testing {verdict["current_test"]}</span>"""


def format_judge_error(verdict):
    return """<span class="text-danger">Judge error</span>"""
