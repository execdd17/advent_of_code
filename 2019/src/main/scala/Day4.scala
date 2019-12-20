class Day4Puzzle(inputLoc: String) extends Puzzle(inputLoc) {

  private def evaluateCandidate(value: String): Boolean = {
    var twoAdjacentAreSame = false
    var doesNotDecrease = true

    for (i <- 0 until value.length) {
      if (i + 1 < value.length) {
        if (value(i) == value(i + 1))
          twoAdjacentAreSame = true
        if (value(i + 1).toInt < value(i).toInt)
          doesNotDecrease = false
      }
    }

    twoAdjacentAreSame && doesNotDecrease
  }

  override def solve(): Int = {
    val Array(min, max) = inputLines.head.split('-')
    var matches = 0

    for (candidate <- min.toInt to max.toInt) {
      if (evaluateCandidate(candidate.toString)) {
        println(s"Match found: $candidate")
        matches += 1
      }
    }

    matches
  }
}

object Day4 {
  def main(args: Array[String]): Unit = {
    val runner = new Day4Puzzle("day4_input.txt")
    println(runner.solve())
  }
}


