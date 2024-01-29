def format_icpc(verdict):
    if verdict['first_test_failed'] is None:
        return """<span class="text-success">OK</span>"""
    first_test_failed = verdict['first_test_failed']
    failed_test_judgement = verdict['per_test_metrics'][first_test_failed - 1]
    return f"""<span class="text-danger">{failed_test_judgement['status'].upper()} {first_test_failed}</span>"""
