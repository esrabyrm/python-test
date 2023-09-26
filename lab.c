#include <stdio.h>
#include <stdlib.h>

int find_max(int arr[], int size) {
    int max = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

int find_min(int arr[], int size) {
    int min = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] < min) {
            min = arr[i];
        }
    }
    return min;
}

int find_diff(int arr[], int size) {
    int max = find_max(arr, size);
    int min = find_min(arr, size);
    return max - min;
}

int find_sum_before_min(int arr[], int size) {
    int min = find_min(arr, size);
    int sum = 0;
    for (int i = 0; i < size; i++) {
        if (arr[i] == min) {
            break;
        }
        sum += arr[i];
    }
    return sum;
}

int main() {
    int choice;
    printf("Enter a choice (0, 1, 2, 3): ");
    scanf("%d", &choice);

    int size;
    do {
        printf("Enter the size of the array (1-100): ");
        scanf("%d", &size);
    } while (size < 1 || size > 100);

    int data[100];
    printf("Enter %d integers separated by spaces: ", size);
    for (int i = 0; i < size; i++) {
        scanf("%d", &data[i]);
    }

    switch (choice) {
        case 0:
            printf("Maximum number in the array: %d\n", find_max(data, size));
            break;
        case 1:
            printf("Minimum number in the array: %d\n", find_min(data, size));
            break;
        case 2:
            printf("The difference between maximum and minimum: %d\n", find_diff(data, size));
            break;
        case 3:
            printf("Sum of numbers before the first minimum in the array: %d\n", find_sum_before_min(data, size));
            break;
        default:
            printf("Invalid input");
    }

    return 0;
}
