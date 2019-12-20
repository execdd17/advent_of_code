import scala.collection.mutable.ArrayBuffer

case class Position(row: Int, column:  Int)

class Day3Puzzle(inputLoc: String) extends Puzzle(inputLoc) {

  val wire1Paths = ArrayBuffer.empty[Position]
  val wire2Paths = ArrayBuffer.empty[Position]

  private def populateWire(movements: Array[String], paths: ArrayBuffer[Position]): Unit = {
    var currRow = 0
    var currCol = 0

    movements.foreach { movement =>
      val amount = movement.substring(1).toInt

      movement(0) match {
        case 'U' =>
          for (i <- 1 to amount) {
            paths += Position(currRow - i, currCol)
          }
          currRow -= amount
        case 'D' =>
          for (i <- 1 to amount) {
            paths += Position(currRow + i, currCol)
          }
          currRow += amount
        case 'L' =>
          for (i <- 1 to amount) {
            paths += Position(currRow, currCol - i)
          }
          currCol -= amount
        case 'R' =>
          for (i <- 1 to amount) {
            paths += Position(currRow, currCol + i)
          }
          currCol += amount
        case _ => throw new IllegalArgumentException("Invalid state")
      }
    }
  }

  private def getShortestManhattanDistance(positions: Set[Position]): Int = {
    var shortest = Int.MaxValue

    positions.foreach { position =>
      val distance = math.abs(0 - position.row) + math.abs(0 - position.column)
      if (distance < shortest)
        shortest = distance
    }

    shortest
  }

  private def getQuickestIntersectionSum(positions: Set[Position]): Int = {
    var shortest = Int.MaxValue

    positions.foreach {  position =>
      val distance = (wire1Paths.indexOf(position) + 1) + (wire2Paths.indexOf(position)) + 1
      if (distance < shortest)
        shortest = distance
    }

    shortest
  }

  override def solve(): Int = {
//    val w1 = Array("R75","D30","R83","U83","L12","D49","R71","U7","L72")
//    val w2 = Array("U62","R66","U55","R34","D71","R55","D58","R83")
//
//    val w1 = Array("R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51")
//    val w2 = Array("U98","R91","D20","R16","D67","R40","U7","R15","U6","R7")

    val w1: Array[String] = inputLines.head.split(',')
    val w2: Array[String] = inputLines(1).split(',')

    populateWire(w1, wire1Paths)
    populateWire(w2, wire2Paths)
    val intersections = wire1Paths.toSet.intersect(wire2Paths.toSet)
//    getShortestManhattanDistance(intersections)
    getQuickestIntersectionSum(intersections)
  }
}

object Day3 {
  def main(args: Array[String]): Unit = {
    val runner = new Day3Puzzle("day3_input.txt")
    println(runner.solve())
  }
}


