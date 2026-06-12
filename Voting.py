class Voter:
    def __init__(self, voter_id, name):
        self.voter_id = voter_id
        self.name = name
        self.has_voted = False


class Candidate:
    def __init__(self, candidate_id, name):
        self.candidate_id = candidate_id
        self.name = name
        self.votes = 0


class VotingSystem:
    def __init__(self):
        self.voters = {}
        self.candidates = {}

    def register_voter(self, voter_id, name):
        if voter_id in self.voters:
            print(f"Voter ID {voter_id} already registered.")
            return False
        self.voters[voter_id] = Voter(voter_id, name)
        print(f"Voter {name} registered successfully with ID {voter_id}.")
        return True

    def add_candidate(self, candidate_id, name):
        if candidate_id in self.candidates:
            print(f"Candidate ID {candidate_id} already exists.")
            return False
        self.candidates[candidate_id] = Candidate(candidate_id, name)
        print(f"Candidate {name} added successfully with ID {candidate_id}.")
        return True

    def vote(self, voter_id, candidate_id):
        if voter_id not in self.voters:
            print("Voter not registered.")
            return False
        voter = self.voters[voter_id]
        if voter.has_voted:
            print(f"Voter {voter.name} has already voted.")
            return False
        if candidate_id not in self.candidates:
            print("Candidate not found.")
            return False

        self.candidates[candidate_id].votes += 1
        voter.has_voted = True
        print(f"Voter {voter.name} voted successfully for {self.candidates[candidate_id].name}.")
        return True

    def results(self):
        print("\nVoting Results:")
        for candidate in self.candidates.values():
            print(f"{candidate.name}: {candidate.votes} votes")

    def voter_status(self, voter_id):
        if voter_id not in self.voters:
            print("Voter not registered.")
            return
        voter = self.voters[voter_id]
        status = "has voted." if voter.has_voted else "has not voted yet."
        print(f"Voter {voter.name} {status}")


def main():
    system = VotingSystem()

    while True:
        print("\nOnline Voting System")
        print("1. Register Voter")
        print("2. Add Candidate")
        print("3. Vote")
        print("4. Show Results")
        print("5. Check Voter Status")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            voter_id = input("Enter voter ID: ")
            name = input("Enter voter name: ")
            system.register_voter(voter_id, name)
        elif choice == '2':
            candidate_id = input("Enter candidate ID: ")
            name = input("Enter candidate name: ")
            system.add_candidate(candidate_id, name)
        elif choice == '3':
            voter_id = input("Enter your voter ID: ")
            candidate_id = input("Enter candidate ID to vote for: ")
            system.vote(voter_id, candidate_id)
        elif choice == '4':
            system.results()
        elif choice == '5':
            voter_id = input("Enter voter ID to check status: ")
            system.voter_status(voter_id)
        elif choice == '6':
            print("Exiting Voting System...........")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
          
