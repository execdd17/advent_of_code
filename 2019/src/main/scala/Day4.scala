import scala.collection.mutable.ArrayBuffer

class Day4Puzzle(inputLoc: String) extends Puzzle(inputLoc) {
  val matches = ArrayBuffer.empty[String]

  private def evaluateCandidate(value: String): Boolean = {
    var doesNotDecrease = true
    val digitMap = collection.mutable.Map(
      '0' -> 0, '1' -> 0, '2' -> 0, '3' -> 0,
      '4' -> 0, '5' -> 0, '6' -> 0, '7' -> 0,
      '8' -> 0, '9' -> 0
    )

    for (i <- 0 until value.length) {
      if (i + 1 < value.length) {
        if (value(i) == value(i + 1))
          digitMap(value(i)) = digitMap(value(i)) + 1
        if (value(i + 1).toInt < value(i).toInt)
          doesNotDecrease = false
      }
    }

    val adjacentMatches = digitMap.find(pair => pair._2 > 0 && pair._2 == 1)
    doesNotDecrease && adjacentMatches.nonEmpty
  }

  override def solve(): Int = {
    val Array(min, max) = inputLines.head.split('-')

    for (candidate <- min.toInt to max.toInt) {
      if (evaluateCandidate(candidate.toString)) {
        matches += candidate.toString
      }
    }

    matches.length
  }
}

object Day4 {
  def main(args: Array[String]): Unit = {
    val runner = new Day4Puzzle("day4_input.txt")
    println(runner.solve())
  }
}