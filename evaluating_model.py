import torch
from torch import load
from torch import FloatTensor
from torch.autograd import Variable

from PIL import Image
from pandas import read_csv

from training_model import NeuralNet
from training_model import dataProcessing

import sys
import random

    


def get_statistics(prediction, outputs):
    prediction_as_list = prediction.tolist()
    range_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    range_correct = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    range_incorrect = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0

    for entry in prediction_as_list:
        val = round(entry[0], 2)

        if(val > 0.00 and val <= 0.05):
            range_counts[0] = range_counts[0] + 1
            if(outputs[i] == 0):
                range_correct[0] = range_correct[0] + 1
            else:
                range_incorrect[0] = range_incorrect[0] + 1

        elif(val > 0.05 and val <= 0.10):
            range_counts[1] = range_counts[1] + 1
            if(outputs[i] == 0):
                range_correct[1] = range_correct[1] + 1
            else:
                range_incorrect[1] = range_incorrect[1] + 1

        elif(val > 0.10 and val <= 0.15):
            range_counts[2] = range_counts[2] + 1
            if(outputs[i] == 0):
                range_correct[2] = range_correct[2] + 1
            else:
                range_incorrect[2] = range_incorrect[2] + 1

        elif(val > 0.15 and val <= 0.20):
            range_counts[3] = range_counts[3] + 1
            if(outputs[i] == 0):
                range_correct[3] = range_correct[3] + 1
            else:
                range_incorrect[3] = range_incorrect[3] + 1

        elif(val > 0.20 and val <= 0.25):
            range_counts[4] = range_counts[4] + 1
            if(outputs[i] == 0):
                range_correct[4] = range_correct[4] + 1
            else:
                range_incorrect[4] = range_incorrect[4] + 1

        elif(val > 0.25 and val <= 0.30):
            range_counts[5] = range_counts[5] + 1
            if(outputs[i] == 0):
                range_correct[5] = range_correct[5] + 1
            else:
                range_incorrect[5] = range_incorrect[5] + 1

        elif(val > 0.30 and val <= 0.35):
            range_counts[6] = range_counts[6] + 1
            if(outputs[i] == 0):
                range_correct[6] = range_correct[6] + 1
            else:
                range_incorrect[6] = range_incorrect[6] + 1

        elif(val > 0.35 and val <= 0.40):
            range_counts[7] = range_counts[7] + 1
            if(outputs[i] == 1):
                range_correct[7] = range_correct[7] + 1
            else:
                range_incorrect[7] = range_incorrect[7] + 1

        elif(val > 0.40 and val <= 0.45):
            range_counts[8] = range_counts[8] + 1
            if(outputs[i] == 1):
                range_correct[8] = range_correct[8] + 1
            else:
                range_incorrect[8] = range_incorrect[8] + 1

        elif(val > 0.45 and val <= 0.50):
            range_counts[9] = range_counts[9] + 1
            if(outputs[i] == 1):
                range_correct[9] = range_correct[9] + 1
            else:
                range_incorrect[9] = range_incorrect[9] + 1

        elif(val > 0.50 and val <= 0.55):
            range_counts[10] = range_counts[10] + 1
            if(outputs[i] == 1):
                range_correct[10] = range_correct[10] + 1
            else:
                range_incorrect[10] = range_incorrect[10] + 1

        elif(val > 0.55):
            range_counts[11] = range_counts[11] + 1
            if(outputs[i] == 1):
                range_correct[11] = range_correct[11] + 1
            else:
                range_incorrect[11] = range_incorrect[11] + 1
        i = i + 1

    # Calculating percentage correct
    percentages = []
    strings = []
    averageCorrect = 0
    numberOfPercentages = 0
    for i in range(len(range_counts)):
        if(range_counts[i] != 0):
            curr = round(((range_correct[i] / range_counts[i]) * 100), 2)
            percentages.append(curr)
            strings.append(str(range_correct[i]) + "/" + str(range_counts[i]))
            numberOfPercentages = numberOfPercentages + 1
            averageCorrect = averageCorrect + curr

        else:
            percentages.append("N/A")
            strings.append("N/A")

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~ Statistics About Predictions ~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(range_counts)
    print("0 - 5 Percent: " + str(range_counts[0]) + " | " + strings[0] + ": " + str(percentages[0]) + "%")
    print("5 - 10 Percent: " + str(range_counts[1]) + " | " + strings[1] + ": " + str(percentages[1]) + "%")
    print("10 - 15 Percent: " + str(range_counts[2]) + " | " + strings[2] + ": " + str(percentages[2]) + "%")
    print("15 - 20 Percent: " + str(range_counts[3]) + " | " + strings[3] + ": " + str(percentages[3]) + "%")
    print("20 - 25 Percent: " + str(range_counts[4]) + " | " + strings[4] + ": " + str(percentages[4]) + "%")
    print("25 - 30 Percent: " + str(range_counts[5]) + " | " + strings[5] + ": " + str(percentages[5]) + "%")
    print("30 - 35 Percent: " + str(range_counts[6]) + " | " + strings[6] + ": " + str(percentages[6]) + "%")
    print("35 - 40 Percent: " + str(range_counts[7]) + " | " + strings[7] + ": " + str(percentages[7]) + "%")
    print("40 - 45 Percent: " + str(range_counts[8]) + " | " + strings[8] + ": " + str(percentages[8]) + "%")
    print("45 - 50 Percent: " + str(range_counts[9]) + " | " + strings[9] + ": " + str(percentages[9]) + "%")
    print("50 - 55 Percent: " + str(range_counts[10]) + " | " + strings[10] + ": " + str(percentages[10]) + "%")
    print("> 55 Percent: " + str(range_counts[11]) + " | " + strings[11] + ": " + str(percentages[11]) + "%")
    averagePercent = round((averageCorrect / numberOfPercentages), 2)
    print("\n\nAverage Correct: " + str(averagePercent) + "%")



def main():
    os.listdir(".")
    grandTotal = read_csv('./deep-education/CSV Files/rgb_labeled_explored.csv', header=None, sep="|").values.tolist()
    x, y = dataProcessing(grandTotal)

    x = FloatTensor(x)
    y = FloatTensor(y)
    inputs = Variable(x)
    outputs = Variable(y)
    model = load("./best_trained_model_tryingtobeat69point8.pt")
    print(model)
    get_statistics(model(inputs), outputs)


if __name__ == '__main__':
    main()
