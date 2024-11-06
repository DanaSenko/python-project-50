from gendiff.file_reader import read_json_file


def generate_diff(dict1, dict2):
    
    keys = sorted(set(dict1.keys() | dict2.keys()))
    result = ['{']

    for key in keys:
        if key in dict1 and key not in dict2:
            result.append(f'  - {key}: {dict1[key]}')
        elif key in dict2 and key not in dict1:
            result.append(f'  + {key}: {dict2[key]}')
        elif dict1[key] != dict2[key]:
            result.append(f'  - {key}: {dict1[key]}')
            result.append(f'  + {key}: {dict2[key]}')
        else:
            result.append(f'    {key}: {dict1[key]}')
    result.append('}')

    return '\n'.join(result)


def gendiff(filepath1, filepath2):
    dict1 = read_json_file(filepath1)
    dict2 = read_json_file(filepath2)
    diff = generate_diff(dict1, dict2)

    return diff

    


