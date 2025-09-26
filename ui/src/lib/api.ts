export const API = import.meta.env.VITE_API_BASE || 'http://localhost:8000';
export async function getLatestReceipts(limit = 50) {
  const r = await fetch(${'$'}{API}/api/receipts/latest?limit={limit});
  return r.json();
}
