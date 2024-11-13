def plain(diff, path=""):
    lines = []
    actions = {
        'added': lambda current_path, change:
            f"Property '{current_path}' was added with value: "
            f"{format_value(change['value'])}",
        'removed': lambda current_path, change:
            f"Property '{current_path}' was removed",
        'changed': lambda current_path, change:
            f"Property '{current_path}' was updated. "
            f"From {format_value(change['old_value'])} to "
            f"{format_value(change['new_value'])}",
        'nested': lambda current_path, change:
            plain(change["value"], current_path)
    }
    for key, change in diff.items():
        current_path = f"{path}.{key}" if path else key
        status = change["status"]
        if status in actions:
            lines.append(actions[status](current_path, change))
    return "\n".join(lines)


def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, bool):
        return "true" if value else "false"
    elif value is None:
        return "null"
    elif isinstance(value, str):
        return f"'{value}'"
    return str(value)
