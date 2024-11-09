def build_diff(dict1, dict2, format_name="stylish"):
    keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    diff = {}

    for key in keys:
        if key not in dict1:
            diff[key] = {"status": "added", "value": dict2[key]}
        elif key not in dict2:
            diff[key] = {"status": "removed", "value": dict1[key]}
        elif dict1[key] == dict2[key]:
            diff[key] = {"status": "unchanged", "value": dict1[key]}
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            diff[key] = {
                "status": "nested",
                "value": build_diff(dict1[key], dict2[key]),
            }
        else:
            diff[key] = {
                "status": "changed",
                "old_value": dict1[key],
                "new_value": dict2[key],
            }
    return diff
