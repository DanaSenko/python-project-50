def handle_added(value):
    return {"status": "added", "value": value}


def handle_removed(value):
    return {"status": "removed", "value": value}


def handle_unchanged(value):
    return {"status": "unchanged", "value": value}


def handle_nested(value):
    return {"status": "nested", "value": value}


def handle_changed(old_value, new_value):
    return {"status": "changed",
            "old_value": old_value,
            "new_value": new_value}


def build_diff(dict1, dict2, format_name="stylish"):
    keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    diff = {}

    for key in keys:
        if key not in dict1:
            diff[key] = handle_added(dict2[key])
        elif key not in dict2:
            diff[key] = handle_removed(dict1[key])
        elif dict1[key] == dict2[key]:
            diff[key] = handle_unchanged(dict1[key])
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            diff[key] = handle_nested(build_diff(dict1[key], dict2[key]))
        else:
            diff[key] = handle_changed(dict1[key], dict2[key])

    return diff
