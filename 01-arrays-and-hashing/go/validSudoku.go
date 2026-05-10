package main

// To be valid:
// Row must contain 1-9 unique values
// column must contain 1-9 unique values
// 3x3 grid must contain 1-9 unique values

func isValidSudoku(board [][]byte) bool {

	rows := make([]map[byte]bool, 9)
	columns := make([]map[byte]bool, 9)
	boxes := make([]map[byte]bool, 9)

	//initialise maps

	for i := range 9 {
		rows[i] = make(map[byte]bool)
		columns[i] = make(map[byte]bool)
		boxes[i] = make(map[byte]bool)
	}

	// loop through board
	for r := range 9 {
		for c := range 9 {

			val := board[r][c]

			// Skip the empty values
			if val == '.' {
				continue
			}

			// find out 3x3 box

			boxIndex := (r/3)*3 + c/3

			// duplicate found
			if rows[r][val] || columns[c][val] || boxes[boxIndex][val] {
				return false
			}

			// mark as seen

			rows[r][val] = true
			columns[c][val] = true
			boxes[boxIndex][val] = true
		}
	}

	return true

}

