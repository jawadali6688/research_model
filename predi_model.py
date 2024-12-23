import google.generativeai as genai
import pandas as pd
import openpyxl
import os

GOOGLE_API_KEY = ""  
genai.configure(api_key=GOOGLE_API_KEY)


model = genai.GenerativeModel("gemini-1.5-flash")


def process_row(row):
    title = row['title']
    abstract = row['abstract']

    prompt = f"""
    You are a researcher rigorously screening titles and abstracts of scientific papers for inclusion or exclusion in a review paper.
    Use the criteria below to inform your decision.
    If any exclusion criteria are met or not all inclusion criteria are met, exclude the article.
    If all inclusion criteria are met, include the article.

    Title: {title}
    Abstract: {abstract}

    Inclusion Criteria: 
    "Parallel randomized controlled trials, Studies that recruited patients with Raynaud's syndrome, Studies that compared the use of acupuncture therapy (including electroacupuncture or acupuncture with moxibustion) with an untreated or sham acupuncture group, A study is eligible if a concurrent adjuvant therapy is administered in addition to acupuncture and the control treatment, Reported any of the outcomes of interest: remission of Raynaud's syndrome, number of Raynaud's attacks per day after acupuncture, positive cold provocation test, positive cold stimulation test."

    Exclusion Criteria:
    "Studies that used different adjuvant therapies for its intervention and control arms."

    Please return only the following in the format below:
    Decision: Include or Exclude
    Reason: Provide a brief explanation for your decision based on the inclusion/exclusion criteria. For example: "The study included parallel randomized controlled trials and recruited patients with Raynaud's syndrome."
    Do not include anything else.
    """
    try:
        
        response = model.generate_content(prompt)
        print(f"Raw model response: {response.text}")
        response_text = response.text.strip()
        lines = response_text.split("\n")
        
        if len(lines) != 2:
            decision = "Error"
            reason = "Could not generate valid decision and reason."
        else:
            decision = lines[0].strip()
            reason = lines[1].strip()


        if "include" in decision.lower():
            decision = "Included"
        elif "exclude" in decision.lower():
            decision = "Excluded"
        else:
            decision = "Excluded" 
            reason = "Reason unclear or not specified."


        return pd.Series([title, abstract, decision, reason])

    except Exception as e:
        print(f"Error processing row: {e}")
        return pd.Series([title, abstract, "Error", f"Error: {e}"])


def process_csv(file_path):
    try:
        df = pd.read_csv(file_path, encoding='ISO-8859-1')

        if 'title' not in df.columns or 'abstract' not in df.columns:
            print("Error: CSV file must contain 'title' and 'abstract' columns.")
            return

        df[['Title', 'Abstract', 'Decision', 'Reason']] = df.apply(process_row, axis=1)


        output_file = os.path.join(os.path.dirname(file_path), 'output.xlsx')
        df.to_excel(output_file, index=False)
        print(f"Results saved to {output_file}")

    except Exception as e:
        print(f"Error processing CSV file: {e}")

if __name__ == "__main__":
    file_name = "p_data.csv"  

    file_path = os.path.join(os.path.dirname(__file__), file_name)
    process_csv(file_path)
