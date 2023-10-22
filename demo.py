import openai
import time
import os
import PyPDF2
from transformers import AutoTokenizer
from pathlib import Path
from tqdm import tqdm
import re
import json

tokenizer = AutoTokenizer.from_pretrained("nomic-ai/gpt4all-falcon")
file_path = '/home/jehu/Documents/law data/data/Contract Law Best Book.pdf'

desired_runs = 55
one_hour_in_seconds = 3600
time_interval = one_hour_in_seconds / desired_runs

# openai.log = "debug"
openai.api_key = "sk-6fIbSjOMAOKeMrKj9SpR5u7xJWZ80eBTBq0epAaohPwBdiEK"
openai.api_base = "https://api.chatanywhere.com.cn/v1"

def read_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def tokenize(text):
    enc = tokenizer.encode(text)
    return enc

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
def submit_to_llm(chunk, retries=3):
    for i in range(retries):
        try:
            messages = [{'role': 'user', 'content': template + " Legal Text: "+legal_text}]
            print(gpt_35_api_stream(messages))
            print(messages)

            response = llm_chain.run(chunk.strip())
            # Extract JSON string from between back-ticks
            if is_json(response):
                print(response)
                return json.loads(response)
            else:
                match = re.search(r'`(.*?)`', response, re.S)
                if match and is_json(match.group(1)):
                    print(f"Attempt {i + 1} failed. Retrying...")
                    return json.loads(match.group(1))  # assuming you want to return the JSON data
                else:
                    print("Request failed:")
                    print(response)
        except requests.exceptions.RequestException as e:
            continue
    print("Max retries exceeded. Skipping this chunk.")
    return None


# non-streaming response
# completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world!"}])
# print(completion.choices[0].message.content)

def gpt_35_api_stream(messages: list):
    """Create a new answer for the provided conversation message (streaming)

    Args:
        messages (list): Complete conversation message
        api_key (str): OpenAI API key

    Returns:
        tuple: (results, error_desc)
    """
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages,
            stream=True,
        )
        completion = {'role': '', 'content': ''}
        for event in response:
            if event['choices'][0]['finish_reason'] == 'stop':
                print(f'Completion data received: {completion}')
                break
            for delta_k, delta_v in event['choices'][0]['delta'].items():
                print(f'Stream response data: {delta_k} = {delta_v}')
                completion[delta_k] += delta_v
        messages.append(completion)  # messages
        return (True, '')
    except Exception as err:
        return (False, f'OpenAI API abnormal: {err}')

