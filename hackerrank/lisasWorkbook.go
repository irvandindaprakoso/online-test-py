package main

import (
	"fmt"
	"math"
)

func workbook(n int32, k int32, arr []int32) int32 {
	page := int32(1)    // Starting page number
	chapter := int32(1) // Starting chapter number
	result := int32(0)  // Initialize the result to 0

	for chapter <= n {
		firstExercise := int32(1)                                                            // Starting exercise number for the current chapter
		lastExercise := int32(math.Min(float64(firstExercise+k-1), float64(arr[chapter-1]))) // Last exercise in the current chapter

		for firstExercise <= arr[chapter-1] {
			if firstExercise <= page && page <= lastExercise {
				result++ // Increment the result if the current exercise is on the current page
			}

			page++                                                                              // Move to the next page
			firstExercise += k                                                                  // Move to the next set of exercises in the chapter
			lastExercise = int32(math.Min(float64(firstExercise+k-1), float64(arr[chapter-1]))) // Update the last exercise for the current chapter if needed
		}

		chapter++ // Move to the next chapter
	}

	return result
}

func main() {
	n := int32(5)                  // Number of chapters
	k := int32(3)                  // Number of problems per page
	arr := []int32{4, 2, 6, 1, 10} // Array of problems per chapter

	result := workbook(n, k, arr)
	fmt.Println(result)
}
