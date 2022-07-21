import jsonManager
import agent
import pickle
import sys

def main():
	if (sys.argv[1] == "initRectangleAgent"):
		jsonMng = jsonManager.JsonManager()
		env = jsonMng.initEnvironment(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8])
		a = agent.RectangleAgent("Rectangle", env)
		fileRect = open("../../python/rectangle.pickle", "wb")
		pickle.dump(a, fileRect)
		fileRect.close()
	elif (sys.argv[1] == "initCircleAgent"):
		jsonMng = jsonManager.JsonManager()
		env = jsonMng.initEnvironment(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8])
		a = agent.CircleAgent("Circle", env)
		fileCircle = open("../../python/circle.pickle", "wb")
		pickle.dump(a, fileCircle)
		fileCircle.close()
	elif (sys.argv[1] == "runRectangleAgent"):
		jsonMng = jsonManager.JsonManager()
		fileRect = open("../../python/rectangle.pickle", "rb")
		a = pickle.load(fileRect)
		fileRect.close()
		jsonMng.updateEnvironment(a, sys.argv[2], sys.argv[3], sys.argv[4]) #update environment
		a.executeAction() #execute action
		print(a.currentAction) #do not remove this print
	elif (sys.argv[1] == "runCircleAgent"):
		jsonMng = jsonManager.JsonManager()
		fileCircle = open("../../python/circle.pickle", "rb")
		a = pickle.load(fileCircle)
		fileCircle.close()
		jsonMng.updateEnvironment(a, sys.argv[2], sys.argv[3], sys.argv[4]) #update environment
		a.executeAction() #execute action
		print(a.currentAction) #do not remove this print
	
if __name__ == "__main__":
	main()
