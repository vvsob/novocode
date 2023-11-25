def format_icpc(verdict):
    if verdict['first_test_failed'] is None:
        return """<div class="text-success">OK</div>"""
    first_test_failed = verdict['first_test_failed']
    failed_test_judgement = verdict['per_test_metrics'][first_test_failed - 1]
    return f"""<div class="text-danger">{failed_test_judgement['status'].upper()} {first_test_failed}</div>"""
