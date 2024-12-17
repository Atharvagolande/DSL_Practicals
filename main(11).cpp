#include <iostream>
#include <string>
using namespace std;

#define MAX 100

class JobQueue {
private:
    string jobs[MAX];
    int front;
    int rear;

public:
    
    JobQueue() : front(-1), rear(-1) {}

    
    bool isFull() {
        return rear == MAX - 1;
    }

    
    bool isEmpty() {
        return front == -1 || front > rear;
    }

    
    void addJob(const string& job) {
        if (isFull()) {
            cout << "Queue is full! Cannot add more jobs." << endl;
            return;
        }
        if (front == -1) front = 0; 
        jobs[++rear] = job;
        cout << "Job '" << job << "' added to the queue." << endl;
    }

    
    void deleteJob() {
        if (isEmpty()) {
            cout << "Queue is empty! No jobs to delete." << endl;
            return;
        }
        cout << "Job '" << jobs[front] << "' completed and removed from the queue." << endl;
        front++;
        if (front > rear) front = rear = -1; 
    }

    
    void displayJobs() {
        if (isEmpty()) {
            cout << "Queue is empty!" << endl;
            return;
        }
        cout << "Jobs in the queue:" << endl;
        for (int i = front; i <= rear; i++) {
            cout << jobs[i] << endl;
        }
    }
};

int main() {
    JobQueue jobQueue;
    int choice;
    string job;

    
    do {
        cout << "\nJob Queue Operations:\n";
        cout << "1. Add Job\n";
        cout << "2. Delete Job\n";
        cout << "3. Display Jobs\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
        case 1:
            cout << "Enter job name: ";
            cin.ignore(); // Clear the buffer before reading a string
            getline(cin, job);
            jobQueue.addJob(job);
            break;
        case 2:
            jobQueue.deleteJob();
            break;
        case 3:
            jobQueue.displayJobs();
            break;
        case 4:
            cout << "Exiting program." << endl;
            break;
        default:
            cout << "Invalid choice. Please try again." << endl;
        }
    } while (choice != 4);

    return 0;
}
