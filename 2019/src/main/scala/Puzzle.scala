import java.net.URL

import scala.io.{BufferedSource, Source}

abstract class Puzzle(inputLoc: String) {
  val inputLines: List[String] = getInputLines(getClass.getResource(inputLoc))

  def getInputLines(url: URL): List[String] = {
    val source: BufferedSource = Source.fromFile(url.getFile)
    val lines = source.getLines().toList
    source.close()

    lines
  }

  def solve(): Int
}