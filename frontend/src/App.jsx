import { useState } from "react";
import axios from "axios";
import "./App.css";
export default function App() {
  const [code, setCode] = useState(`matrix A = [[1, 2]; [3, 4]]
matrix B = [[5, 6]; [7, 8]]
C = A.T`);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const runCode = async () => {
    setLoading(true);
    try {
      const res = await axios.post("http://localhost:5000/run", { code });
      setResult(res.data.result);
    } catch (err) {
      setResult(err.response?.data?.error || "Unknown error");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-zinc-900 text-zinc-100 p-6 font-mono">
      <div className="grid grid-cols-2 gap-6 max-w-7xl mx-auto mb-6">
        {/* Left: Notes */}
        <div className="bg-zinc-800 border border-zinc-700 rounded-xl p-4">
          <h1 className="text-xl font-bold text-lime-400 mb-2">📘 Matrix DSL Guide</h1>
          <ul className="text-sm text-zinc-300 list-disc list-inside space-y-1">
            <li>Declare matrices using <code className="text-lime-300">matrix A = [[1, 2]; [3, 4]]</code></li>
            <li>Use <code className="text-lime-300">A.T</code> for transpose</li>
            <li>Use <code className="text-lime-300">A.inv</code> for inverse</li>
            <li>Support for <code className="text-lime-300">+, -, *</code> operations</li>
            <li>Separate rows with <code className="text-lime-300">;</code> and values with <code className="text-lime-300">,</code></li>
          </ul>
        </div>

        {/* Right: Code Input */}
        <div className="bg-zinc-800 border border-zinc-700 rounded-xl p-4 flex flex-col">
          <label htmlFor="code" className="text-sm text-zinc-400 mb-2">
            ✍️ Code Editor
          </label>
          <textarea
            id="code"
            rows={8}
            value={code}
            onChange={(e) => setCode(e.target.value)}
            className="flex-1 bg-zinc-900 text-lime-300 border border-zinc-600 rounded-lg p-3 resize-none focus:outline-none focus:ring-2 focus:ring-lime-500"
          />
          <button
            onClick={runCode}
            disabled={loading}
            className="mt-4 self-end px-6 py-2 bg-lime-500 text-black rounded-lg font-semibold hover:bg-lime-600 disabled:opacity-50 transition-all"
          >
            {loading ? "Running..." : "Run ▶"}
          </button>
        </div>
      </div>

      {/* Output section at bottom */}
      <div className="max-w-7xl mx-auto bg-black border border-zinc-700 rounded-xl p-4">
        <h2 className="text-lime-400 mb-2">🖥️ Output Console</h2>
        <pre className="bg-zinc-900 p-4 rounded text-lime-200 overflow-x-auto min-h-[4rem]">
          {result ? JSON.stringify(result, null, 2) : "No output yet."}
        </pre>
      </div>
    </div>
  );
}
