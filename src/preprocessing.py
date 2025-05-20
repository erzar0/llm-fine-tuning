import pandas as pd

def create_sharegpt_format(dataframe: pd.DataFrame):
    """
    Converts a pandas DataFrame into the ShareGPT JSON format for SQL fine-tuning.

    Args:
        dataframe (pd.DataFrame): DataFrame with columns 'sql_prompt', 'sql_context' and 'sql' etc.

    Returns:
        list: A list of dictionaries in the ShareGPT format.
    """

    def _trim(docstring):
        # https://stackoverflow.com/questions/2504411/proper-indentation-for-multiline-strings
        import sys
        if not docstring:
            return ''
        # Convert tabs to spaces (following the normal Python rules)
        # and split into a list of lines:
        lines = docstring.expandtabs().splitlines()
        # Determine minimum indentation (first line doesn't count):
        indent = sys.maxsize
        for line in lines[1:]:
            stripped = line.lstrip()
            if stripped:
                indent = min(indent, len(line) - len(stripped))
        # Remove indentation (first line is special):
        trimmed = [lines[0].strip()]
        if indent < sys.maxsize:
            for line in lines[1:]:
                trimmed.append(line[indent:].rstrip())
        # Strip off trailing and leading blank lines:
        while trimmed and not trimmed[-1]:
            trimmed.pop()
        while trimmed and not trimmed[0]:
            trimmed.pop(0)
        # Return a single string:
        return '\n'.join(trimmed)

    sharegpt_data = []
    for _, row in dataframe.iterrows():
        system_prompt = _trim("""You are a helpful assistant specialized in generating SQL queries.
                                Generate an SQL query that correctly answers the user's question based on the provided database schema and context.""")

        conversations = [
            {
                "from": "user",
                "value": _trim(f"""Context:\n'{row["sql_context"]}'
                                    Question:\n'{row["sql_prompt"]}'""")
            },
            {
                "from": "assistant",
                "value": f"Result: '{row['sql']}'"
            }
        ]

        sharegpt_item = {
            "conversations": conversations,
            "system": system_prompt,
            "tools": ""
        }
        sharegpt_data.append(sharegpt_item)

    return sharegpt_data


def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2)+1)
    for i, c1 in enumerate(s1):
        current_row = [i+1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1!= c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]