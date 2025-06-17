from llamafactory.chat import ChatModel
import re

BASE_MODEL_PATH = "Qwen/Qwen3-0.6B"
DEFAULT_SYSTEM_PROMPT = (
    "You are a fair and strict SQL evaluator. "
)

class SqlJudge():
    def __init__(self):
        args = dict(
            model_name_or_path=BASE_MODEL_PATH,
            template="qwen3",
        )
        self.evaluator_model = ChatModel(args)
    
    def _create_judging_prompt(self, reference_sql, predicted_sql):
        return f"""
            You are a SQL expert evaluating an assistant's response. The user asked a question, and the assistant replied with a SQL query.

            Reference SQL (correct answer):
            {reference_sql}

            Assistant's SQL (candidate response):
            {predicted_sql}

            Score the assistant's SQL query from 0 to 10 based on correctness, completeness, and formatting.
            0 means completely wrong, 10 means perfect.
            """
    
    def score_response(self, reference_sql, predicted_sql):
        prompt = self._create_judging_prompt(reference_sql, predicted_sql)
        messages = [{"role": "user", "content": prompt}]
        response = ""
        for chunk in self.evaluator_model.stream_chat(messages, system=DEFAULT_SYSTEM_PROMPT):
            response += chunk

        try:
            print(response)
            number = re.search(r'\b\d+\b', response)
            if number:
                score = float(number.group(0))
                return min(max(score, 0), 10)
            else:
                print("No valid score found in response:", response)
                return None
        except Exception as e:
            print("Scoring failed:", e, "Raw response:", response)
            return None
