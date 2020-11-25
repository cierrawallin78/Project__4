from Organization import Org
from NeuralNet import NeuralNet
def main():
    """ Kieran Ringel
    For each data set three lines are run in main.
    The first one creates an instance of Org with the arguments being the file name, where the header
    is located to be removed ([-1] if there is no header, the location of the class so they can all
    be moved to the last column, and the column location of any categorical features so that one hot
    encoding can be applied.
    The next line calls to open the file and returns the dataframe of the file
    The final line creates an instance of NeuralNet with the arguments being the dataframe, the number
    of hidden layers, the number of hidden nodes per layer, whether classification or regression are
    to be performed, how the weights are being trained (GA, DE, BP, PSO), and the population size (1 for algorithms that
    don't need a population).
    """

    print('Breast Cancer')
    print("generations: 30 \n"
          "beta = 1.5 \n"
          "pop = 30 \n"
          "pr = .3")
    cancer = Org('Data/breast-cancer-wisconsin.data', [-1], -1, [-1])
    df = cancer.open()
    # ##NN(file, number hidden layers, number hidden nodes per layer)
    NeuralNet(df, 0, 12, 'classification', 'DE', 30)

    #print('glass')
    #glass = Org('Data/glass.data', [-1], -1, [-1])
    #df = glass.open()
    #NeuralNet(df, 0, 6, 'classification', "GA", 10)

    #print('soybean')
    #soybean = Org('Data/soybean-small.data', [-1], -1, [-1])
    #df = soybean.open()
    #NeuralNet(df, 2, 11, 'classification')

    #print('abalone')
    #abalone = Org('Data/abalone.data', [-1], -1, [0])
    #df = abalone.open()
    #NeuralNet(df, 2, 2, 'regression')

    #print('machine')
    #machine = Org('Data/machine.data', [-1], -1, [-1])
    #df = machine.open()
    #NeuralNet(df, 2, 3, 'regression')
    #print(df)

    #print('forest')
    #forest = Org('Data/forestfires.data', [0], -1, [2,3])
    #df = forest.open()
    #NeuralNet(df, 0, 3, 'regression')

if __name__ == '__main__':
    main()
