case class Cell(wireNum: Int, representation:  Char)

class Day3Puzzle(inputLoc: String) extends Puzzle(inputLoc) {

  val wire1Movements: Array[String] = inputLines.head.split(',')
  val wire2Movements: Array[String] = inputLines(1).split(',')
  val numRows = 30
  val numCols = 30
  val originRow = 15
  val originCol = 15
  val matrix: Array[Array[Cell]] = Array.ofDim[Cell](numRows,numCols)

  for (i <- 0 until numRows) {
    for (j <- 0 until numCols) {
      matrix(i)(j) = Cell(0, '.')
    }
  }

  matrix(originCol)(originRow) = Cell(0, 'O')

  private def printMatrix(): Unit = {
    for (row <- 0 until numRows) {
      for (column <- 0 until numCols) {
        print(matrix(row)(column).representation)
      }
      println()
    }
  }

  private def populateWire(wireNum: Int, movements: Array[String]): Unit = {
    var currRow = originRow
    var currCol = originCol

    movements.foreach { movement =>
      val amount = movement.substring(1).toInt

      movement(0) match {
        case 'U' =>
          for (i <- 1 to amount) {
            matrix(currRow - i)(currCol) = Cell(wireNum, '|')
          }
          currRow -= amount
          matrix(currRow)(currCol) = Cell(wireNum, '+')
        case 'D' =>
          for (i <- 1 to amount) {
            matrix(currRow + i)(currCol) = Cell(wireNum, '|')
          }
          currRow += amount
          matrix(currRow)(currCol) = Cell(wireNum, '+')
        case 'L' =>
          for (i <- 1 to amount) {
            matrix(currRow)(currCol - i) = Cell(wireNum, '-')
          }
          currCol -= amount
          matrix(currRow)(currCol) = Cell(wireNum, '+')
        case 'R' =>
          for (i <- 1 to amount) {
            matrix(currRow)(currCol + i) = Cell(wireNum, '-')
          }
          currCol += amount
          matrix(currRow)(currCol) = Cell(wireNum, '+')
        case _ => throw new IllegalArgumentException("Invalid state")
      }
    }
  }

  override def solve(): Int = {
//    val w1 = Array("R75","D30","R83","U83","L12","D49","R71","U7","L72")
//    val w2 = Array("U62","R66","U55","R34","D71","R55","D58","R83")
    val w1 = Array("R8","U5","L5","D3")
    val w2 = Array("U7","R6","D4","L4")
    populateWire(1,w1)
    populateWire(2,w2)
    printMatrix()
    10000
  }
}

object Day3 {
  def main(args: Array[String]): Unit = {
    val runner = new Day3Puzzle("day3_input.txt")
    println(runner.solve())
  }
}


