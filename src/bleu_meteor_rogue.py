from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.meteor_score import meteor_score
from rouge_score import rouge_scorer
import nltk

nltk.download('wordnet')
nltk.download('omw-1.4')

def compare_texts(reference, candidate):
    ref_tokens = reference.split()
    cand_tokens = candidate.split()

    bleu = sentence_bleu([ref_tokens], cand_tokens, weights=(0.25, 0.25, 0.25, 0.25))
    
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    rouge_scores = scorer.score(reference, candidate)
    
    meteor = meteor_score([ref_tokens], cand_tokens)
    
    return {
        'BLEU': round(bleu, 4),
        'ROUGE-1': round(rouge_scores['rouge1'].fmeasure, 4),
        'ROUGE-2': round(rouge_scores['rouge2'].fmeasure, 4),
        'ROUGE-L': round(rouge_scores['rougeL'].fmeasure, 4),
        'METEOR': round(meteor, 4)
    }


# Translation
reference_translation = "The cat sits on the mat"
candidate_translation = "A cat is sitting on the mat"
print("Translation:", compare_texts(reference_translation, candidate_translation))

# Sum ups
original_text = "The quick brown fox jumps over the lazy dog. The dog barked loudly."
summary_human = "A fox jumps over a dog which barks."
summary_ai = "Fast fox jumps over sleeping dog."
print("\Sum ups (human vs AI):")
print("- Human:", compare_texts(original_text, summary_human))
print("- AI:", compare_texts(original_text, summary_ai))

# Paraphases
original = "The government announced new economic policies"
paraphrase = "New fiscal measures were introduced by authorities"
print("\Paraphases:", compare_texts(original, paraphrase))