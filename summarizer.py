from transformers import pipeline

# Load the summarization pipeline (this downloads the model weights the first time)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text):
    """
    Generates a concise summary from the provided text.
    
    Parameters:
      text (str): The input text extracted from the PDF.
      
    Returns:
      str: A concise summary.
    """
    # Depending on the length of the input, you might need to chunk the text.
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Example usage:
if __name__ == '__main__':
    input_text = "Your extracted PDF text goes here. It might be very long, so you may want to split it into chunks if needed."
    print("Summary:")
    print(generate_summary(input_text))
