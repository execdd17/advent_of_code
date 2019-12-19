import scala.collection.mutable.ArrayBuffer

case class Cell(wireNum: Int, representation:  Char)

class Day3Puzzle(inputLoc: String) extends Puzzle(inputLoc) {

  val wire1Movements: Array[String] = inputLines.head.split(',')
  val wire2Movements: Array[String] = inputLines(1).split(',')
  val numRows = 500
  val numCols = 500
  val originRow = 250
  val originCol = 250
  val matrix: Array[Array[Int]] = Array.ofDim[Int](numRows,numCols)
  matrix(originRow)(originCol) = -1

  private def printMatrix(): Unit = {
    for (row <- 0 until numRows) {
      for (column <- 0 until numCols) {
        matrix(row)(column) match {
          case -1 => print("O")
          case 0 => print(".")
          case 1 => print("*")
          case 2 => print("X")
        }
      }
      println()
    }
  }

  private def populateWire(movements: Array[String]): Unit = {
    var currRow = originRow
    var currCol = originCol
    movements.foreach { movement =>
      val amount = movement.substring(1).toInt

      movement(0) match {
        case 'U' =>
          for (i <- 1 to amount) {
            matrix(currRow - i)(currCol) = matrix(currRow - i)(currCol) + 1
          }
          currRow -= amount
        case 'D' =>
          for (i <- 1 to amount) {
            matrix(currRow + i)(currCol) = matrix(currRow + i)(currCol) + 1
          }
          currRow += amount
        case 'L' =>
          for (i <- 1 to amount) {
            matrix(currRow)(currCol - i) = matrix(currRow)(currCol - i) + 1
          }
          currCol -= amount
        case 'R' =>
          for (i <- 1 to amount) {
            matrix(currRow)(currCol + i) = matrix(currRow)(currCol + i) + 1
          }
          currCol += amount
        case _ => throw new IllegalArgumentException("Invalid state")
      }
    }
  }

  private def getShortestIntersectionDistance: Int = {
    var shortest = Int.MaxValue
    val list = ArrayBuffer.empty[Int]

    for (row <- 0 until numRows) {
      for (column <- 0 until numCols) {
        if (matrix(row)(column) == 2) {
          val distance = math.abs(originRow - row) + math.abs(originCol - column)
          list += distance
          println(s"Distance: $distance Origin: ($originRow)($originCol) Intersection: ($row)($column)")
          if (distance < shortest) {
            shortest = distance
          }
        }
      }
    }

    println(list.sorted)
    shortest
  }

  override def solve(): Int = {
    val w1 = Array("R75","D30","R83","U83","L12","D49","R71","U7","L72")
    val w2 = Array("U62","R66","U55","R34","D71","R55","D58","R83")

//    val w1 = Array("R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51")
//    val w2 = Array("U98","R91","D20","R16","D67","R40","U7","R15","U6","R7")

    populateWire(w1)
    populateWire(w2)
//    printMatrix()
    getShortestIntersectionDistance
  }
}

object Day3 {
  def main(args: Array[String]): Unit = {
    val runner = new Day3Puzzle("day3_input.txt")
    println(runner.solve())
  }
}


