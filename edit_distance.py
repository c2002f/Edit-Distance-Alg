from flask import Flask, render_template
import numpy as np

app = Flask(__name__)

def editDistance(n, m):

    #ignoring case sensitivity
    n = n.lower()
    m = m.lower()

    #determining size of matrix
    print("Here is string one: " + n)
    print("Here is string two: " + m)
    n_len = len(n)
    m_len = len(m)

    rows = n_len + 1 #matrix row
    columns = m_len + 1 #initialize matrix column


    #initializing matrix with zeroes
    matrix = [[0 for _ in range(columns)] for _ in range(rows)]
    # print(matrix) #debug, check size
    print(rows, columns)


    # for i in range(columns):
    #     for j in range(rows):
    #         #row[0]

    return rows, columns, matrix, n, m

#function to draw matrix
def matrix(row, column, matrix_val, str1, str2):
    result=" "

    #iteration through matrix
    i=0 
    j=0

    #iteration through string
    a=0
    b=0
    str1 = "*" + str1
    str2 = "*" + str2
    for b in range(len(str2)):
        result += f"  {str2[b]}  "

    result+= "\n"
    for i in range(row):
        result+="  "
        for _ in range(column):
            result += "-----"
        result += "\n"
        if j!= column:
            result += f"{str1[a]}|"
            a+=1
            for _ in range(column):
                result += ("  " + f"{matrix_val[i][j]}" + " :")
            result += "\n"

    # last line of matrix printed out
    result+="  "
    for _ in range(column):
        result += "-----"
    print(result)
    return result
    
    

@app.route("/", methods=["GET", "POST"])

def web_page():
    return render_template("index.html", matrix=matrix_str, edit_dist=None)
if __name__ == "__main__":
    row, col, ed_matrix, str1, str2 = editDistance("love", "life")
    matrix_str = matrix(row, col, ed_matrix, str1, str2)
    app.run(debug=True)


# in terminal, run python edit_distance.py
#or python3 edit_distance.py
#make sure necessary libraries like flask and numpy are installed locally