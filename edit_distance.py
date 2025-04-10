from flask import Flask, render_template
import numpy as np

app = Flask(__name__)

def editDistance(n, m):
    #ignoring case sensitivity, adding space between
    n = " " + n.lower()
    m = " " + m.lower()

    #determining size of matrix
    print("Here is string one: " + n) #debug, delete
    print("Here is string two: " + m)

    rows = len(n) #matrix row
    columns = len(m) #initialize matrix column

    #initializing matrix with zeroes
    matrix = [[0 for _ in range(columns)] for _ in range(rows)]
    print(matrix)
    print(rows, columns) ##DEBUG, check size


    for i in range(rows):
        for j in range(columns):
            if n[i]==m[j]:
                print("match")
                if matrix[i-1][j-1]!=None:
                    matrix[i][j]=matrix[i-1][j-1]
                # else:
                #     matrix[i][j]=0
            else:
                
                min_cell = min(
                    matrix[i][j-1], #cell before
                    matrix[i-1][j], #cell above
                    matrix[i-1][j-1] #cell diagnol
                )
                matrix[i][j] = min_cell + 1
                print(f"Row:{i} Column:{j} Cell Value:", matrix[i][j])

    print(matrix)
    return matrix

#function to draw matrix
def matrix(matrix_val, str1, str2):
    result=" "

    #saving matrix to result to be printed out
    for b in range(len(str2)):
        result += f"  {str2[b]}  " 
    result+= "\n"
    for i in range(len(str1)):
        result+="  "
        for j in range(len(str2)):
            result += "-----"
        result += "\n"
        result += f"{str1[i]}|"
        for j in range(len(str2)):
            result += ("  " + f"{matrix_val[i][j]}" + " :")
        result += "\n"

    # last line of matrix printed out
    result+="  "
    for _ in range(len(str2)):
        result += "-----"

    print(result)
    return result
    
    

@app.route("/", methods=["GET", "POST"])

def web_page():
    return render_template("index.html", matrix=matrix_str, edit_dist=None)
if __name__ == "__main__":
    str1 = "evaluation"
    str2 = "elution"
    ed_matrix = editDistance(str1, str2)
    matrix_str = matrix(ed_matrix, str1, str2)
    # app.run(debug=True)


# in terminal, run python edit_distance.py
#or python3 edit_distance.py
#make sure necessary libraries like flask and numpy are installed locally