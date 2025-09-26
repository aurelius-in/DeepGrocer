import { useEffect, useState } from 'react';
import { getLatestReceipts } from './lib/api';

type Receipt = { id:number; ts:string; agent:string; action:string; policy_version:string; risk_tier:string };

export default function App() {
  const [rows, setRows] = useState<Receipt[]>([]);
  useEffect(() => { getLatestReceipts().then(setRows); }, []);
  return (
    <div style={{padding:20}}>
      <h1>DeepGrocer Dashboard</h1>
      <p>Status: <a href='http://localhost:8000/health' target='_blank'>API Health</a></p>
      <section>
        <h2>Latest Receipts</h2>
        <table>
          <thead><tr><th>ID</th><th>Time</th><th>Agent</th><th>Action</th><th>Policy</th><th>Risk</th></tr></thead>
          <tbody>
            {rows.map(r => (
              <tr key={r.id}>
                <td>{r.id}</td><td>{new Date(r.ts).toLocaleString()}</td>
                <td>{r.agent}</td><td>{r.action}</td><td>{r.policy_version}</td><td>{r.risk_tier}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>
    </div>
  );
}

