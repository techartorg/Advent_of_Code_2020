#include "advent.h"

int input_length = sizeof day_1_input / sizeof day_1_input[0];



int main() {
	find_two_that_sum_2020();
	find_three_that_sum_2020();
	return 0;
}

void find_two_that_sum_2020() {
	int entries_that_sum_2020[2];
	
	int found = 1;

	for(int i = 0; i < input_length; i++) {
		for(int j = 0; j < input_length; j++) {
			if (found != 0) {
				if ((day_1_input[i] + day_1_input[j]) == 2020) {
					entries_that_sum_2020[0] = day_1_input[i];
					entries_that_sum_2020[1] = day_1_input[j];
					found = 0;
				}
			}
		}
	}

	if (found == 0) {
		printf("The three entries that sum 2020 are\n%d and %d\n", entries_that_sum_2020[0], entries_that_sum_2020[1]);
		printf("Which multiplied they give: %d\n\n", (entries_that_sum_2020[0] * entries_that_sum_2020[1]));
	} else {
		printf("Could not find any two that sum 2020 :(\n");
	}
}

void find_three_that_sum_2020() {
	int entries_that_sum_2020[3];
	
	int found = 1;

	for(int i = 0; i < input_length; i++) {
		for(int j = 0; j < input_length; j++) {
			for(int k = 0; k < input_length; k++){
				if (found != 0) {
					if ((day_1_input[i] + day_1_input[j] + day_1_input[k]) == 2020) {
						entries_that_sum_2020[0] = day_1_input[i];
						entries_that_sum_2020[1] = day_1_input[j];
						entries_that_sum_2020[2] = day_1_input[k];
						found = 0;
					}
				}
			}
		}
	}

	if (found == 0) {
		printf("The two entries that sum 2020 are\n%d, %d and %d\n", entries_that_sum_2020[0], entries_that_sum_2020[1], entries_that_sum_2020[2]);
		printf("Which multiplied they give: %d\n\n", (entries_that_sum_2020[0] * entries_that_sum_2020[1] * entries_that_sum_2020[2]));
	} else {
		printf("Could not find any two that sum 2020 :(\n");
	}
}