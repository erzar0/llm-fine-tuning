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
        system_prompt = _trim("""
            You are a highly precise SQL generation engine.
            Your sole task is to translate natural language questions into correct, executable SQL queries.
            You must only rely on the provided database schema and context.
            Do not explain or comment.
            Do not include anything except a valid SQL query enclosed in <sql>...</sql> tags.
            Ensure the SQL query is syntactically correct and executable.
            You are only allowed to use the generic SQL syntax, no specific dialects.
            /no_think
            """)

        conversations = [
            {
                "from": "user",
                "value": _trim(f"""You are provided with the following database schema and context:

                    --- SCHEMA START ---
                    {row["sql_context"]}
                    --- SCHEMA END ---

                    Using only this information, write an SQL query that answers the following question:

                    "{row["sql_prompt"]}"

                    Output only the SQL query, with no additional text.
                    Wrap your final query inside <sql> and </sql> tags.
                    /no_think
                    """)
            },
            {
                "from": "assistant",
                "value": f"<sql>\n{row['sql'].strip()}\n</sql>"
            }
        ]

        sharegpt_item = {
            "conversations": conversations,
            "system": system_prompt,
            "tools": ""
        }

        sharegpt_data.append(sharegpt_item)

    return sharegpt_data

