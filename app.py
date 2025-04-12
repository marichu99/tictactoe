from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

def check_winner(board):
    winning_combinations = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in winning_combinations:
        a, b, c = combo
        if board[a] and board[a] == board[b] == board[c]:
            return f"Player {board[a]} wins!"
    if "" not in board:
        return "It's a draw!"
    return "continue"

@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    board = data.get('board')
    status = check_winner(board)
    return jsonify({
        'status': status,
        'message': status if status != 'continue' else f"Player {data.get('player')} moved."
    })

if __name__ == '__main__':
    app.run(debug=True)
