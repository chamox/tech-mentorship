package main

import (
	"io/ioutil"
	"os"
	"strconv"
	"strings"
	"log"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func numIslands(grid [][]string) int {
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
		id := strings.Split(dirs[i].Name(), "_")[len(strings.Split(dirs[i].Name(), "_"))-2][0:1]

		dat, err := os.ReadFile("matrices/" + dirs[i].Name())
		check(err)

		initial_array := strings.Split(string(dat), ",")

		rows := len(initial_array) / cols

		matrix := make([][]string, rows)

		for i := 0; i < len(matrix); i++ {
			matrix[i] = make([]string, cols)
		}


		// ahora debo formar las matrices

		actual_row := 0
		actual_col := 0

		for i := 0; i < len(initial_array); i++ {
			matrix[actual_row][actual_col] = initial_array[i]

			if actual_col < cols-1 {
				actual_col += 1
			} else {
				actual_row += 1
				actual_col = 0
			}

		}

		res := numIslands(matrix)

		f, err := os.Create("respuestas/numberOfIslands_"+id+".txt")

		if err != nil {
			log.Fatal(err)
		}
	
		defer f.Close()
	
		_, err2 := f.WriteString(strconv.Itoa(res))
	
		if err2 != nil {
			log.Fatal(err2)
		}

	}

}
