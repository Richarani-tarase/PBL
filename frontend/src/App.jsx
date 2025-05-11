import { useState } from "react";
import axios from "axios";

export default function App() {
  const [code, setCode] = useState(`matrix A = [1,2;3,4]
matrix B = [5,6;7,8]
C = A + B`);
  const [result, setResult] = useState(null);

  const runCode = async () => {
    try {
      const res = await axios.post("http://localhost:5000/run", { code });
      setResult(res.data.result);
    } catch (err) {
      setResult(err.response?.data?.error || "Unknown error");
    }
  };

  return (
    <div className="p-4 font-mono">
      <h1 className="text-xl mb-2 font-bold">Matrix DSL</h1>
      <textarea
        rows={6}
        value={code}
        onChange={(e) => setCode(e.target.value)}
        className="w-full border p-2 rounded"
      />
      <button onClick={runCode} className="mt-2 bg-blue-600 text-white p-2 rounded">
        Run
      </button>
      <pre className="mt-4 bg-gray-100 p-2 rounded">
        {result ? JSON.stringify(result, null, 2) : "No output yet."}
      </pre>
    </div>
  );
}
