def stylish(diff, depth=0):
    indent = "    " * depth
    lines = ["{"]
    for key, change in diff.items():
        if change["status"] == "added":
            lines.append(
                f"{indent}  + {key}: {format_value(change['value'], depth + 1)}"
            )
        elif change["status"] == "removed":
            lines.append(
                f"{indent}  - {key}: {format_value(change['value'], depth + 1)}"
            )
        elif change["status"] == "unchanged":
            lines.append(
                f"{indent}    {key}: {format_value(change['value'], depth + 1)}"
            )
        elif change["status"] == "changed":
            lines.append(
                f"{indent}  - {key}: {format_value(change['old_value'], depth + 1)}"
            )
            lines.append(
                f"{indent}  + {key}: {format_value(change['new_value'], depth + 1)}"
            )
        elif change["status"] == "nested":
            lines.append(f"{indent}    {key}: {stylish(change['value'], depth + 1)}")
    lines.append(f"{'    ' * depth}}}")
    return "\n".join(lines)


def format_value(value, depth):
    if isinstance(value, dict):
        lines = ["{"]
        indent = "    " * (depth + 1)
        for k, v in value.items():
            lines.append(f"{indent}{k}: {format_value(v, depth + 1)}")
        lines.append(f"{'    ' * depth}}}")
        return "\n".join(lines)
    elif isinstance(value, bool):
        return "true" if value else "false"
    elif value is None:
        return "null"
    return str(value)
