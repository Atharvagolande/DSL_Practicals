#include <iostream>
using namespace std;

#define MAX 100

class Deque {
private:
    int arr[MAX];
    int front;
    int rear;

public:
    
    Deque() {
        front = -1;
        rear = -1;
    }

    
    bool isEmpty() {
        return front == -1;
    }

    
    bool isFull() {
        return (front == 0 && rear == MAX - 1) || (rear + 1 == front);
    }

    
    void addFront(int data) {
        if (isFull()) {
            cout << "Deque is full! Cannot add element at front." << endl;
            return;
        }
        if (isEmpty()) { 
            front = rear = 0;
        } else if (front == 0) {
            front = MAX - 1; 
        } else {
            front--;
        }
        arr[front] = data;
        cout << "Added " << data << " at the front." << endl;
    }

    
    void addRear(int data) {
        if (isFull()) {
            cout << "Deque is full! Cannot add element at rear." << endl;
            return;
        }
        if (isEmpty()) { 
            front = rear = 0;
        } else if (rear == MAX - 1) {
            rear = 0; 
        } else {
            rear++;
        }
        arr[rear] = data;
        cout << "Added " << data << " at the rear." << endl;
    }

    
    void deleteFront() {
        if (isEmpty()) {
            cout << "Deque is empty! Cannot delete element from front." << endl;
            return;
        }
        cout << "Deleted " << arr[front] << " from the front." << endl;
        if (front == rear) {
            front = rear = -1;
        } else if (front == MAX - 1) {
            front = 0; 
        } else {
            front++;
        }
    }

    
    void deleteRear() {
        if (isEmpty()) {
            cout << "Deque is empty! Cannot delete element from rear." << endl;
            return;
        }
        cout << "Deleted " << arr[rear] << " from the rear." << endl;
        if (front == rear) { 
            front = rear = -1;
        } else if (rear == 0) {
            rear = MAX - 1; 
        } else {
            rear--;
        }
    }

    
    void display() {
        if (isEmpty()) {
            cout << "Deque is empty!" << endl;
            return;
        }
        cout << "Elements in the deque are: ";
        int i = front;
        while (true) {
            cout << arr[i] << " ";
            if (i == rear)
                break;
            i = (i + 1) % MAX; 
        }
        cout << endl;
    }
};


int main() {
    Deque deque;
    int choice, data;

    do {
        cout << "\nDeque Operations:\n";
        cout << "1. Add Front\n";
        cout << "2. Add Rear\n";
        cout << "3. Delete Front\n";
        cout << "4. Delete Rear\n";
        cout << "5. Display\n";
        cout << "6. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
        case 1:
            cout << "Enter value to add at front: ";
            cin >> data;
            deque.addFront(data);
            break;
        case 2:
            cout << "Enter value to add at rear: ";
            cin >> data;
            deque.addRear(data);
            break;
        case 3:
            deque.deleteFront();
            break;
        case 4:
            deque.deleteRear();
            break;
        case 5:
            deque.display();
            break;
        case 6:
            cout << "Exiting program." << endl;
            break;
        default:
            cout << "Invalid choice. Please try again." << endl;
        }
    } while (choice != 6);

    return 0;
}
