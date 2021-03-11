import tkinter as tk
from apyori import apriori
import pandas as pd
import csv

root = tk.Tk()
root.geometry('600x600')
root.title('Market Basket Analysis')



canvas1 = tk.Canvas(root, width=600, height=600, bg='#13ede6', relief='raised')
canvas1.pack()
entry1 = tk.Entry (root)
canvas1.create_window(320, 210, window=entry1)
entry2 = tk.Entry (root)
canvas1.create_window(320, 265, window=entry2)
entry3 = tk.Entry (root)
canvas1.create_window(320, 315, window=entry3)

label1 = tk.Label(root, text="Market Basket Analysis", fg='black', bg='#13ede6',
                  font=("roboto", 20, 'bold')).place(x=150, y=70)
label2 = tk.Label(root, text="Enter Support : ", fg='#717D7E', bg='#13ede6', font=("roboto", 15)).place(x=50, y=200)
label3 = tk.Label(root, text="Enter Confidence :", fg='#717D7E', bg='#13ede6', font=("roboto", 15)).place(x=50, y=250)
label4 = tk.Label(root, text="Enter Lift : ", fg='#717D7E', bg='#13ede6', font=("roboto", 15)).place(x=50, y=300)


def my_process():
    dataset = pd.read_csv(r'E:\Study\Market-Basket-Analysis-master\final_dataset.csv', header=None)

    transaction = []
    for i in range(0, 7501):
        transaction.append([str(dataset.values[i, j]) for j in range(0, 20)])
    fn = tk.IntVar()
    support = entry1.get()
    a = float(support)
    confidence = entry2.get()
    b = float(confidence)
    lift = entry3.get()
    c = float(lift)
    rules = apriori(transactions=transaction, min_support=a, min_confidence=b, min_lift=c, min_length=2,
                    max_length=2)
    results = list(rules)
    return results


def inspect(results):
    lhs = [tuple(result[2][0][0])[0] for result in results]
    rhs = [tuple(result[2][0][1])[0] for result in results]
    supports = [result[1] for result in results]
    confidence = [result[2][0][2] for result in results]
    lifts = [result[2][0][3] for result in results]

    return list(zip(lhs, rhs, supports, confidence, lifts))


def abc():
    resultsinDataFrame = pd.DataFrame(inspect(my_process()),
                                          columns=['Left hand Side', 'Right hand side', 'Support', 'Confidence', 'Lifts'])
    var1.set(resultsinDataFrame)
   # return resultsinDataFrame

var1 = tk.StringVar()

# tempvar = abc()
# print(tempvar)

b2 = tk.Button(root, text='Analyse',fg = 'white',bg='DarkGreen', command=abc, font=("roboto", 12, "bold"))
b2.place(x=255, y=350)
l1 = tk.Label(root, textvariable=var1)
l1.place(x=20, y = 400 )
root.mainloop()
