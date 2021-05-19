//C:\Users\Vicky\Desktop\Repository\Algorithms\Data Structure\Doubly Linked List\C++

#include <stdio.h>

struct node{
	
	int data;
	struct node *next;
	struct node *prev;
};

struct node *head, *tail;

void createDLL(){
	
	struct node *newnode;
	head = 0;
	
//	printf("%d\n", head);
//	getch();
	
	int choice;
	
	do{
		newnode = (struct node*) malloc(sizeof(struct node));
		
		printf("\nEnter data : ");
		scanf("%d", &newnode -> data);
		
		newnode -> prev = NULL, newnode -> next = NULL;
		
		if(head == NULL){
			head = tail = newnode;
		}
		
		else{
			tail -> next = newnode;
			newnode -> prev = tail;
			tail = newnode;
		}
		
		printf("\nWant to create more nodes ? (1/0) : ");
		scanf("%d", &choice);
		
	}while(choice);
}

void display() {
	
   struct node *ptr;
   ptr = head;
   
   printf("\n");
   while(ptr != NULL) {
   	
      printf("%d >> ", ptr->data);
      ptr = ptr->next;
   }
   
   printf("\n");
}

int main()
{
	createDLL();
	display();
	return 0;
}
