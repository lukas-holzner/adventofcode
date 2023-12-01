package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
)

func main() {
	winner_map := map[string]int{
        "A X": 3+0,
        "A Y": 1+3,
        "A Z": 2+6,
        "B X": 1+0,
        "B Y": 2+3,
        "B Z": 3+6,
        "C X": 2+0,
        "C Y": 3+3,
        "C Z": 1+6,
	}

    f, err := os.Open("2/input.txt")

    if err != nil {
        log.Fatal(err)
    }

    defer f.Close()
	totalsum := 0
    scanner := bufio.NewScanner(f)
    for scanner.Scan() {
        totalsum += winner_map[scanner.Text()]
    }

	fmt.Println("Total Sum: ", totalsum)

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }
}