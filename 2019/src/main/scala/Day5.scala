import scala.collection.mutable.ArrayBuffer
import scala.io.StdIn

object ParameterMode extends Enumeration {
  type ParameterMode = Value
  val POSITIONAL, IMMEDIATE = Value
}

import ParameterMode._

case class Parameter(value: Int, mode: ParameterMode)

case class Instruction(opcode: Int, parameters: Array[Parameter], length: Int) {
  def isAddition: Boolean = opcode == 1
  def isMultiplication: Boolean = opcode == 2
  def isInput: Boolean = opcode == 3
  def isOutput: Boolean = opcode == 4
  def isJumpIfTrue: Boolean = opcode == 5
  def isJumpIfFalse: Boolean = opcode == 6
  def isLessThan: Boolean = opcode == 7
  def isEqual: Boolean = opcode == 8
  def isHalt: Boolean = opcode == 99
}

case object Instruction {
  private def getLengthForCode(code: String): Int = {
    val fourLengthInstr = code.endsWith("1") || code.endsWith("2") ||
      code.endsWith("7") || code.endsWith("8")

    if (fourLengthInstr) {
      4
    } else if (code.endsWith("3") || code.endsWith("4")) {
      2
    } else if (code.endsWith("99")) {
      1
    } else if (code.endsWith("5") || code.endsWith("6")) {
      3
    } else {
      throw new IllegalArgumentException(s"invalid opcode [$code]")
    }
  }

  // assumes that rawInput is a valid instruction
  def apply(rawInput: Array[Int]): Instruction = {

    // for some reason the puzzle puts the opcode and parameter modes all together
    // and calls that the opcode. I decouple them.
    val opcode = rawInput.head.toString
    var parameterModes = opcode.splitAt(opcode.length - 2)._1
    val actualOpcode = opcode.splitAt(opcode.length - 2)._2

    val paddingAmt = 3 - parameterModes.length
    parameterModes = ("0" * paddingAmt) + parameterModes
    parameterModes = parameterModes.reverse // because we need to read right-to-left

    val instructionLength = getLengthForCode(opcode)
    val originalParams = rawInput.slice(1, instructionLength)
    val descriptiveParams = ArrayBuffer.empty[Parameter]

    for (i <- 0 until originalParams.length) {
      if (parameterModes(i) == '0')
        descriptiveParams += Parameter(originalParams(i), ParameterMode.POSITIONAL)
      else if (parameterModes(i) == '1')
        descriptiveParams += Parameter(originalParams(i), ParameterMode.IMMEDIATE)
      else
        throw new IllegalArgumentException(s"Encountered illegal parameter mode [${parameterModes(i)}]")
    }

    new Instruction(opcode = actualOpcode.toInt, parameters = descriptiveParams.toArray, instructionLength)
  }
}

class Day5Puzzle(inputLoc: String) extends Puzzle(inputLoc) {
  val intcodeNumbers: Array[Int] = inputLines.head.split(',').map(_.toInt)
  val memory: ArrayBuffer[Int] = collection.mutable.ArrayBuffer.from(intcodeNumbers)

  private def resolveParamValue(parameter: Parameter): Int = {
    if (parameter.mode == POSITIONAL)
      memory(parameter.value)
    else
      parameter.value
  }

  private def handleArithmeticInstruction(instruction: Instruction, memory: ArrayBuffer[Int]): Unit = {
    val resolvedParams = instruction.parameters.take(2).map(param => resolveParamValue(param))

    if (instruction.isMultiplication) {
      memory(instruction.parameters(2).value) = resolvedParams(0) * resolvedParams(1)
    } else if (instruction.isAddition) {
      memory(instruction.parameters(2).value) = resolvedParams(0) + resolvedParams(1)
    } else {
      throw new IllegalArgumentException("Unrecognized arithmetic operation")
    }
  }

  override def solve(): Int = {
    var instrPtr = 0
    var continue = true

    while (continue) {
      val instruction = Instruction.apply(memory.toArray.slice(instrPtr, memory.length))

      if (instruction.isHalt) {
        continue = false
      } else if (instruction.isInput) {
        val userInput = StdIn.readInt()
        memory(instruction.parameters(0).value) = userInput
        instrPtr += instruction.length
      } else if (instruction.isOutput) {
        println(resolveParamValue(instruction.parameters(0)))
        instrPtr += instruction.length
      } else if (instruction.isAddition || instruction.isMultiplication) {
        handleArithmeticInstruction(instruction, memory)
        instrPtr += instruction.length
      } else if (instruction.isJumpIfTrue) {
        if (resolveParamValue(instruction.parameters(0)) != 0) {
          instrPtr = resolveParamValue(instruction.parameters(1))
        } else {
          instrPtr += instruction.length
        }
      } else if (instruction.isJumpIfFalse) {
        if (resolveParamValue(instruction.parameters(0)) == 0) {
          instrPtr = resolveParamValue(instruction.parameters(1))
        } else {
          instrPtr += instruction.length
        }
      } else if (instruction.isLessThan) {
        if (resolveParamValue(instruction.parameters(0)) < resolveParamValue(instruction.parameters(1))) {
          memory(instruction.parameters(2).value) = 1
        } else {
          memory(instruction.parameters(2).value) = 0
        }
        instrPtr += instruction.length
      } else if (instruction.isEqual) {
        if (resolveParamValue(instruction.parameters(0)) == resolveParamValue(instruction.parameters(1))) {
          memory(instruction.parameters(2).value) = 1
        } else {
          memory(instruction.parameters(2).value) = 0
        }
        instrPtr += instruction.length
      } else {
        throw new IllegalArgumentException(s"Encountered invalid opcode [${instruction.opcode}]")
      }
    }
    -1 // this is only here because the method has to return an Int
  }
}

object Day5 {
  def main(args: Array[String]): Unit = {
    val runner = new Day5Puzzle("day5_input.txt")
    runner.solve()
  }
}


