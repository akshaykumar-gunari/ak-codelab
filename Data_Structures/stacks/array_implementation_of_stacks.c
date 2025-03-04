#include <stdio.h>
#include <stdlib.h>
#include "ak_utils.h"  // Include ak_utils.h

#define MAX 100

// Stack structure definition
typedef struct {
    int top;
    int items[MAX];
} Stack;

// Function to initialize the stack
void init_stack(Stack *s) {
    s->top = -1;
}

// Function to check if the stack is full
int is_stack_full(Stack *s) {
    return s->top == MAX - 1;
}

// Function to check if the stack is empty
int is_stack_empty(Stack *s) {
    return s->top == -1;
}

// Function to push an element onto the stack
void push(Stack *s, int value) {
    if (is_stack_full(s)) {
        printf("Stack Overflow!\n");
        return;
    }
    s->items[++(s->top)] = value;
}

// Function to pop an element from the stack
int pop(Stack *s) {
    if (is_stack_empty(s)) {
        printf("Stack Underflow!\n");
        return -1;
    }
    return s->items[(s->top)--];
}

// Function to display stack elements in a structured format
void display_stack(Stack *s) {
    if (is_stack_empty(s)) {
        printf("Stack is empty.\n");
        return;
    }

    printf("\nStack (Top -> Bottom):\n");
    printf("----------------------\n");

    for (int i = s->top; i >= 0; i--) {
        printf("| %-4d |\n", s->items[i]);  // Left-aligned inside the box
        printf("--------\n");
    }

    printf("\n");
}


int main() {
    print_provenance();  // Call provenance function

    Stack s;
    init_stack(&s);

    int choice, value;

    while (1) {
        printf("\nStack Operations Menu:\n");
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Display\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        if (scanf("%d", &choice) != 1) {  // Validate integer input
            printf("Invalid input! Please enter an integer.\n");
            clear_input_buffer();  // Clear buffer to prevent infinite loop
            return 0;
        }
        switch (choice) {
            case 1:
                printf("Enter value to push: ");
                //scanf("%d", &value);
                if (scanf("%d", &value) != 1) {  // Validate integer input
                    printf("Invalid input! Please enter an integer.\n");
                    clear_input_buffer();  // Clear buffer to prevent infinite loop
                    return 0;
                }
                push(&s, value);
                break;
            case 2:
                value = pop(&s);
                if (value != -1) {
                    printf("Popped value: %d\n", value);
                }
                break;
            case 3:
                display_stack(&s);
                break;
            case 4:
                printf("Exiting...\n");
                return 0;
            default:
                printf("Invalid choice! Try again.\n");
        }
    }

    return 0;
}
