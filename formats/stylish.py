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


def stylish(diff, depth=0):
    indent = "    " * depth
    lines = ["{"]
    status_handlers = {
        "added": lambda key, change: (
            f"{indent}  + {key}: {format_value(change['value'], depth + 1)}"
        ),
        "removed": lambda key, change: (
            f"{indent}  - {key}: {format_value(change['value'], depth + 1)}"
        ),
        "unchanged": lambda key, change: (
            f"{indent}    {key}: {format_value(change['value'], depth + 1)}"
        ),
        "changed": lambda key, change: [
            f"{indent}  - {key}: "
            f"{format_value(change['old_value'], depth + 1)}",
            f"{indent}  + {key}: "
            f"{format_value(change['new_value'], depth + 1)}",
        ],
        "nested": lambda key, change: (
            f"{indent}    {key}: {stylish(change['value'], depth + 1)}"
        ),
    }

    for key, change in diff.items():
        status = change["status"]
        if status in status_handlers:
            result = status_handlers[status](key, change)
            if isinstance(result, list):
                lines.extend(result)
            else:
                lines.append(result)

    lines.append(f"{'    ' * depth}}}")
    return "\n".join(lines)
