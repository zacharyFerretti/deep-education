import tkinter as tk
import tkinter.ttk as ttk
from tkcolorpicker import askcolor


def random_color_generation(red_green_blue):
    generatedTensors = []
    generatedColors = []
    for i in range(5000):
        r = float(random.randint(0, 256)) / 256
        g = float(random.randint(0, 256)) / 256
        b = float(random.randint(0, 256)) / 256
        curr = red_green_blue + [r, g, b]
        generatedTensors.append(curr)
        curr_rgb = []
        for entry in curr:
            curr_rgb.append(int(entry * 256))
        generatedColors.append(curr_rgb)
    return generatedTensors, generatedColors

    
def getColor():
    print(askcolor((255, 255, 0), root))


def display_results(generatedColors):
    figures = []
    original = (generatedColors[0][0], generatedColors[0][1], generatedColors[0][2])
    figures.append(Image.new("RGB", (200, 200), original))
    colors = [0, 100, 400, 600, 800, 1600, 1800, 2200]
    # colors = [4993,4994,4995,4996,4997,4998,4999]
    for i in colors:
        rgb = (generatedColors[i][3], generatedColors[i][4], generatedColors[i][5])
        figures.append(Image.new("RGB", (200, 200), rgb))

    x, y = figures[0].size
    ncol = 4
    nrow = 2
    tuple = x * ncol, x * nrow
    allInOne = Image.new('RGB', (x * ncol, x * nrow))
    for i in range(len(figures)):
        px, py = x * int(i / nrow), y * (i % nrow)
        allInOne.paste(figures[i], (px, py))

    allInOne.show()


def main():
	model = load("./best_trained_model_tryingtobeat69point8.pt")
    red_green_blue = [float(sys.argv[1]) / 256, float(sys.argv[2]) / 256, float(sys.argv[3]) / 256]
    print(red_green_blue)
    grandTotal = read_csv('./rgb_labeled_explored.csv', header=None, sep="|").values.tolist()

    x, colors = random_color_generation(red_green_blue)
    print(x[0])
    print(colors[0])
    x = FloatTensor(x)

    inputs = Variable(x)
    prediction = model(inputs)  # Prediction for each rgb pair.
    print(type(prediction.tolist()))

    Z = [colors for _, colors in sorted(zip(prediction, colors))]
    # print(Z[0])
    display_results(Z)
    '''
    root = tk.Tk()
	style = ttk.Style(root)
	style.theme_use('clam')

	root.bind("<space>", lambda event: getColor())

	root.mainloop()
	'''


if __name__ == '__main__':
	main()
