print("""You enter a laboratory with two rooms.
Do you enter chamber #1 or chamber #2?""")
chamber = input("> ")

if chamber == "1":
	print("There's a molecular dynamics simulation running.")
	print("What do you do?")
	print("1. Increase the temperature to 1000K.")
	print("2. Modify the force field parameters.")
	simulation = input("> ")

	if simulation == "1":
		print("The protein denatures and your simulation crashes. Experiment failed!")
	elif simulation == "2":
		print("The water molecules escape the periodic boundary. Experiment failed!")
	else:
		print(f"Well, trying {simulation} might be a novel approach.")
		print("The molecular system stabilizes.")
		print("Excellent research!")

elif chamber == "2":
	print("You stare into a quantum entanglement experiment.")
	print("1. Measure the superposition.")
	print("2. Apply Schrödinger's equation.")
	print("3. Observe the wave function collapse.")
	quantum = input("> ")

	if quantum == "1" or quantum == "2":
		print("Your experiment succeeds through quantum decoherence.")
		print("Excellent research!")
	else:
		print("The quantum uncertainty corrupts your measurements.")
		print("Experiment failed!")
else:
	print("You calibrate the instruments incorrectly and cause a lab explosion. Experiment failed!")
