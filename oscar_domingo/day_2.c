#include "advent.h"

int main(void)
{
	int valid_passwords = 0;

    FILE * file_pointer;
    char * line = NULL;
    size_t line_length = 0;
    size_t read;

    file_pointer = fopen("day_2_input.txt", "r");
    if (file_pointer == NULL)
        exit(EXIT_FAILURE);

    while ((read = getline(&line, &line_length, file_pointer)) != -1) {
        if (check_for_password(line) == 0) {
        	valid_passwords++;
        }
    }

    fclose(file_pointer);
    if (line)
        free(line);

    printf("The number of valid passwords is: %d", valid_passwords);
	return 0;
}

int check_for_password(char * line) {
	// Unpack the line string into the things we need
	char min[3];
	char max[3];
	char letter[2];
	char password [20];

	int dash_separator_index;
	int colon_separator_index;
	int line_length = strlen(line);

	for (int i = 0; i < line_length; i++) {
		if (line[i] == '-') {
			dash_separator_index = i;
		} else if (line[i] == ':') {
			colon_separator_index = i;
		}
	}

	for (int i = 0; i <= dash_separator_index; i++) {
		if (i == dash_separator_index){
			min[i] = '\0';
		} else {
			min[i] = line[i];
		}
	}

	int max_counter = 0;
	int end_of_max_index = (colon_separator_index - 2);
	for (int i = dash_separator_index + 1; i <= (colon_separator_index - 2); i++) {
		if (i == end_of_max_index) {
			max[max_counter] = '\0';
		} else {
			max[max_counter] = line[i];
			max_counter++;
		}
	}

	letter[0] = line[(colon_separator_index - 1)];
	letter[1] = '\0';


	int password_start_index = colon_separator_index + 2;

	strncpy(password, line + password_start_index, line_length - 2);
	// For the love of me, I can't get why strncpy is adding an extra newline at the end?
	// I think it might have to do with `getline`

	int is_password_valid = part2_check_password_validity(atoi(min), atoi(max), letter, password);

	return is_password_valid;

}


int part1_check_password_validity(int min, int max, char *letter, char *password) {
	// Perform the actual validity check
	int times_seen_letter = 0;

	for (int i = 0; i < strlen(password); i++){
		if (password[i] == letter[0]) {
			times_seen_letter++;
		}
	}

	if (min <= times_seen_letter && times_seen_letter <= max) {
		return 0;
	} else {
		return 1;
	}
}

int part2_check_password_validity(int min, int max, char *letter, char *password) {
	// Given the same example list from above:

	// 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
	// 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
	// 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
	int min_from_zero = min - 1;
	int max_from_zero = max - 1;

	int is_it_valid = 1;

	for (int i = 0; i < strlen(password); i++){
		if (i == min_from_zero && password[i] == letter[0]) {
			is_it_valid = 0;
		}

		if (i == max_from_zero && password[i] == letter[0]) {
			if (is_it_valid == 1) {
				is_it_valid = 0;
			} else {
				is_it_valid = 1;
			}
		}
	}

	return is_it_valid;
}