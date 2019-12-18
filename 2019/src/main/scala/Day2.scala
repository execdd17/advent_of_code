import scala.collection.mutable.ArrayBuffer

case class Solution(noun: Int, verb: Int)

class Day2Puzzle(inputLoc: String) extends Puzzle(inputLoc) {

  def findCombination(memory: ArrayBuffer[Int], target: Int): Option[Solution] = {
    for (noun <- 0 until 100) {
      for (verb <- 0 until 99) {
        val input = memory.clone()
        input(1) = noun
        input(2) = verb

        val result = runProgram(input)
        if (result == 19690720)
          return Some(Solution(noun, verb))
      }
    }

    None
  }

  def runProgram(input: ArrayBuffer[Int]): Int = {

    var start = 0
    var end = 4
    var continue = true

    while(continue) {
      val instruction = input.slice(start, end)
      instruction(0) match {
        case 99 => continue = false
        case 1 =>
          val result = input(instruction(1)) + input(instruction(2))
          input(instruction(3)) = result
        case 2 =>
          val result = input(instruction(1)) * input(instruction(2))
          input(instruction(3)) = result
      }
      start += 4
      end += 4
    }
    input(0) // this is considered the "output"
  }

  override def solve(): Int = {
    val intcodeNumbers = inputLines.head.split(',').map(_.toInt)
    val input = collection.mutable.ArrayBuffer.from(intcodeNumbers)

    val maybeSolution = findCombination(input, target = 19690720)
    if (maybeSolution.nonEmpty) {
      val solution = maybeSolution.get
      100 * solution.noun + solution.verb
    } else {
      throw new IllegalStateException("Terrible Programmer Exception")
    }
  }
}

object Day2 {
  def main(args: Array[String]): Unit = {
    val runner = new Day2Puzzle("day2_input.txt")
    println(runner.solve())
  }
}


