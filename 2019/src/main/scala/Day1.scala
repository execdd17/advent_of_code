class Day1Puzzle(inputLoc: String) extends Puzzle(inputLoc) {
  def getRequiredFuelAmount(currentMass: Int, fuelValues: List[Int], totalRequired: Int): Int = {
    if (currentMass <= 6) // 6 or less ends up being <= 0
      return totalRequired
    val fuelRequired = math.floor(currentMass / 3.0).toInt - 2
    return getRequiredFuelAmount(fuelRequired, fuelValues:::List(fuelRequired), totalRequired + fuelRequired)
  }

  override def solve(): Int = {
    val numbers = inputLines.map(_.toInt)

    numbers.foldLeft(0) { (memo, number) =>
      memo + getRequiredFuelAmount(currentMass = number, fuelValues = List.empty[Int], totalRequired = 0)
    }
  }
}

object Day1 {
  def main(args: Array[String]): Unit = {
    val runner = new Day1Puzzle("day1_input.txt")
    println(runner.solve())
  }
}


