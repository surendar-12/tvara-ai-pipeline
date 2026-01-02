import sys
from utils.pdfLoader import load_pdf_text
from utils.retry import retry
from moderation.moderation import moderate_text
from llm.llm import generate_response


def run_pipeline(pdf_path: str):
    # 1. Load PDF
    text = load_pdf_text(pdf_path)

    # 2. Moderation
    moderation_result = moderate_text(text)
    if not moderation_result["allowed"]:
        return moderation_result

    # 3. GPT-5-Nano (mocked) with retry
    response = retry(lambda: generate_response(text))

    return {
        "allowed": True,
        "response": response
    }


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python app.py <pdf_path>")
        sys.exit(1)

    output = run_pipeline(sys.argv[1])
    print(output)
