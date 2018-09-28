# Advanced Python
A collection of various advanced Python projects I have completed

## Sounds Good!
A Python 2.0 project that manipulates sound. It can:

- [x] Change the audio file's speed (make it slower or faster).
- [x] Swap the two halves of an audio file and playing the resultant audio file.
- [x] Reverse the sound by redefining the new sample rate and playing it in reverse.
- [x] Change the volume of the sound by multiplying the number of samples.
- [x] Overlap the audio with a controllable static noise.
- [x] Take two audio files (each with different sample rates) and layers them into a new .wav file to play them both together. This function also has the capability of controlling the scale factor (volume) of each sound, so one sound will play a little louder than the other.
- [x] Add an echo to the sound file by adding a time delay.

## Game of Life
A Python 2.0 project which mimics Game of Life's rules:

1) Any live cell with fewer than two live neighbors dies, as if caused by underpopulation.
2) Any live cell with more than three live neighbors dies, as if by overcrowding.
3) Any live cell with two or three live neighbors lives on to the next generation.
4) Any dead cell with exactly three live neighbors becomes a live cell.

| Functions Created  | Description |
| ------------- | ------------- |
| def createOneRow(width)  | Returns one row of zeros of width "width"...   |
| def createBoard(width,height)  | Returns a 2d array of width and height  |
| def printBoard(A)  | Prints the 2d lost-of-lists: A, without spaces(using sys.stdout.write)  |
| def diagonalize(width, height)  | Creates an empty board and then modifies it so that it has a diagonal strip of "on" cells, but only in the *intereior* of the 2d array  |
| def innerCells(width, height)  | Returns a 2d array that has all live cells except for a one-cell-wide border of empty cells around the endge of the 2d array  |
| def randomCells(width, height)  | Returns an array of randomly-assigned 1's and 0's except that the outer edge of the array is still completely empty (all 0's)  |
| def copy(A)  | Accepts a 2d array: A, as its argument and it will return a new 2d array of data that has the same pattern as the original array  |
| def innerReverse(A)  | Takes an old 2d array (or "generation") and then creates a new generation of the same shape and size. |
| def countNeighbors(row, col, A)  | Returns the number of live neighbors for a cell in the board A at a particular row and col  |
| def next_life_generation(A)  | Makes a copy of A and then advances one generation of Game of Life within  the *inner cells* of that copy   |











