from flask import Flask, request, jsonify
from flask_cors import CORS
from compiler.parser import parse_code
from compiler.semantic import check_semantics
from compiler.ir import generate_ir
from compiler.executor import execute
import traceback

app = Flask(__name__)
CORS(app)

@app.route('/run', methods=['POST'])
def run():
    try:
        data = request.get_json()
        code = data['code']
        ast = parse_code(code)
        check_semantics(ast)
        ir = generate_ir(ast)
        env = execute(ir)
        result = {k: v.tolist() for k, v in env.items()}
        return jsonify({"result": result})
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": f"{type(e).__name__}: {str(e)}"}), 400

if __name__ == '__main__':
    app.run(debug=True)
