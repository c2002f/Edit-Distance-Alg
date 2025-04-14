#to run this program, the Flask library must be installed locally
# pip install Flask
# this program can be compiled using python edit_distance.py OR python3 edit_distance.py
# and should direct you to a locally hosted Flask application

from flask import Flask, render_template, request

app = Flask(__name__)

def editDistance(n, m):
    rows = len(n) #matrix row
    columns = len(m) #initialize matrix column

    shortestMatch=[]
    #initializing matrix with zeroes
    matrix = [[0 for _ in range(columns)] for _ in range(rows)]

    #initalizing the first row and column
    for i in range(rows):
        matrix[i][0] = i
    for j in range(columns):
        matrix[0][j] = j

    #start of edit distance algorithm
    for i in range(1, rows):
        for j in range(1, columns):
            if n[i]==m[j]:
                matrix[i][j] = matrix[i-1][j-1]  # No cost
                if len(n)<=len(m):
                    shortestMatch.append(i)
                else:
                    shortestMatch.append(j)
                    
            else : #if chars in string do not match
                min_cell = min(
                    matrix[i][j-1], #cell before
                    matrix[i-1][j], #cell above
                    matrix[i-1][j-1] #cell diagonal
                )
                matrix[i][j] = min_cell + 1 #take minimal cost and add one 
    print(shortestMatch)
    return matrix, matrix[i][j], shortestMatch

#function to draw matrix
def matrix(matrix_val, n, m):
    result=" "
    #saving matrix to result to be printed out
    for b in range(len(m)):
        result += f"   {m[b]}   " 
    result+= "\n"
    for i in range(len(n)):
        result+="  "
        for j in range(len(m)):
            result += "-------"
        result += "\n"
        result += f"{n[i]}|"
        for j in range(len(m)):
            result += ("    " + f"{matrix_val[i][j]}" + " :")
        result += "\n"

    # last line of matrix printed out
    result+="  "
    for _ in range(len(m)):
        result += "-------"

    print(result)
    return result

def stringAlignment(n, m, shortestMatch):
    #str1 represents the longer string if one is present
    #if equal length, then the first given string stays as first string
    if len(n)>=len(m):
        str1=n
        str2=m
    elif len(n)<len(m):
        str1=m
        str2=n
    
    alignment=str1+"\n"

    j = 0
    i = 0
    # for i in range(len(str1)): #check if shortest match is empty
    #     if j < len(shortestMatch) and str1[i]==str2[shortestMatch[j]]:
    #         alignment+=str2[shortestMatch[j]]
    #         j+=1
    #     else:
    #         alignment+="_"

    # checking if a char in str2 has already been used in alignemnt
    #in case of duplicate chars
    usedChar = set() 
    for i in range(len(str1)): #iterating through entirety of string, making sure string matches
        if j < len(shortestMatch):
            if str1[i]==str2[shortestMatch[j]] and j not in usedChar:
                alignment+=str2[shortestMatch[j]]
                usedChar.add(j)
                j+=1
            else:
                alignment+="_"


    print (alignment)
    return alignment


@app.route("/", methods=["GET", "POST"])

def web_page():
    matrix_str = ""
    dist = None

    # if request.method == "POST":
    #     str1 = " " + request.form["word1"].lower()
    #     str2 = " " + request.form["word2"].lower()
    #     ed_matrix, dist = editDistance(str1, str2)
    #     matrix_str = matrix(ed_matrix, str1, str2)
    #     print(dist)
    return render_template("index.html", matrix=matrix_str, edit_dist=dist)
if __name__ == "__main__":
    str1 = " evaluation"
    str2 = " evolution"
    # app.run(debug=True)
    editMatrix, dist, shortestString = editDistance(str1, str2)
    alignment = stringAlignment(str1, str2, shortestString)
    matrix_str = matrix(editMatrix, str1, str2)

