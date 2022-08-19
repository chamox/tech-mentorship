package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func numIslands2(grid [][]string) int {
	var queue [][]int
	res := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			if grid[i][j] == "1" {
				queue = append(queue, []int{i, j})
				for len(queue) > 0 {
					row, col := queue[0][0], queue[0][1]
					queue = queue[1:]
					if row > 0 && grid[row-1][col] == "1" {
						queue = append(queue, []int{row - 1, col})
						grid[row-1][col] = "0"
					}
					if row < len(grid)-1 && grid[row+1][col] == "1" {
						queue = append(queue, []int{row + 1, col})
						grid[row+1][col] = "0"
					}
					if col > 0 && grid[row][col-1] == "1" {
						queue = append(queue, []int{row, col - 1})
						grid[row][col-1] = "0"
					}
					if col < len(grid[i])-1 && grid[row][col+1] == "1" {
						queue = append(queue, []int{row, col + 1})
						grid[row][col+1] = "0"
					}
				}
				res++
			}
		}
	}
	return res
}

func main() {

	// Leemos el nombre de los archivos
	dirs, err := ioutil.ReadDir("matrices")
	check(err)

	//////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////
	// Leer todos los archivos ”.txt” que se encuentren en la carpeta ./matrices/. Se asume que la carpeta
	// existe al ejecutar el programa. Los archivos seguiran el formato "matriz {id} {cols}.txt", siendo id el
	// identificador unico de matriz y cols el numero de columnas de la matriz.
	//
	// El numero de filas se deduce con
	// el tamano total dividido al numero de columnas. Si la carpeta esta vacia, levante una alarma y detenga la
	// ejecucion. Los archivos siempre tendran matrices M x N validas.
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////

	for i := 0; i < len(dirs); i++ {

		// Obtengo las columnas y las convierto a int
		cols, err := strconv.Atoi(strings.Split(dirs[i].Name(), "_")[len(strings.Split(dirs[i].Name(), "_"))-1][0:1])

		// Obtengo el id como string
		// id := strings.Split(dirs[i].Name(), "_")[len(strings.Split(dirs[i].Name(), "_"))-2][0:1]

		dat, err := os.ReadFile("matrices/" + dirs[i].Name())
		check(err)

		initial_array := strings.Split(string(dat), ",")

		rows := len(initial_array) / cols

		// fmt.Print(string(dat))
		// fmt.Print("\n")
		// fmt.Print(initial_array)
		// fmt.Print("\n")
		// fmt.Printf("%d", cols)
		// fmt.Print("\n")
		// fmt.Printf("%d", rows)
		// fmt.Print("\n")
		// fmt.Print(string(id))
		// fmt.Print("\n")

		matrix := make([][]string, rows)

		for i := 0; i < len(matrix); i++ {
			matrix[i] = make([]string, cols)
		}

		// fmt.Println(matrix)

		// ahora debo formar las matrices

		////////////////////////////////////////

		actual_row := 0
		actual_col := 0

		for i := 0; i < len(initial_array); i++ {
			matrix[actual_row][actual_col] = initial_array[i]
			// fmt.Print(initial_array[i])

			if actual_col < cols-1 {
				actual_col += 1
			} else {
				actual_row += 1
				actual_col = 0
			}

			// fmt.Printf("%d \n", actual_col)
			// fmt.Printf("%d \n", actual_row)

		}

		fmt.Println(matrix)

		res := numIslands2(matrix)
		fmt.Println(res)

		////////////////////////////////////////

		// fmt.Println(dirs[i].Name())
		// fmt.Println(dirs[i])
	}

	// f, err := os.Open("/tmp/dat")
	// check(err)

	// b1 := make([]byte, 5)
	// n1, err := f.Read(b1)
	// check(err)
	// fmt.Printf("%d bytes: %s\n", n1, string(b1[:n1]))

	// o2, err := f.Seek(6, 0)
	// check(err)
	// b2 := make([]byte, 2)
	// n2, err := f.Read(b2)
	// check(err)
	// fmt.Printf("%d bytes @ %d: ", n2, o2)
	// fmt.Printf("%v\n", string(b2[:n2]))

	// o3, err := f.Seek(6, 0)
	// check(err)
	// b3 := make([]byte, 2)
	// n3, err := io.ReadAtLeast(f, b3, 2)
	// check(err)
	// fmt.Printf("%d bytes @ %d: %s\n", n3, o3, string(b3))

	// _, err = f.Seek(0, 0)
	// check(err)

	// r4 := bufio.NewReader(f)
	// b4, err := r4.Peek(5)
	// check(err)
	// fmt.Printf("5 bytes: %s\n", string(b4))

	// f.Close()
}
