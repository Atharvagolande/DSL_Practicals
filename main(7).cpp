#include <iostream>
#include <string>
using namespace std;

// Define structure for a node
struct Node {
    int prn;
    string name;
    Node* next;

    Node(int p, string n) : prn(p), name(n), next(nullptr) {}
};

// Class to manage the club
class PinnacleClub {
private:
    Node* head;

public:
    PinnacleClub() : head(nullptr) {}

    // Function to add a member (president, secretary, or regular member)
    void addMember(int prn, string name, char position) {
        Node* newNode = new Node(prn, name);

        if (position == 'P') { // Add as president
            newNode->next = head;
            head = newNode;
        } else if (position == 'S') { // Add as secretary
            if (head == nullptr) {
                head = newNode;
            } else {
                Node* temp = head;
                while (temp->next != nullptr) {
                    temp = temp->next;
                }
                temp->next = newNode;
            }
        } else { // Add as regular member
            if (head == nullptr) {
                cout << "Add a president first.\n";
                delete newNode;
                return;
            }
            Node* temp = head;
            while (temp->next != nullptr && temp->next->next != nullptr) {
                temp = temp->next;
            }
            newNode->next = temp->next;
            temp->next = newNode;
        }
    }

    // Function to delete a member (by PRN)
    void deleteMember(int prn) {
        if (head == nullptr) {
            cout << "The list is empty.\n";
            return;
        }

        Node* temp = head;

        if (temp->prn == prn) { // Delete president
            head = temp->next;
            delete temp;
            return;
        }

        Node* prev = nullptr;
        while (temp != nullptr && temp->prn != prn) {
            prev = temp;
            temp = temp->next;
        }

        if (temp == nullptr) {
            cout << "Member with PRN " << prn << " not found.\n";
            return;
        }

        prev->next = temp->next;
        delete temp;
    }

    // Function to count total members
    int countMembers() const {
        int count = 0;
        Node* temp = head;
        while (temp != nullptr) {
            count++;
            temp = temp->next;
        }
        return count;
    }

    // Function to display members
    void displayMembers() const {
        if (head == nullptr) {
            cout << "The club has no members.\n";
            return;
        }

        cout << "Club Members:\n";
        Node* temp = head;
        while (temp != nullptr) {
            cout << "PRN: " << temp->prn << ", Name: " << temp->name << "\n";
            temp = temp->next;
        }
    }

    // Function to concatenate two linked lists
    void concatenate(PinnacleClub& other) {
        if (head == nullptr) {
            head = other.head;
        } else {
            Node* temp = head;
            while (temp->next != nullptr) {
                temp = temp->next;
            }
            temp->next = other.head;
        }
        other.head = nullptr; // Clear the other list
    }

    ~PinnacleClub() {
        while (head != nullptr) {
            Node* temp = head;
            head = head->next;
            delete temp;
        }
    }
};

int main() {
    PinnacleClub division1;
    PinnacleClub division2;

    int choice;
    do {
        cout << "\n1. Add Member to Division 1\n";
        cout << "2. Add Member to Division 2\n";
        cout << "3. Display Members of Division 1\n";
        cout << "4. Display Members of Division 2\n";
        cout << "5. Concatenate Division 2 into Division 1\n";
        cout << "6. Delete Member from Division 1\n";
        cout << "7. Count Members in Division 1\n";
        cout << "8. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
        case 1: {
            int prn;
            string name;
            char position;
            cout << "Enter PRN: ";
            cin >> prn;
            cin.ignore(); // Ignore newline
            cout << "Enter Name: ";
            getline(cin, name);
            cout << "Enter Position (P: President, S: Secretary, M: Member): ";
            cin >> position;
            division1.addMember(prn, name, position);
            break;
        }
        case 2: {
            int prn;
            string name;
            char position;
            cout << "Enter PRN: ";
            cin >> prn;
            cin.ignore(); // Ignore newline
            cout << "Enter Name: ";
            getline(cin, name);
            cout << "Enter Position (P: President, S: Secretary, M: Member): ";
            cin >> position;
            division2.addMember(prn, name, position);
            break;
        }
        case 3:
            cout << "\nDivision 1 Members:\n";
            division1.displayMembers();
            break;
        case 4:
            cout << "\nDivision 2 Members:\n";
            division2.displayMembers();
            break;
        case 5:
            division1.concatenate(division2);
            cout << "\nDivision 2 concatenated into Division 1.\n";
            break;
        case 6: {
            int prn;
            cout << "Enter PRN to delete: ";
            cin >> prn;
            division1.deleteMember(prn);
            break;
        }
        case 7:
            cout << "\nTotal members in Division 1: " << division1.countMembers() << "\n";
            break;
        case 8:
            cout << "Exiting...\n";
            break;
        default:
            cout << "Invalid choice!\n";
        }
    } while (choice != 8);

    return 0;