from Interperter import Interperter

interperter = Interperter()
interperter.read_file()
program = interperter.visitnodes()
interperter.runprogram(program)