if __name__ == '__main__':
    template = '''
        Task:You are an API that Generates a description of a function which will be added to the computational grammar. a description of that function would be clear and concise, labelling what the expected input should be and the expected output and how that python function from the lawlia will transform the input to output 
        your output should be in this format:
        [function name]
        [inputs:]
        step by step procedures:
        [output:]

        Lawlia has a class called contract law presented below:
        class ContractLaw:
    def __init__(self, contract_name, parties, effective_date, expiration_date, terms, governing_law):
        """
        Initialize a ContractLaw instance.

        :param contract_name: The name or identifier of the contract.
        :param parties: List of parties involved in the contract.
        :param effective_date: The date when the contract becomes effective.
        :param expiration_date: The date when the contract expires.
        :param terms: The terms and conditions of the contract.
        :param governing_law: The governing law under which the contract is subject.
        """
        self.contract_name = contract_name
        self.parties = parties
        self.effective_date = effective_date
        self.expiration_date = expiration_date
        self.terms = terms
        self.governing_law = governing_law
        self.breach_claim = None
        self.misrepresentation = None
        self.warranty = None
        self.arbitration_clause = None
        self.choice_of_forum = None
        self.choice_of_forum = None
        self.payment_clause = None
        self.confidentiality_clause = None
        self.force_majeure_clause = None
        self.termination_clause = None
        self.liquidated_damages_clause = None

    def is_valid_contract(self, current_date):
        """
        Check if the contract is valid based on the current date.

        :param current_date: The current date to validate against the contract's effective and expiration dates.
        :return: True if the contract is valid, False otherwise.
        """
        return self.effective_date <= current_date <= self.expiration_date

    def parties_involved(self):
        """
        Get the list of parties involved in the contract.

        :return: List of parties.
        """
        return self.parties

    def get_contract_terms(self):
        """
        Get the terms and conditions of the contract.

        :return: The contract terms.
        """
        return self.terms

    def set_governing_law(self, new_governing_law):
        """
        Set or update the governing law of the contract.

        :param new_governing_law: The new governing law to be set.
        """
        self.governing_law = new_governing_law

    def extend_contract_expiration(self, new_expiration_date):
        """
        Extend the contract's expiration date if the new date is later than the current expiration date.

        :param new_expiration_date: The new expiration date to be set.
        """
        if new_expiration_date > self.expiration_date:
            self.expiration_date = new_expiration_date

    def terminate_contract(self, termination_date):
        """
        Terminate the contract if the termination date is earlier than the current expiration date.

        :param termination_date: The termination date to be applied.
        """
        if termination_date < self.expiration_date:
            self.expiration_date = termination_date

    def is_party_to_contract(self, party_name):
        """
        Check if a party is involved in the contract.

        :param party_name: The name of the party to check.
        :return: True if the party is involved, False otherwise.
        """
        return party_name in self.parties

    def assert_breach_claim(self, claim_description):
        """
        Assert a breach claim in the contract.

        :param claim_description: Description of the breach claim.
        """
        self.breach_claim = claim_description
        
    def assert_termination_clause(self, termination_clause_description):
        """
        Assert the termination clause in the contract.

        :param termination_clause_description: Description of the termination clause.
        """
        self.termination_clause = termination_clause_description

    def assert_indemnification_clause(self, indemnification_clause_description):
        """
        Assert the indemnification clause in the contract.

        :param indemnification_clause_description: Description of the indemnification clause.
        """
        self.indemnification_clause = indemnification_clause_description

    
    def evaluate_breach_claim(self):
        """
        Evaluate the breach claim in the contract.

        :return: Evaluation result of the breach claim.
    
        """
        if self.breach_claim is not None:
            if "force majeure" in self.breach_claim:
                return "Force majeure is a valid defense."
            else:
                return "Breach claim is valid."
        return "No breach claim asserted."

    def assert_misrepresentation(self, misrepresentation_description):
        """
        Assert a misrepresentation in the contract.

        :param misrepresentation_description: Description of the misrepresentation.
        """
        self.misrepresentation = misrepresentation_description

    def evaluate_misrepresentation(self):
        """
        Evaluate the misrepresentation in the contract.

        :return: Evaluation result of the misrepresentation.
        """
        if self.misrepresentation is not None:
            if "innocent misrepresentation" in self.misrepresentation:
                return "Misrepresentation is innocent."
            elif "fraudulent misrepresentation" in self.misrepresentation:
                return "Misrepresentation is fraudulent."
            else:
                return "Misrepresentation occurred."
        return "No misrepresentation asserted."

    def assert_warranty(self, warranty_description):
        """
        Assert a warranty in the contract.

        :param warranty_description: Description of the warranty.
        """
        self.warranty = warranty_description

    def evaluate_warranty(self):
        """
        Evaluate the warranty in the contract.

        :return: Evaluation result of the warranty.
        """
        if self.warranty is not None:
            return "Warranty is in effect."
        return "No warranty asserted."

    def set_arbitration_clause(self, arbitration_clause_description):
        """
        Set the arbitration clause in the contract.

        :param arbitration_clause_description: Description of the arbitration clause.
        """
        self.arbitration_clause = arbitration_clause_description

    def get_arbitration_clause(self):
        """
        Get the arbitration clause in the contract.

        :return: The arbitration clause.
        """
        return self.arbitration_clause

    def set_choice_of_forum(self, choice_of_forum_description):
        """
        Set the choice of forum in the contract.

        :param choice_of_forum_description: Description of the choice of forum.
        """
        self.choice_of_forum = choice_of_forum_description

    def get_choice_of_forum(self):
        """
        Get the choice of forum in the contract.

        :return: The choice of forum.
        """
        return self.choice_of_forum

    def resolve_contract_dispute(self, party_a_demand, party_b_demand):
        """
        Resolve a contract dispute based on demands from the involved parties.

        :param party_a_demand: The demand from Party A.
        :param party_b_demand: The demand from Party B.
        :return: Resolution outcome of the contract dispute.
        """
        if party_a_demand == "compensation" and party_b_demand == "termination":
            return "Contract termination granted."
        elif party_a_demand == "compensation":
            return "Compensation awarded."
        elif party_b_demand == "termination":
            return "Contract termination granted."
        else:
            return "No resolution required."

    def add_party(self, party_name):
        """
        Add a party to the contract.
        
        :param party_name: The name of the party to be added.
        """
        if party_name not in self.parties:
           self.parties.append(party_name)

    def remove_party(self, party_name):
        """
        Remove a party from the contract.

        :param party_name: The name of the party to be removed.
        """
        if party_name in self.parties:
            self.parties.remove(party_name)

    def add_term(self, new_term):
        """
        Add a new term to the contract.

        :param new_term: The new term to be added.
        """
        self.terms += "\\n" + new_term

    def modify_term(self, existing_term, new_term):
        """
        Modify an existing term in the contract.

        :param existing_term: The term to be modified.
        :param new_term: The new term to replace the existing term.
        """
        if existing_term in self.terms:
            self.terms = self.terms.replace(existing_term, new_term)

    def assert_choice_of_forum(self, forum_description):
        """
        Assert the choice of forum in the contract.

        :param forum_description: Description of the choice of forum.
        """
        self.choice_of_forum = forum_description

    def assert_arbit'''



    for _ in range(desired_runs):
        legal_text = """Form is not an aspect of contract law that most ALevel syllabuses now concern themselves with. However, it can in some instances be an important issue, and it is therefore worth knowing at least the basic rules. It is not, however, ever likely to be a major part of any A Level contract exam.
        It is generally fair to say that with the majority of contracts the form in which they are made is not an issue. We make contracts every day, and probably all day long, without ever contemplating their legal significance and certainly without worrying about the specific form in which we have created them.
        We can distinguish between ‘simple’ contracts and ‘speciality’ contracts.
        In the case of simple contracts, these can be made orally or in writing, or possibly even be implied by conduct. An example is where an auctioneer completes a contract at an auction by the fall of his hammer (although this might also be accompanied by words such as ‘sold to the lady in the red dress’).
        With contracts made in this way, then there is no requirement for there to be any particular form and evidence of compliance with the basic rules of formation will be sufficient to make such contracts enforceable in law.
        However, with speciality contracts, these need to have been created in a specific form in order to gain their validity: the ‘form’ in question will be to do with being written or evidenced in writing, and this formal requirement indicates that a higher level of proof of the existence of the contract is required, and so speciality contracts are concerned with more significant property such as land or other transferable interests.
        Speciality contracts come in one of three types: agreements which must be created in the form of a deed, agreements which must be made in writing, agreements which need only to be evidenced in writing, e.g. in a memorandum"""
        submit_to_llm()