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
        self.terms += "\n" + new_term

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

    def assert_arbitration_clause(self, arbitration_clause_description):
        """
        Assert the arbitration clause in the contract.

        :param arbitration_clause_description: Description of the arbitration clause.
        """
        self.arbitration_clause = arbitration_clause_description

    def assert_payment_clause(self, payment_clause_description):
        """
        Assert the payment clause in the contract.

        :param payment_clause_description: Description of the payment clause.
        """
        self.payment_clause = payment_clause_description

    def assert_confidentiality_clause(self, confidentiality_clause_description):
        """
        Assert the confidentiality clause in the contract.

        :param confidentiality_clause_description: Description of the confidentiality clause.
        """
        self.confidentiality_clause = confidentiality_clause_description

    def assert_force_majeure_clause(self, force_majeure_clause_description):
        """
        Assert the force majeure clause in the contract.

        :param force_majeure_clause_description: Description of the force majeure clause.
        """
        self.force_majeure_clause = force_majeure_clause_description

    def evaluate_contract(self, current_date):
        """
        Evaluate the overall status of the contract based on the current date.

        :param current_date: The current date for evaluation.
        :return: Evaluation result of the contract.
        """
        if current_date < self.effective_date:
            return "Contract has not yet become effective."
        elif current_date > self.expiration_date:
            return "Contract has expired."
        else:
            return "Contract is in effect."

    def get_contract_details(self):
        """
        Get all details of the contract as a dictionary.

        :return: A dictionary containing all contract details.
        """
        contract_details = {
            "Contract Name": self.contract_name,
            "Parties": self.parties,
            "Effective Date": self.effective_date,
            "Expiration Date": self.expiration_date,
            "Governing Law": self.governing_law,
            "Breach Claim": self.breach_claim,
            "Misrepresentation": self.misrepresentation,
            "Warranty": self.warranty,
            "Arbitration Clause": self.arbitration_clause,
            "Choice of Forum": self.choice_of_forum,
            "Terms": self.terms,
        }
        return contract_details

    def assert_payment_clause(self, payment_clause_description):
        """
        Assert the payment clause in the contract.

        :param payment_clause_description: Description of the payment clause.
        """
        self.payment_clause = payment_clause_description

    def assert_confidentiality_clause(self, confidentiality_clause_description):
        """
        Assert the confidentiality clause in the contract.

        :param confidentiality_clause_description: Description of the confidentiality clause.
        """
        self.confidentiality_clause = confidentiality_clause_description

    def assert_force_majeure_clause(self, force_majeure_clause_description):
        """
        Assert the force majeure clause in the contract.

        :param force_majeure_clause_description: Description of the force majeure clause.
        """
        self.force_majeure_clause = force_majeure_clause_description

    def evaluate_contract(self, current_date):
        """
        Evaluate the overall status of the contract based on the current date.

        :param current_date: The current date for evaluation.
        :return: Evaluation result of the contract.
        """
        if current_date < self.effective_date:
            return "Contract has not yet become effective."
        elif current_date > self.expiration_date:
            return "Contract has expired."
        else:
            return "Contract is in effect."

    def get_contract_details(self):
        """
        Get all details of the contract as a dictionary.

        :return: A dictionary containing all contract details.
        """
        contract_details = {
            "Contract Name": self.contract_name,
            "Parties": self.parties,
            "Effective Date": self.effective_date,
            "Expiration Date": self.expiration_date,
            "Governing Law": self.governing_law,
            "Breach Claim": self.breach_claim,
            "Misrepresentation": self.misrepresentation,
            "Warranty": self.warranty,
            "Arbitration Clause": self.arbitration_clause,
            "Choice of Forum": self.choice_of_forum,
            "Payment Clause": self.payment_clause,
            "Confidentiality Clause": self.confidentiality_clause,
            "Force Majeure Clause": self.force_majeure_clause,
            "Terms": self.terms,
        }
        return contract_details

    def assert_termination_clause(self, termination_clause_description):
        """
        Assert the termination clause in the contract.

        :param termination_clause_description: Description of the termination clause.
        """
        self.termination_clause = termination_clause_description

    def assert_liquidated_damages_clause(self, liquidated_damages_clause_description):
        """
        Assert the liquidated damages clause in the contract.

        :param liquidated_damages_clause_description: Description of the liquidated damages clause.
        """
        self.liquidated_damages_clause = liquidated_damages_clause_description

    def evaluate_termination(self, termination_date):
        """
        Evaluate the termination status of the contract.

        :param termination_date: The date on which termination is considered.
        :return: Evaluation result of the termination clause.
        """
        if termination_date < self.effective_date:
            return "Termination is not applicable before the effective date."
        elif termination_date >= self.expiration_date:
            return "Termination is not applicable after the expiration date."
        elif termination_date < self.expiration_date and self.termination_clause is not None:
            return f"Contract can be terminated as per the clause: {self.termination_clause}"
        else:
            return "Termination is not applicable based on current conditions."

    def evaluate_liquidated_damages(self, breach_occurred):
        """
        Evaluate the applicability of liquidated damages in case of breach.

        :param breach_occurred: Boolean indicating whether a breach has occurred.
        :return: Evaluation result of the liquidated damages clause.
        """
        if breach_occurred and self.liquidated_damages_clause is not None:
            return f"Liquidated damages are applicable as per the clause: {self.liquidated_damages_clause}"
        elif breach_occurred:
            return "Liquidated damages are applicable based on standard legal principles."
        else:
            return "Liquidated damages are not applicable."

    def get_all_contract_clauses(self):
        """
        Get all contract clauses as a dictionary.

        :return: A dictionary containing all contract clauses.
        """
        contract_clauses = {
            "Breach Claim": self.breach_claim,
            "Misrepresentation": self.misrepresentation,
            "Warranty": self.warranty,
            "Arbitration Clause": self.arbitration_clause,
            "Choice of Forum": self.choice_of_forum,
            "Payment Clause": self.payment_clause,
            "Confidentiality Clause": self.confidentiality_clause,
            "Force Majeure Clause": self.force_majeure_clause,
            "Termination Clause": self.termination_clause,
            "Liquidated Damages Clause": self.liquidated_damages_clause,
        }
        return contract_clauses

    def assert_payment_clause(self, payment_clause_description):
        """
        Assert the payment clause in the contract.

        :param payment_clause_description: Description of the payment clause.
        """
        self.payment_clause = payment_clause_description

    def assert_confidentiality_clause(self, confidentiality_clause_description):
        """
        Assert the confidentiality clause in the contract.

        :param confidentiality_clause_description: Description of the confidentiality clause.
        """
        self.confidentiality_clause = confidentiality_clause_description

    def assert_force_majeure_clause(self, force_majeure_clause_description):
        """
        Assert the force majeure clause in the contract.

        :param force_majeure_clause_description: Description of the force majeure clause.
        """
        self.force_majeure_clause = force_majeure_clause_description

    def evaluate_payment(self, payment_due_date):
        """
        Evaluate the payment status of the contract.

        :param payment_due_date: The date on which the payment is due.
        :return: Evaluation result of the payment clause.
        """
        if payment_due_date < self.effective_date:
            return "Payment is not applicable before the effective date."
        elif payment_due_date >= self.expiration_date:
            return "Payment is not applicable after the expiration date."
        elif payment_due_date < self.expiration_date and self.payment_clause is not None:
            return f"Payment is due as per the clause: {self.payment_clause}"
        else:
            return "Payment is not applicable based on current conditions."

    def evaluate_confidentiality(self):
        """
        Evaluate the compliance with the confidentiality clause.

        :return: Evaluation result of the confidentiality clause.
        """
        if self.confidentiality_clause is not None:
            return f"Confidentiality is required as per the clause: {self.confidentiality_clause}"
        else:
            return "Confidentiality requirements are not defined."

    def evaluate_force_majeure(self, force_majeure_event):
        """
        Evaluate the applicability of the force majeure clause.

        :param force_majeure_event: Description of the force majeure event.
        :return: Evaluation result of the force majeure clause.
        """
        if force_majeure_event and self.force_majeure_clause is not None:
            return f"Force majeure clause is applicable as per the clause: {self.force_majeure_clause}"
        elif force_majeure_event:
            return "Force majeure clause is applicable based on standard legal principles."
        else:
            return "Force majeure clause is not applicable."	
    def get_contract_summary(self):
        """
        Get a summary of the contract, including parties, dates, and key clauses.

        :return: A summary of the contract.
        """
        contract_summary = {
            "Contract Name": self.contract_name,
            "Parties": self.parties,
            "Effective Date": self.effective_date,
            "Expiration Date": self.expiration_date,
            "Governing Law": self.governing_law,
            "Key Clauses": self.get_all_contract_clauses(),
        }
        return contract_summary

    def __str__(self):
        """
        Return a string representation of the contract.

        :return: String representation of the contract details.
        """
        return f"Contract Name: {self.contract_name}\nParties: {', '.join(self.parties)}\nEffective Date: {self.effective_date}\n" \
               f"Expiration Date: {self.expiration_date}\nGoverning Law: {self.governing_law}\nBreach Claim: {self.breach_claim}\n" \
               f"Misrepresentation: {self.misrepresentation}\nWarranty: {self.warranty}\n" \
               f"Arbitration Clause: {self.arbitration_clause}\nChoice of Forum: {self.choice_of_forum}"
