import tempfile
import os
import subprocess

def extract_sql(text):
    import re
    pattern = r"<sql>(.*?)</sql>"
    match = re.search(pattern, text, re.DOTALL)
    return match.group(1)
    
def chdiff(str1, str2):
    with tempfile.TemporaryDirectory() as tmpdir:
        file1_path = os.path.join(tmpdir, "a.txt")
        file2_path = os.path.join(tmpdir, "b.txt")

        with open(file1_path, 'w') as f1:
            f1.write(str1)
        with open(file2_path, 'w') as f2:
            f2.write(str2)

        # Run git diff with color
        cmd = [
            "git", "diff", "--no-index",
            "--word-diff=color", "--word-diff-regex=.",
            "--color=always", "-U9999",  # Force ANSI color codes in output
            file1_path, file2_path
        ]

        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Clean up the output: skip metadata lines
        return result.stdout