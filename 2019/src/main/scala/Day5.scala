import scala.collection.mutable.ArrayBuffer
import scala.io.StdIn

object ParameterMode extends Enumeration {
  type ParameterMode = Value
  val POSITIONAL, IMMEDIATE = Value
}

import ParameterMode._

case class Parameter(value: Int, mode: ParameterMode)

class AdditionInstruction(opcode: Int, parameters: Array[Parameter], length: Int)
  extends Instruction(opcode, parameters, length) {

  override def execute(memory: ArrayBuffer[Int], instructionPointer: Int): Int = {
    val resolvedParams = parameters.take(2).map(param => resolveParamValue(memory, param))
    memory(parameters(2).value) = resolvedParams(0) + resolvedParams(1)
    instructionPointer + length
  }
}

class InputInstruction(opcode: Int, parameters: Array[Parameter], length: Int)
  extends Instruction(opcode, parameters, length) {

  override def execute(memory: ArrayBuffer[Int], instructionPointer: Int): Int = {
    val userInput = StdIn.readInt()
    memory(parameters(0).value) = userInput
    instructionPointer + length
  }
}

class MultiplicationInstruction(opcode: Int, parameters: Array[Parameter], length: Int)
  extends Instruction(opcode, parameters, length) {

  override def execute(memory: ArrayBuffer[Int], instructionPointer: Int): Int = {
    val resolvedParams = parameters.take(2).map(param => resolveParamValue(memory, param))
    memory(parameters(2).value) = resolvedParams(0) * resolvedParams(1)
    instructionPointer + length
  }
}

class OutputInstruction(opcode: Int, parameters: Array[Parameter], length: Int)
  extends Instruction(opcode, parameters, length) {

  override def execute(memory: ArrayBuffer[Int], instructionPointer: Int): Int = {
    println(resolveParamValue(memory, parameters(0)))
    instructionPointer + length
  }
}

class HaltInstruction(opcode: Int, parameters: Array[Parameter], length: Int)
  extends Instruction(opcode, parameters, length) {

  override def execute(memory: ArrayBuffer[Int], instructionPointer: Int): Int = {
    -1
  }
}

class JumpIfTrueInstruction(opcode: Int, parameters: Array[Parameter], length: Int)
  extends Instruction(opcode, parameters, length) {

  override def execute(memory: ArrayBuffer[Int], instructionPointer: Int): Int = {
    if (resolveParamValue(memory, parameters(0)) != 0) {
      resolveParamValue(memory, parameters(1))
    } else {
      instructionPointer + length
    }
  }
}

class JumpIfFalseInstruction(opcode: Int, parameters: Array[Parameter], length: Int)
  extends Instruction(opcode, parameters, length) {

  override def execute(memory: ArrayBuffer[Int], instructionPointer: Int): Int = {
    if (resolveParamValue(memory, parameters(0)) == 0) {
      resolveParamValue(memory, parameters(1))
    } else {
      instructionPointer + length
    }
  }
}

class IsLessThanInstruction(opcode: Int, parameters: Array[Parameter], length: Int)
  extends Instruction(opcode, parameters, length) {

  override def execute(memory: ArrayBuffer[Int], instructionPointer: Int): Int = {
    val isLessThan = resolveParamValue(memory, parameters(0)) <
      resolveParamValue(memory, parameters(1))

    if (isLessThan) {
      memory(parameters(2).value) = 1
    } else {
      memory(parameters(2).value) = 0
    }

    instructionPointer + length
  }
}

class IsEqualToInstruction(opcode: Int, parameters: Array[Parameter], length: Int)
  extends Instruction(opcode, parameters, length) {

  override def execute(memory: ArrayBuffer[Int], instructionPointer: Int): Int = {
    val isEqualTo = resolveParamValue(memory, parameters(0)) ==
      resolveParamValue(memory, parameters(1))

    if (isEqualTo) {
      memory(parameters(2).value) = 1
    } else {
      memory(parameters(2).value) = 0
    }

    instructionPointer + length
  }
}


abstract class Instruction(val opcode: Int,
                           val parameters: Array[Parameter],
                           val length: Int) {

  def resolveParamValue(memory: ArrayBuffer[Int], parameter: Parameter): Int = {
    if (parameter.mode == POSITIONAL)
      memory(parameter.value)
    else
      parameter.value
  }

  def execute(memory: ArrayBuffer[Int], instructionPointer: Int): Int
}

object Instruction {
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

    val instruction:Instruction = actualOpcode.toInt match {
      case 1 => new AdditionInstruction(actualOpcode.toInt, descriptiveParams.toArray, instructionLength)
      case 2 => new MultiplicationInstruction(actualOpcode.toInt, descriptiveParams.toArray, instructionLength)
      case 3 => new InputInstruction(actualOpcode.toInt, descriptiveParams.toArray, instructionLength)
      case 4 => new OutputInstruction(actualOpcode.toInt, descriptiveParams.toArray, instructionLength)
      case 5 => new JumpIfTrueInstruction(actualOpcode.toInt, descriptiveParams.toArray, instructionLength)
      case 6 => new JumpIfFalseInstruction(actualOpcode.toInt, descriptiveParams.toArray, instructionLength)
      case 7 => new IsLessThanInstruction(actualOpcode.toInt, descriptiveParams.toArray, instructionLength)
      case 8 => new IsEqualToInstruction(actualOpcode.toInt, descriptiveParams.toArray, instructionLength)
      case 99 => new HaltInstruction(actualOpcode.toInt, descriptiveParams.toArray, instructionLength)
    }
    instruction
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

  override def solve(): Int = {
    var instrPtr = 0

    while (instrPtr != -1) {
      val instruction = Instruction.apply(memory.toArray.slice(instrPtr, memory.length))
      instrPtr = instruction.execute(memory, instrPtr)
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


