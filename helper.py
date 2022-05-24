from dataclasses import dataclass
import matplotlib.pyplot as plt
import pandas as pn
from IPython import display
from pyparsing import col


plt.ion()
#Plot data
def plot(scores, mean_scores):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    plt.show(block=False)
    plt.pause(.1)

#Export data to excel sheet.
def export(scores, n_games, means, records):
    col1 = 'scores'
    col2 = 'number of games'
    col3 = 'mean score'
    col4 = 'record'
    data = pn.DataFrame({
        col1:scores,
        col2:n_games,
        col3:means,
        col4:records
    })
    data.to_excel('data.xlsx',sheet_name='sheet1',index=False)