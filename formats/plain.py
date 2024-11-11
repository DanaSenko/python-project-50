def plain(diff, path=""):
    lines = []
    for key, change in diff.items():
        current_path = f"{path}.{key}" if path else key
        status = change["status"]
        if status == "added":
            lines.append(
                f"Property '{current_path}' was added with value: {format_value(change['value'])}"
            )
        elif status == "removed":
            lines.append(f"Property '{current_path}' was removed")
        elif status == "changed":
            lines.append(
                f"Property '{current_path}' was updated. From {format_value(change['old_value'])} to {format_value(change['new_value'])}"
            )
        elif status == "nested":
            lines.append(plain(change["value"], current_path))

    return "\n".join(lines)


def format_value(value):
    if isinstance(value, dict):
        return f"[complex value]"
    elif isinstance(value, bool):
        return "true" if value else "false"
    elif value is None:
        return "null"
    elif isinstance(value, str):
        return f"'{value}'"
    return str(value)
