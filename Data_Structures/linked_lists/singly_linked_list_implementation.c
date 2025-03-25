#include <stdio.h>
#include <stdlib.h>
#include "ak_utils.h"  // Include ak_utils.h

#define CURRENT_PROGRAM_NAME "Singly Linked list"

// Define the structure for a linked list node
struct Node {
    int data;
    struct Node* next;
};

// Function to create a new node
struct Node* getNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (!newNode) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Function to insert a node at the end
void insertEnd(struct Node** head, int data) {
    struct Node* newNode = getNode(data);
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    struct Node* temp = *head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = newNode;
}

// Function to delete a node by value
void deleteNode(struct Node** head, int key) {
    struct Node* temp = *head, *prev = NULL;
    if (temp != NULL && temp->data == key) {
        *head = temp->next;
        free(temp);
        return;
    }
    while (temp != NULL && temp->data != key) {
        prev = temp;
        temp = temp->next;
    }
    if (temp == NULL) {
        printf("Node with value %d not found.\n", key);
        return;
    }
    prev->next = temp->next;
    free(temp);
}

// Function to display the linked list
void displayList(struct Node* head) {
    struct Node* temp = head;
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

int main() {

    set_program_name(CURRENT_PROGRAM_NAME);
    print_provenance();  // Call provenance function

    struct Node* head = NULL;
    int choice, value;

     while (1) {
        printf("\nSingly Linked List Operations Menu:\n");
        printf("1. Insert at End\n");
        printf("2. Delete a Node\n");
        printf("3. Display List\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        //scanf("%d", &choice); 
        if (scanf("%d", &choice) != 1) {  // Validate integer input
            printf("Invalid input! Please enter an integer.\n");
            clear_input_buffer();  // Clear buffer to prevent infinite loop
            return 0;
        }

        switch (choice) {
            case 1:
                printf("Enter value to insert: ");
                if (scanf("%d", &value) != 1) {  // Validate integer input
                    printf("Invalid input! Please enter an integer.\n");
                    clear_input_buffer();  // Clear buffer to prevent infinite loop
                    return 0;
                }
                //scanf("%d", &value);
                insertEnd(&head, value);
                break;
            case 2:
                printf("Enter value to delete: "); 
                if (scanf("%d", &value) != 1) {  // Validate integer input
                    printf("Invalid input! Please enter an integer.\n");
                    clear_input_buffer();  // Clear buffer to prevent infinite loop
                    return 0;
                }
                //scanf("%d", &value); 
                deleteNode(&head, value);
                break;
            case 3:
                printf("Linked List: ");
                displayList(head);
                break;
            case 4:
                printf("Exiting...\n");
                exit(0);
            default:
                printf("Invalid choice! Try again.\n");
        }
     }
    return 0;
}
